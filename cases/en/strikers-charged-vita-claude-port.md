# Mario Strikers Charged: a Claude-assisted PS Vita port directed and console-tested by a human

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-26
Stage: In progress

At 15:30 Beijing time on October 25, 2026, yibie's resource update separately introduced a native PS Vita port of Mario Strikers Charged, saying AI involvement was identified through 19 commit trailers. Public-repository lookup identifies CBOC-Vita-Lab/strikers-charged-vita. Its goal is to run the Wii football game on Vita: documentation describes rebuilding game code for the Vita processor, rewriting the renderer for its graphics chip and adapting buttons, touch, audio and saves rather than streaming or full-console emulation. These are project implementation statements, not console verification by this collection.

README credits explicitly describe coding by Claude and other AI assistants, directed and play-tested on real hardware by a human. The work builds on yannicksuter/mscharged-decomp, vitaGL and VitaSDK; prior decompilation must not all be attributed to new AI work. Commit e80d886, dated October 24 at 04:50:42 UTC, credits Claude Opus 5.5 and reports moving expressive facial skinning to the GPU and reducing repeated decoding. It reports 16% fewer ARM instructions per frame in the replay renderer thread and 3% fewer in the game thread, a project measurement rather than this collection's benchmark. REA use is unconfirmed.

The README at fixed commit 4fbe675, dated October 25 at 03:43:38 UTC, reports version 1.1 reaching up to 60 fps in light scenes, usually 30 fps, about 20–25 fps for goal replays and celebrations, and about 0.1 seconds of normal input delay. Up to 60 fps is not a locked frame rate throughout. Known issues, scene-dependent performance and further work remain documented. Users need their own Wii USA Rev 1 game data; this collection supplies no game, package or operating instructions.

This is a previously deferred project. Supplementary public commits and documentation predate the October 26 00:00–04:00 window and establish identity, AI division of labor and concrete limits. The candidate's six stars, 4,146 files and 19 trailers were not recounted and do not verify capability. No dependencies were installed, code executed, game assets downloaded or native execution, performance, input and saves independently tested. It remains in progress. The README now explicitly credits AI collaboration, so the candidate's implication that only trailers disclose AI involvement is not repeated.

In progress; builds on mscharged-decomp, vitaGL and VitaSDK. Human direction and project console tests are not independent reproduction by this collection.
Version 1.1 performance is project-reported and scene-dependent. REA use is unknown; no original game data is distributed.

## Sources

- [Previously deferred candidate: yibie introduces the Vita port, October 25, 2026 Beijing time](https://x.com/i/status/2114258253253329233)
- [Supplementary README and AI/human credits at fixed commit 4fbe675, October 25, 2026 UTC](https://github.com/CBOC-Vita-Lab/strikers-charged-vita/blob/4fbe6759ea0f255364666534551aee7fb3676549/README.md)
- [GPU facial-skinning implementation crediting Claude, October 24, 2026 UTC](https://github.com/CBOC-Vita-Lab/strikers-charged-vita/commit/e80d886e2f7b262defb22f9ffb1a535e174f560a)

[中文](../strikers-charged-vita-claude-port.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
