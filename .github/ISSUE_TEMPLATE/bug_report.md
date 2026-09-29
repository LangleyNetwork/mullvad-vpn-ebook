---
name: Bug report
about: Report a typo, broken link, or factual error in the free edition
title: "[bug] "
labels: ["bug", "needs-triage"]
assignees: []
---

## What is incorrect?

<!-- One sentence describing the error. -->

**Where is it?** *(file path + section/line if known)*:

```
MANUSCRIPT/01-why-mullvad-vpn.md, Part A.2, paragraph 3
```

**Currently says**:

```
<!-- Paste the exact text that is wrong -->
```

**Should say**:

```
<!-- Paste the corrected text -->
```

## Source for the correction

<!-- Paste the URL you verified the correction against. Must be a Mullvad-owned
     URL or the live api.mullvad.net JSON. PRs without a verifiable source will
     be declined. -->

```
https://mullvad.net/en/help/...
```

## Chapter(s) affected

- [ ] Ch 1 — Why Mullvad VPN
- [ ] Ch 2 — The threat model
- [ ] Ch 18 — Multihop with SOCKS5
- [ ] Ch 38 — Glossary
- [ ] Ch 39 — FAQ
- [ ] Build pipeline (`build/`)
- [ ] Other: ___________

## Severity

- [ ] Typo / grammar (low)
- [ ] Broken link (medium)
- [ ] Outdated factual claim (medium-high)
- [ ] Misleading or incorrect technical instruction (high)
- [ ] Security-impacting error (critical)

## Reproducible in pre-built artifact?

- [ ] Yes — visible in `mullvad-vpn-ebook.epub`
- [ ] Yes — visible in `mullvad-vpn-ebook.pdf`
- [ ] Yes — visible in `mullvad-vpn-ebook.html`
- [ ] N/A — source-only
- [ ] I haven't checked

## Anything else?

<!-- Add screenshots, additional context, or related issues. -->