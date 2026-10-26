# Precursor: Claude-assisted Android ARM64 porting of OpenGOAL's Jak trilogy

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-24
Stage: In progress

The candidate is yibie's October 24, 2026 roundup at 15:30:21 Beijing time. Supplementary reading of Precursor's public README clarifies a broader target than the roundup's single-game synopsis: an unofficial, nonprofit OpenGOAL fork trying to run the PS2 games Jak 1, Jak 2 and Jak 3 natively on Android ARM64. OpenGOAL's existing decompilation, GOAL compiler, runtime and asset tools are the foundation, not work to credit to this AI-assisted fork. The OpenGOAL team neither makes, endorses nor supports the fork.

The author, thebardockgames, directs development, tests real phones and publishes releases. The README says Claude through Claude Code writes and reviews substantial portions of port code, diagnostics and documentation, with AI-assisted and Co-Authored-By commit markers. Concrete work includes an ARM64 GOAL compiler backend, C++/GOAL calling bridges, an OpenGL ES 3.2 renderer, SDL3, cubeb audio, and a launcher that extracts and compiles on the phone. AI participation does not make all of OpenGOAL or its original decompilation an AI result.

The project reports Jak 1 reaching the title, intro, menu, new game and initial gameplay at approximately 60 FPS with touch controls and audio; Jak 2 reaching the intro, title, city and prison with working collisions but remaining crashes; and Jak 3 reaching the menu, new game and first complete cutscene before a white screen. It reports passing on-device ARM64 regression tests while explicitly stating that none of the three games is verified end to end. These are not this collection's device tests or independent frame-rate measurements. Users must supply legally obtained PS2 games; no game assets are included. The supplementary README is pinned to 04ee88b20636b0975e4f7d1552f2c828f25b2671, committed October 23 Beijing time, to establish background and status rather than add another window candidate. No APK was installed and no game compiled or run.

Approximately 60 FPS, three-game booting and passing device regressions are project reports. None is verified end to end; Jak 3's white screen remains unresolved.
AI contributions concern this fork's port, launcher and diagnostics; OpenGOAL's original work and team retain separate attribution.

## Sources

- [yibie's introduction of Precursor, October 24, 2026](https://x.com/i/status/2113895858207105458)
- [Supplementary first-party Precursor README at a pinned commit, October 23, 2026 Beijing time](https://github.com/thebardockgames/Precursor/blob/04ee88b20636b0975e4f7d1552f2c828f25b2671/README.md)

[中文](../precursor-opengoal-claude-android-arm64.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
