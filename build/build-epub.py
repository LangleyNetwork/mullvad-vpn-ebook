#!/usr/bin/env python3
"""build-epub.py — Build EPUB3 from MANUSCRIPT/ + per-edition manifest."""
import sys, re, yaml
from pathlib import Path

CHAPTERS_DIR = Path(__file__).resolve().parent.parent / "MANUSCRIPT"
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


def md_to_html(text, chapter_title=""):
    import markdown
    md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'toc'])
    body = md.convert(text)
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">\n'
        f'<head><title>{chapter_title}</title></head>\n'
        f'<body>{body}</body>\n'
        '</html>'
    )


def embed_qr(html, qr_png_dir):
    """Replace [QR:slug] placeholders with inline base64 PNGs."""
    import base64
    def replace(m):
        slug = m.group(1)
        png_path = qr_png_dir / f"{slug}.png"
        if png_path.exists():
            data = base64.b64encode(png_path.read_bytes()).decode()
            return (
                f'<figure class="qr-code">'
                f'<img src="data:image/png;base64,{data}" alt="{slug} QR" '
                f'width="100" height="100" />'
                f'</figure>'
            )
        return m.group(0)
    return re.sub(r'\[QR:(\S+?)\]', replace, html)


def build_edition(manifest_path, output_path):
    from ebooklib import epub
    manifest = yaml.safe_load(Path(manifest_path).read_text())
    qr_png_dir = ASSETS_DIR / "qr-codes" / "png"

    book = epub.EpubBook()
    book.set_identifier(f"mullvad-vpn-ebook-{manifest['edition']}-v1-2026")
    book.set_title(manifest.get('title', 'Mullvad VPN — A Practical Guide'))
    book.set_language('en')
    book.add_author(manifest['author']['aka'])

    chapters = []
    spine = ['cover', 'nav']

    # Cover
    cover_html = (
        '<html><body>'
        '<div style="text-align:center; padding:50px; background:#192E45; color:white; height:90vh;">'
        '<h1 style="font-size:3em; color:#FFD524;">Mullvad VPN</h1>'
        '<h2 style="font-size:1.5em;">A Practical Guide</h2>'
        f'<p style="font-size:1.1em;">{manifest.get("title_suffix","")}</p>'
        f'<p style="margin-top:300px;">{manifest["author"]["aka"]}</p>'
        '<p style="font-size:0.9em;">Edition ' + manifest['edition'] + ' · v1.0 · September 2026</p>'
        '</div></body></html>'
    )
    cover_ch = epub.EpubItem(uid="cover", file_name="cover.xhtml", media_type="application/xhtml+xml", content=cover_html.encode())
    book.add_item(cover_ch)

    # Chapters
    marketing = manifest.get('marketing_block', '')
    for ch_num in manifest['chapters']['include']:
        ch_files = sorted(CHAPTERS_DIR.glob(f"{ch_num:02d}-*.md"))
        if not ch_files:
            print(f"  WARN: No chapter file for {ch_num}, skipping")
            continue
        ch_path = ch_files[0]
        title = ch_path.stem.replace(f'{ch_num:02d}-', '').replace('-', ' ').title()
        print(f"  + Chapter {ch_num}: {ch_path.name}")
        html = md_to_html(ch_path.read_text(), title)
        html = embed_qr(html, qr_png_dir)
        if marketing:
            html += f'<div class="marketing"><pre>{marketing}</pre></div>'
        ch = epub.EpubHtml(title=title, file_name=f"chapter-{ch_num:02d}.xhtml", content=html.encode())
        book.add_item(ch)
        chapters.append(ch)
        spine.append(ch)

    book.toc = tuple(chapters)
    book.spine = spine
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(output_path, book)
    size_kb = Path(output_path).stat().st_size // 1024
    print(f"  ✓ Wrote {output_path} ({size_kb} KB)")


if __name__ == '__main__':
    edition = sys.argv[1] if len(sys.argv) > 1 else 'free'
    manifest_path = Path(__file__).resolve().parent.parent / f"MANIFEST-{edition}.yaml"
    output_path = Path(__file__).resolve().parent.parent / f"out/{edition}/epub/mullvad-vpn-ebook.epub"
    build_edition(manifest_path, output_path)