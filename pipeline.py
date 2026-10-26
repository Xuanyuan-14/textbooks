#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
pipeline.py —— PaddleOCR-VL 输出 → AI 友好的自包含教材包（通用版）

一键完成三件事：
  1. 抓取所有插图到本地 images/（不再依赖百度云签名链接）
  2. 生成带页码锚点的 book.md，图片引用改成本地相对路径
  3. 输出 pages.jsonl / outline.json / README.md，供 RAG 与精读使用

用法：
    python pipeline.py "数学物理方法 (顾樵)"        # 书名关键字
    python pipeline.py --all                        # 处理 Downloads 下所有新书

设计要点（与模电那次一致，且修掉了当时的坑）：
  - 图片路径在生成 book.md 时就写成 ../images/p<页号>_<原名>，不再事后替换
  - 章节按 Markdown # 深度判定（# = 章，## = 节），PaddleOCR-VL 的标题自带井号
  - 题注剥掉 HTML 标签后写进 alt，模型读 alt 就知道图是什么
  - 下载幂等：已存在的文件跳过，重跑只补缺
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

# ---------------------------------------------------------------- 配置

DOWNLOADS = Path(r"C:\Users\Xuanyuan14\Downloads")
OUT_ROOT = Path(r"D:\杂项\work\教材")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

# 版式噪声，对理解内容无价值
NOISE_LABELS = {"header", "footer", "number", "header_image", "footer_image"}

# 标题类标签
TITLE_LABELS = {"paragraph_title", "doc_title", "title"}

RE_CHAPTER = re.compile(r"^\s*(第\s*[0-9一二三四五六七八九十]+\s*章|Chapter\s+\d+)")
RE_SECTION = re.compile(r"^\s*(\d+\.\d+(?:\.\d+)?)\s*\S")
RE_FRONT = re.compile(r"(序|前言|目录|符号表|内容简介|编目数据|习题答案|附录)")
# 「第一章习题」「本章小结」这类虽以「第N章」开头，但不是章标题
RE_NOT_CHAPTER = re.compile(r"(习题|答案|小结|思考题|复习|自测|参考文献)")
# 在任意位置找「第N章 xxx」「第N篇 xxx」（用于页眉反推章边界）
RE_CHAPTER_FULL = re.compile(r"第\s*([一二三四五六七八九十百零〇\d]+)\s*章")
RE_PART = re.compile(r"第\s*([一二三四五六七八九十]+)\s*篇")
# 练习册/答案这类教辅：以「练习N 标题」为章，「一、填空题」为节
# 注意不要加 \b：Python 的 \w 包含中文，「练习27简谐振动」里 7 与「简」之间
# 不存在词边界，加 \b 会漏掉这类无空格的标题
RE_EXERCISE = re.compile(r"^\s*练习\s*[0-9一二三四五六七八九十]+")
RE_CN_SECTION = re.compile(r"^\s*[一二三四五六七八九十]+\s*[、.．]")
# 缺「练习」二字的裸编号章标题，如「13 麦克斯韦分子速率分布律」
RE_BARE_CHAPTER = re.compile(r"^\s*(\d{1,2})\s+[^0-9.、．,，]")

_CN_NUM = {
    "零": 0, "〇": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
    "六": 6, "七": 7, "八": 8, "九": 9, "十": 10, "百": 100,
}


def cn2int(s: str) -> int:
    """中文/阿拉伯章号 → int。支持 一…十九、二十一、百 以内。"""
    s = (s or "").strip()
    if s.isdigit():
        return int(s)
    if s in _CN_NUM:
        return _CN_NUM[s]
    # 十X / X十 / X十Y
    if "十" in s:
        head, _, tail = s.partition("十")
        tens = _CN_NUM.get(head, 1) if head else 1
        ones = _CN_NUM.get(tail, 0) if tail else 0
        return tens * 10 + ones
    return 999


# ---------------------------------------------------------------- 工具


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s or "")


def clean_caption(s: str) -> str:
    """剥掉 HTML 标签，只留题注文字。"""
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()


def safe_name(s: str) -> str:
    s = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", s).strip(" ._")
    return s[:60] or "book"


def clean_title(s: str) -> str:
    """从 PaddleOCR 输出的文件名还原干净书名。

    Z-Library 下载名会拼上站点水印且被截断，例如：
      `电路分析第二版 (张小梅 刘岚 李政颖) (z-library.sk 1lib.sk z-l`
    剥掉 .pdf_* 后缀与水印括号，只留「书名 (作者)」。
    """
    s = re.sub(r"\.pdf_by_PaddleOCR-VL-[\d.]+$", "", s, flags=re.I)
    s = re.sub(r"\.pdf_.*$", "", s, flags=re.I)
    # 括号可能被截断，不要求闭合
    s = re.sub(r"\s*[\(\[]?\s*(?:z-library|1lib|z-lib|singlelogin)[^)\]]*[)\]]?\s*$",
               "", s, flags=re.I)
    # 只去空白和句点，保留书名的括号（(作者) 是有意义的）
    return s.strip(" ._") or "book"


# ---------------------------------------------------------------- 下载


def fetch(url: str, dest: Path, retries: int = 3) -> tuple[bool, int, str]:
    if dest.exists() and dest.stat().st_size > 0:
        return True, dest.stat().st_size, "cached"
    last = ""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                blob = r.read()
            if not blob:
                last = "empty body"
                time.sleep(0.5 * (attempt + 1))
                continue
            dest.write_bytes(blob)
            return True, len(blob), "ok"
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
            last = f"{type(e).__name__}: {e}"
            time.sleep(0.8 * (attempt + 1))
    return False, 0, last


# ---------------------------------------------------------------- 单本处理


def process(md_path: Path, json_path: Path) -> dict:
    title = clean_title(md_path.stem)
    out = OUT_ROOT / safe_name(title)
    img_dir = out / "images"
    out.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(exist_ok=True)

    print(f"\n{'=' * 74}")
    print(f"[*] {title}")
    print(f"[*] 输出：{out}")

    pages = json.loads(json_path.read_text(encoding="utf-8"))
    n_pages = len(pages)
    print(f"[*] 页数：{n_pages}")

    # ---------- 1. 下载插图 ----------
    total_imgs = sum(len((p.get("markdown") or {}).get("images") or {})
                     for p in pages)
    print(f"[*] 插图：{total_imgs} 张，开始下载…")

    url_to_local: dict[str, str] = {}
    ok = fail = 0
    bytes_total = 0
    failures: list[dict] = []
    done = 0

    for pno, page in enumerate(pages, start=1):
        imgs = (page.get("markdown") or {}).get("images") or {}
        for name, url in imgs.items():
            done += 1
            if url in url_to_local:
                continue
            base = Path(name).name
            local = f"p{pno:04d}_{base}"
            dest = img_dir / local
            success, nbytes, err = fetch(url, dest)
            if success:
                url_to_local[url] = local
                ok += 1
                bytes_total += nbytes
            else:
                fail += 1
                failures.append({"page": pno, "name": base, "url": url,
                                 "error": err})
            if done % 40 == 0 or done == total_imgs:
                sys.stdout.write(f"\r    [{done}/{total_imgs}] "
                                 f"成功 {ok} 失败 {fail}  ")
                sys.stdout.flush()

    print(f"\n[+] 下载完成：{ok} 成功 / {fail} 失败，"
          f"{bytes_total / 1048576:.1f} MB")

    # ---------- 2. 组装每页记录 ----------
    recs = []
    for i, p in enumerate(pages, start=1):
        md = p.get("markdown") or {}
        text = (md.get("text") or "").strip()

        # 图片路径统一写成 images/p<页号>_<原名>
        # 注意：book.md 与 images/ 同级，所以用 images/ 而非 ../images/
        def fix_src(m):
            base = Path(m.group(1).split("?")[0]).name
            return f'src="images/p{i:04d}_{base}"'

        text = re.sub(r'src="([^"]+\.(?:jpg|jpeg|png|gif))[^"]*"', fix_src,
                      text, flags=re.I)

        blocks = (p.get("prunedResult") or {}).get("parsing_res_list") or []

        captions = []
        for b in blocks:
            if b.get("block_label") != "figure_title":
                continue
            cap = clean_caption(b.get("block_content") or "")
            if cap:
                captions.append(cap)

        recs.append({"page": i, "text": text, "captions": captions,
                     "blocks": blocks, "chars": len(text)})

    # ---------- 3. 章节大纲 ----------
    entries = []
    for r in recs:
        for b in r["blocks"]:
            if b.get("block_label") not in TITLE_LABELS:
                continue
            raw = (b.get("block_content") or "").strip()
            if not raw:
                continue
            m = re.match(r"^(#{1,6})\s*(.*)$", raw)
            depth = len(m.group(1)) if m else 0
            t = (m.group(2) if m else raw).strip()
            if not t or len(t) > 60:
                continue
            entries.append({"page": r["page"], "title": t, "depth": depth})

    # ---------- 3a. 从页眉补全章/篇 ----------
    # 有些书（如姚端正《数学物理方法》）只把章标题识别成 header，正文里没有独立的
    # 标题块。此时用页眉首现页反推章边界，这是版面信息里最可靠的信号。
    chap_first: dict[int, tuple[int, str]] = {}
    part_first: dict[int, tuple[int, str]] = {}
    for r in recs:
        for b in r["blocks"]:
            lbl = b.get("block_label")
            if lbl != "header" and lbl not in TITLE_LABELS:
                continue
            c = re.sub(r"^#+\s*", "", clean_caption(b.get("block_content") or ""))
            if not c or len(c) > 80:
                continue
            mc = RE_CHAPTER_FULL.search(c)
            if mc and not RE_NOT_CHAPTER.search(c):
                num = cn2int(mc.group(1))
                if num not in chap_first:
                    chap_first[num] = (r["page"], c.strip())
                continue
            mp = RE_PART.search(c)
            if mp:
                num = cn2int(mp.group(1))
                if num not in part_first:
                    part_first[num] = (r["page"], c.strip())

    header_geo = []
    for num in sorted(part_first):
        pg, t = part_first[num]
        header_geo.append({"page": pg, "title": t, "depth": 0, "_geo": "part"})
    for num in sorted(chap_first):
        pg, t = chap_first[num]
        header_geo.append({"page": pg, "title": t, "depth": 0, "_geo": "chapter"})

    # 页眉地理信息优先：把标题块里同名的章/篇条目去掉，避免重复
    if header_geo:
        geo_titles = {norm(g["title"]) for g in header_geo}
        entries = [e for e in entries if norm(e["title"]) not in geo_titles]
        entries = header_geo + entries

    seen, outline = set(), []
    for e in entries:
        k = (norm(e["title"]), e["page"])
        if k in seen:
            continue
        seen.add(k)
        outline.append(e)

    # 页眉反推出来的章/篇直接定级
    for e in outline:
        if e.get("_geo") == "chapter":
            e["level"] = "chapter"
        elif e.get("_geo") == "part":
            e["level"] = "part"

    # 先判断全书使用哪种章的编号体系。
    #   「第N章」 → 只认它为章，深度仅用于分节（复变、顾樵、电路分析）
    #   「练习N」 → 教辅书，练习即章，「一、填空题」为节
    #   都没有    → 回退到「depth==1 且不是编号小节」为章（模电那种）
    has_chapter_numbering = any(
        (RE_CHAPTER.match(e["title"]) and not RE_NOT_CHAPTER.search(e["title"]))
        or RE_EXERCISE.match(e["title"])
        for e in outline)
    RE_NUMLIST = re.compile(r"^\s*(?:\d+[.、]|[（(]\d+[)）]|[一二三四五六七八九十]+[、.])")

    for e in outline:
        if e.get("level") in ("part", "chapter") and e.get("_geo"):
            continue        # 页眉反推的章/篇已定级，不再重判

        t = e["title"]
        d = e["depth"]
        is_chap = bool(RE_CHAPTER.match(t)) and not RE_NOT_CHAPTER.search(t)
        is_ex = bool(RE_EXERCISE.match(t))
        is_cn_sec = bool(RE_CN_SECTION.match(t))
        is_bare = bool(RE_BARE_CHAPTER.match(t)) and d <= 2
        is_sec = bool(RE_SECTION.match(t))
        is_front = bool(RE_FRONT.search(t))
        is_numlist = bool(RE_NUMLIST.match(t))       # 「1. 某某」编号小节

        if is_front and d <= 1 and not has_chapter_numbering:
            e["level"] = "front"
        elif has_chapter_numbering:
            if is_chap or is_ex or is_bare:
                e["level"] = "chapter"
            elif is_cn_sec or is_sec:
                e["level"] = "section"
            else:
                e["level"] = "subsection"
        else:
            # 无「第N章」编号的书
            if d <= 1 and not is_numlist:
                e["level"] = "front" if is_front else "chapter"
            elif d == 2 or is_sec:
                e["level"] = "section"
            else:
                e["level"] = "subsection"

    # 把章节归属写进每页记录，并继续生成 book.md / jsonl / 打包
    chap_iter = sorted([e for e in outline if e["level"] == "chapter"],
                       key=lambda x: x["page"])
    sec_iter = sorted([e for e in outline if e["level"] == "section"],
                      key=lambda x: x["page"])
    cur_c = cur_s = ""
    chap_page = 0
    for r in recs:
        for e in chap_iter:
            if e["page"] <= r["page"]:
                cur_c, chap_page = e["title"], e["page"]
                if e["page"] == r["page"]:
                    cur_s = ""          # 新章首页，清掉上一章残留的节名
        for e in sec_iter:
            # 节必须落在当前章之内，否则会继承上一章的最后一节
            if chap_page <= e["page"] <= r["page"]:
                cur_s = e["title"]
        r["chapter"], r["section"] = cur_c, cur_s

    # ---------- 4. 生成 book.md ----------
    parts = [f"# {title}", "",
             f"> 源文件：`{json_path.name}`",
             f"> 共 {n_pages} 页，由 PaddleOCR-VL-1.6 从 PDF 转出。",
             "> 页码锚点格式 `<!-- page: N -->`，N 为 PDF 页码（从 1 起）。",
             "> 图片位于同级的 `images/`，已本地化。", ""]

    chap = [e for e in outline if e["level"] == "chapter"]
    part_list = [e for e in outline if e["level"] == "part"]
    if chap:
        parts += ["## 章节索引", ""]
        # 有「篇」的先按篇分组，没有就平铺
        if part_list:
            for p in part_list:
                parts.append(f"### {p['title']}（第 {p['page']} 页）")
                nxt = [q["page"] for q in part_list if q["page"] > p["page"]]
                hi = nxt[0] if nxt else 10 ** 9
                for c in chap:
                    if p["page"] <= c["page"] < hi:
                        parts.append(f"- {c['title']} — 第 {c['page']} 页")
                parts.append("")
            # 落在所有篇之前的章
            first_part = min(q["page"] for q in part_list)
            for c in chap:
                if c["page"] < first_part:
                    parts.append(f"- {c['title']} — 第 {c['page']} 页")
        else:
            for e in chap:
                parts.append(f"- **{e['title']}** — 第 {e['page']} 页")
        parts += ["", "---", ""]

    for r in recs:
        parts += [f"<!-- page: {r['page']} -->", ""]
        text = r["text"]

        # 丢掉独立的纯页码行
        lines = []
        for ln in text.split("\n"):
            s = ln.strip()
            if s and len(s) <= 4 and re.fullmatch(
                    r"[0-9ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ！!·.．\-—_]+", s):
                continue
            lines.append(ln)
        text = "\n".join(lines).strip()

        # 题注填进 alt
        if r["captions"]:
            it = iter(r["captions"])

            def add_alt(m):
                tag = m.group(0)
                if 'alt="Image"' not in tag:
                    return tag
                try:
                    cap = next(it)
                except StopIteration:
                    return tag
                cap = clean_caption(cap).replace('"', "'").replace("<", "")
                cap = re.sub(r"\s+", " ", cap).strip()[:100]
                return tag.replace('alt="Image"', f'alt="{cap}"') if cap else tag

            text = re.sub(r"<img\b[^>]*>", add_alt, text)

        if text:
            parts += [text, ""]

    book_md = "\n".join(parts)
    (out / "book.md").write_text(book_md, encoding="utf-8")

    # ---------- 5. pages.jsonl ----------
    with (out / "pages.jsonl").open("w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps({
                "page": r["page"], "chapter": r["chapter"],
                "section": r["section"], "text": r["text"],
                "images": [Path(k).name for k in r["images"]] if r.get("images") else [],
                "chars": r["chars"],
            }, ensure_ascii=False) + "\n")

    # ---------- 6. outline.json ----------
    (out / "outline.json").write_text(json.dumps({
        "title": title,
        "total_pages": n_pages,
        "chapters": chap,
        "sections": [e for e in outline if e["level"] == "section"],
        "all_headings": outline,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---------- 7. 校验 ----------
    refs = set(re.findall(r'src="(?:\.\./)?images/([^"]+)"', book_md))
    have = {f.name for f in img_dir.iterdir() if f.is_file()}
    broken = refs - have
    remote_left = len(re.findall(r"https://pplines", book_md))

    # ---------- 8. README ----------
    total_chars = sum(r["chars"] for r in recs)
    readme = f"""# {title} · AI 友好版

由 `pipeline.py` 从 PaddleOCR-VL-1.6 输出生成。

## 文件

| 文件 | 用途 |
|---|---|
| `book.md` | 主文档：页码锚点 + 章节索引 + 题注，直接喂模型 |
| `pages.jsonl` | 每页一条 JSON，RAG 切片用 |
| `outline.json` | 章节树（含页码） |
| `images/` | {len(have)} 张插图，已本地化 |

## 规模

- 页数：{n_pages}
- 正文：{total_chars:,} 字符
- 图片：{len(have)} 张
- 章节：{len(chap)} 章

## 怎么用

```python
import json
for line in open("pages.jsonl", encoding="utf-8"):
    r = json.loads(line)
    # r 的字段：page / chapter / section / text / images / chars
    # 用 r["page"] 回 book.md 找 <!-- page: N --> 读原文
```

## 已知局限

- 表格为 HTML `<table>` 格式，非 Markdown 表格。
- 扫描件 OCR 误差：公式下标、希腊字母偶有误。关键处建议回原图核对。
"""
    (out / "README.md").write_text(readme, encoding="utf-8")

    # ---------- 9. 打包 ----------
    # 只收 book.md / pages.jsonl / outline.json / README / report / images，
    # 跳过所有 .zip（否则旧包会被打进新包，体积逐次翻倍）与 __pycache__
    zpath = out / f"{safe_name(title)}-AI友好版.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.rglob("*")):
            if not f.is_file() or f == zpath:
                continue
            if f.suffix.lower() == ".zip":
                continue
            if "__pycache__" in f.parts:
                continue
            zf.write(f, f.relative_to(out))

    result = {
        "title": title, "dir": str(out), "pages": n_pages,
        "downloaded_ok": ok, "downloaded_fail": fail,
        "images_on_disk": len(have), "chars": len(book_md),
        "chapters": len(chap),
        "refs": len(refs), "broken": len(broken),
        "remote_left": remote_left,
        "zip_mb": round(zpath.stat().st_size / 1048576, 2),
        "failures": failures[:50],
    }
    (out / "report.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[+] book.md      {len(book_md):,} 字符")
    print(f"[+] 图片引用     {len(refs)} 处 / 本地 {len(have)} 张")
    print(f"[+] 断链         {len(broken)}   残留远程 {remote_left}")
    print(f"[+] 章节         {len(chap)} 章")
    print(f"[+] 打包         {zpath.name}  {result['zip_mb']} MB")
    if failures:
        print(f"[!] 失败 {len(failures)} 张，详见 report.json")
    return result


# ---------------------------------------------------------------- main


def main() -> int:
    args = sys.argv[1:]
    flags = {a for a in args if a.startswith("--")}
    keys = [a for a in args if not a.startswith("--")]

    if not keys:
        md_files = sorted(DOWNLOADS.glob("*PaddleOCR-VL-1.6.md"))
    else:
        md_files = sorted(f for f in DOWNLOADS.glob("*PaddleOCR-VL-1.6.md")
                          if any(k in f.name for k in keys))

    if not md_files:
        print("[x] 没找到匹配的 .md")
        return 2

    results = []
    for md in md_files:
        stem = md.name.replace(".md", "")
        js = DOWNLOADS / f"{stem}.json"
        if not js.exists():
            print(f"[!] 缺 JSON，跳过：{md.name}")
            continue
        title = clean_title(md.stem)
        out = OUT_ROOT / safe_name(title)
        if (out / "report.json").exists() and "--force" not in flags:
            print(f"[=] 已处理过，跳过：{title}（加 --force 可重跑）")
            continue
        r = process(md, js)
        if isinstance(r, dict):
            results.append(r)

    print(f"\n{'=' * 74}")
    print(f"[完成] 共处理 {len(results)} 本")
    for r in results:
        print(f"  {r['title'][:38]:40s} {r['pages']:>4}页 "
              f"图{r['images_on_disk']:>4}  断链{r['broken']}  "
              f"章{r['chapters']:>3}  {r['zip_mb']}MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
