#!/usr/bin/env python3
"""generate-qr.py — Read URL manifest, generate SVG + PNG per URL with brand styling."""
import json, sys, os
from pathlib import Path

# Brand spec — kept in sync with feedback-mullvad-ebook-qr-styling-2026-09
MULLVAD_BRAND = {
    'blue':       '#294D73',
    'dark_blue':  '#192E45',
    'green':      '#44AD4D',
    'red':        '#E34039',
    'yellow':     '#FFD524',
    'brown':      '#D2943B',
    'beige':      '#FFCD86',
}

DEFAULT_FG = MULLVAD_BRAND['dark_blue']
DEFAULT_BG = '#FFFFFF'
ERROR_CORRECTION = 'H'
QUIET_ZONE = 4


def slugify(url: str) -> str:
    s = url.replace('https://', '').replace('http://', '')
    for c in '/:?.=&%#':
        s = s.replace(c, '_')
    return s.strip('_').lower()[:80]


def generate_one(url, label, out_svg, out_png, fg=DEFAULT_FG, bg=DEFAULT_BG, size_px=600):
    import segno
    qr = segno.make(url, error=ERROR_CORRECTION)
    slug = slugify(url)
    svg_path = out_svg / f"{slug}.svg"
    png_path = out_png / f"{slug}.png"
    qr.save(str(svg_path), scale=4, border=QUIET_ZONE, dark=fg, light=bg)
    qr.save(str(png_path), scale=max(1, size_px // 25), border=QUIET_ZONE, dark=fg, light=bg)
    return {
        'url': url,
        'slug': slug,
        'label': label,
        'svg': str(svg_path),
        'png': str(png_path),
        'svg_size_bytes': svg_path.stat().st_size,
        'png_size_bytes': png_path.stat().st_size,
    }


def main(manifest_path, out_root):
    manifest_path = Path(manifest_path)
    out_root = Path(out_root)
    manifest = json.loads(manifest_path.read_text())
    out_svg = out_root / 'svg'
    out_png = out_root / 'png'
    out_svg.mkdir(parents=True, exist_ok=True)
    out_png.mkdir(parents=True, exist_ok=True)

    generated = []
    errors = 0
    for entry in manifest.get('urls', []):
        try:
            r = generate_one(
                entry['url'], entry['label'],
                out_svg, out_png,
                fg=entry.get('fg', DEFAULT_FG),
                bg=entry.get('bg', DEFAULT_BG),
            )
            generated.append(r)
            print(f"  ✓ {r['slug'][:50]:50s} → SVG {r['svg_size_bytes']:5d}B  PNG {r['png_size_bytes']:5d}B")
        except Exception as e:
            errors += 1
            print(f"  ✗ {entry['url']}: {e}")

    manifest['generated'] = generated
    manifest_path.write_text(json.dumps(manifest, indent=2))
    total = len(manifest.get('urls', []))
    print(f"\nGenerated {len(generated)}/{total} QR codes ({errors} errors)")
    print(f"SVG: {out_svg}")
    print(f"PNG: {out_png}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: generate-qr.py <manifest.json> <out-dir>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])