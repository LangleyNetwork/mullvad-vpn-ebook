---
title: "Multihop with SOCKS5"
slug: "multihop-with-socks5"
---

# Chapter 18 — Multihop with SOCKS5

> **This is the showcase chapter.** You'll learn the architecture that powers SOCKS5 multihop on Mullvad, then walk through a hands-on tutorial that connects you to a Swedish server while your browser exits through the Netherlands.

## Learning Objectives

By the end of this chapter, you'll be able to:

- Explain in your own words what Multihop with SOCKS5 is and why it exists
- Configure Firefox to exit your traffic through a different country than your WireGuard tunnel
- Verify your exit IP and DNS are different from your entry tunnel
- Understand the security trade-offs of SOCKS5 multihop vs. WireGuard end-to-end multihop

---

## Part A — Detailed Information

### A.1 What Multihop with SOCKS5 Is

Multihop with SOCKS5 is the privacy feature that lets your browser traffic **exit** through a different country than the WireGuard tunnel you connected through. Concretely:

> "By connecting to any of our WireGuard® servers and configuring your browser (or other SOCKS5 compatible software) to use another WireGuard server's SOCKS5 proxy, the browser's traffic will EXIT in a different location than the WireGuard server you are connecting to. For example, you can connect using the Mullvad VPN app to a WireGuard server in Sweden, and configure your browser to use a SOCKS5 proxy in the US. Your browser traffic will then first enter a server in Sweden and then exit through a server the US."
>
> — Mullvad Help: https://mullvad.net/en/help/different-entryexit-node-using-wireguard-and-socks5-proxy

In other words:

```
Without SOCKS5 multihop:
  You → [WireGuard tunnel] → Exit Server → Internet
            ↑ entry↓ from your ISP ↑

With SOCKS5 multihop:
  You → [WireGuard tunnel] → Entry Server → SOCKS5 (different server) → Internet
            ↑ entry↓ from your ISP ↑                        ↑ exit↑ from different country ↑
```

The wireguard tunnel protects your traffic as it leaves your network. The SOCKS5 proxy at a different exit server determines where your traffic **appears to come from** to the websites you visit.

### A.2 Why It Matters (Threat Model Fit)

SOCKS5 multihop helps against:

- **Timing correlation attacks** — splitting your entry and exit across jurisdictions makes it harder for an adversary to correlate your entry traffic with your exit traffic
- **ISP-level logging** — your ISP only sees encrypted WireGuard traffic; the destination websites only see the exit server's IP
- **Cloudflare CAPTCHAs** — sites that block known VPN IPs will still see the exit IP; SOCKS5 multihop with the proxy's stable IP reduces CAPTCHAs (per Mullvad's docs)
- **IP-based whitelisting** — the SOCKS5 proxy provides a stable IP for whitelisting (the server's IP, not the dynamic exit of a regular tunnel)

It does **NOT** help against:

- **Root access to the entry server** — see the caveat in A.5 below
- **Browser fingerprinting** — use Mullvad Browser to address that

### A.4 Architecture (The Two SOCKS5 Endpoints Per Server)

Mullvad's WireGuard servers expose exactly **two SOCKS5 proxies**:

| SOCKS5 endpoint | Address | Reachable from where? | Purpose |
|---|---|---|---|
| **Local** | `10.64.0.1:1080` | Inside the WireGuard tunnel to **this same server** | The "single-hop" SOCKS5; same exit IP as the connected server |
| **Peer-reachable** | `10.124.0.x:1080` | From any other WireGuard server, via Mullvad's inter-server overlay | SOCKS5 multihop exit; `.x` is unique per server |

Verbatim from Mullvad:

> "All our WireGuard servers have two SOCKS5 proxies listening on them:
> • The SOCKS5 proxy on 10.64.0.1 with port 1080 which is not reachable from other WireGuard servers.
> • The SOCKS5 proxy on 10.124.0.x to 10.124.1.x with port 1080 which is reachable from other WireGuard servers. These IPs are unique for each WireGuard server. For instance, 10.124.0.4 belongs to nl-ams-wg-001 and 10.124.0.2 belongs to se-mma-wg-001."
>
> — Mullvad Help: https://mullvad.net/en/help/socks5-proxy/ (dateModified 2026-07-30)

For browser-based SOCKS5 multihop, you use the **public hostname** that DNS-resolves to one of Mullvad's servers. The hostname is:

```
xx-xyz-wg-socks5-###.relays.mullvad.net
```

For example, to exit via `nl-ams-wg-001`, you use `nl-ams-wg-socks5-001.relays.mullvad.net:1080`.

### A.5 Specifications (Verified Live, 2026-09-28)

| Property | Value |
|---|---|
| SOCKS5 endpoints | Two per WireGuard server |
| SOCKS5 port | `1080/tcp` (always) |
| Local address | `10.64.0.1` (always the same; per-server routing handles the magic) |
| Peer address | `10.124.0.x` through `10.124.1.x` (unique per server) |
| SOCKS5 protocol version | SOCKS5 |
| Encryption | None at SOCKS5 level; HTTPS on top protects content |
| DNS handling | "Proxy DNS when using SOCKS v5" recommended (browser-level) |
| Total WireGuard servers | 553 |
| Verified example | `se-mma-wg-001` → SOCKS5 alias `se-mma-wg-socks5-001.relays.mullvad.net` |
| Verified example | `nl-ams-wg-001` → SOCKS5 alias `nl-ams-wg-socks5-001.relays.mullvad.net` |

### A.6 Caveats and Warnings (Verbatim, Reproduced Prominently)

> ⚠️ **THE BIG SECURITY CAVEAT — PLEASE READ BEFORE USING**
>
> "Note: This technique to jump from one server to another is generally called Multihop, however, even though all traffic between the WireGuard servers are encrypted, if someone has root access to the first server and the user data transported is not encrypted, the person with root access can see the data. If the data is encrypted with HTTPS the person with root access can see the domain names that are accessed (root access is something that only sysadmins at Mullvad have) and IP-addresses used. This is no different from our normal OpenVPN solution. However Multihop using our WireGuard guide protects even from root access to the entry server since it has end-to-end encryption. If you use the WireGuard configuration generator to enable multihop you can still use SOCKS5 as described here and add a third hop."

In plain English: **SOCKS5 multihop does not protect against root access to the entry server.** If you're worried about that, use **WireGuard multihop** (Chapter 19) for end-to-end encryption.

Other caveats:

- The SOCKS5 proxy only works when you're connected to Mullvad VPN. If you disconnect, the proxy is unreachable. (This is actually a feature: it's a kill switch for the browser.)
- "Proxy DNS when using SOCKS v5" must be enabled in Firefox for DNS leak protection. Enabling it disables the Mullvad app's DNS content blockers.
- Edge (Windows) does NOT enable IPv6 SOCKS5 proxy — only IPv4.

---

## Part B — 90s Tutorial Walkthrough ("Now, you do it!")

### B.1 What You'll Need

- A working Mullvad VPN subscription (Ch 1)
- The Mullvad app installed and connected to `se-mma-wg-001` (or any server; we'll use Sweden for this walkthrough)
- Firefox installed (we'll use Firefox for this walkthrough)
- A terminal (Terminal.app on macOS, PowerShell on Windows, gnome-terminal / xterm on Linux)
- About 20 minutes

### B.2 Objectives

In this walkthrough, you'll:

1. Confirm your baseline (no SOCKS5)
2. Configure Firefox with `10.64.0.1:1080` (single-hop SOCKS5)
3. Configure Firefox with `nl-ams-wg-socks5-001.relays.mullvad.net:1080` (multi-hop SOCKS5)
4. Verify each step's exit IP

### B.3 Step 1. Confirm your baseline (no SOCKS5).

Open your terminal and run:

```
curl https://am.i.mullvad.net
```

The output is your current exit IP (the IP of the Mullvad server you're connected to). In our walkthrough, you'll see a Swedish IP — because we connected to `se-mma-wg-001`. Write it down.

***Tip:*** The `am.i.mullvad.net` endpoint exists specifically for this purpose. There's an IPv4 variant (`ipv4.am.i.mullvad.net`) and an IPv6 variant (`ipv6.am.i.mullvad.net`) for testing each protocol.

### B.4 Step 2. Connect to `se-mma-wg-001`.

Open the Mullvad app. **Switch location** → **Sweden** → `se-mma-wg-001`. Wait for the connection to establish.

Alternatively via the Mullvad CLI:

```
mullvad relay set hostname se-mma-wg-001
mullvad connect
```

Confirm by re-running:

```
curl https://am.i.mullvad.net
```

You should still see a Swedish IP (since you're connected to a Swedish server).

### B.5 Step 3. Configure Firefox to use the single-hop SOCKS5 proxy.

Open Firefox. Navigate to:

```
about:preferences#general
```

Scroll down to **Network Settings** → click **Settings...**. The Connection Settings dialog opens.

A popup options box:

```
  Configure Proxy Access:
  ○ Use system proxy settings
  ○ Auto-detect proxy settings
  ○ Use automatic proxy configuration script
  ● Manual proxy configuration

  SOCKS Host:  10.64.0.1
  SOCKS Port:  1080

  [✓] Proxy DNS when using SOCKS v5
```

Click the radio button for **Manual proxy configuration**. In the **SOCKS Host** field, type `10.64.0.1`. In the **SOCKS Port** field, type `1080`. Tick the checkbox **"Proxy DNS when using SOCKS v5"** (this is critical for DNS leak protection). Click **OK**.

***Gotcha:*** Firefox has separate fields for HTTP Proxy and SOCKS Host. Make sure you're filling in the SOCKS fields, not HTTP. The HTTP fields should be **empty**.

***Tip:*** "Proxy DNS when using SOCKS v5" routes DNS through the SOCKS5 tunnel. Without this, your browser would resolve DNS via your system DNS (likely leaking to your ISP), even though the connection itself is tunneled.

### B.6 Step 4. Verify the single-hop SOCKS5 proxy.

Open a **new tab** in Firefox (the existing tab may have cached the old connection). Visit:

```
https://am.i.mullvad.net
```

You should see a **different Swedish IP** than your baseline. That's because the SOCKS5 proxy has its own stable exit IP (different from the WireGuard tunnel's dynamic exit IP).

***Tip:*** Open a **private window** (Cmd-Shift-P on macOS, Ctrl-Shift-P on Windows/Linux) to avoid cookies and cache influencing the test. Private windows start fresh.

Confirm by visiting the same URL in your terminal:

```
curl https://ipv4.am.i.mullvad.net --socks5-hostname 10.64.0.1
```

This is the command-line equivalent. You should see the same IP as Firefox shows.

### B.7 Step 5. Reconfigure Firefox for multi-hop SOCKS5 (the real Multihop).

Now the magic step. Go back to **about:preferences#general** → **Network Settings** → **Settings...**. Replace:

```
  SOCKS Host:  nl-ams-wg-socks5-001.relays.mullvad.net
  SOCKS Port:  1080
```

The SOCKS Host is now a hostname, not an IP. Click **OK**.

***Gotcha:*** Make sure you type the hostname EXACTLY. The `relays.mullvad.net` suffix is required. A typo will give you a confusing error.

### B.8 Step 6. Verify multi-hop SOCKS5 (the showcase).

Open a **new tab** (and/or private window). Visit:

```
https://am.i.mullvad.net
```

You should now see a **Dutch IP** — even though your WireGuard tunnel is still going to Sweden. That's the multihop in action: Swedish entry, Dutch exit.

Verify with the command line:

```
curl https://ipv4.am.i.mullvad.net --socks5-hostname nl-ams-wg-socks5-001.relays.mullvad.net
```

Same Dutch IP.

***Tip:*** The curl command should be from the SAME machine — not from inside Firefox. Your terminal will use your system's SOCKS5 settings (or the explicit `--socks5-hostname` flag). Firefox uses its own SOCKS5 settings.

### B.9 Step 7. Confirm IPv6 exit.

Mullvad's SOCKS5 proxies support dual-stack. To verify your IPv6 exit:

```
curl https://ipv6.am.i.mullvad.net --socks5-hostname nl-ams-wg-socks5-001.relays.mullvad.net
```

You'll see a `2a03:1b20:...` style IPv6 address (Mullvad uses this AS range). The exit IP for IPv6 will be different from your IPv4 exit — that's expected (each proxy has both an IPv4 and IPv6 address, both unique).

### B.10 Step 8. Confirm DNS is not leaking.

Visit https://dnsleaktest.com and click **Extended Test**. After the test runs, the DNS servers shown should NOT be your ISP's. They should be either Mullvad's DNS (set by the tunnel) or "no servers found" (your browser's DNS is going through the SOCKS5 tunnel, which is the intended behavior).

If you see your ISP's DNS, double-check:

1. Firefox's "Proxy DNS when using SOCKS v5" is ticked
2. The SOCKS Host is `nl-ams-wg-socks5-001.relays.mullvad.net` (or another valid SOCKS5 alias), not an IP that doesn't resolve
3. Your Mullvad tunnel is still up (the SOCKS5 proxy only works inside the tunnel)

### B.11 Step 9. Restore your normal settings.

When you're done testing, restore Firefox's network settings to **Use system proxy settings** (or whatever you had before). Otherwise all your browser traffic will keep going through the Dutch exit.

You can also disable the Mullvad tunnel (Settings → Disconnect) when you're done — Firefox will then have no proxy to use and won't be able to reach the internet.

***Gotcha:*** This is actually the kill-switch bonus of SOCKS5 multihop. If you forget to disable the SOCKS5 proxy in Firefox and you disable the Mullvad tunnel, Firefox will refuse to connect to anything — preventing accidental leaks.

### B.12 Summary

| New concept | Meaning |
|---|---|
| **Multihop with SOCKS5** | WireGuard tunnel + SOCKS5 proxy at a different server |
| **`10.64.0.1:1080`** | The single-hop SOCKS5 (same exit as your tunnel) |
| **`xx-xyz-wg-socks5-###.relays.mullvad.net`** | The hostname for a specific server's SOCKS5 |
| **Multi-hop SOCKS5** | Tunnel to one server, exit through a different one |
| **DNS leak** | Without "Proxy DNS when using SOCKS v5", DNS may leak |
| **Kill-switch bonus** | If the tunnel drops, the SOCKS5 proxy becomes unreachable |

| New command | Meaning |
|---|---|
| `curl https://am.i.mullvad.net` | See your current exit IP |
| `curl --socks5-hostname 10.64.0.1 <url>` | Route through the single-hop SOCKS5 |
| `curl --socks5-hostname nl-ams-wg-socks5-001.relays.mullvad.net <url>` | Route through the multihop SOCKS5 |
| `mullvad relay set hostname se-mma-wg-001` | Pick a specific WireGuard tunnel entry |

### B.13 Exercises

1. **Try a different exit country.** Pick a different SOCKS5 alias — e.g., `us-nyc-wg-socks5-204.relays.mullvad.net` (if it exists in the API). Set it in Firefox. Visit `am.i.mullvad.net`. **→ What country does your exit IP show?**

2. **Test DNS leak prevention.** With multihop configured, visit https://dnsleaktest.com. Run the extended test. **→ What DNS servers does it report?**

3. **Test IPv6 + IPv4 simultaneously.** Run both curl commands in two terminal tabs:

   ```
   curl https://ipv4.am.i.mullvad.net --socks5-hostname nl-ams-wg-socks5-001.relays.mullvad.net
   curl https://ipv6.am.i.mullvad.net --socks5-hostname nl-ams-wg-socks5-001.relays.mullvad.net
   ```

   **→ Are the IPs in the same country? Are they from the same subnet?**

4. **Test the kill switch.** With Firefox configured for SOCKS5 multihop, disconnect the Mullvad app. Try to load any page in Firefox. **→ What happens?** (Hint: it should refuse to connect — that's the kill switch.)

---

## Part C — Platform-Specific Notes

### C.1 macOS / Windows / Linux (Firefox)

Same steps as above. Firefox's network settings dialog is identical across platforms.

### C.2 Chrome / Chromium (Command-Line Flag)

Chrome doesn't expose SOCKS5 settings in the GUI — you need to launch it from the command line:

```
chromium-browser --proxy-server=socks5://10.64.0.1:1080
```

For multi-hop:

```
chromium-browser --proxy-server=socks5://nl-ams-wg-socks5-001.relays.mullvad.net:1080
```

To force WebRTC to not leak:

```
chromium-browser \
  --proxy-server=socks5://nl-ams-wg-socks5-001.relays.mullvad.net:1080 \
  --force-webrtc-ip-handling-policy \
  --webrtc-ip-handling-policy=disable_non_proxied_udp
```

### C.3 Firefox About:Config DNS

By default, Firefox uses the system DNS. The "Proxy DNS when using SOCKS v5" option in the network settings dialog overrides this for SOCKS5 connections.

For tighter control, visit `about:config` and set:
- `network.proxy.socks` = `nl-ams-wg-socks5-001.relays.mullvad.net`
- `network.proxy.socks_port` = `1080`
- `network.proxy.socks_remote_dns` = `true`
- `network.proxy.type` = `1` (manual)

### C.4 Edge (Windows)

Edge's SOCKS5 support is similar to Chrome, but: **Edge does NOT enable IPv6 SOCKS5 proxy** (only IPv4). If you need IPv6 exit, use Firefox or Chrome.

### C.5 Mullvad Browser

Mullvad Browser includes a Mullvad extension that lets you switch location easily. Click the Mullvad icon in the toolbar → pick a city → done. No command-line flags, no about:config.

### C.6 Per-App Configs

Many apps support SOCKS5 proxies:

| App | How to configure SOCKS5 |
|---|---|
| Firefox | Settings → Network → Manual proxy |
| Chrome / Edge | `--proxy-server=socks5://...` flag |
| Telegram | Settings → Advanced → Connection type → SOCKS5 |
| Thunderbird | Settings → General → Network → Manual proxy |
| curl | `--socks5-hostname <host>` |
| SSH | `ssh -D 1080 ...` then configure app to use `127.0.0.1:1080` |

For apps that don't support SOCKS5, use `tsocks` or `proxychains` on Linux to force the app's traffic through the SOCKS5 proxy.

---

## Part D — References

The resources below are referenced throughout this chapter. Each link has a QR code for instant scanning.

| Resource | URL | QR |
|---|---|---|
| SOCKS5 proxy guide (Mullvad) | https://mullvad.net/en/help/socks5-proxy/ | [QR:socks5_proxy_doc] |
| Multihop with SOCKS5 + WG (Mullvad) | https://mullvad.net/en/help/different-entryexit-node-using-wireguard-and-socks5-proxy | [QR:multihop_socks5_wg_doc] |
| Am I Mullvad? connection check | https://am.i.mullvad.net | [QR:am_i_mullvad] |
| IPv4 connection check | https://ipv4.am.i.mullvad.net | [QR:ipv4_am_i_mullvad] |
| IPv6 connection check | https://ipv6.am.i.mullvad.net | [QR:ipv6_am_i_mullvad] |
| Mullvad homepage | https://mullvad.net | [QR:mullvad_net] |
| Mullvad WireGuard relays API | https://api.mullvad.net/www/relays/wireguard/ | [QR:api_relays_wireguard] |
| Mullvad on GitHub | https://github.com/mullvad | [QR:github_mullvad] |
| DNS leak test | https://dnsleaktest.com | (see Ch 14 for full reference) |

---

## Closing Encouragement

You just walked through the architecture that powers one of the most distinctive Mullvad features. You can now:

- Explain why there are two SOCKS5 endpoints per server
- Configure Firefox (and Chrome/Edge via flags) for both single-hop and multi-hop
- Verify your exit IP, IPv6 address, and DNS leak status
- Know that SOCKS5 multihop has caveats (no entry-server protection) and when to use WireGuard multihop instead

In **Chapter 19 (Multihop with WireGuard)**, we'll explore the end-to-end encrypted variant — which protects against root access to the entry server. **Have fun — and remember, the only person who knows your traffic is you.**