---
title: "Frequently Asked Questions"
slug: "faq"
---

# Chapter 39 — Frequently Asked Questions

> Compiled from the official Mullvad Help FAQ plus community questions.

## General

### Q: Why €5 flat? Why not a free tier?

Mullvad has no free tier. The flat €5 is intentionally simple — no upsells, no "premium" tier. Operating a privacy-respecting VPN costs money (servers, bandwidth, audits, staff); €5 covers it without surveillance-based monetization.

### Q: Is Mullvad based in a 14-Eyes country?

Yes — Sweden is a 14-Eyes member. However, Sweden has strong domestic privacy laws (Personal Data Act + GDPR). Mullvad argues (and many privacy advocates agree) that **what matters is the no-logging policy**, not the jurisdiction, because there's nothing to hand over even if compelled.

### Q: Has Mullvad ever handed over user data?

Mullvad publishes transparency reports. In every case where police or courts requested logs of a specific account, Mullvad had no data to provide (because of the no-logging policy + RAM-only infrastructure).

### Q: Do you support port forwarding?

Yes. Mullvad supports port forwarding since 2024. Configure via the Mullvad app or CLI.

### Q: Can I use Mullvad for torrenting / P2P?

Yes. Mullvad allows P2P traffic on all servers. Use the WireGuard protocol for best speeds.

## Account + Payment

### Q: I lost my account number. Can you recover it?

No. Mullvad cannot recover your account number — they don't store any identifying info. Create a new account.

### Q: Can I pay with crypto?

Yes — Bitcoin and Monero. Mullvad also accepts cash in envelope and credit cards.

### Q: Can I pay anonymously?

Yes — cash in envelope (most anonymous), Monero, or Bitcoin via Tor.

### Q: Do you accept PayPal?

PayPal support was deprecated in ~2024. Use crypto, cash, or credit card instead.

## Technical

### Q: WireGuard or OpenVPN?

**WireGuard** is faster, simpler, and Mullvad's recommended default. Use **OpenVPN** only for Bridge mode (censorship circumvention).

### Q: How do I multihop?

- **Easiest:** enable Multihop in the Mullvad app (Settings → Advanced → Multihop)
- **More control:** use SOCKS5 multihop (configure your browser to use `nl-ams-wg-socks5-001.relays.mullvad.net:1080`)

### Q: Why do I get CAPTCHAs all the time?

> "This is a known issue that happens on many sites using Cloudflare. Please follow our SOCKS5 guide to reduce the occurrence of CAPTCHAs, or you can try switching to another server."
> — Mullvad FAQ id:8

### Q: Is Shadowsocks available in the app?

> "Yes. By using Bridge mode you will be using the Shadowsocks proxy."
> — Mullvad FAQ id:54

### Q: How do I get around censorship?

> "Activate Bridge mode in the app. This will make use of the Shadowsocks proxy."
> — Mullvad FAQ id:55

### Q: How fast is Mullvad?

20 Gbps server ports (verified across samples). Real-world throughput depends on your ISP, the server's distance, and current load. Typically 500 Mbps - 2 Gbps for nearby servers.

### Q: Can I use Mullvad on my router?

Yes. See the router deployment chapter for OpenWrt and pfSense guides.

### Q: Can I use Mullvad with Netflix / BBC iPlayer?

Streaming services often detect and block VPN IPs. Mullvad tries to keep working with major services, but there's no guarantee. Switch servers if one gets blocked.

### Q: How many devices can I use simultaneously?

**5 devices** per account, enforced server-side.

## Privacy

### Q: Do you keep logs of my activity?

No. See the no-logging policy chapter for the full policy + audit history.

### Q: Do you keep logs of my IP address?

No — your real IP is only seen during WireGuard handshake, then discarded. RAM-only servers mean it's gone on reboot anyway.

### Q: Can I use Mullvad with Tor?

Yes. Connect to Mullvad, then open Tor Browser. The Tor exit node sees traffic from a Mullvad IP, not your real IP.