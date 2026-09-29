---
title: "Why Mullvad VPN"
slug: "why-mullvad-vpn"
---

# Chapter 1 — Why Mullvad VPN

## Learning Objectives

By the end of this chapter, you'll be able to:

- Describe Mullvad VPN's mission, ownership, and history in your own words
- Articulate what makes Mullvad different from other commercial VPNs
- Match Mullvad's features to your personal privacy threat model
- Decide whether Mullvad is the right VPN for your use case

---

## Part A — Detailed Information

### A.1 What Mullvad VPN Is

Mullvad VPN is a commercial VPN service operated by **Mullvad VPN AB**, a Swedish company registered in Gothenburg under corporate number **559238-4001**. Founded in **March 2009**, Mullvad was among the first consumer VPNs to be designed around an account-number-only login model — no email, no password, no real name.

The company is wholly owned by **Amagicom AB**, which is in turn owned by its two founders: **Fredrik Strömberg** and **Daniel Berntsson**. Both founders remain actively involved in the company. The parent company's name, "Amagicom," comes from the Sumerian word *ama-gi*, which is the oldest recorded word for "freedom" — fitting for a company whose central mission is to defend personal privacy.

The current Mullvad website is at <https://mullvad.net> [QR:mullvad_net], and they also operate a Tor onion service for users who want to visit the site anonymously.

### A.2 Why It Matters (Threat Model Fit)

Mullvad's design choices map directly onto the threat models of:

- **Casual users** who don't want their ISP to log their browsing history
- **Journalists** who need to protect sources and themselves
- **Activists** who face state-level surveillance
- **Anyone in a censorship-heavy country** who needs reliable internet access
- **Privacy advocates** who believe data minimization is a fundamental right

What sets Mullvad apart from competitors is a combination of choices, not a single killer feature:

1. **Anonymous payment** — cash in envelope, Monero, Bitcoin
2. **No-logs policy** — independently audited by Cure53 (2020) and Assured AB (2023)
3. **Account-number-only login** — no email, no password, no recovery option
4. **RAM-only infrastructure** — servers cannot retain data after reboot
5. **Flat €5/month pricing** — no upsells, no "premium" tier
6. **Open source** — both client apps and significant server-side code
7. **Swedish jurisdiction + 14 Eyes** — controversial but combined with no logs, moot

> "Mullvad VPN exists to fight against mass surveillance and censorship. We do this primarily through our VPN service and our browser. We believe in a free and open society where people have the right to privacy; the right to their own beliefs and thoughts, and the right to decide for themselves exactly when and with whom they want to share them." — Mullvad Press page

### A.3 Architecture (Brief Overview)

Mullvad's network consists of two distinct populations of servers:

- **553 WireGuard servers** (live as of 2026-09-28) — the primary network. Each server has a unique hostname in the form `xx-xyz-wg-###.relays.mullvad.net` (e.g., `se-mma-wg-001`, `nl-ams-wg-001`). Each exposes two SOCKS5 proxies (one local-only at `10.64.0.1:1080` and one peer-reachable at `10.124.0.x:1080`) and one WireGuard tunnel endpoint at a unique UDP port (`multihop_port`).
- **13 Bridge servers** — OpenVPN + Shadowsocks endpoints designed to bypass censorship. Naming: `xx-xyz-br-###.relays.mullvad.net`.

You'll learn the full architecture in detail in Part IV (WireGuard + SOCKS5 Internals) of this book, but for now the key facts are:

| Server type | Count | Tunnel protocol | SOCKS5 endpoint |
|---|---|---|---|
| WireGuard | 553 | WireGuard (UDP, port varies) | `10.64.0.1:1080` + `10.124.0.x:1080` |
| Bridge | 13 | OpenVPN + Shadowsocks | None |

### A.4 Specifications

| Property | Value |
|---|---|
| Company | Mullvad VPN AB |
| Registration | 559238-4001 (Sweden) |
| Headquarters | Box 53049, 400 14 Gothenburg, Sweden |
| Parent company | Amagicom AB |
| Founded | March 2009 |
| Pricing | €5/month flat (no upsells) |
| Server count | 553 WireGuard + 13 Bridges |
| Protocols | WireGuard (preferred), OpenVPN (Bridge mode only) |
| Account model | 16-digit account number (no email, no password) |
| Payment methods | Cash, Monero, Bitcoin, voucher, credit card |
| Audit history | Cure53 (2020), Assured AB (2023) |
| Open source | Yes — github.com/mullvad |
| Tagline | "Privacy is for the people" (homepage), "Privacy is a universal right" (GitHub) |

### A.5 Caveats and Warnings

**Sweden is a 14 Eyes member.** This is the single most-cited criticism of Mullvad. Sweden has agreed to share intelligence with the UK, US, Canada, Australia, New Zealand, and eight other countries. Mullvad's counter-argument: since there are no logs to hand over, the jurisdiction matters less. Court cases (2023 Swedish police case, 2024 German case) have validated that a non-deployment of logs is genuinely enforceable — Mullvad has consistently reported they have no logs to provide.

**No free tier.** Mullvad has no free tier (unlike ProtonVPN, Windscribe, etc.). The €5/month is the only option. Operating a privacy-respecting VPN costs money; Mullvad refuses to monetize via ads or data sales.

**No 24/7 support.** Support hours are Sweden business hours, weekdays only. Email support (PGP-encrypted for sensitive matters) is the only channel.

**Bridges are NOT multihop.** Bridges solve a different problem (censorship circumvention). SOCKS5 multihop (Chapter 18) is the privacy-focused exit-chaining feature. Don't confuse the two.

---

## Part B — 90s Tutorial Walkthrough ("Now, you do it!")

### B.1 What You'll Need

- A computer (macOS, Windows, or Linux)
- A working internet connection
- An email account (optional — for backup, not required)
- About 30 minutes

### B.2 Objectives

In this walkthrough, you'll:

1. Visit Mullvad's homepage and explore the marketing site
2. Generate an account number
3. Add 30 days to your account
5. Verify your new IP

### B.3 Step 1. Visit Mullvad's homepage.

Open a web browser and navigate to:

```
https://mullvad.net
```

You'll see Mullvad's homepage with their tagline "Privacy is for the people" prominently displayed. Take a moment to read the homepage hero copy. This is Mullvad's mission in their own words. It sets the tone for everything else you'll encounter.

***Tip:*** For maximum privacy during signup, you can visit Mullvad's homepage via their Tor onion service instead. The onion URL is published on their homepage footer. Use Tor Browser to access it.

### B.4 Step 2. Generate your account number.

Click the **"Generate account number"** button on the homepage. A 16-digit number will appear on screen. **Copy this number immediately** and save it somewhere safe — you won't be able to recover it later if you lose it.

Your account number looks like this (example, do not use):

```
1234 5678 9012 3456
```

***Gotcha:*** You will NOT receive an email. You will NOT be asked for an email. This is by design. Without an email, Mullvad cannot accidentally leak your identity via a third-party email breach.

***Important:*** Write this number down. Mullvad literally cannot recover it — they have no way to verify you are who you say you are. If you lose the number, you must create a new account (and start over with time on the account).

### B.5 Step 3. Add time to your account.

Click **"Add time"** on the account page. Choose your payment method:

- **Credit card / PayPal / Swish** — easiest, fastest, but ties your identity to Mullvad
- **Cryptocurrency** (Monero or Bitcoin) — better privacy
- **Cash in envelope** — best privacy, slowest (mail to Sweden)
- **Voucher** — buy a code from an authorized reseller

For this walkthrough, use credit card to add 1 month (€5). In a follow-up chapter (Ch 36 — Pricing), we'll go deeper on anonymous payment.

### B.6 Step 4. Visit the about page.

Open <https://mullvad.net/en/about/>. You'll see the full history of the company, including:

> "March 2009 — The Mullvad VPN service launches!"

> "Mullvad VPN AB is owned by parent company Amagicom AB. The name Amagicom is derived from the Sumerian word ama-gi — the oldest word for 'freedom' or, literally, 'back to mother' in the context of slavery — and the abbreviation for communication. Amagicom stands for 'free communication'."

> "Mullvad VPN AB and its parent company Amagicom AB are 100% owned by founders Fredrik Strömberg and Daniel Berntsson who are actively involved in the company."

***Tip:*** Mullvad's history page is genuinely interesting — it shows a 17-year journey from a small Gothenburg-based startup to one of the most-respected VPN providers globally.

### B.7 Step 5. Skim the press page.

Open <https://mullvad.net/en/press/>. Note:

- The full mission statement (verbatim in Part A.2 above)
- The brand assets (logos, fonts, color palette)
- The official fonts: body = **Open Sans**, headlines = **Source Sans Pro**
- The official palette: dark blue `#192E45`, blue `#294D73`, green `#44AD4D`, red `#E34039`

This page is where journalists and authors (like the author of this book) get permission to use Mullvad's brand assets.

### B.8 Summary

| New concept | Meaning |
|---|---|
| **Account number** | 16-digit number, no email or password — your credential |
| **Mullvad VPN AB** | Legal name (Gothenburg, Sweden) |
| **Amagicom AB** | Parent company, 100% owned by founders |
| **14 Eyes** | Intelligence-sharing alliance Sweden belongs to |
| **RAM-only servers** | No persistent storage; lose state on reboot |
| **Cure53 / Assured AB** | Independent audit firms |

| New command | Meaning |
|---|---|
| (no commands yet — that's for Chapter 7 on Linux CLI) | |

### B.9 Exercises

1. **Generate a throwaway account.** Use Mullvad's homepage to generate a test account number. Don't add time — just see the flow. **→ What does the UI show you?**

2. **Try the onion service.** Open Tor Browser and navigate to the onion URL published on Mullvad's homepage footer. **→ Does the site load? Does it look different from the clearnet version?**

3. **Read the privacy policy.** Open https://mullvad.net/en/help/privacy-policy. Count how many third-party trackers the site loads. **→ Compare with another major VPN's privacy policy page. Who's cleaner?**

---

## Part C — Platform-Specific Notes

### C.1 macOS

- The Mullvad homepage renders well in Safari. Use **Get the app** → macOS for next steps (covered in Chapter 5).
- For maximum privacy during signup: use Safari with **Private Browsing** enabled (Cmd-Shift-N), or use Tor Browser.

### C.2 Windows

- The Mullvad homepage works in Edge, Chrome, and Firefox identically.
- Use **InPrivate** (Edge) or **Incognito** (Chrome) for private browsing during signup.

### C.3 Linux

- The Mullvad homepage works in all major browsers.
- For maximum privacy during signup: use Tor Browser (apt install torbrowser-launcher) and access via onion.

### C.4 iOS / Android

- The Mullvad homepage is mobile-responsive. Works in Safari (iOS) and Chrome (Android).
- For maximum privacy: download Onion Browser (iOS) or Tor Browser for Android, and access via onion.

---

## Part D — References

The resources below are referenced throughout this chapter. Each link has a QR code for instant scanning to your phone.

| Resource | URL | QR |
|---|---|---|
| Mullvad homepage | https://mullvad.net | [QR:mullvad_net] |
| About Mullvad | https://mullvad.net/en/about/ | |
| Press page | https://mullvad.net/en/press/ | |
| Privacy policy | https://mullvad.net/en/help/privacy-policy | |
| Terms of service | https://mullvad.net/en/help/terms-service | |
| Cookies policy | https://mullvad.net/en/help/cookie-policy | |
| All policies | https://mullvad.net/en/policies | |
| Mullvad on GitHub | https://github.com/mullvad | |
| Mullvad YouTube | https://www.youtube.com/c/MullvadVPNNet | |
| Mullvad on X | https://www.x.com/mullvadnet | |
| Mullvad on Mastodon | https://mastodon.online/@mullvadnet | |

---

## Closing Encouragement

That's the quick tour of Mullvad's purpose and philosophy. You now know:

- What Mullvad is (a Swedish VPN provider founded in 2009)
- Why they exist (to fight mass surveillance and censorship)
- Who owns it (the two founders, via Amagicom AB)
- What makes them different (account-number-only, anonymous payment, audited no-logs)
- How to start (generate an account, add time, log in)

In Chapter 2, we'll dig into *what VPNs can and cannot do* — the threat model. This is essential reading before you configure anything, because understanding what you're defending against shapes every decision you'll make about server choice, payment method, and feature enablement.

**Have fun — and remember, privacy is for the people.**