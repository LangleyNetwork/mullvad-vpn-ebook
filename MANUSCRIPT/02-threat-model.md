---
title: "The Threat Model"
slug: "threat-model"
---

# Chapter 2 — The Threat Model

## Learning Objectives

By the end of this chapter, you'll understand:

- What a VPN can and cannot protect
- The four-tier adversary categorization
- How Mullvad's features map to each tier
- When to use Mullvad, and when not to

---

## Part A — Detailed Information

### A.1 What a VPN Can Do

A VPN (Virtual Private Network) routes your traffic through a server operated by the VPN provider, replacing your real IP address with the VPN server's IP. This gives you several protections:

- **Hide your IP** from the websites you visit
- **Hide your DNS lookups** from your ISP (with proper DNS handling)
- **Hide the contents** of your traffic from your local network operator (your ISP, a hotel WiFi, etc.)
- **Bypass geographic restrictions** on content (Netflix, BBC iPlayer, etc.)
- **Bypass ISP-level censorship** of specific services

### A.2 What a VPN Cannot Do

A VPN is not magic. It does NOT:

- **Make you anonymous** if you log into identifiable accounts (Google, Facebook, etc.)
- **Protect against malware, phishing, or social engineering**
- **Protect against browser fingerprinting** or cookies
- **Make you invisible** to a global passive adversary capable of timing attacks
- **Replace the need for good OpSec** (password managers, 2FA, etc.)

> The fundamental law: *a VPN shifts your trust from your ISP to the VPN provider*. If the VPN provider logs your activity, you've gained nothing.

### A.3 Adversary Categorization (for the book)

#### Tier 1 — Casual observers

Public WiFi operator, your ISP, a website you visit. **Mullvad fully protects against them.**

#### Tier 2 — Local law enforcement / civil litigants

Police in your country wanting to know "who connected to X", a copyright troll wanting to identify a downloader. **Mullvad fully protects** — there are no records to subpoena.

#### Tier 3 — National intelligence agency

NSA, GCHQ, FRA, etc. Capability: passive collection at IXPs, optional collaboration with ISP.

**Mullvad partial protection.** Multihop helps. End-to-end encrypted multihop (the WireGuard variant, Ch 19) provides the strongest protection. Your *metadata* (timing, volumes) may still be inferable.

#### Tier 4 — A Global passive adversary

A hypothetical adversary with access to multiple jurisdictions simultaneously.

**Mullvad limited protection.** Only multihop with both layers (WireGuard multihop + SOCKS5 third hop) makes this difficult. Still not impossible against a patient adversary.

### A.4 When NOT to Use a VPN

- **Banking sites** often block VPN IPs (fraud prevention) — disable Mullvad to access
- **Streaming services with strong geo-restrictions** (Netflix, BBC iPlayer) may detect and block VPN IPs
- **When you need real identity** for a service (your bank's fraud detection)

### A.5 When TO Use a VPN

- **Always** when on public WiFi
- **Always** when downloading or sharing content you don't want logged
- **Often** when you want geographic content distribution
- **Frequently** when working with sensitive information (journalism, activism)
- **As a baseline** for daily browsing to deny your ISP visibility

---

## Part B — 90s Tutorial Walkthrough

### B.1 What You'll Need

- A working browser
- An honest assessment of who you're worried about

### B.2 Objectives

1. Map your concerns to a threat tier
2. Choose the right Mullvad features for that tier
3. Set up your account with appropriate payment

### B.3 Step 1. Identify your adversary.

Write down — on paper, ideally — who you're worried about seeing your traffic. Common answers:

- "My ISP" → Tier 1
- "A nosy landlord or IT department" → Tier 1
- "Local law enforcement" → Tier 2
- "A foreign state-level adversary" → Tier 3
- "A global passive adversary" → Tier 4

### B.4 Step 2. Pick the Mullvad features that match.

| Tier | Recommended Mullvad features |
|---|---|
| 1 | Default config + ad-blocking DNS |
| 2 | Default config + Mullvad Browser + ad-blocking DNS |
| 3 | Multihop (WireGuard end-to-end) + DAITA + Monero payment |
| 4 | Multihop + DAITA + SOCKS5 third hop + Monero + onion service + dedicated laptop |

### B.5 Step 3. Choose your payment method.

| Tier | Recommended payment |
|---|---|
| 1 | Credit card is fine |
| 2 | Credit card or voucher |
| 3 | Bitcoin via Tor or Monero |
| 4 | Cash in envelope + Monero |

***Gotcha:*** Payment method matters because **your payment ties to your identity** (bank, exchange, mailing envelope). A no-logs VPN can only protect you from the network layer; the payment layer is separate.

### B.6 Summary

| Tier | Adversary | Mullvad protection |
|---|---|---|
| 1 | Casual observers (ISP, public WiFi) | Complete |
| 2 | Local law / copyright trolls | Complete |
| 3 | National intelligence | Partial (multihop helps) |
| 4 | Global passive | Limited (only multi-layer helps) |

### B.7 Exercises

1. **Write down your threat model.** Spend 10 minutes listing: who are you protecting from? What are you protecting? What trade-offs are you willing to make? → Keep this as a reference.

2. **Match your threat to Mullvad features.** Use the table in Step 2 to pick your configuration. → Be honest about whether you're Tier 1 or Tier 3.

3. **Check your browser fingerprint.** Visit https://coveryourtracks.eff.org (run by the EFF) → See how unique your browser fingerprint is. Mullvad Browser masks this; regular Chrome/Firefox do not.

---

## Part C — Platform-Specific Notes

The threat model applies uniformly across platforms. What's different is the *implementation* — Mullvad Browser, kill switch settings, etc.

| Platform | Best practice |
|---|---|
| macOS | Enable kill switch; use Mullvad Browser for sensitive browsing |
| Windows | Enable "Always require VPN"; disable IPv6 |
| Linux | Configure iptables-based kill switch; mullvad status for monitoring |
| iOS | Always-on VPN; Mullvad Browser for sensitive browsing |
| Android | Always-on VPN + Block connections without VPN |

---

## Part D — References

| Resource | URL | QR |
|---|---|---|
| Mullvad homepage | https://mullvad.net | [QR:mullvad_net] |
| Mullvad on X | https://www.x.com/mullvadnet | |
| EFF Cover Your Tracks | https://coveryourtracks.eff.org | |

---

## Closing Encouragement

The threat model is the foundation of every privacy decision you'll make. If you skipped it because it felt abstract — go back and write yours down. **Have fun — and think before you click.**