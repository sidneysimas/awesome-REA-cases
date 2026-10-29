# Forza Motorsport 4: AI-assisted static recompilation with hardware-bounded frame-rate comparisons

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-29
Stage: In progress

At 19:44:22 Beijing time on October 29, 2026, The Gaming Emporium reports i2kiselev's Forza Motorsport 4 static recompilation. Supplementary reading obtained the README and guide/performance.md at commit 0be771c68af81af5d74ca2e2c6284ec6b6642207, timestamped 09:13:11Z that day, or 17:13:11 within the candidate window. The documents explicitly acknowledge AI assistance in code, scripts, documentation and game-binary reverse engineering, without specifying models or REA use.

ShiftGlue translates original PowerPC code ahead of time into C++ compiled for x86-64, with Vulkan graphics. The project builds on arcanite24's Pinyon Shift and ShiftGlue fork, crediting ReXGlue, Xenia and the earlier fm4-recomp. FM4-specific depth, camera and object motion feed DLSS/FSR 2/FSR 3. Other features include keyboard controls, in-game graphics settings, Disc 2 and DLC. Inherited runtime and renderer work is not attributed to this author or AI building everything from scratch.

The README supports up to 5120×2880 and a 240 fps ceiling, not a combined measurement. The project's 0.3.0 test uses a Ryzen 7 5700X3D, 32 GB DDR4-3600, RTX 4070 Ti SUPER 16 GB and Windows 10 Pro 22H2, racing at Bernese Alps against eleven AI cars for roughly twelve seconds per row. Figures are medians of three runs, with upscaling off and the Console preset. At 1x/2x/3x/4x, average rates are 233/232/156/102 fps; 4x is 5K. The same PC running a pinned Xenia Canary revision records 102/88/68/45. The project reports 2.3–2.6× speed, not a universal result across tracks, GPUs or configurations. The 170 Hz display is distinct from rendering throughput.

Reported play tests include World Tour to Expert Division, about thirty Event List races, Free Play, garage, replays and saving. Split screen, wheels and most AMD/Intel GPUs are untested. Windows 10 2004+ x64 is current; Linux and wheels remain roadmap items, and Xbox LIVE/Kinect are unsupported. Only specified PAL/USA 1.0 Disc 1 versions are supported, not Rev 1/1.1. Users provide legal game files and generate the executable locally; original assets and prebuilt games are not distributed.

These are developer documents and secondary reporting, not this collection's performance measurements or comprehensive compatibility validation. No game files were downloaded, installers executed, target tests run or recompilation performed here.

Candidate snapshot: 1 like, 81 views, 0 reposts; later engagement is not substituted.
Project's short-race, single-PC medians of three runs: 5K at 102 fps, not 5K at 240 fps. Not independently rerun.
Experimental, requiring a supported Disc 1. Windows currently; split screen and most GPUs untested.

## Sources

- [The Gaming Emporium reports FM4 recompilation and AI assistance, October 29, 2026](https://x.com/i/status/2115771724390178926)
- [Supplementary: pinned FM4 README, commit dated October 29, 2026, 09:13:11Z](https://github.com/i2kiselev/fm4-static-recomp/blob/0be771c68af81af5d74ca2e2c6284ec6b6642207/README.md)
- [Supplementary: same-commit test scope, environment and Xenia comparison](https://github.com/i2kiselev/fm4-static-recomp/blob/0be771c68af81af5d74ca2e2c6284ec6b6642207/guide/performance.md)

[中文](../i2kiselev-forza4-ai-static-recompilation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
