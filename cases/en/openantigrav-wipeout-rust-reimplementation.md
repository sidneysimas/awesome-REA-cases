# OpenAntiGrav: a Rust shared-engine reconstruction of WipEout, with Pulse as the reference

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-23
Stage: In progress

At 18:09:05 Beijing time on October 23, 2026, Aman (@mdaman010) introduces OpenAntiGrav as an AI-assisted WipEout Pulse reimplementation. This review read the original thread, located topaxi/OpenAntiGrav through public repository search and inspected its README, development documentation and relevant CLAUDE.md sections. Aman is the recommender, not presented as the maintainer. The repository gives Claude Code investigation and verification rules, but no audited AI-contribution percentage. REA is not mentioned.

The README defines a clean-room Rust reimplementation of Studio Liverpool's anti-gravity racing engine, not a line-by-line transliteration of decompiled source. Pulse on PSP/PS2 is the reference; Pure, HD/Fury, 2048 and Omega Collection share the architecture. Original binary behavior is observed, recorded with evidence and a confidence score, then rebuilt from scratch. Development documentation lists Ghidra/GhidraMCP, a PSP Allegrex processor module, and PPSSPP, PCSX2, RPCS3 and Vita3K as behavioral references. CLAUDE.md says ground-truth tests requiring real game data do not run automatically in CI; ordinary CI therefore does not establish original-game parity.

The README's status table is dated October 14, 2026. Pulse has menus through racing, race modes, a campaign with medals and unlocks, records and ghosts. Some physics and weapons are checked against the original, but Zone remains partial and full-race tick parity is not claimed. Other titles still have partial campaigns or incomplete races. Split-screen and other features are documented, but this review did not check every mode or retest the candidate's LAN claim. For platforms, the README says only Linux has run natively, Windows through Wine, and Mac and iOS have not run on real hardware; Android has separate documentation. The candidate's broad works-well framing is not extended to every platform.

The supplementary README is pinned to commit e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd, dated October 22, 2026, 19:41:30 UTC: public project material predating the candidate, not a new release in this window. No game was downloaded, dependencies installed, build or browser version run, or physics independently compared. Users must supply legally obtained games; the project distributes no game content. This is an in-progress preservation project; public documentation and listed tests are not independent reproduction.

Candidate: October 23, 2026, 18:09:05 Beijing time; supplementary commit October 22, 2026, 19:41:30 UTC.
Status and tests are project reports; no game execution, test run or full platform verification here.

## Sources

- [Candidate: Aman introduces OpenAntiGrav, gameplay and platform limits, October 23, 2026](https://x.com/i/status/2113573415844241533)
- [Supplementary first-party pinned README; status table dated October 14, 2026](https://github.com/topaxi/OpenAntiGrav/blob/e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd/README.md)
- [Supplementary development guide: Ghidra, emulator behavior references and Claude rules](https://github.com/topaxi/OpenAntiGrav/blob/e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd/docs/overview/developing.md)
- [Supplementary Claude Code rules: ground-truth tests versus CI](https://github.com/topaxi/OpenAntiGrav/blob/e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd/CLAUDE.md)

[中文](../openantigrav-wipeout-rust-reimplementation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
