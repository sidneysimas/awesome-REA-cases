# A proprietary-format Rust CLI: eight Claude subagents saturate a 200-file workload

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-21
Stage: In progress

At 09:08 and 09:10 Beijing time on October 21, 2026, Dwayne (CtrlAltDwayne) explains a stalled computer: eight Claude subagents were running a Rust CLI he is building for a proprietary file format, benchmarking against 200 files. Some contain hundreds of thousands of lines to extract. He reports recovering and capping concurrency at three to avoid further beachballing.

This is an in-progress report of AI-assisted proprietary-format reading/extraction development. The follow-up adds data scale and reduced concurrency and is combined here. No format name, samples, repository, comparison baseline, accuracy, timing or memory measurements are supplied. The 200 files are not established passed tests, and lower concurrency does not establish parsing correctness. REA is not stated and no tool was executed here.

## Sources

- [Dwayne's eight Claude subagents, 200 files and cap of three](https://x.com/i/status/2112712706218447004)
- [Same author's follow-up on extraction scale and concurrency](https://x.com/i/status/2112713050117869783)

[中文](../claude-rust-proprietary-format-cli-concurrency.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
