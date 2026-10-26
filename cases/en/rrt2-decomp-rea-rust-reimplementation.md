# Railroad Tycoon II: a Rust reimplementation assisted by REA and specialized AI agents

Category: Games and preservation · REA
Record date: 2026-10-26
Stage: In progress

At 15:30 Beijing time on October 25, 2026, yibie introduced a Rust reverse-engineering/reimplementation project for Railroad Tycoon 2 in a resource-directory update, reporting AI participation found in commit trailers. Supplementary public-repository lookup identifies pedryvo/rrt2-decomp: it studies the 1998–2001 Railroad Tycoon II Platinum executable to retain its isometric view and gameplay while supporting modern resolutions. This is a previously deferred candidate, not a newly captured result from the October 26 00:00–04:00 window.

The README read statically explains that REA MCP connects to Ghidra and specialized AI agents divide the work. Strings, imports and data tables anchor subsystem analysis; specifications record addresses, constants and pseudocode before Rust implementation. Original functions run through Unicorn for bit-exact comparisons with Rust; whole-game behavior is compared field by field by advancing the same save in the original under Wine and in the reimplementation. Commit 0d26aca, dated October 23 at 23:03:18 UTC, credits Claude Opus 5.5 as co-author on reports, charts and CSV export. This supports AI collaboration, not a measured proportion of AI-written code.

The README reports 2,945 functions, 616 specified and 304 verified bit-exact, plus agreement in all 131 save-advancement scoreboard cases. These are project-reported results, not tests rerun by this collection, and do not establish recovery of every function or all game semantics. It remains labeled pre-alpha, with partial file-format, simulation, UI and multiplayer work; roadmap labels are not fully synchronized with later implementation progress. Windows/macOS builds are explicitly untested by the author. The entry therefore remains in progress, not an accepted complete-game reconstruction.

The candidate says the README did not mention AI, but the documentation now read explicitly describes specialized AI agents and REA; that generalization is corrected rather than repeated. Eight stars, 421 files and 20 trailers are only the post's snapshot and were not recounted here. The project requires legitimately owned original game data, which this entry does not distribute. Supplementary repository material predates this run's window and is used for identity and methodology checks. No dependencies were installed, game assets downloaded, project code executed or visuals, performance and save results independently verified.

Previously deferred candidate; in progress, with project-reported differential results not independently rerun and a partly stale README roadmap.
The current README explicitly names REA and AI agents, correcting the post's no-AI-in-README generalization. Co-authorship is not a measured AI-code percentage.

## Sources

- [Previously deferred candidate: yibie introduces two independent game projects, October 25, 2026 Beijing time](https://x.com/i/status/2114258253253329233)
- [Supplementary project README at fixed commit 0d26aca, October 23, 2026 UTC](https://github.com/pedryvo/rrt2-decomp/blob/0d26aca502ec36730c6b261713f71cda890319d5/README.md)
- [Public reports implementation commit crediting Claude Opus 5.5, October 23, 2026 UTC](https://github.com/pedryvo/rrt2-decomp/commit/0d26aca502ec36730c6b261713f71cda890319d5)

[中文](../rrt2-decomp-rea-rust-reimplementation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
