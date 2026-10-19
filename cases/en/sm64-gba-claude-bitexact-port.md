# sm64-gba: Claude adapts a human-made decompilation with frame-by-frame GBA physics oracles

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-19
Stage: In progress

At 12:13 Beijing time on October 19, @riabcevv describes Kodoque's sm64-gba project, correcting the claim that Claude wrote Super Mario 64 for GBA: movement comes from the human-made n64decomp/sm64 project, while AI handles adaptation, optimization and strict comparisons. Supplementary research located the public Kodoque1/sm64-gba repository rather than treating the post's shortened name as an exact GitHub account. Its README attributes code, test harness and engineering notes to Claude Opus 5.5, with the developer choosing goals and tradeoffs. REA use is unconfirmed.

The goal is bit-identical movement and collision within a 16.78 MHz ARM7 GBA budget without an FPU. Unmodified decompilation code supplies the strict IEEE reference. Host, ARM and GBA builds receive identical inputs and compare state every frame. The README reports 23 scripts and 53,139 frames, requires both deliberately broken builds to fail, and supplements replay with 12 million direct collision queries. A 683-frame position replay of the playable four-level demo is reported bit-identical. This coverage does not prove all game behavior correct.

Commit e45fdfadfc1582a5cdb46d3ef7223bfd0385fa8f, dated October 19 at 04:56 Beijing time, adds mGBA/NanoBoyAdvance comparisons, a bench ROM logging to cartridge save RAM and random power-on memory checks. The project reports 30 FPS on 99.9%/99.8% of a 1,228-frame tour in the two emulators. This is a fixed route, not a full-game frame-rate guarantee. GitHub test run 39172132182, created at 06:25 Beijing time, was completed/success when queried. That verifies project CI status only: this collection did not execute code, rerun the oracle or operate a GBA.

Real GBA hardware remains untested. The demo has no enemies, coins, platforms or doors, and uses simplified visuals, a replacement follow camera and adaptive resolution. The default renders collision meshes and a neutral mannequin; users can import models and scenery from their own ROM, but the original ROM is not distributed. This is a scoped porting and verification project built on human decompilation, not AI rediscovering original source, a completed full game or a hardware playthrough. Supplementary repository and CI records are earlier engineering evidence, not new candidates from this window.

October 19 candidate snapshot: 2 likes, 69 views and 0 reposts; engagement establishes neither test coverage nor hardware compatibility.

## Sources

- [Candidate: riabcevv separates human decompilation from Claude adaptation](https://x.com/i/status/2112034312769900668)
- [Public README: scope, oracles, performance and hardware limits](https://github.com/Kodoque1/sm64-gba/blob/e45fdfadfc1582a5cdb46d3ef7223bfd0385fa8f/README.md)
- [October 19, 04:56 supplementary commit: two emulators and power-on memory checks](https://github.com/Kodoque1/sm64-gba/commit/e45fdfadfc1582a5cdb46d3ef7223bfd0385fa8f)
- [Public test run 39172132182: successful when queried](https://github.com/Kodoque1/sm64-gba/actions/runs/39172132182)

[中文](../sm64-gba-claude-bitexact-port.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
