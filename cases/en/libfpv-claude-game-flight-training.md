# libfpv: Claude Code-assisted Betaflight simulation inside SM64 and GTA IV for FPV practice

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-24
Stage: Related project

The candidate posted at 13:00:51 Beijing time on October 24, 2026 introduces u/Hammerill's libfpv, reportedly built with Claude Code. A real drone radio connected to a PC lets players practice throttle, turns and flying through gaps in Super Mario 64 or GTA IV without damaging a physical drone. The AI attribution comes from the candidate, not an audit here of commits or generated-code percentages. REA is not mentioned.

The supplementary hammerill/libfpv README describes real Betaflight 2025.12 running through SimITL on a separate 1 kHz simulation thread. Radio or gamepad input drives pose, cameras, OSD and motor sounds supplied to a game. The game supplies collision geometry and rendering; the library has no renderer and exposes a C API. The README links sm64ex-fpv and gtaiv-fpv integrations. Each game still needs individual integration: this is not automatic support for arbitrary games, and existing SM64 decompilation, Betaflight and SimITL must not be attributed to AI.

This is a public project related to AI-assisted game modification, not an established case of AI decompiling both games. The README is pinned to 9133485ba325ad10c8be767364e7aa599f36f93d, committed at 06:29:59 Beijing time on October 24, before this window. The 1 kHz figure is project design documentation, not this collection's performance measurement. No library was built, game launched or physical radio used; simulation fidelity and transfer to real flight training were not independently tested.

Claude Code involvement is attributed by the candidate. The 1 kHz loop, firmware version and integration architecture come from project documentation and were not run here.
Related project: no claim that AI decompiled the original games or that simulation proves real-flight training effectiveness.

## Sources

- [Candidate on Hammerill, Claude Code and FPV practice, October 24, 2026](https://x.com/i/status/2113858235912630778)
- [Supplementary first-party libfpv README at a pinned commit, October 24, 2026, before this window](https://github.com/hammerill/libfpv/blob/9133485ba325ad10c8be767364e7aa599f36f93d/README.md)

[中文](../libfpv-claude-game-flight-training.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
