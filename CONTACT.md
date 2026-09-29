# Mullvad VPN Book — Author Contact & PGP Information

> Use this information to verify the integrity of the book files and contact the author.

## Author

**S. Langley** (Stephen Langley)

## Contact

- **Email:** `langleycmd@gmail.com` *(primary)*
- **PGP fingerprint:** `A781EF83F8ECCC2B7850459B709A29A39885AD8E`
- **PGP key:** RSA 4096, created 2026-09-19, uid `Langley CMD <langleycmd@gmail.com>`
- **Keyserver:** https://keys.openpgp.org/search?q=A781EF83F8ECCC2B7850459B709A29A39885AD8E

## PGP Signing Key for Book Files

This book was signed with a dedicated project key:

- **PGP fingerprint:** `508C4AC59EEEC280E088247B33AD6D25004DB838`
- **Algorithm:** EdDSA (Ed25519)
- **uid:** `Langley eBook Signing <ebooksign@langley.services>`
- **Public key:** See `SIGNATURES/ebook-signing-public-key.asc`

To verify any signed book file:

```bash
# Import the project signing key
gpg --import SIGNATURES/ebook-signing-public-key.asc

# Verify a book file
gpg --verify SIGNATURES/full-epub.asc out/full/epub/mullvad-vpn-ebook.epub
# Expected: "Good signature from Langley eBook Signing <ebooksign@langley.services>"
```

## Social Media

### Author

| Platform | URL | Handle |
|---|---|---|
| **Email** | `langleycmd@gmail.com` | — |
| **GitHub** | https://github.com/LangleyNetwork | @LangleyNetwork |
| **LinkedIn** | https://www.linkedin.com/in/stephenlangley | @stephenlangley |
| **Mastodon** | https://mastodon.social/@stephenlangley | @stephenlangley@mastodon.social |
| **X (Twitter)** | https://www.x.com/stephenlangley | @stephenlangley |
| **YouTube** | https://www.youtube.com/@stephenlangley | @stephenlangley |
| **Personal site** | https://langley.services | stephen@langley.services |

### Publisher

- **Publisher:** S. Langley (Stephen Langley)
- **Site:** https://langley.services
- **GitHub org:** https://github.com/LangleyNetwork
- **Ebooks portal:** https://langleynetwork.github.io/mullvad-vpn-ebook/

## Subject of the Book (Mullvad VPN)

The book is *about* Mullvad VPN — these are the official Mullvad channels (for technical support, account help, press inquiries):

| Channel | URL / Contact |
|---|---|
| **Website** | https://mullvad.net |
| **Support email** | `support@mullvadvpn.net` |
| **Press email** | `press@mullvad.net` |
| **Mullvad PGP key** | fingerprint `291F CE63 2170 E5D9 005F 1556 3A91 DB0E 8DA8 01C4` |
| **X (Twitter)** | https://www.x.com/mullvadnet |
| **Mastodon** | https://mastodon.online/@mullvadnet |
| **YouTube** | https://www.youtube.com/c/MullvadVPNNet |
| **GitHub** | https://github.com/mullvad |
| **Tor onion service** | `http://o54hon2e2vj6c7m3aqqu6uyece65by3vgoxxhlqlsvkmacw6a7m7kiad.onion` |

## Verifying Downloads

Each download comes with a `.asc` signature in `SIGNATURES/`:

| Edition | File | Signature |
|---|---|---|
| Full | `out/full/epub/mullvad-vpn-ebook.epub` | `SIGNATURES/full-epub.asc` |
| Full | `out/full/pdf/mullvad-vpn-ebook.pdf` | `SIGNATURES/full-pdf.asc` |
| Full | `out/full/html/index.html` | `SIGNATURES/full-html.asc` |
| Full | `out/full/docx/mullvad-vpn-ebook.docx` | `SIGNATURES/full-docx.asc` |
| Free | `out/free/epub/mullvad-vpn-ebook.epub` | `SIGNATURES/free-epub.asc` |
| Free | `out/free/pdf/mullvad-vpn-ebook.pdf` | `SIGNATURES/free-pdf.asc` |
| Free | `out/free/html/index.html` | `SIGNATURES/free-html.asc` |
| Free | `out/free/docx/mullvad-vpn-ebook.docx` | `SIGNATURES/free-docx.asc` |

## Trademark Notice

- "Mullvad" and the Mullvad logo are trademarks of **Mullvad VPN AB** (Sweden, reg. no. 559238-4001)
- "WireGuard" is a registered trademark of **Jason A. Donenfeld**
- All other trademarks are the property of their respective owners

This book is **not affiliated with, endorsed by, sponsored by, or reviewed by** Mullvad VPN AB. Mention of Mullvad's trademarks is purely descriptive (the book documents the service).

---

© 2026 S. Langley (Stephen Langley). All rights reserved (Full Edition).
Free Limited Edition released under CC BY-NC-SA 4.0.
