# Touhou reconstruction projects

Category: Games and preservation · REA
Record date: 2026-10-12

Touhou Reconstruction Factory is N0zoM1z0's project bringing together tools and workflows from several Touhou game reconstruction projects. TH08 means Touhou Eiyashou (Imperishable Night); the other identifier in the source material is TH095, Touhou Bunkachou (Shoot the Bullet), not TH09; TH04 is Touhou Gensokyo. All are Touhou Project games. The author uses agents to analyze original executables, recover C++ function by function, then compile and compare it against the original binary, aiming for runnable, maintainable code. Project records include playable Linux and browser versions of TH08 and a playable Windows reconstruction of TH095. TH04's DOS version has author-recorded manual gameplay tests; its modern 64-bit port remains in development. TH08 continues existing GensokyoClub work, and TH04 draws on ReC98. Historical projects also used specialized tools, so the entire result cannot be attributed to REA.

A third-party long-form overview on 2026-10-14 additionally claims that 1,106 of TH08's 1,107 game-specific functions match the original machine code. It notes that this roughly two-week effort built on prior manual research, and only 260 of a further 1,119 library functions met the same standard: the entire executable was not exactly reconstructed. This is a third-party account, not direct confirmation by the project author in that post; the whole result is not credited to REA.

Third-party overview (2026-10-14): reports TH08 game-function machine-code matches; not directly confirmed by the project author.
A tutorial in the October 15 window says a 128.0 constant written as 0.0 still passed byte checks. This review traced REA evidence documentation and TH08 issue #10 and merged PR #13: September 2 records show ItemManager::OnUpdate used 0.0 incorrectly in its auto-collection condition. The comparator replayed relocation addresses without checking the floating-point data they referenced, so matching instruction bytes could conceal a semantic error. This was not a floating-point tolerance issue.
PR #13's project records report checking 1,548 floating-point references, correcting another 12 old references in five functions, and automatically checking 32/64-bit floating-point relocations lacking explicit data_hex. They record an intentionally incorrect declaration test and a 1,106/1,106 successful cold replay. This collection only read historical issues, PRs and documentation; it did not rerun the compiler or game. The September repair is historical evidence added in this review, not a newly completed result in the current window.

## Sources

- [Case article PR](https://github.com/morluto/rea/pull/1475)
- [Methods and project evidence](https://github.com/morluto/rea/blob/main/website/evidence/touhou-reconstruction-method.md)
- [TH08 project](https://github.com/N0zoM1z0/th08)
- [TH095 project](https://github.com/N0zoM1z0/th095)
- [TH04 project](https://github.com/N0zoM1z0/th04)
- [Third-party long-form overview: TH08 comparison figures (secondhand, not author-confirmed)](https://x.com/i/status/2110211900051210691)
- [This window's tutorial: warning about unchecked TH08 floating-point constants](https://x.com/i/status/2110683568644964737)
- [September 2 original issue: auto-collection threshold and oracle gap (traced this review)](https://github.com/N0zoM1z0/th08/issues/10)
- [September 2 merged fix: global floating-point reference verification (traced this review)](https://github.com/N0zoM1z0/th08/pull/13)

[中文](../touhou-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
