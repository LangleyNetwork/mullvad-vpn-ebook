#!/usr/bin/env python3
"""build-html.py — Standalone HTML for GitHub Pages hosting of the Free Limited Edition."""
import sys, base64, yaml
from pathlib import Path

CHAPTERS_DIR = Path(__file__).resolve().parent.parent / "MANUSCRIPT"
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
QR_DIR = ASSETS_DIR / "qr-codes" / "png"

SCREEN_CSS = """
:root { --brand-dark-blue: #192E45; --brand-blue: #294D73; --brand-green: #44AD4D; --brand-red: #E34039; }
* { box-sizing: border-box; }
body { font-family: 'Open Sans', system-ui, -apple-system, sans-serif; font-size: 17px; line-height: 1.65; color: #222; max-width: 760px; margin: 0 auto; padding: 20px; background: #fdfdfd; }
h1, h2, h3 { font-family: 'Source Sans Pro', system-ui, sans-serif; color: var(--brand-dark-blue); }
h1 { font-size: 2.2em; border-bottom: 3px solid var(--brand-green); padding-bottom: 0.3em; margin-top: 1.5em; }
h2 { font-size: 1.6em; color: var(--brand-blue); margin-top: 1.8em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.2em; }
h3 { font-size: 1.25em; color: var(--brand-blue); margin-top: 1.4em; }
pre, code { font-family: 'Consolas', 'SF Mono', monospace; font-size: 0.9em; background: #f6f8fa; padding: 0.6em; border-radius: 4px; overflow-x: auto; }
pre { line-height: 1.4; padding: 1em; border-left: 4px solid var(--brand-green); }
blockquote { border-left: 4px solid var(--brand-green); padding: 0.8em 1em; background: #f6f8fa; margin: 1em 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th { background: var(--brand-blue); color: white; padding: 8px; text-align: left; }
td { border: 1px solid #ddd; padding: 8px; }
.qr-code { display: inline-block; width: 90px; height: 90px; vertical-align: middle; margin: 0 0.3em; border: 1px solid #eee; }
img { max-width: 100%; height: auto; }
nav.toc { background: #f6f8fa; padding: 1.5em; border-radius: 8px; border: 1px solid #e0e0e0; }
nav.toc ul { padding-left: 1.5em; }
nav.toc li { margin: 0.3em 0; }
nav.toc a { color: var(--brand-blue); text-decoration: none; font-weight: 600; }
nav.toc a:hover { text-decoration: underline; }
.marketing-block { margin-top: 3em; padding: 1.5em; background: linear-gradient(135deg, #192E45 0%, #294D73 100%); color: white; border-radius: 8px; }
.marketing-block pre { background: transparent; color: white; border: none; white-space: pre-wrap; }
.marketing-block a { color: #FFD524; }
@media (max-width: 720px) { body { padding: 12px; font-size: 16px; } h1 { font-size: 1.8em; } }
"""


def md_to_html(md_text):
    import markdown
    md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'toc'])
    return md.convert(md_text)


def embed_qr(html):
    import re
    def replace(m):
        slug = m.group(1)
        png_path = QR_DIR / f"{slug}.png"
        if png_path.exists():
            data = base64.b64encode(png_path.read_bytes()).decode()
            return f'<img class="qr-code" src="data:image/png;base64,{data}" alt="{slug} QR" />'
        return m.group(0)
    return re.sub(r'\[QR:(\S+?)\]', replace, html)


def build_edition(manifest_path, output_dir):
    manifest = yaml.safe_load(Path(manifest_path).read_text())
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    title = manifest.get('title', 'Mullvad VPN — Free Limited Edition')

    parts = [
        '<!DOCTYPE html>',
        '<html lang="en"><head><meta charset="utf-8">',
        f'<title>{title}</title>',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<style>{SCREEN_CSS}</style>',
        '</head><body>',
        '<header style="text-align:center; padding:30px 0; border-bottom:3px solid var(--brand-green); margin-bottom:30px;">',
        '<h1 style="font-size:2.8em; border:none; margin:0;">Mullvad VPN</h1>',
        '<p style="font-size:1.1em; color:var(--brand-blue);">A Practical Guide to Privacy, Multihop, and the SOCKS5 Multihop Workflow</p>',
        f'<p style="font-size:0.95em; color:#666;">{manifest["author"]["aka"]} · {manifest["edition"].title()} Edition · v1.0 · September 2026</p>',
        '</header>',
    ]

    # TOC
    parts.append('<nav class="toc"><h2>Table of Contents</h2><ul>')
    for ch_num in manifest['chapters']['include']:
        ch_files = sorted(CHAPTERS_DIR.glob(f"{ch_num:02d}-*.md"))
        if ch_files:
            ch_path = ch_files[0]
            ch_title = ch_path.stem.replace(f'{ch_num:02d}-', '').replace('-', ' ').title()
            parts.append(f'<li><a href="#chapter-{ch_num}">Chapter {ch_num}: {ch_title}</a></li>')
    parts.append('</ul></nav>')

    # Chapters
    marketing = manifest.get('marketing_block', '')
    for ch_num in manifest['chapters']['include']:
        ch_files = sorted(CHAPTERS_DIR.glob(f"{ch_num:02d}-*.md"))
        if not ch_files:
            continue
        ch_path = ch_files[0]
        html = md_to_html(ch_path.read_text())
        html = embed_qr(html)
        html = html.replace('<h1>', f'<h1 id="chapter-{ch_num}">', 1)
        if marketing:
            html += f'<div class="marketing-block"><pre>{marketing}</pre></div>'
        parts.append(html)

    parts.append('</body></html>')

    output_path = Path(output_dir) / 'index.html'
    output_path.write_text('\n'.join(parts))
    size_kb = output_path.stat().st_size // 1024
    print(f"  ✓ Wrote {output_path} ({size_kb} KB)")


if __name__ == '__main__':
    edition = sys.argv[1] if len(sys.argv) > 1 else 'free'
    manifest_path = Path(__file__).resolve().parent.parent / f"MANIFEST-{edition}.yaml"
    output_dir = Path(__file__).resolve().parent.parent / f"out/{edition}/html"
    build_edition(manifest_path, output_dir)