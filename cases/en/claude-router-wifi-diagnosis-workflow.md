# Home router: a Claude workflow for admin-API investigation and Wi-Fi diagnosis

Category: Hardware and interoperability · REA
Record date: 2026-10-26
Stage: Needs verification

At 03:06 Beijing time on October 21, 2026, codila (0xCodila) says Claude Code reversed a home Wi-Fi router and fixed slow service in five minutes, then posts the full prompt. It tries official APIs, open-source libraries or Home Assistant before researching the admin page's JavaScript API, backing up settings, checking band, channel, width, mode, power and latency under load, and building a chat device-list/reboot tool.

At 04:46 and 05:24 the author identifies an ISP-supplied Huawei router with customized firmware, no public API or internal documentation. Claude reportedly read the panel code, traced login/device/Wi-Fi/reboot endpoints and form fields, found menu-hidden code and wrote a controller. The author explicitly used official REA skills, and the 05:24 parent confirms this is the same 03:06 investigation, not independent endpoint inspection. The original prompt permits diagnosis only, requires showing old/new settings, approval and readback, and prohibits changing network names, passwords or firmware, factory resets or unapproved reboots. Passwords stay in the system password store. These are requested constraints, not implementation guarantees.

At 16:35 Beijing time on October 26, Xiangxiang103 relays the same author's router privacy investigation. Supplementary discovery of Bodila51/reverse-engineer-Wi-Fi-router found a README with the same claims: 29 remembered devices, a TR069_INTERNET connection that cannot be disabled, June 2025 firmware and no update button. Matching attribution and workflow support updating the existing target rather than counting a new project. Pinned commit f643dd25b7577ffb17b2ddec7c2219bae5d24f5b is dated October 26 at 01:12:31 Beijing time, before the candidate; it is supplementary material, not a new candidate post. Static README/SKILL reading shows photo-led hidden-panel API research split into read-only privacy inspection and approved Wi-Fi remediation. It prohibits password guessing, exploits, SSH/telnet attempts and port scans, and requires stopping after one failed login. DNS-checking and output-masking scripts are listed, but were not run or fully audited.

The skill explicitly says TR-069 is remote-management capability, not proof of ISP spying; encrypted DNS hides lookups rather than server connections. _nomap does not apply to hidden networks or promise removal of existing location records; users rename networks themselves. Retellings' generalized ARP/nmap workflow must not be attributed as this skill's executed steps. Public guidance is now available, but exact model, raw device logs, before/after Mbps, configuration changes and actual controller output remain absent. The 29 devices and telemetry remain project reports. Neither the five-minute fix, cross-router compatibility nor complete privacy protection is established. This collection connected to or modified no device and ran no script.

October 26, 16:35 backlog candidate snapshot: 6 likes, 1,695 views, 1 repost. The 29 devices and firmware date are project reports.
Documentation was read only; no scripts were run. Remote management is not spying, and _nomap does not guarantee removal of existing records.

## Sources

- [Author's five-minute router diagnosis/fix claim](https://x.com/i/status/2112621488650011124)
- [Same thread's full prompt for API investigation, approval and configuration readback](https://x.com/i/status/2112621492370297166)
- [04:46 clarification: panel investigation before controller construction](https://x.com/i/status/2112646579517857949)
- [05:24 author update: Huawei ISP firmware, internal endpoints and official REA skills](https://x.com/i/status/2112656256599019727)
- [Backlog candidate: Xiangxiang103 relays 29 devices and the privacy skill, October 26, 2026](https://x.com/i/status/2114636916138312112)
- [Supplementary public README at pinned commit f643dd2, October 26, 2026](https://github.com/Bodila51/reverse-engineer-Wi-Fi-router/blob/f643dd25b7577ffb17b2ddec7c2219bae5d24f5b/README.md)
- [Same-commit SKILL: read-only investigation, approval and _nomap limits](https://github.com/Bodila51/reverse-engineer-Wi-Fi-router/blob/f643dd25b7577ffb17b2ddec7c2219bae5d24f5b/SKILL.md)

[中文](../claude-router-wifi-diagnosis-workflow.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
