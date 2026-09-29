#!/usr/bin/env python3
"""build-pdf.py — Markdown → HTML → PDF via Playwright/Chrome."""
import sys, asyncio, base64, yaml
from pathlib import Path

CHAPTERS_DIR = Path(__file__).resolve().parent.parent / "MANUSCRIPT"
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

PRINT_CSS = """
@page { size: A4; margin: 2cm 1.8cm 2.5cm 1.8cm;
  @bottom-center { content: counter(page); font-size: 9pt; color: #666; }
}
@page :first { margin-top: 0; }
body { font-family: 'Open Sans', 'Source Sans Pro', sans-serif; font-size: 10.5pt; line-height: 1.55; color: #1a1a1a; max-width: 720px; margin: 0 auto; padding: 20px; }
h1 { font-family: 'Source Sans Pro', sans-serif; font-size: 26pt; color: #192E45; border-bottom: 3pt solid #44AD4D; padding-bottom: 6pt; margin-top: 30pt; page-break-before: always; }
h2 { font-family: 'Source Sans Pro', sans-serif; font-size: 16pt; color: #294D73; margin-top: 1.4em; border-bottom: 1pt solid #e0e0e0; padding-bottom: 0.2em; }
h3 { font-size: 13pt; color: #294D73; margin-top: 1.2em; }
pre, code { font-family: 'Consolas', monospace; font-size: 9pt; background: #f5f5f5; padding: 0.5em; border-radius: 3pt; }
pre { page-break-inside: avoid; line-height: 1.4; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; page-break-inside: avoid; }
th { background: #294D73; color: white; padding: 0.5em; text-align: left; }
td { border: 1pt solid #ddd; padding: 0.5em; }
blockquote { border-left: 4pt solid #44AD4D; padding-left: 1em; color: #333; background: #f6f8fa; margin: 1em 0; }
.qr-code { display: inline-block; vertical-align: middle; margin: 0 0.3em; width: 70pt; height: 70pt; }
img { max-width: 100%; }
.marketing-block { margin-top: 2em; padding: 1.5em; background: #192E45; color: white; border-radius: 4pt; }
.marketing-block pre { background: transparent; color: white; }
.cover { text-align: center; padding-top: 25vh; page-break-after: always; }
.cover h1 { font-size: 48pt; border: none; color: #FFD524; }
hr.page-break { page-break-after: always; border: 0; }
"""


def md_to_html(md_text):
    import markdown
    md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'toc'])
    return md.convert(md_text)


def embed_qr(html, qr_png_dir):
    """Replace [QR:slug] placeholders with inline base64 PNGs."""
    import re
    def replace(m):
        slug = m.group(1)
        png_path = qr_png_dir / f"{slug}.png"
        if png_path.exists():
            data = base64.b64encode(png_path.read_bytes()).decode()
            return (
                f'<img class="qr-code" src="data:image/png;base64,{data}" '
                f'alt="{slug} QR" />'
            )
        return m.group(0)
    return re.sub(r'\[QR:(\S+?)\]', replace, html)


async def build_edition(manifest_path, output_path):
    from playwright.async_api import async_playwright
    manifest = yaml.safe_load(Path(manifest_path).read_text())
    qr_png_dir = ASSETS_DIR / "qr-codes" / "png"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    parts = []
    parts.append(
        '<div class="cover">'
        '<h1>Mullvad VPN</h1>'
        '<p style="font-size:1.4em;color:#294D73;">A Practical Guide to Privacy, Multihop, and the SOCKS5 Multihop Workflow</p>'
        f'<p style="margin-top:200px;font-size:1.2em;">{manifest["author"]["aka"]}</p>'
        '<p style="font-size:0.9em;color:#666;">Edition ' + manifest['edition'] + ' · v1.0 · September 2026</p>'
        '</div>'
    )

    marketing = manifest.get('marketing_block', '')
    for ch_num in manifest['chapters']['include']:
        ch_files = sorted(CHAPTERS_DIR.glob(f"{ch_num:02d}-*.md"))
        if not ch_files:
            print(f"  WARN: No chapter file for {ch_num}, skipping")
            continue
        ch_path = ch_files[0]
        print(f"  + Chapter {ch_num}: {ch_path.name}")
        html = md_to_html(ch_path.read_text())
        html = embed_qr(html, qr_png_dir)
        if marketing:
            html += f'<div class="marketing-block"><pre>{marketing}</pre></div>'
        parts.append(html)

    full_html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        f'<style>{PRINT_CSS}</style></head><body>'
        + '<hr class="page-break">'.join(parts)
        + '</body></html>'
    )

    debug_html = Path(output_path).with_suffix('.html')
    debug_html.write_text(full_html)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path='/usr/sbin/google-chrome')
        page = await browser.new_page()
        await page.goto(f"file://{debug_html.resolve()}")
        await page.wait_for_load_state('networkidle')
        await page.pdf(
            path=output_path,
            format='A4',
            print_background=True,
            margin={'top': '20mm', 'right': '18mm', 'bottom': '25mm', 'left': '18mm'},
            display_header_footer=True,
            header_template='<div style="font-size:8pt;color:#888;width:100%;text-align:center;"><span class="title"></span></div>',
            footer_template='<div style="font-size:8pt;color:#888;width:100%;text-align:center;padding:0 18mm;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
        )
        await browser.close()

    size_kb = Path(output_path).stat().st_size // 1024
    print(f"  ✓ Wrote {output_path} ({size_kb} KB)")


if __name__ == '__main__':
    edition = sys.argv[1] if len(sys.argv) > 1 else 'free'
    manifest_path = Path(__file__).resolve().parent.parent / f"MANIFEST-{edition}.yaml"
    output_path = Path(__file__).resolve().parent.parent / f"out/{edition}/pdf/mullvad-vpn-ebook.pdf"
    asyncio.run(build_edition(manifest_path, output_path))