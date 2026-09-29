# Changelog

All notable changes to the **Mullvad VPN Ebook — Free Limited Edition** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

> The Paid Full Edition is shipped separately. Changes that only affect the paid edition are **not** listed here.

## [1.0.0] — 2026-09-28

### Added

- **Initial public release** of the Free Limited Edition
- **Chapters included:** 1 (Why Mullvad VPN), 2 (The Threat Model), 18 (Multihop with SOCKS5 — *showcase*), 38 (Glossary), 39 (FAQ)
- **Dual-format source:** Markdown manuscript in `MANUSCRIPT/` driven by `MANIFEST-free.yaml`
- **Pure-Python build pipeline** (`build/`) — no Pandoc dependency; `segno` for QR codes, `ebooklib` for EPUB3, `playwright` + headless Chromium for PDF, standalone HTML output
- **QR code pipeline** — every URL in `assets/qr-codes/urls.json` generates an SVG + PNG pair in the Mullvad brand palette
- **Pre-built artifacts** attached to the v1.0 release: EPUB3, screen PDF, and standalone HTML
- **Editorial-grade book sections** in every chapter: Learning Objectives, Part A (Detailed Information), Part B (90s Tutorial Walkthrough), Part C (Platform-Specific Notes), Part D (References + QR grid), Closing Encouragement
- **Brand assets directory** (`assets/brand/`) — Mullvad palette and editorial-use logo permissions reference
- **GitHub Pages-ready** standalone HTML output (self-contained, no CDN, no telemetry)
- **`LICENSE.md`** — dual license (CC BY-NC-SA 4.0 for the free edition + All Rights Reserved for the paid edition)

### Build pipeline

- `build/build-edition.sh <edition> <format>` — single-edition, single-format build
- `build/build-all.sh` — both editions, all formats (free + full)
- `build/generate-qr.py` — regenerate QR codes from manifest
- `build/generate-qr-manifests.py` — generate per-edition QR manifests from the URL list
- `build/build-{epub,pdf,html}.py` — format-specific builders

### Notes for contributors

- Pull requests welcome for typo fixes, broken-link fixes, and outdated API values — see `CONTRIBUTING.md`
- The free edition's chapter selection is locked at chapters 1, 2, 18, 38, 39
- Cover art and full-colour diagrams deferred to v1.1