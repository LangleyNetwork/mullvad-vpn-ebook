# Attributions

## Research Sources

This book synthesizes information from Mullvad VPN's official documentation. Every technical claim is traceable to one or more of these primary sources:

- **Mullvad Help Center** — <https://mullvad.net/en/help/>
  - SOCKS5 proxy guide
  - Multihop with SOCKS5 + WireGuard guide
  - Multihop with WireGuard guide
  - FAQ
- **Mullvad Press page** — <https://mullvad.net/en/press/>
  - Mission statement (verbatim in Ch 1)
  - Brand assets, fonts (Open Sans + Source Sans Pro), color palette
- **Mullvad API** — <https://api.mullvad.net/www/relays/>
  - 553 WireGuard relays + 13 bridge relays
  - Per-server `multihop_port` (range 3002–3622)
  - SOCKS5 endpoints, DAITA capability flags, public keys
- **Mullvad Blog** — <https://mullvad.net/blog>
  - "Introducing Multihop Modes" (2026-08-24)

## Audits Referenced

- **Cure53** (June 2020) — penetration test of Mullvad's infrastructure
- **Assured AB** (June 2023) — no-logging policy audit

## Author

**S. Langley** (Stephen Langley) — author, designer, and publisher.

## Tools Used

### AI Pair-Programmer

**[Claude Code](https://claude.com/claude-code)** was used throughout the creation of this book as a development and research tool, including:

- Synthesizing Mullvad's official documentation into a unified manuscript
- Drafting all 40 chapters in the established voice (90s-tutorial style + technical prose)
- Designing and building the manuscript-to-EPUB/PDF/HTML/DOCX pipeline (pure-Python, no Pandoc)
- Composing the cover design (full-page flush composition at 3000×4500)
- Generating QR codes for every URL via `segno`
- Designing the Web3 NFT integration (Polygon ERC-1155 + IPFS + AES-256-GCM)
- Writing all build, publish, and infrastructure scripts

**Claude Code is used as a tool, not a co-author.** All editorial decisions, factual claims, and creative direction are the author's alone.

### Open-Source Libraries

| Library | Use |
|---|---|
| `segno` | QR code generation |
| `ebooklib` | EPUB3 builder |
| `playwright` + `google-chrome` | PDF + HTML rendering |
| `python-docx` | Microsoft Word output |
| `Pillow` | Cover image processing |
| `svglib` + `reportlab` | SVG diagram conversion (initial approach) |
| `pyyaml` | Manifest parsing |
| `markdown` | Markdown → HTML conversion |
| `cryptography` | AES-256-GCM encryption for paid edition |

### Infrastructure

- **GitHub** — version control + Pages hosting
- **Polygon mainnet** — NFT contract deployment (planned)
- **Pinata / web3.storage** — IPFS pinning for the DApp + book bundles (planned)

## License

**The Free Limited Edition** is licensed under **CC BY-NC-SA 4.0** — see `LICENSE.md`.

**The Full Edition** is **All Rights Reserved** — see the buy-links in the README.

## Trademark Notice

- "Mullvad" and the Mullvad logo are trademarks of **Mullvad VPN AB** (Sweden, reg. no. 559238-4001)
- Used here under the editorial usage guidelines published at <https://mullvad.net/en/press/>
- "WireGuard" is a registered trademark of **Jason A. Donenfeld**
- All other trademarks are the property of their respective owners

This book is **not affiliated with, endorsed by, sponsored by, or reviewed by** Mullvad VPN AB.

---

© 2026 S. Langley (Stephen Langley). All rights reserved (Full Edition).

---

## Author Contact

**S. Langley** (Stephen Langley)

- **Email:** `langleycmd@gmail.com`
- **PGP fingerprint:** `A781EF83F8ECCC2B7850459B709A29A39885AD8E`
- **Book signing key fingerprint:** `508C4AC59EEEC280E088247B33AD6D25004DB838`
- **GitHub:** https://github.com/LangleyNetwork

### Social Media

- LinkedIn: https://www.linkedin.com/in/stephenlangley
- Mastodon: https://mastodon.social/@stephenlangley
- X (Twitter): https://www.x.com/stephenlangley
- YouTube: https://www.youtube.com/@stephenlangley
- Personal site: https://langley.services

## PGP-Signed Book Files

All book files (EPUB, PDF, HTML, DOCX) in both editions are PGP-signed. Detached `.asc` signatures are in the `SIGNATURES/` directory. Verification:

```bash
gpg --import SIGNATURES/ebook-signing-public-key.asc
gpg --verify SIGNATURES/full-epub.asc out/full/epub/mullvad-vpn-ebook.epub
```
