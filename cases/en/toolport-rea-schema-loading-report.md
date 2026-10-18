# Toolport: reported initial-context reduction for a 371-tool setup including REA

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: Analysis test

At 17:58 Beijing time on October 18, a Toolport promotional post describes measurements on someone else's real configuration: 371 tools in total, 207 from REA, loading 358K tokens before work begins. With Toolport, initial context is reportedly 19.1K, while all 371 tools allegedly remain functional. The concrete problem is context overhead from preloading reverse-engineering tool schemas, not correctness of code recovered from target binaries.

The candidate supplies no verifiable configuration, model and token counter, per-tool invocation records or task benchmark. Identical measurement conditions and complete availability of every tool cannot be confirmed. No general savings percentage is calculated, and this is not conflated with LeanREA's 36-run task comparison. Numbers are the poster's measurement claims, not independently rerun.

October 18 candidate snapshot: 9 likes, 377 views; 358K/19.1K describe initial context, not full-task cost or output length.

## Sources

- [Toolport's measurement claim for a real setup including REA](https://x.com/i/status/2111758754098421760)

[中文](../toolport-rea-schema-loading-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
