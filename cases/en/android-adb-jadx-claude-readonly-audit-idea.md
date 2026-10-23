# Read-only Android auditing: a Claude prompt combining adb and jadx for suspicious APKs

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-24
Stage: Needs verification

At 03:48:26 Beijing time on October 24, 2026, Raytar (@Raytar) publishes a complete Android security-audit prompt for Claude Code. The goal is to help an owner understand what suspicious apps can access and where data might go, preserving evidence before removal rather than immediately deleting software. It requires an owned phone or the owner's permission, connected through USB debugging and adb.

The workflow collects package/display names, install dates and installers, flags apps without launcher icons or with misleading system-like names, and checks accessibility, device administration, files/photos, microphone, location, SMS, notifications and overlay access. It also requests screen-off battery use, per-app traffic for the past seven days and uploads between 1 a.m. and 5 a.m. Selected APKs are pulled and decompiled with jadx to inspect server addresses, gallery/screenshot/keystroke code and upload timers. The final report should explain risk, possible data access and destinations, and an evidence-preservation, privilege-removal and password-change plan. It explicitly prohibits modification, disabling or deletion until the user requests removal.

These are prompt requirements, not proof ordinary adb access can retrieve all historical network activity. Suspicious permissions or URLs do not establish actual exfiltration. No sample hash, execution log, actual report, false-positive rate or independent test is supplied. REA is not mentioned. This prompt does not validate the author's other private-photo story, and no photos or unfamiliar servers were accessed. This collection connected no device and ran no audit; the entry is a defensive reverse-engineering workflow idea.

Source: October 24, 2026, 03:48:26 Beijing time; seven days and 1-5 a.m. are requested inspection ranges.
Read-only behavior and authorization are design requirements, not validated permission guarantees; no sample or execution results obtained.

## Sources

- [Raytar's full read-only Android adb/jadx audit prompt, October 24, 2026](https://x.com/i/status/2113719215165432302)

[中文](../android-adb-jadx-claude-readonly-audit-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
