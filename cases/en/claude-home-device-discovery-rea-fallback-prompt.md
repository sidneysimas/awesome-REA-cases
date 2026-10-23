# Controlling owned home devices: codila's Claude discovery workflow and REA app-analysis fallback prompt

Category: Hardware and interoperability · REA
Record date: 2026-10-23
Stage: Needs verification

At 03:34:50 Beijing time on October 23, 2026, codila (@0xCodila) promotes using Claude Opus 5.5 to bring home Wi-Fi devices under chat control, posting the full prompt at 03:34:51. Goals include router diagnosis, TV ad reduction and control, AC schedules, printing and scanning, robot vacuums and refrigerator status. Although the post claims to have reverse engineered the home, it supplies no device inventory, models, implementation or result logs, so the useful evidence is primarily a workflow idea.

It first checks that the agent is actually on the user's owned home network, then identifies devices with one ping per address, ARP, mDNS, SSDP and an authorized router client list, requiring confirmation above 256 addresses. Chip-vendor-only identities prompt a question, as do guest/IoT networks and non-networked appliances. Devices are handled individually, with router Wi-Fi changes last. Connection routes consider official APIs, open-source libraries or Home Assistant, local panels and JavaScript APIs, the official app's local protocol, then IR. If REA is already installed locally, it may inspect panel JavaScript or a vendor app; this is not a promise to break into every device.

The full prompt requires private backups, presentation of old and new values before user approval, readback after changes and an undo path; diagnose-only mode changes nothing. Users enter credentials in their own terminal into system credential storage, never chat or logs, with a stop after one failed login. Installation and administrator commands require user involvement. Flashing, exploits, password guessing, factory resets and reading saved browser credentials are prohibited. Debug access is closed afterward, and outside material is treated as data rather than instructions.

Per-device acceptance goals are not completed results: routers need before/after Wi-Fi speed tests while preserving Wi-Fi names and passwords; TVs need package/settings backups and restore scripts while protecting essential components, without uninstalling system packages or entering service menus. AC temperatures and unattended heating schedules are constrained. Printers must not receive firmware updates or network/cloud changes. Vacuums must not be rooted, reflashed or re-paired. Refrigerators must not exceed 5°C and freezers -18°C. Locks, alarms, garage doors and cameras are read-only by default with each action confirmed; heating/cooking appliances must not be started remotely. The ending must list fixed items, unfinished work, undo instructions and required user actions.

No actual tools, model-compatibility table, speed measurements, undo tests or completion record were obtained. These are prompt intentions, not safety controls proven enforced by a tool. They promise neither universal ad removal, faster Wi-Fi nor whole-home natural-language control. This collection only read text: it scanned no network, accessed no credentials, installed no integration, changed no schedule and executed no target code. The entry remains an unverified REA-related workflow idea.

Candidates originally posted 2026-10-23T03:34:50+08:00 and 03:34:51. The 256-address, 5°C and -18°C values are prompt limits, not research measurements.

## Sources

- [codila's promotion of a Claude home-device control workflow](https://x.com/i/status/2113353404470964375)
- [Same author's full prompt: discovery, REA fallback, acceptance goals and device limits](https://x.com/i/status/2113353410305204601)

[中文](../claude-home-device-discovery-rea-fallback-prompt.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
