# Kindle WeRead: Ding Hong Liam packages existing jailbreaks, KOReader and SimpleUI into an agent installation skill

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-26
Stage: Related project

At 09:28 Beijing time on October 26, 2026, Ding Hong Liam (@ding_liam) introduced a v0.1 installation skill intended to give an owned Kindle a modern home screen and WeRead access while reducing manual jailbreaking, installation and configuration. The author says Claude Code, Codex, Cursor or Grok Bot can follow the skill over USB with on-device confirmations. It enables Qiaomu SimpleUI by default, prioritizes the WeChat QR login card and refines the community plugin's interactions. The author reports success on a seventh-generation Kindle Paperwhite running firmware 5.16.2.1.1.

Public repository search identified LiamZJU/kindle-weread-skill, whose README matches the candidate's v0.1 description, device, firmware and purpose. Supplementary static reading corresponds to commit 93b1ef8caa048cb81c09fd20fa8c1798e33ee392, dated October 26 at 04:12:51 Beijing time, before the candidate; it is not another newly collected window post. The documentation explicitly reuses community jailbreaks such as WinterBreak/AdBreak, KOReader, finlater's weread.koplugin and Qiaomu SimpleUI. It does not establish discovery of a new exploit, rewritten Kindle firmware or execution of the official Android WeRead app. The helper identifies the device volume, downloads pinned packages, checks hashes and writes installation files, pausing for required on-device actions. This is narrower than the promotion's entirely hands-off wording.

The README defines completion as reaching SimpleUI on first launch, obtaining the user's own WeRead API key on a phone and logging in by QR code, then displaying a book's text. Only one KP3 with serial prefix G090 and firmware 5.16.2.1.1 is project-verified; other models and firmware are untested. It warns of warranty, bricking and third-party-client account risks and documents recovery routes, but cannot repair a device whose volume the computer cannot detect. These are not safety or recovery guarantees verified by this collection. No account credentials were requested, read or used. The skill was not installed, installation packages downloaded, a Kindle connected, target scripts executed or the result independently reproduced. The candidate does not claim REA use. This is retained as a related AI-assisted old-device adaptation project, distinct from the baseline Android firmware port and Tailscale/Readeck workflow.

Candidate engagement snapshot (October 26, 2026): 35 likes, 2,400 views and 8 reposts; later lookup growth is not substituted.
Only KP3/5.16.2.1.1 is project-reported as tested; other models are unverified. Reuses community jailbreaks, not a new exploit or Android port; not independently run.

## Sources

- [Candidate: Ding Hong Liam introduces the Kindle WeRead skill and single-device test, October 26, 2026 at 09:28 Beijing time](https://x.com/i/status/2114529444446818627)
- [Supplementary public README at pinned commit 93b1ef8, October 26, 2026 at 04:12:51 Beijing time](https://github.com/LiamZJU/kindle-weread-skill/blob/93b1ef8caa048cb81c09fd20fa8c1798e33ee392/README.md)

[中文](../ding-liam-kindle-weread-agent-installation-skill.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
