# Way of the Samurai: an LLM and real-address byte oracle, with about 266 currently reproducible matches out of 382 historical submissions

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-24
Stage: In progress

At 15:30:21 Beijing time on October 24, 2026, yibie's project roundup describes a Way of the Samurai PS2 decompilation and relays 382 byte-matched functions. Supplementary reading of dnb4ever's public README identifies the target as the 2002 PS2 game, North American SLUS-20407. It aims at readable reconstructed source alongside a native PC static-recompilation port based on PS2Recomp. The project calls this greenfield work rather than completion of someone else's decompilation; that historical claim remains attributed to the project.

The stated AI method pairs an LLM with a byte-exact compile oracle. Source-patched ee-gcc 2.9 from the 991111 line compiles C, links each function at its real address and compares bytes against a user-supplied retail binary. A crucial qualification: 382 is the historical committed-match count. Only about 266 reproduce with the current unified compiler; earlier matches await reverification, with yes, no and legacy states in MATCHES.tsv, against approximately 3,143 total functions. Neither 382 currently passing functions nor a fully recovered game is established.

The PC port reportedly executes recompiled Emotion Engine code through kernel initialization, IOP reboot and seven modules, filesystem mounting and entry to the main loop, emitting its first GS primitives. The README explicitly says GS rendering and VU1 are not implemented. Emitting primitives is not a rendered first frame or a playable PC release, correcting the more optimistic directory synopsis. The supplementary README is pinned to commit 1a49bb50b466e8090c4a406379b6a35ea2d3214f, dated October 23 Beijing time, not a new post in this window. This collection read documentation only, downloaded no game, and neither compiled nor reran the oracle. The project remains in progress and its results are project reports.

382 historical committed matches, about 266 currently reproducible matches and approximately 3,143 total functions are project reports; nothing was independently run.
The PC port reports emitting GS primitives only; GS rendering and VU1 are unimplemented, not a rendered first frame or a fully playable port.

## Sources

- [yibie's project roundup, October 24, 2026](https://x.com/i/status/2113895858207105458)
- [Supplementary first-party README at a pinned commit, October 23, 2026 Beijing time](https://github.com/dnb4ever/way-of-the-samurai-decomp/blob/1a49bb50b466e8090c4a406379b6a35ea2d3214f/README.md)

[中文](../way-of-samurai-ps2-ai-matching.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
