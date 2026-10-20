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

    seen, outline = set(), []
    for e in entries:
        k = (norm(e["title"]), e["page"])
        if k in seen:
            continue
        seen.add(k)
        outline.append(e)

    # 先判断全书是否使用「第N章」编号。
    #   有  → 只认「第N章」为章，深度仅用于分节（复变、顾樵、电路分析都属此类）
    #   没有 → 回退到「depth==1 且不是编号小节」为章（模电那种以章名直接作标题的书）
    has_chapter_numbering = any(RE_CHAPTER.match(e["title"]) for e in outline)
    RE_NUMLIST = re.compile(r"^\s*(?:\d+[.、]|[（(]\d+[)）]|[一二三四五六七八九十]+[、.])")

    for e in outline:
        t = e["title"]
        d = e["depth"]
        is_chap = bool(RE_CHAPTER.match(t))
        is_sec = bool(RE_SECTION.match(t))
        is_front = bool(RE_FRONT.search(t))
        is_numlist = bool(RE_NUMLIST.match(t))       # 「1. 某某」编号小节

        if is_front and d <= 1 and not has_chapter_numbering:
            e["level"] = "front"
        elif has_chapter_numbering:
            if is_chap:
                e["level"] = "chapter"
            elif is_sec:
                e["level"] = "section"
            elif d <= 1 or d == 2:
                e["level"] = "subsection"
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
    chap_iter = [e for e in outline if e["level"] == "chapter"]
    sec_iter = [e for e in outline if e["level"] == "section"]
    cur_c = cur_s = ""
    for r in recs:
        for e in chap_iter:
            if e["page"] <= r["page"]:
                cur_c = e["title"]
        for e in sec_iter:
            if e["page"] <= r["page"]:
                cur_s = e["title"]
        r["chapter"], r["section"] = cur_c, cur_s

    # ---------- 4. 生成 book.md ----------
    parts = [f"# {title}", "",
             f"> 源文件：`{json_path.name}`",
             f"> 共 {n_pages} 页，由 PaddleOCR-VL-1.6 从 PDF 转出。",
             "> 页码锚点格式 `<!-- page: N -->`，N 为 PDF 页码（从 1 起）。",
             "> 图片位于 `../images/`，已本地化。", ""]

    chap = [e for e in outline if e["level"] == "chapter"]
    if chap:
        parts += ["## 章节索引", ""]
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
    zpath = out / f"{safe_name(title)}-AI友好版.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.rglob("*")):
            if f.is_file() and f != zpath:
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
