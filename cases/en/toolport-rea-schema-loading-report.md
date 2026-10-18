# Toolport: initial-context claims and two-crackme tests with REA

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: Analysis test

At 17:58 Beijing time on October 18, a Toolport promotion describes someone else's configuration: 371 tools, including 207 from REA, loading 358K tokens before work. It claims Toolport reduces initial context to 19.1K while keeping 371 tools functional. The problem is tool-schema preload overhead, not correctness of software reconstruction.

At 23:21 the same day, @btsouth says REA 6.7.0 and Ghidra were tested on two stripped crackmes, with five runs per setup. All approaches reportedly solved them with the same answers, and Toolport found the required REA tools. A crackme is a small practice reverse-engineering challenge. The author attributes the earlier FuurinFuu numbers to ZCode, which preloads tools, and reports 6.1x fewer tokens and 3.2x faster completion with Toolport on similarly preloading OpenCode 1.19. Claude Code, Codex and OpenCode v2 already search for tools, so those token savings do not apply there. Five runs per setup is preserved without inferring the unspecified number of setups or total runs.

These are additional author self-test claims, not a publicly reproducible benchmark. No samples, complete configuration, model, token counter, per-run logs or answers are supplied, so equal conditions, all-tool functionality and accuracy cannot be verified. The 358K/19.1K figures describe initial context rather than total task cost; 6.1x and 3.2x do not generalize to every client. This is separate from LeanREA's 36-run comparison and was not independently rerun here.

October 18 original candidate snapshot: 9 likes, 377 views; 358K/19.1K describe initial context, not full-task cost or output length.
October 18, 23:21 supplementary candidate snapshot: 1 like, 14 views. Five runs per setup and 6.1x/3.2x are author reports without public raw records.

## Sources

- [Toolport's measurement claim for a real setup including REA](https://x.com/i/status/2111758754098421760)
- [btsouth's two-crackme self-test and client-specific conditions](https://x.com/i/status/2111840141765390359)

[中文](../toolport-rea-schema-loading-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
