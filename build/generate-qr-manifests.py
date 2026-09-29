#!/usr/bin/env python3
"""generate-qr-manifests.py — Derive per-edition QR manifests from MANIFEST-*.yaml.

Reads the global URL list in assets/qr-codes/urls.json + each MANIFEST's
qr_codes_inline list, and emits per-edition manifests.
"""
import json, sys, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URLS_FILE = ROOT / "assets" / "qr-codes" / "urls.json"


def build_manifest(edition: str):
    """Read MANIFEST-<edition>.yaml + urls.json, emit manifest-<edition>.json."""
    manifest_yaml = yaml.safe_load((ROOT / f"MANIFEST-{edition}.yaml").read_text())
    urls_data = json.loads(URLS_FILE.read_text())
    inline_slugs = set(manifest_yaml.get('qr_codes_inline', []))
    edition_urls = manifest_yaml.get('qr_codes_edition', None)  # subset override

    emitted = []
    for entry in urls_data['urls']:
        slug = entry['slug']
        if edition_urls is not None and slug not in edition_urls:
            continue
        emitted.append({
            'url': entry['url'],
            'label': entry['label'],
            'chapter': entry.get('chapter'),
            'slug': slug,
            'inline': slug in inline_slugs,
            'fg': entry.get('fg', '#192E45'),
            'bg': entry.get('bg', '#FFFFFF'),
        })

    out = {
        'version': '1.0',
        'edition': edition,
        'total': len(emitted),
        'inline_count': sum(1 for e in emitted if e['inline']),
        'urls': emitted,
    }
    out_path = ROOT / "assets" / "qr-codes" / f"manifest-{edition}.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"  ✓ {out_path.name}: {len(emitted)} URLs ({out['inline_count']} inline)")


if __name__ == '__main__':
    for edition in ('free', 'full'):
        build_manifest(edition)