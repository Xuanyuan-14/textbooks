# 模电教材 · AI 友好版

由 `enhance.py` 从 PaddleOCR-VL-1.6 的输出生成，目标是让模型**更好读**。

## 文件

| 文件 | 用途 |
|---|---|
| `book.md` | 主文档。页码锚点 + 章节索引 + 题注补全，直接喂给模型 |
| `pages.jsonl` | 每页一条 JSON，按页切片入库（RAG）用 |
| `outline.json` | 章节树，含页码，用于「先定位再精读」 |
| `README.md` | 本文件 |

图片在 `../images/`（1133 张，已本地化）。

## 规模

- 页数：527
- 正文：1,002,460 字符
- 图片：1133 张
- 章节：10 章 / 228 节
- book.md：1,021,465 字符

## 怎么用

### 1. 直接丢给模型（长上下文）
把 `book.md` 整份作为上下文。开头有章节索引，模型可以先定位再回答。

### 2. 检索增强（推荐，省 token）
用 `pages.jsonl` 建索引，每行是一条独立页：

```python
import json
for line in open("pages.jsonl", encoding="utf-8"):
    rec = json.loads(line)
    # rec["page"]    页号
    # rec["text"]    正文
    # rec["chapter"] 所属章
    # rec["images"]  该页图片文件名列表
```

命中某页后，用 `rec["page"]` 回 `book.md` 里找 `<!-- page: N -->` 读原文。

### 3. 引用页码
`<!-- page: N -->` 里的 N 就是 PDF 页码，可以直接说「第 N 页」。

### 4. 按章节精读
读 `outline.json` 拿到章节起止页，再定向取 pages.jsonl 的对应区间。

## 已知局限

- **表格是 HTML `<table>` 格式**，不是 Markdown 表格。多数模型能直接读。
- **扫描件的 OCR 误差**：公式下标、希腊字母偶有识别错。关键数据建议回原图核对。
- **图片是切割出的插图**，不含整页版面。需要整页图请用原始 JSON 的 `inputImage`。
