# CSV export evaluators: three deliberately broken implementations pass simple tests

Category: Algorithms and feature recovery · REA
Record date: 2026-10-16
Stage: Analysis test

On October 16, @superfang119 reported an experiment about acceptance testing for REA-assisted reconstruction: three deliberately broken CSV exporters passed simple tests, but 215 byte-level comparisons against original output exposed all three. The author traces the investigation through REA's MCP, Evidence and TH08 repair records, focusing on establishing that an evaluator can detect mistakes before relying on it to judge a reconstruction. The candidate does not supply exporter names, mutations, the 215 input/output pairs or runnable code; the linked article body was not obtained. Only the author's reported test contrast is recorded. It does not establish coverage of all CSV boundaries, a completed TH08 or commercial-app reconstruction, or independent verification by this collection.

October 16 candidate snapshot: 3 likes, 242 views, 0 reposts; the 215 comparisons and three implementations are author-reported.

## Sources

- [Author's CSV mutation and 215-comparison experiment report](https://x.com/i/status/2110963427791487391)

[中文](../rea-csv-evaluator-mutation-test.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
