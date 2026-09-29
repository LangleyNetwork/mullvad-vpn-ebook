# Mullvad VPN — A Practical Guide to Privacy, Multihop, and the SOCKS5 Multihop Workflow

[![Edition: Free Limited](https://img.shields.io/badge/edition-free%20limited-294D73)](#what-this-edition-contains)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)](LICENSE.md)
[![Release: v1.0](https://img.shields.io/badge/release-v1.0-44AD4D)](https://github.com/LangleyNetwork/mullvad-vpn-ebook/releases/tag/v1.0)
[![No telemetry](https://img.shields.io/badge/telemetry-none-E34039)](#privacy)

> A 40-chapter professional reference about Mullvad VPN — its features, security model, and best-use workflows — written by **S. Langley** (Stephen Langley). This repository ships the **Free Limited Edition sampler** (Chapters 1, 2, 18, 38, 39). The full 40-chapter edition is sold separately.

- **Author:** S. Langley (Stephen Langley)
- **License:** [CC BY-NC-SA 4.0](LICENSE.md) (this free edition)
- **Repository:** <https://github.com/LangleyNetwork/mullvad-vpn-ebook>
- **First edition:** v1.0 — September 2026

---

## What this edition contains

This **Free Limited Edition** contains the showcase Multihop with SOCKS5 chapter (Ch 18) plus the introductory chapters and the glossary + FAQ. It is published as a free sampler so you can evaluate the writing quality, the depth of technical coverage, and the build pipeline before purchasing the full 40-chapter edition.

Included chapters:

1. **Why Mullvad VPN** — mission, ownership, history
2. **The threat model** — what VPNs do (and don't)
3. **Multihop with SOCKS5** *(the showcase chapter)*
4. **Glossary**
5. **FAQ**

The full source-of-truth for every chapter lives in [`MANUSCRIPT/`](MANUSCRIPT/). The free edition's chapter selection is declared in [`MANIFEST-free.yaml`](MANIFEST-free.yaml).

---

## Repository layout

```
mullvad-vpn-ebook/
├── README.md                  ← you are here
├── LICENSE.md                 ← dual license (CC BY-NC-SA + All Rights Reserved)
├── MANIFEST-free.yaml         ← edition config (chapters, marketing, pricing)
├── MANUSCRIPT/                ← canonical Markdown source (free chapters)
│   ├── 01-why-mullvad-vpn.md
│   ├── 02-threat-model.md
│   ├── 38-glossary.md
│   └── 39-faq.md
│   # (Chapter 18 — Multihop with SOCKS5 — lands in v1.0.1)
├── build/                     ← pure-Python build pipeline (open source)
│   ├── build-edition.sh       ← entry point
│   ├── build-all.sh           ← both editions end-to-end
│   ├── build-epub.py          ← EPUB3 via ebooklib
│   ├── build-pdf.py           ← PDF via Playwright + headless Chrome
│   ├── build-html.py          ← standalone HTML
│   ├── generate-qr.py         ← segno QR pipeline
│   └── generate-qr-manifests.py
├── assets/
│   ├── qr-codes/              ← URL list + QR manifests (PNG/SVG gitignored — regenerated)
│   ├── covers/                ← cover art (deferred to v1.1)
│   ├── diagrams/ascii/        ← ASCII topology diagrams
│   └── brand/                 ← brand assets (editorial use only)
├── .github/                   ← issue + PR templates
├── CHANGELOG.md
└── CONTRIBUTING.md
```

Files **not** in this repository (by design):

- `MANIFEST-full.yaml` — paid-edition metadata (kept in a private sibling directory)
- `out/` — generated artifacts (regenerate locally with `bash build/build-all.sh`)
- `memory/` — internal research mirror
- `docs/superpowers/` — internal planning notes
- `prompts/` — agent-internal authoring prompts

See [`.gitignore`](.gitignore) for the full exclusion list.

---

## Building this edition

Requires Python 3.11+, [`segno`](https://pypi.org/project/segno/), [`ebooklib`](https://pypi.org/project/EbookLib/), [`pyyaml`](https://pypi.org/project/PyYAML/), and (for PDF) [`playwright`](https://playwright.dev/python/) with the Chromium browser installed.

```bash
# one-time setup
python3 -m pip install --user segno ebooklib pyyaml playwright
python3 -m playwright install chromium

# build the free edition (EPUB + PDF + HTML)
bash build/build-all.sh

# outputs land in out/free/{epub,pdf,html}/
ls out/free/
xdg-open out/free/html/index.html
```

For finer control:

```bash
bash build/build-edition.sh free epub      # EPUB3 only
bash build/build-edition.sh free pdf       # PDF only
bash build/build-edition.sh free html      # standalone HTML only
bash build/generate-qr.py                  # regenerate QR codes (SVG + PNG)
```

---

## Downloading a pre-built copy

If you just want to read the book and don't need to rebuild it from source, grab the latest release:

**[v1.0 release page →](https://github.com/LangleyNetwork/mullvad-vpn-ebook/releases/tag/v1.0)**

Pre-built artifacts include:

- `mullvad-vpn-ebook.epub` — EPUB3 (works in Calibre, Apple Books, Kobo, PocketBook, etc.)
- `mullvad-vpn-ebook.pdf` — screen PDF
- `mullvad-vpn-ebook.html` — standalone HTML (single-folder)

All artifacts are reproducible from source via the build pipeline.

---

# The Full Edition — Available Now

The **Full Edition** contains all **40 chapters**, ~350 pages, every chapter with:

- **Part A** — Detailed information (verbatim Mullvad quotes, architecture, specifications, caveats)
- **Part B** — A 90s-style hands-on tutorial walkthrough ("Now, you do it!")
- **Part C** — Platform-specific notes for macOS, Windows, Linux, iOS, Android, and routers
- **Part D** — A QR-coded reference grid (every link is scannable)

Full-edition pricing: **$9.99 USD · €9.99 · £7.99**

Buy the Full Edition at any of these stores:

| Store | Format |
|---|---|
| **Amazon Kindle** | Kindle (MOBI/AZW3) + Paperback |
| **Apple Books** | EPUB3 |
| **Kobo** | EPUB |
| **Google Play Books** | EPUB |
| **Samsung Books** *(via Draft2Digital)* | EPUB |
| **Gumroad** | EPUB + PDF + MOBI bundle |
| **Leanpub** | EPUB + PDF + MOBI |
| **Smashwords** *(via Draft2Digital)* | EPUB (also B&N, libraries, Scribd) |
| **Lulu** *(paperback + hardcover)* | Print PDF |
| **itch.io** | EPUB + PDF (pay-what-you-want) |

*(Direct store links are pinned in the README of the Gumroad listing above and at the end of every chapter in the pre-built files.)*

> Direct store links live on the [Releases page](https://github.com/LangleyNetwork/mullvad-vpn-ebook/releases/tag/v1.0) and at the end of every chapter in the pre-built files.

---

## What the Full Edition adds

- **35 additional chapters** — installation on every platform, server network deep-dive, WireGuard + SOCKS5 internals, multihop variants (WireGuard end-to-end, 2026 modes, configuration decision tree), bridge mode + Shadowsocks, DAITA, split tunneling, kill switch, port forwarding, Mullvad Browser, custom DNS, Mullvad CLI, WireGuard config generator, router deployment, multi-device + family use, performance tuning, logs + diagnostics, PGP support workflow, pricing, refunds, reseller + careers + open source
- **Extended Glossary + FAQ**
- **Complete back-matter** (about Mullvad, contact, social URLs, PGP fingerprint, colophon, no-endorsement disclaimer)
- **QR codes for every URL in the entire book**

---

## Contributing

Pull requests welcome for typo fixes, broken links, outdated API values, and missing URLs. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow.

The build pipeline is fully open-source — fork it, republish your own version, or learn from it. The pipeline is pure Python (no Pandoc), uses `segno` for QR codes, `ebooklib` for EPUB3, and Playwright + headless Chromium for PDF rendering.

---

## About the author

**S. Langley** (Stephen Langley) is a privacy-focused developer and writer. This book is the result of independent research into Mullvad VPN's official documentation and live infrastructure as of September 2026. The author has no affiliation with Mullvad VPN AB.

## No endorsement

This book is not affiliated with, endorsed by, sponsored by, or reviewed by Mullvad VPN AB. "Mullvad" is a trademark of Mullvad VPN AB. The "Mullvad" wordmark and logo are used in this book under the editorial usage guidelines published at <https://mullvad.net/en/press/>. "WireGuard" is a registered trademark of Jason A. Donenfeld. All other trademarks are the property of their respective owners.

Mention of third-party products, services, and trademarks is for informational purposes only and does not constitute endorsement.

---

## Privacy

This repository contains no tracking, analytics, telemetry, or third-party CDN assets. The HTML build is fully self-contained. The build pipeline makes no network calls beyond fetching URL lists already present in the QR manifest.

---

*© 2026 S. Langley (Stephen Langley). Free Limited Edition licensed under [CC BY-NC-SA 4.0](LICENSE.md).*