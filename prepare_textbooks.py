"""Build a chapter-organized upload copy; never modify the source books."""
import hashlib
import json
from pathlib import Path
import re
import shutil
from urllib.parse import quote

SOURCE = Path(r'D:\杂项\work\教材')
DEST = Path(r'D:\杂项\work\textbooks-github')


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def safe(title):
    return re.sub(r'[<>:"/\\|?*]', '_', title).strip().rstrip('.')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def boundaries(book, outline):
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
    result += [(395, '10-封底')] if '复变' in book.name else [(546, '16-索引与封底')]
    return result


def main():
    if (DEST / '.git').exists():
        raise SystemExit(f'Output is already a Git repository: {DEST}')
    DEST.mkdir(exist_ok=True)
    shutil.copy2(SOURCE / 'pipeline.py', DEST / 'pipeline.py')
    shutil.copy2(Path(__file__), DEST / 'prepare_textbooks.py')
    (DEST / '.gitignore').write_text('__pycache__/\n*.pyc\n', encoding='utf-8')
    (DEST / '.gitattributes').write_text('*.md text eol=lf\n*.json text eol=lf\n*.jsonl text eol=lf\n*.jpg binary\n*.zip binary\n', encoding='utf-8')
    summaries = []
    root_links = []
    for book in SOURCE.iterdir():
        if not (book / 'book.md').exists():
            continue
        out = DEST / book.name
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
        (out / 'book.md').write_text(rewrite(original).replace('图片位于 `../images/`', '图片按章节存于 `chapters/*/images/`'), encoding='utf-8')
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
        (out / 'README.md').write_text(f'# {book.name}\n\n正文与图片已按章节整理，习题归入相应章。\n\n' + '\n'.join(rows) +
            '\n\n`book.md` 为全书；`pages.jsonl` 为逐页数据；`chapters.json` 为校正后的章节边界；'
            '`images-manifest.json` 记录原图片名、新路径和 SHA-256。原始 OCR 章节索引保存在 `outline.json`，可能包含误识别。'
            '\n\n原始说明保存在 `README-original.md`，原压缩包保留。OCR 公式和文字未经逐字校对。\n', encoding='utf-8')
        summaries.append(dict(book=book.name, pages=len(pages), images=len(images), groups=len(ranges),
                              image_bytes=sum(i.stat().st_size for i in images), image_hashes_verified=True,
                              page_coverage_verified=True, image_references_verified=True))
        root_links.append(f'- [{book.name}]({quote(book.name + "/README.md")})')
    write_json(DEST / 'validation.json', summaries)
    (DEST / 'README.md').write_text('# 教材\n\n' + '\n'.join(root_links) +
        '\n\n每本书位于独立目录，章节正文和对应的 `images/` 放在 `chapters/` 下。'
        '前言、目录、附录、索引单独分组；页码均为从 1 开始的 PDF 页码。'
        '\n\n3 本教材合计 35 个正文章，原始文件在本地源目录中保持不变。'
        '仓库保留全部原始压缩包、元数据和转换脚本；忽略 Python 缓存。'
        '\n\n图片按文件名中的页码归章，跨章引用使用相对路径。已核对全部图片 SHA-256、正文页码完整性和新生成正文的图片路径。'
        '详见 `validation.json`。原始 OCR 内容未逐字校对，原始归档及旧说明中的旧路径保持原样。\n', encoding='utf-8')
    print(json.dumps(summaries, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
