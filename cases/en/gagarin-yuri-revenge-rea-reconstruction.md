# gagarin: reconstructing Yuri's Revenge with REA and a compiler oracle, without claiming a running engine

Category: Games and preservation · REA
Record date: 2026-10-24
Stage: In progress

At 15:30:21 Beijing time on October 24, 2026, yibie introduces gagarin and emphasizes that matching functions and compiling do not prove behavior. Supplementary reading of r-melvin's README identifies the retail Command & Conquer: Red Alert 2 — Yuri's Revenge gamemd.exe v1.001 as the target. The aim is structured, readable C++ following Westwood's class organization as far as binary evidence supports, using the period MSVC 6.0 toolchain. This is distinct from Xi's baseline project using Chrono Divide to rewrite behavior for reinforcement learning, so it receives a separate record.

The README explicitly credits REA and Ghidra for focused reverse engineering and evidence gathering, with retail instructions and the VC6 oracle deciding addresses, layouts and matches. External projects supply restricted naming/structure references only. This records an AI-tool-assisted workflow, not a claim that all source was model-generated. As of October 23 the project reports 10,204 matches among 19,778 functions in its extent census (51.6%), plus 686 partials. Matched bodies cover 704,282 of 3,878,653 listed function bytes (18.2%); these percentages measure different things.

The project says matched rows pass raw-byte and strict relocation checks. At the historical 2a00ae5d link snapshot, M1 resolves all externals and places 10,174 functions at retail addresses, noting a remaining matched row sharing its symbol with another address. That historical link count and today's function count are not the same snapshot. M0 is a force-link diagnostic and M1 uses int3 stubs; the README explicitly says neither image runs, the engine does not run from this build, and whole-executable identity is not claimed. Statically linked CRT and third-party code are outside source-recovery scope. The supplementary README is pinned to ac9e6716bdf3aaad5885d166e144118bdd51dd3f, committed at 15:24:27 Beijing time on October 24, and distinguished from the candidate post. This collection downloaded no target EXE or toolchain and ran neither verifier nor game; all figures are project reports.

README progress as of October 23, 2026: 10,204/19,778 function matches, 686 partials, 704,282/3,878,653 function bytes; not independently rechecked.
The historical M1 link count is 10,174, not the current 10,204; neither link probe produces a running image.

## Sources

- [yibie on gagarin and its evidence limits, October 24, 2026](https://x.com/i/status/2113895858207105458)
- [Supplementary first-party gagarin README at a pinned commit, October 24, 2026](https://github.com/r-melvin/gagarin/blob/ac9e6716bdf3aaad5885d166e144118bdd51dd3f/README.md)

[中文](../gagarin-yuri-revenge-rea-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
