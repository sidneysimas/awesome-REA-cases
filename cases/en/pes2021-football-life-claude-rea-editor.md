# PES 2021 / Football Life: a Claude/REA-assisted cross-platform Master League save editor

Category: Games and preservation · REA
Record date: 2026-10-21
Stage: In progress

At 07:57 Beijing time on October 21, 2026, Felipe Mikeias (felipemikeias) says he used Claude and REA to study a PES 2021 / Football Life save editor and rebuild it as an open-source cross-platform project. It edits Master League transfer and salary budgets, club followers and manager names, rather than rebuilding the football game.

Supplementary inspection found pes21-ml-editor at dfa862df, committed at 01:51 Beijing time on October 19, before this candidate window. Its repository description calls it a preview; the README describes a Rust core, egui desktop app and show/set/decrypt/encrypt CLI, claiming Windows, Linux and Intel/Apple Silicon macOS support. It explicitly credits public-domain pesXdecrypter, zlac's PES 2021 key and field positions from Devil Cold52's PES 2021 ML Money Tool. This prior research must not be attributed to Claude.

The documentation says editing requires an unchanged decrypt/re-encrypt byte-for-byte round trip, writes only selected fields, creates backups, uses atomic writes and rollback on failed checks, and refuses writes if the game changes the save concurrently. These are project design statements, not results obtained here. Supplementary GitHub Actions inspection found run 39151490045 on October 19 for the current commit completed with failure; older commits have successful runs. Neither current CI success nor validation on all three platforms is established. No target was downloaded or executed and no save modified. Individual AI contributions, game-version compatibility and actual save results remain independently unverified. Use only personal offline saves and keep backups.

Validation boundary: public code and safe-save documentation do not mean the current build passes; CI for dfa862df failed, and no saves were edited here.

## Sources

- [Felipe Mikeias announces Claude/REA-assisted cross-platform save editing](https://x.com/i/status/2112694820657393735)
- [Project README at dfa862df: features, safe saving and prior-work credits](https://github.com/felipemikeias/pes21-ml-editor/blob/dfa862df2f2f7f077ebd16d0d4b0da4b507b0e7c/README.md)
- [Current commit's project CI: failed October 19 run](https://github.com/felipemikeias/pes21-ml-editor/actions/runs/39151490045)

[中文](../pes2021-football-life-claude-rea-editor.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
