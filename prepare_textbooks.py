"""Build a chapter-organized upload copy; never modify the source books."""
import hashlib
import json
import posixpath
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import quote

SOURCE = Path(r'D:\杂项\work\教材')
DEST = Path(r'D:\杂项\work\textbooks-github')
EXCLUDED_BOOKS = {'复变函数论 (钟玉泉)', '数学物理方法 (顾樵)'}


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def safe(title):
    return re.sub(r'[<>:"/\\|?*]', '_', title).strip().rstrip('.')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def boundaries(book, outline):
    if book.name.startswith('大学物理练习册'):
        result = []
        for chapter in outline['chapters']:
            match = re.match(r'^(?:练习\s*)?(\d+)\s*(.*)', chapter['title'])
            assert match, chapter
            number, title = int(match[1]), match[2]
            result.append((chapter['page'], f'{number:02d}-练习{number} {title}'))
        assert result[0][0] == 1
        return result
    if '电子' in book.name:
        titles = ['绪论', '运算放大器', '二极管及其基本电路', '场效应三极管及其放大电路',
                  '双极结型三极管（BJT）及其放大电路', '频率响应', '模拟集成电路',
                  '反馈放大电路', '功率放大电路', '信号处理与信号产生电路', '直流稳压电源']
        starts = [29, 46, 79, 117, 180, 216, 254, 328, 385, 409, 470]
        return [(1, '00-封面与前言目录')] + [
            (p, f'{i:02d}-第{i}章 {t}') for i, (p, t) in enumerate(zip(starts, titles), 1)
        ] + [(507, '12-附录A PSpice-SPICE软件简介'), (510, '13-附录B 电路理论简明复习'),
             (515, '14-附录C 电阻的彩色编码和标称阻值'), (517, '15-参考文献'),
             (519, '16-索引'), (527, '17-封底')]
    chapters = [c for c in outline['chapters']
                if re.match(r'^第[一二三四五六七八九十百\d]+章\s', c['title'])
                and '习题' not in c['title']]
    result = [(1, '00-封面与前言目录')] + [
        (c['page'], f'{i:02d}-{c["title"]}') for i, c in enumerate(chapters, 1)]
    if '姚端正' in book.name:
        result = [(147 if title.startswith('08-') else page, title) for page, title in result]
        result += [(20, '00a-第一篇导言 复变函数论'), (114, '05a-第二篇导言 数学物理方程'),
                   (229, '10a-第三篇导言 特殊函数'), (281, '13a-第四篇导言 近似方法及现代内容'),
                   (340, '18-习题参考答案'), (362, '19-参考文献'), (363, '20-附表'),
                   (368, '21-索引'), (377, '22-封底')]
        result.sort()
    elif '复变' in book.name:
        result += [(395, '10-封底')]
    elif '电路分析' in book.name:
        result += [(447, '17-附录A Multisim简明教程'), (452, '18-参考文献'), (453, '19-封底')]
    else:
        result += [(546, '16-索引与封底')]
    return result


def book_link(book):
    label = book.name
    if label == '大学物理练习册':
        label += '（无答案版，31 个练习）'
    elif label.startswith('大学物理练习册答案'):
        label = '大学物理练习册（带答案版，48 个练习）'
    return f'- [{label}]({quote(book.name + "/README.md")})'


def build_combined():
    source = SOURCE / '大学物理练习册-题目+答案'
    answer_name = '大学物理练习册答案(已修正部分错误)'
    out = DEST / answer_name
    if not (source / 'combined.md').exists() or not out.exists():
        return
    text = (source / 'combined.md').read_text(encoding='utf-8')
    for name in ['大学物理练习册', answer_name]:
        manifest = json.loads((DEST / name / 'images-manifest.json').read_text(encoding='utf-8'))
        mapping = {m['source']: m['path'] for m in manifest}
        pattern = re.compile(re.escape('../' + name + '/') + r'(images/[^\s\"\'<>`)]+\.jpg)')
        def replace(match):
            target = DEST / name / mapping[match[1]]
            assert target.is_file(), target
            return posixpath.relpath(name + '/' + mapping[match[1]], answer_name)
        text = pattern.sub(replace, text)
    (out / 'combined.md').write_text(text, encoding='utf-8')
    shutil.copy2(source / 'exercises.jsonl', out / 'exercises.jsonl')
    shutil.copy2(source / 'README.md', out / 'README-combined-original.md')
    for archive in source.glob('*.zip'):
        shutil.copy2(archive, out / archive.name)
    shutil.copy2(SOURCE / 'merge_exercise.py', DEST / 'merge_exercise.py')


def main():
    add_new = '--add-new' in sys.argv
    if (DEST / '.git').exists() and not add_new:
        raise SystemExit(f'Output is already a Git repository: {DEST}')
    DEST.mkdir(exist_ok=True)
    shutil.copy2(SOURCE / 'pipeline.py', DEST / 'pipeline.py')
    shutil.copy2(Path(__file__), DEST / 'prepare_textbooks.py')
    (DEST / '.gitignore').write_text('__pycache__/\n*.pyc\n', encoding='utf-8')
    (DEST / '.gitattributes').write_text('*.md text eol=lf\n*.json text eol=lf\n*.jsonl text eol=lf\n*.jpg binary\n*.zip binary\n', encoding='utf-8')
    summaries = json.loads((DEST / 'validation.json').read_text(encoding='utf-8')) if add_new else []
    summaries = [s for s in summaries if s['book'] not in EXCLUDED_BOOKS]
    root_links = []
    for book in SOURCE.iterdir():
        if book.name in EXCLUDED_BOOKS:
            continue
        if not (book / 'book.md').exists():
            continue
        out = DEST / book.name
        if add_new and out.exists():
            assert any(s['book'] == book.name for s in summaries), f'Existing unvalidated output: {out}'
            root_links.append(book_link(book))
            continue
        out.mkdir(exist_ok=True)
        generated = (out / 'chapters').resolve()
        assert generated.is_relative_to(DEST.resolve()) and not generated.is_relative_to(SOURCE.resolve())
        if generated.exists():
            shutil.rmtree(generated)
        # Retain the supplied archives and metadata, including their original OCR output.
        for f in book.iterdir():
            if f.is_file():
                shutil.copy2(f, out / ('README-original.md' if f.name == 'README.md' else f.name))
        outline = json.loads((book / 'outline.json').read_text(encoding='utf-8'))
        original = (book / 'book.md').read_text(encoding='utf-8')
        matches = list(re.finditer(r'<!-- page: (\d+) -->', original))
        pages = {int(m[1]): original[m.start():matches[i+1].start() if i+1 < len(matches) else len(original)]
                 for i, m in enumerate(matches)}
        assert list(pages) == list(range(1, outline['total_pages'] + 1))
        bounds = boundaries(book, outline)
        ranges = []
        location = {}
        for i, (start, title) in enumerate(bounds):
            end = bounds[i+1][0] - 1 if i+1 < len(bounds) else outline['total_pages']
            folder = f'chapters/{safe(title)}'
            (out / folder / 'images').mkdir(parents=True, exist_ok=True)
            for page in range(start, end+1):
                location[page] = folder
            ranges.append(dict(title=title, start_page=start, end_page=end, path=folder, images=0))
        images = list((book / 'images').glob('*'))
        mapping = {}
        for img in images:
            page_match = re.match(r'p(\d+)_', img.name)
            assert page_match, img
            page = int(page_match[1])
            target = f'{location[page]}/images/{img.name}'
            shutil.copy2(img, out / target)
            assert digest(img) == digest(out / target), img
            mapping[img.name] = target
        pattern = re.compile(r'(?:\.\./)?images/([^\s\"\'<>\)`]+\.jpg)')

        def rewrite(text, chapter_folder=None):
            def replace(m):
                name = m[1]
                assert name in mapping, (book.name, name)
                target = mapping[name]
                if chapter_folder:
                    target = ('images/' + name if target.startswith(chapter_folder + '/')
                              else '../../' + target)
                assert (out / chapter_folder / target if chapter_folder else out / target).resolve().is_file()
                return target
            return pattern.sub(replace, text)

        for section in ranges:
            folder = section['path']
            section['images'] = sum(1 for t in mapping.values() if t.startswith(folder + '/'))
            body = ''.join(pages[p] for p in range(section['start_page'], section['end_page']+1))
            head = f'# {section["title"]}\n\n[返回全书目录](../../README.md)\n\n> PDF 页码：{section["start_page"]}–{section["end_page"]}\n\n'
            (out / folder / 'README.md').write_text(head + rewrite(body, folder), encoding='utf-8')
        # Full-book reading and per-page RAG keep working with the new image locations.
        full_text = rewrite(original)
        full_text = full_text.replace('图片位于 `../images/`', '图片按章节存于 `chapters/*/images/`')
        full_text = full_text.replace('图片位于同级的 `images/`', '图片按练习存于 `chapters/*/images/`')
        (out / 'book.md').write_text(full_text, encoding='utf-8')
        records = [json.loads(l) for l in (book / 'pages.jsonl').read_text(encoding='utf-8').splitlines()]
        for rec in records:
            rec['text'] = rewrite(rec['text'])
            rec['images'] = [mapping[n] for n in mapping if int(re.match(r'p(\d+)_', n)[1]) == rec['page']]
            rec['chapter_path'] = location[rec['page']]
            rec['chars'] = len(rec['text'])
        (out / 'pages.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
        assert sum(s['images'] for s in ranges) == len(images)
        assert len(list(out.rglob('*.jpg'))) == len(images)
        write_json(out / 'chapters.json', dict(page_numbering='PDF pages, 1-based', chapters=ranges))
        write_json(out / 'images-manifest.json', [dict(source='images/' + n, path=t, sha256=digest(out/t)) for n,t in mapping.items()])
        rows = ['| 章节 | PDF 页码 | 图片数 |', '|---|---:|---:|']
        for s in ranges:
            rows.append(f'| [{s["title"]}]({quote(s["path"] + "/README.md")}) | {s["start_page"]}–{s["end_page"]} | {s["images"]} |')
        edition_note = ''
        if book.name == '大学物理练习册':
            edition_note = ('无答案版，适合先独立作答。按原练习号整理，共 31 个练习、62 页、77 张图片。'
                            '原文件未收录练习 11–13、27–39、48 的题目页，编号跳号按原文保留。\n\n')
        elif book.name.startswith('大学物理练习册答案'):
            edition_note = ('带答案版，按练习 1–48 整理，共 361 页、194 张图片。文件名中的“已修正部分错误”沿用来源说明，未逐题复核。\n\n'
                            '[题目与答案对照阅读](combined.md)：31 个练习有独立题目页和对应解答；其余 17 个练习仅收录答案册内容，'
                            '不表示已经补齐缺失题目页。自测时先使用[无答案版](' + quote('../大学物理练习册/README.md') + ')。\n\n'
                            '`exercises.jsonl` 记录两册练习号、题目与解答的原始页码；对照版用 `<!-- src: 练习册 p.N -->` 和 `<!-- src: 答案 p.N -->` 区分页码来源。\n\n')
        (out / 'README.md').write_text(f'# {book.name}\n\n' + edition_note + '正文与图片已按章节或练习整理。\n\n' + '\n'.join(rows) +
            '\n\n`book.md` 为全书；`pages.jsonl` 为逐页数据；`chapters.json` 为校正后的章节边界；'
            '`images-manifest.json` 记录原图片名、新路径和 SHA-256。原始 OCR 章节索引保存在 `outline.json`，可能包含误识别。'
            '\n\n原始说明保存在 `README-original.md`，原压缩包保留。OCR 公式和文字未经逐字校对。\n', encoding='utf-8')
        summaries.append(dict(book=book.name, pages=len(pages), images=len(images), groups=len(ranges),
                              image_bytes=sum(i.stat().st_size for i in images), image_hashes_verified=True,
                              page_coverage_verified=True, image_references_verified=True))
        root_links.append(book_link(book))
    build_combined()
    write_json(DEST / 'validation.json', summaries)
    chapter_count = sum(
        bool(re.match(r'^\d+-第[一二三四五六七八九十百\d]+章', c['title']))
        for s in summaries
        for c in json.loads((DEST / s['book'] / 'chapters.json').read_text(encoding='utf-8'))['chapters']
    )
    exercise_count = sum(s['groups'] for s in summaries if s['book'].startswith('大学物理练习册'))
    exercise_stats = f'、{exercise_count} 个练习单元（两册分别计数）' if exercise_count else ''
    exercise_note = ''
    if exercise_count:
        combined_link = quote('大学物理练习册答案(已修正部分错误)/combined.md')
        exercise_note = ('\n\n大学物理练习册分为无答案版与带答案版。无答案版收录 31 个练习，带答案版覆盖练习 1–48。'
                         f'可先独立作答，再查看[题目与答案对照版]({combined_link})。'
                         '对照版中有 17 个练习缺少独立题目页，保留答案册内容，不补造题目。')
    school_note = ('数学物理方法使用学校同步教材：姚端正等《数学物理方法（第四版）》。\n\n'
                   if any('姚端正' in s['book'] for s in summaries) else '')
    (DEST / 'README.md').write_text(f'''# PDF 教材 OCR 资源库

用于自学的 PDF 教材 OCR 资源库：按章节整理正文与插图，便于 AI 阅读、理解与辅助学习。

原始 PDF 来源于 Z-Library，经 OCR 解析后整理为 Markdown、逐页 JSON 和本地图片。希望在自学时，能直接把相关章节提供给 AI，用来解释概念、梳理推导、讨论习题，并按页码回查教材。

## 教材目录

{school_note}{chr(10).join(root_links)}

目前共 **{len(summaries)} 份教材与练习资源、{chapter_count} 个教材正文章{exercise_stats}、{sum(s['images'] for s in summaries):,} 张图片**。前言、篇导言、附录、答案与索引另行分组。{exercise_note}

## 如何用于 AI 自学

1. 从上面的教材目录进入，选择要学习的章节，打开对应的 `README.md`。
2. 把章节文件或正文提供给 AI，再说明具体问题，例如“解释这一节的概念，并按教材顺序推导公式”。
3. 涉及电路图、示意图等内容时，同时提供该章 `images/` 中的相关图片。只粘贴文字，AI 不一定能读取其中的图片链接。
4. 需要引用或核对时，使用正文中的 `<!-- page: N -->` 定位。这里的 N 是从 1 开始的 PDF 页码，可能与书上印刷页码不同。

按章学习优先使用章节文件；需要检索全书时，可使用 `book.md`，或用 `pages.jsonl` 构建逐页检索。

## 文件结构

每本教材有独立目录：

```text
教材目录/
├── README.md              # 教材说明与章节导航
├── book.md                # 全书 OCR 正文
├── pages.jsonl            # 逐页文本、图片路径和章节归属
├── chapters.json          # 整理后的章节范围与路径
├── images-manifest.json   # 图片路径与 SHA-256 校验记录
├── outline.json           # 原始 OCR 目录索引
└── chapters/
    └── 章节目录/
        ├── README.md      # 本章正文
        └── images/        # 对应页码的插图
```

仓库还保留原始 OCR 压缩包、元数据和转换脚本。`README-original.md` 为原始说明；旧压缩包和旧说明中的目录结构可能与整理后的结构不同。

## 内容质量与核对

- OCR 正文未经逐字校对，公式、上下标、希腊字母和表格可能有识别错误。关键推导和答案请对照原 PDF 核实。
- `images/` 主要是教材插图的裁剪图，不是完整的 PDF 页面。
- 已核对整理后的正文页码覆盖、图片文件哈希与正文图片链接，记录见 [validation.json](validation.json)。这些检查不代表 OCR 内容或 AI 回答一定正确。
''', encoding='utf-8')
    print(json.dumps(summaries, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
