# Contributing to the Mullvad VPN Ebook

Thank you for your interest in improving this book. Pull requests are welcome for **typo fixes, broken links, outdated API values, and missing URLs**. This document explains the workflow and the scope of accepted contributions.

## Scope of accepted contributions

The Free Limited Edition is the canonical, free, open-source edition. The following changes are always welcome:

- **Typo and grammar fixes** in `MANUSCRIPT/*.md`
- **Broken-link fixes** — if a URL in any chapter or in `assets/qr-codes/urls.json` returns 404, opens the wrong page, or has moved, update it
- **Outdated factual corrections** that you can verify against a current Mullvad-owned URL (e.g. `https://mullvad.net/en/help/...`) or the live `https://api.mullvad.net/www/relays/wireguard/` API
- **Missing URLs** — if you spot a chapter referencing a Mullvad resource that lacks a QR entry, add it to `assets/qr-codes/urls.json` and (if applicable) `assets/qr-codes/manifest-free.json`
- **Build pipeline improvements** — bug fixes, dependency updates, portability fixes, and documentation improvements to `build/*.py` and `build/*.sh`

## Out of scope

The following changes will be declined because they belong to the paid Full Edition, not this free repository:

- **Adding new chapters** beyond the five in the free edition (1, 2, 18, 38, 39). The chapter plan is fixed at 40 chapters across two editions; the 35 paid chapters live in a private sibling directory and are not contributed to from this repo.
- **Editing `MANIFEST-full.yaml`** — this file is excluded from the public repo (see `.gitignore`).
- **Adding brand assets** beyond editorial use — Mullvad's logo and palette are trademarks; do not add commercial usage beyond the editorial guidelines at <https://mullvad.net/en/press/>.
- **Reformatting the writing voice** — the 90s-tutorial walkthrough voice is intentional. Voice-rule changes belong in an issue for discussion, not a direct PR.

## Workflow

1. **Open an issue first** for non-trivial changes. For typos and one-line fixes, you can skip directly to a PR.
2. **Fork the repository** and create a topic branch: `git checkout -b fix/broken-socks5-url` (or similar).
3. **Make your change** in the smallest, most focused commit you can.
4. **Run the build locally** to verify nothing is broken:

   ```bash
   bash build/build-all.sh
   xdg-open out/free/html/index.html   # visually verify
   ```

5. **Open a Pull Request** against `main`. Use the PR template (`.github/PULL_REQUEST_TEMPLATE.md`).
6. **Wait for review**. PRs are reviewed by the maintainer (S. Langley). Expect 1–14 days.

## Source-attribution rule

Every factual claim must trace to a Mullvad-owned URL or to the live `api.mullvad.net/www/relays/` API. If you add a new fact, cite the source URL inline in the chapter and add it to `assets/qr-codes/urls.json` so a QR code is generated for it.

Do **not** invent numbers, IPs, port ranges, relay names, or any technical detail. If you cannot verify a number, open an issue and ask.

## Style

- Markdown is the source of truth (no Pandoc-specific extensions).
- Use the per-chapter template already established (Learning Objectives, Parts A–D, Summary, Exercises). New sections should fit the existing structure.
- Wrap prose at 100 characters.
- Imperative voice for walkthrough steps ("Click *Generate account number*").
- Third-person, technical voice for detailed-info sections.

## Versioning

This repository follows [Semantic Versioning](https://semver.org/) for the ebook itself:

- **Major** (`v2.0`) — restructured edition, new chapter set, license change
- **Minor** (`v1.1`) — new chapter added, significant rewrite, new section
- **Patch** (`v1.0.1`) — typo fixes, broken-link fixes, build-pipeline patches

## No telemetry, no third-party CDN assets

This repository and its build pipeline make no third-party CDN requests, embed no analytics, and ship no telemetry. Please keep it that way — no PR adding Google Fonts, jsDelivr, Cloudflare, or any external runtime dependency will be accepted.

## License

By contributing, you agree that your contributions will be licensed under the same [CC BY-NC-SA 4.0](LICENSE.md) license as the rest of this free edition.

## Questions?

Open an issue or email **S. Langley** at the address published in the back-matter of the pre-built PDF.

---

*Thank you for helping make this book more accurate, more useful, and more honest.*