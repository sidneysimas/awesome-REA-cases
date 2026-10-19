# DX-Ball: positional audio function

Category: Games and preservation · REA
Record date: 2026-10-19

DX-Ball is an older brick-breaking game. This case recovers how sound effects are distributed between left and right audio channels according to horizontal screen position, rather than rebuilding the entire game. A contributor followed sound-playback calls to the panning function and used assembly, constants and callers to complete pseudocode and recover a C implementation. Evidence includes 3,205 differential tests against original x86 code and an exact match of the complete 63-byte function after recompilation. The result is an accurate reconstruction of one sound algorithm.

Japanese commentary posted at 14:10 Beijing time on October 19 further separates REA's instructions, callers and data from the reconstruction project's responsibility for comparison tests. Citing an October 7 progress table, it says 528 Ghidra function candidates include library code and are not a completion-rate denominator; at that time 55 functions were rewritten, 33 byte-matched, and a complete playable game had not been built. These remain third-party reports of dated earlier progress, not October 19 measurements or current progress. A successful build is not treated as a match.

Single-function evidence does not cover ball physics, every collision or full-game playability. The candidate's separate Berman/Mario discussion is not new DX-Ball verification. This collection did not rerun differential tests or compile the target.

## Sources

- [Case PR](https://github.com/morluto/rea/pull/876)
- [Evidence record](https://github.com/morluto/rea/blob/main/website/evidence/dx-ball-sound-pan.md)
- [October 19 commentary: single-function versus full-game verification, citing October 7 progress](https://x.com/i/status/2112063745824616946)

[中文](../dx-ball-sound-pan.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
