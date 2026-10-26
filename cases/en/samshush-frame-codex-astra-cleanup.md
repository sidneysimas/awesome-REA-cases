# Samshush: Matt Silverlock uses Codex/Astra to investigate a Samsung Frame and disable selected services

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-26
Stage: Needs verification

At 01:09 Beijing time on October 26, 2026, Matt Silverlock (@elithrar) explicitly said in his Samshush launch thread that he did the work in Codex with Astra on a Windows computer using a regular Pro subscription. He initially wanted to fix receiver-volume suspend/wake issues and planned to build and sign his own firmware; Astra suggested network login instead. He credits lucataco's LG home-screen modifications and log4j's Samsung investigation, but Samshush is his independent Frame TV project, not log4j's result.

The author reports disabling or cleaning up selected microphone/listening, advertising, telemetry, presence-detection and eMudhra trust-root components, using startup scripts to reapply some changes after reboots, and turning off automatic firmware updates to avoid breakage. This describes investigating and adjusting the existing system's services, not successfully signing or flashing custom firmware.

Supplementary reading covered the public README at commit e70d2bb3800daf344b4227c452f0c630b966f446, dated October 26 at 19:35:13 Beijing time. This is after the strict candidate window and only bounds the current implementation. Documentation limits support to the Frame Pro QN65LS03FWFXZA running firmware 1301.0, describing Samsung SDB connectivity, temporary root and Python tools that save the original state, disable rather than uninstall apps, and offer restoration and an optional startup hook. It reports preserving HDMI-CEC, ARC/eARC, playback, networking, manual Art Mode and other core functions; some presence detection and hands-free voice functionality are lost, while shared sensor services need preservation. The README explicitly leaves other telemetry and microphone inputs outside coverage. Firmware updates can reset changes or patch the root route, so this does not establish elimination of all collection.

The same document credits GPT-6 Astra development; the original post does not confirm REA use. Public source and documentation do not mean this collection verified root access, reboot persistence, restoration or privacy effects. No dependencies were installed, target code executed or television connected. This remains an unverified author report with a public project, not proof that described service capabilities, the author's wording or certificate filtering demonstrate actual audio exfiltration or certificate abuse.

Author report; the supplementary README postdates the 00:00–04:00 candidate window. No code or television tests were run.
Documentation supports Frame Pro QN65LS03FWFXZA firmware 1301.0, not universal Samsung compatibility. REA use is unconfirmed.
Disables apps and selected services, not a firmware flash or proof of ending all telemetry; startup hooks and firmware updates carry risks.

## Sources

- [Candidate: Matt on Codex/Astra, Windows and the network-login suggestion, October 26, 2026 at 01:09 Beijing time](https://x.com/i/status/2114403952468910538)
- [Author's Samshush launch and service-cleanup objectives, October 26 Beijing time](https://x.com/i/status/2114403936476033220)
- [Author reports Frame, startup scripts and reboot persistence, October 26 Beijing time](https://x.com/i/status/2114403940301418754)
- [Post-window public README at fixed commit e70d2bb, October 26, 2026 at 19:35 Beijing time](https://github.com/elithrar/samshush/blob/e70d2bb3800daf344b4227c452f0c630b966f446/README.md)

[中文](../samshush-frame-codex-astra-cleanup.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
