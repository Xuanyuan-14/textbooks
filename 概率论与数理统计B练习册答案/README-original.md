# 概率论与数理统计B练习册答案 · AI 友好版

由 `pipeline.py` 从 PaddleOCR-VL-1.6 输出生成。

## 文件

| 文件 | 用途 |
|---|---|
| `book.md` | 主文档：页码锚点 + 章节索引 + 题注，直接喂模型 |
| `pages.jsonl` | 每页一条 JSON，RAG 切片用 |
| `outline.json` | 章节树（含页码） |
| `images/` | 1 张插图，已本地化 |

## 规模

- 页数：105
- 正文：89,342 字符
- 图片：1 张
- 章节：28 章

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
