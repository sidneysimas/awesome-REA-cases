# DX-Ball: positional audio function

Category: Games and preservation · REA
Record date: 2026-10-12

DX-Ball is an older brick-breaking game. This case recovers how sound effects are distributed between left and right audio channels according to horizontal screen position, rather than rebuilding the entire game. A contributor followed sound-playback calls to the panning function and used assembly, constants and callers to complete pseudocode and recover a C implementation. Evidence includes 3,205 differential tests against original x86 code and an exact match of the complete 63-byte function after recompilation. The result is an accurate reconstruction of one sound algorithm.

## Sources

- [Case PR](https://github.com/morluto/rea/pull/876)
- [Evidence record](https://github.com/morluto/rea/blob/main/website/evidence/dx-ball-sound-pan.md)

[中文](../dx-ball-sound-pan.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
