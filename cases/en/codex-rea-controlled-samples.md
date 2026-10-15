# Controlled JS/.NET samples: Codex with and without REA

Category: Algorithms and feature recovery · REA
Record date: 2026-10-12
Stage: Analysis test

蓝哥AI compared native Codex with Codex plus REA on a readable script, a package still containing JavaScript after unpacking, and a small source-unavailable managed .NET sample, requiring independent functions checked against original program behavior. The same gpt-6.1-sol model followed both routes for each of the three tasks. The author reports all 360 cases passed in total. REA supplied method locations and instruction clues, but complete decoding still required the model to write additional scripts. Each route ran only once per task, and extra validation steps varied, so elapsed times do not establish a general efficiency ranking. This was also not large-scale decompilation of commercial software.

Posted: 2026-10-12T19:14:00+08:00 (Beijing time)
Engagement snapshot (2026-10-12): 2 likes | 198 views | 0 reposts

## Sources

- [Author's comparison tests from this review](https://x.com/0xlangeai/status/2109603485914206498)

[中文](../codex-rea-controlled-samples.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
