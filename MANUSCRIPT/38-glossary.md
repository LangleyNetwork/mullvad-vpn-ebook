---
title: "Glossary"
slug: "glossary"
---

# Chapter 38 — Glossary

> A reference of VPN + Mullvad-specific terms used throughout this book.

## VPN + Tunneling

**Bridge (server)** — An OpenVPN + Shadowsocks endpoint designed to bypass censorship. Has no SOCKS5 capability. Naming: `xx-xyz-br-###.relays.mullvad.net`.

**Bridge mode** — A Mullvad app setting that routes your traffic through a Shadowsocks bridge server. For restrictive networks.

**DAITA** — **D**efense **A**gainst **I**ntegral **a**ssistants of **T**raffic **A**nalysis. Mullvad's patented traffic-analysis resistance feature. Server capability flag: `daita: true/false`.

**DNS leak** — When DNS queries leak outside the VPN tunnel, exposing the websites you visit to your ISP. Mullvad's kill switch + custom DNS prevent this.

**IP leak** — When your real IP address is exposed despite being connected to the VPN. Usually due to WebRTC (browser), IPv6 leak, or app misconfiguration.

**Kill switch** — A setting that blocks all network traffic if the VPN tunnel drops. Prevents accidental unencrypted traffic.

**Multihop** — Routing your traffic through two (or more) VPN servers in sequence. Privacy benefit against timing-correlation attacks.

**Shadowsocks** — A SOCKS5-based proxy protocol designed to look like normal HTTPS traffic. Used by Mullvad's Bridge mode.

**Split tunneling** — Routing some apps through the VPN while others use the direct internet connection. Power-user feature.

**WireGuard** — A modern VPN protocol. Fast, simple, audited. Mullvad's preferred protocol (since ~2020).

**OpenVPN** — An older but still popular VPN protocol. Slower than WireGuard but more flexible. Mullvad supports it for Bridge mode.

## Mullvad-Specific

**Account number** — A 16-digit number that serves as your only login credential. No email, no password, no name.

**Amagicom** — The parent company of Mullvad VPN AB. 100% owned by founders Fredrik Strömberg and Daniel Berntsson.

**Cure53** — Berlin security firm that audited Mullvad in 2020.

**Assured AB** — Swedish security firm that audited Mullvad's no-logs policy in 2023.

**DAITA server** — A WireGuard relay with `daita: true` in the API. Required for DAITA-enabled connections.

**Direct only** — The legacy setting name for "when a feature requires multihop, use direct connection" (replaced by "When needed" mode in 2026).

**Entry server** — The WireGuard server you connect to first. The "input" of your tunnel.

**Exit server** — The server your traffic exits to the destination website. Where your traffic "appears to come from" to the outside world.

**Mullvad Browser** — A Mullvad-curated Firefox fork with privacy hardening. Free, separate from the VPN app.

**Mullvad VPN AB** — The legal entity operating Mullvad VPN. Swedish reg. no. 559238-4001.

**Multihop_port** — The per-server WireGuard UDP listen port. Range 3002–3622 (verified 2026-09-28). Misleading name; it's the tunnel endpoint, not the SOCKS5 port.

**SOCKS5 alias** — The DNS hostname for a server's SOCKS5 listener: `xx-xyz-wg-socks5-###.relays.mullvad.net`.

**Stboot** — Mullvad's "secure boot" server property. Servers with `stboot: true` boot from a verified image.

**10.64.0.1** — The single, fixed SOCKS5 listener address on every WireGuard server. Reachable only from inside the tunnel to that server.

**10.124.0.0/16** — Mullvad's inter-server overlay network. Each WG server has a unique IP in this range.

## Security + Privacy

**Anonymity** — Not being identifiable. Distinct from privacy (which is "not being observed").

**Jurisdiction** — The country whose laws apply to a service. Sweden is Mullvad's jurisdiction.

**14 Eyes** — An intelligence-sharing alliance of 14 countries (UK, US, Canada, AU, NZ + 9 others). Sweden is a 14-Eyes member.

**Threat model** — A structured analysis of who you're protecting against, what you're protecting, and what trade-offs you're willing to make.

**Warrant canary** — A signed statement that the service has NOT received a secret gag order. If the canary disappears, infer a gag order.

**Wintun** — Windows tunneling driver used by WireGuard on Windows.

## Network

**Endpoint** — In WireGuard config, the `Endpoint = host:port` line specifies where the tunnel terminates.

**IXP** — Internet Exchange Point. Where ISPs interconnect.

**MTU** — Maximum Transmission Unit. The largest packet size. Mullvad recommends 1380 for WireGuard over most networks.

**NAT** — Network Address Translation. Hides multiple private IPs behind one public IP.

**TCP** — Transmission Control Protocol. Reliable, ordered, slower.

**UDP** — User Datagram Protocol. Unreliable, faster, used by WireGuard.

**WireGuard protocol** — UDP-based VPN. Fast, modern, in-kernel on Linux.

## Payment

**Monero (XMR)** — A cryptocurrency with strong privacy properties. Mullvad accepts it.

**Bitcoin (BTC)** — The first cryptocurrency. Less private than Monero but Mullvad accepts it.

**Voucher** — A pre-paid code redeemable for Mullvad time. Sold by resellers.

**Cash in envelope** — Most anonymous payment method. Send Swedish kronor to Mullvad's address.