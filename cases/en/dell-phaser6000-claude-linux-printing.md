# Dell / Phaser 6000: restoring Arch printing and diagnosing a legacy driver with Claude

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At 21:19 Beijing time on October 20, 2026, Xiao Tan (tvytlx) recounts a general practitioner's approximately one-hour Claude Code session to print from a 2011 Dell color laser printer on Arch Linux. The account says the USB ID identified a rebadged Xerox Phaser 6000 using HBPL v1, while the attempted foo2zjs route supported only v2. An AUR package was found, and a July 2025 Wayback Machine archive reportedly supplied the vendor ZIP after the official link stopped working; its SHA256 was compared with PKGBUILD.

Reported troubleshooting includes blank PDF pages: an offline run through the CUPS filter showed 0% ink, then Ghostscript rewrote the ReportLab PDF. A request for two copies produced four because both CUPS and the old driver duplicated them; an eight-line wrapper reportedly fixed this. Toner levels were also parsed from USB status strings and compared with the printer's display bars. The account retains an agent error: claiming installation had finished while compilation was still running, then correcting itself. The human entered sudo passwords.

Writing an open-source 64-bit driver based on others' existing format research and testing it on hardware is a future plan, not an implemented driver. The hour, estimated two days of manual work, matching hash and toner comparison are all secondhand claims. The doctor's original account, exact Dell model, package hash, wrapper and test logs were not obtained, and this collection did not print. Reusing a legacy binary driver is not complete from-scratch protocol recovery.

## Sources

- [Xiao Tan's account of legacy Dell printer recovery, driver diagnosis and a future rewrite](https://x.com/i/status/2112534046769111446)

[中文](../dell-phaser6000-claude-linux-printing.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
