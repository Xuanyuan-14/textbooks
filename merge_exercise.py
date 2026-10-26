#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
merge_exercise.py —— 把「练习册」与「答案」按练习编号合成一份对照版。

练习册和答案各自转成 AI 友好版后仍是两份文件，模型要回答「练习5 第3题怎么做」
得跨文件检索。本脚本按练习号对齐，输出：

    <out>/combined.md
        ## 练习5 动量 功和能
        ### 题目          ← 来自练习册
        <!-- page: 0 * 纯答案练习标记 -->

        ### 解答          ← 来自答案

    <out>/exercises.jsonl   每个练习一条，含题面、解答、两份原始页码
    <out>/index.md          练习号 → 标题 → 是否有题/有答案 的速查表

页码约定：题面用 `<!-- src: 练习册 p.N -->`，解答用 `<!-- src: 答案 p.N -->`，
两个文件的原始页码互不混淆。
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"D:\杂项\work\教材")
BOOK_DIR = ROOT / "大学物理练习册"
ANS_DIR = ROOT / "大学物理练习册答案(已修正部分错误)"
OUT = ROOT / "大学物理练习册-题目+答案"

RE_EX = re.compile(r"^\s*练习\s*([0-9一二三四五六七八九十]+)")
RE_BARE = re.compile(r"^\s*(\d{1,2})\s+[^0-9.、．,，]")
_CN = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7,
       "八": 8, "九": 9, "十": 10}


def ex_num(title: str) -> int | None:
    """从标题里取练习号。支持「练习9」「练习 9」「练习27简谐」「13 麦克斯韦」。"""
    m = RE_EX.match(title)
    if m:
        s = m.group(1)
        if s.isdigit():
            return int(s)
        if s in _CN:
            return _CN[s]
        if "十" in s:
            head, _, tail = s.partition("十")
            return (_CN.get(head, 1) if head else 1) * 10 + (_CN.get(tail, 0) if tail else 0)
    m = RE_BARE.match(title)
    if m:
        return int(m.group(1))
    return None


def load_pages(jsonl: Path) -> list[dict]:
    return [json.loads(l) for l in jsonl.read_text(encoding="utf-8").splitlines() if l.strip()]


def group_by_exercise(pages: list[dict]) -> dict[int, dict]:
    """按练习号聚合页面。返回 {练习号: {title, pages:[...]}}"""
    out: dict[int, dict] = {}
    cur = None
    for p in pages:
        n = ex_num(p.get("chapter") or "")
        if n is not None:
            cur = n
            if cur not in out:
                out[cur] = {"title": (p.get("chapter") or "").strip(), "pages": []}
        if cur is not None:
            out[cur]["pages"].append(p)
    return out


def strip_html_tables(s: str) -> str:
    return s


def drop_dup_exercise_headings(text: str) -> str:
    """整理原文标题，适配合并版的层级。

    1. 去掉原文里已存在的「## 练习N ...」——合并版自己会生成一级标题，
       保留原文那份会让同一练习名下出现两个同名标题。
    2. 把原文的 `## 一、填空题` 之类降为 `#### `，因为它们现在位于
       `### 题目` / `### 解答` 之下，同级会把层级拉平。
    """
    out = []
    for ln in text.split("\n"):
        s = ln.strip()
        if re.match(r"^#{1,6}\s*练习\s*[0-9一二三四五六七八九十]+", s):
            continue
        m = re.match(r"^(#{1,6})\s*(.+)$", s)
        if m and len(m.group(1)) <= 2:
            out.append("#### " + m.group(2).strip())
            continue
        out.append(ln)
    return "\n".join(out)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    book_pages = load_pages(BOOK_DIR / "pages.jsonl")
    ans_pages = load_pages(ANS_DIR / "pages.jsonl")

    book_ex = group_by_exercise(book_pages)
    ans_ex = group_by_exercise(ans_pages)

    all_nums = sorted(set(book_ex) | set(ans_ex))
    print(f"[*] 练习册 {len(book_ex)} 个练习（{len(book_pages)} 页）")
    print(f"[*] 答案   {len(ans_ex)} 个练习（{len(ans_pages)} 页）")
    print(f"[*] 合并   {len(all_nums)} 个练习，编号 {all_nums[0]}–{all_nums[-1]}")

    parts = [
        "# 大学物理练习册 · 题目与答案对照版",
        "",
        "> 由「大学物理练习册」与「大学物理练习册答案（已修正部分错误）」按练习号合并。",
        "> 题面出自练习册，解答出自答案册，两边原始页码分别标注。",
        "> `<!-- src: 练习册 p.N -->` 与 `<!-- src: 答案 p.N -->` 指向各自 PDF 的页码。",
        "",
        "## 练习索引",
        "",
    ]

    recs = []
    only_ans = []

    for n in all_nums:
        b = book_ex.get(n)
        a = ans_ex.get(n)
        title = (b or a)["title"]
        # 去掉标题里的练习号前缀，得到纯标题
        clean = RE_EX.sub("", title).strip()
        clean = RE_BARE.sub("", clean).strip() if not clean else clean
        clean = clean.strip("、.．-— ")

        has_q = bool(b)
        has_a = bool(a)
        if not has_q:
            only_ans.append(n)

        mark = ""
        if has_q and has_a:
            mark = ""
        elif has_a:
            mark = " ⚠️仅答案"
        elif has_q:
            mark = " ⚠️仅题目"

        parts.append(f"- 练习{n}　{clean}{mark}")

        recs.append({
            "ex": n, "title": clean,
            "has_question": has_q, "has_answer": has_a,
            "question_pages": [p["page"] for p in (b or {}).get("pages", [])],
            "answer_pages": [p["page"] for p in (a or {}).get("pages", [])],
        })

    parts += ["", "---", ""]

    for rec in recs:
        n = rec["ex"]
        parts += [f"## 练习{n} {rec['title']}".rstrip(), ""]

        if rec["has_question"]:
            b = book_ex[n]
            parts += [f"<!-- src: 练习册 p.{b['pages'][0]['page']} -->", "", "### 题目", ""]
            for p in b["pages"]:
                t = (p.get("text") or "").strip()
                if t:
                    # 两册图片各自留在原目录，这里改写成跨目录相对路径
                    t = t.replace('src="images/',
                                  'src="../大学物理练习册/images/')
                    t = drop_dup_exercise_headings(t)
                    if t.strip():
                        parts += [t.strip(), ""]
        else:
            parts += ["> 本次未收录该练习的题目页（练习册仅覆盖部分练习）。", ""]

        if rec["has_answer"]:
            a = ans_ex[n]
            parts += [f"<!-- src: 答案 p.{a['pages'][0]['page']} -->", "", "### 解答", ""]
            for p in a["pages"]:
                t = (p.get("text") or "").strip()
                if t:
                    t = t.replace('src="images/',
                                  'src="../大学物理练习册答案(已修正部分错误)/images/')
                    t = drop_dup_exercise_headings(t)
                    if t.strip():
                        parts += [t.strip(), ""]
        else:
            parts += ["> 本次未收录该练习的答案页。", ""]

        parts += ["---", ""]

    combined = "\n".join(parts)
    (OUT / "combined.md").write_text(combined, encoding="utf-8")

    with (OUT / "exercises.jsonl").open("w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 图片软链接不存在，直接复制目录引用说明
    (OUT / "README.md").write_text(f"""# 大学物理练习册 · 题目与答案对照版

按练习号把练习册与答案合并成一份，模型可直接读到「题目 + 解答」。

## 文件

| 文件 | 用途 |
|---|---|
| `combined.md` | 主文档，{len(all_nums)} 个练习，题目与解答交替 |
| `exercises.jsonl` | 每个练习一条 JSON（练习号/标题/页码/有无题解） |
| `README.md` | 本文件 |

## 规模

- 练习数：{len(all_nums)}（第 {all_nums[0]}–{all_nums[-1]} 号）
- 有题有答：{sum(1 for r in recs if r['has_question'] and r['has_answer'])} 个
- 仅有答案：{sum(1 for r in recs if r['has_answer'] and not r['has_question'])} 个
- 仅有题目：{sum(1 for r in recs if r['has_question'] and not r['has_answer'])} 个
- combined.md：{len(combined):,} 字符

## 图片

题图与公式截图不在此目录，分别位于：

- `../大学物理练习册/images/`
- `../大学物理练习册答案(已修正部分错误)/images/`

`combined.md` 里保留了两册各自的相对图片引用前缀，
需要看图时到对应目录取。

## 页码约定

- `<!-- src: 练习册 p.N -->` → 练习册 PDF 第 N 页
- `<!-- src: 答案 p.N -->` → 答案册 PDF 第 N 页
""", encoding="utf-8")

    print(f"[+] combined.md  {len(combined):,} 字符")
    print(f"[+] exercises.jsonl  {len(recs)} 行")
    if only_ans:
        print(f"[+] 仅有答案的练习: {only_ans}")
    print(f"[+] 输出目录: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
