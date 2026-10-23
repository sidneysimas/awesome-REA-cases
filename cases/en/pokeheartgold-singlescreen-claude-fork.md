# HeartGold/SoulSilver single-screen fork: Claude changes the UI, crediting pret's existing decompilation

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-23
Stage: In progress

This lead comes from yibie's directory update at 15:31:12 Beijing time on October 23, 2026, re-reviewed from the earlier 12:00-16:00 window rather than new retrieval in the current window. The post also mentions Monster Hunter 2 and Champagne. This record covers only the directly documented HeartGold/SoulSilver single-screen target, not a shared verification of those projects. The yibie/awesome-rea directory led to ClickingMaster/pokeheartgold-single-screen, whose README was read.

Built on ctrl-cheeb-del/pokeheartgold and pret/pokeheartgold, the fork adds a SINGLE_SCREEN build mode to the Pokémon HeartGold/SoulSilver decompilation tree for ssrecomp to turn SoulSilver into a native single-screen program. Former touchscreen UI, including battle commands and moves, bag and party, is drawn in the upper-screen area. Menu and selection state is exposed for widescreen and controller layouts. The README explicitly credits pret for the original tooling and decompilation. Nearly all fork changes are disclosed as written by Claude through Claude Code under maintainer direction and play-testing, with a warning about bugs a human might not make. Years of upstream work are not attributed to AI starting from zero.

The README says everything is C/C++ and both HeartGold and SoulSilver ROMs build byte-for-byte in the normal configuration. That is a project claim, not independently compiled here. SINGLE_SCREEN deliberately changes the game; byte-exact original builds do not mean the single-screen result also matches the original ROM. Setup programs and the asset script are tested only with SoulSilver USA. Users must supply a lawful ROM, mwccarm and Nitro SDK; the project distributes no game, compiler or SDK. pret does not accept AI-generated contributions and the documentation asks users not to send this fork's changes upstream.

The supplementary README is pinned to 6984a3d67592157195940049be2e4bbbf933f9ff, originally committed October 22, 2026, 03:08:18 UTC, before the candidate. It is first-party support for the target, attribution and verification boundaries. The candidate's 13 stars and 11,231 files are not adopted as current statistics. No ROM was downloaded, installer run or single-screen build tested. This is an in-progress preservation and interface-adaptation project, retaining upstream credit and each component's rights; repository licensing statements are not extended to game assets.

Older candidate: October 23, 2026, 15:31:12 Beijing time; supplementary commit October 22, 2026, 03:08:18 UTC.
Byte-exactness is a project claim for normal builds, not proof for the single-screen modification; no independent build.

## Sources

- [Older candidate: yibie's HGSS single-screen directory lead, October 23, 2026](https://x.com/i/status/2113533682187211069)
- [Supplementary first-party ClickingMaster README pinned to October 22, 2026](https://github.com/ClickingMaster/pokeheartgold-single-screen/blob/6984a3d67592157195940049be2e4bbbf933f9ff/README.md)

[中文](../pokeheartgold-singlescreen-claude-fork.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
