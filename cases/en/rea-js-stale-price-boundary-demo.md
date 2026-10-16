# REA JavaScript demo: a stale-price check at 400 ms

Category: Algorithms and feature recovery · REA
Record date: 2026-10-16
Stage: Analysis test

Using a small self-made JavaScript demo module, the author illustrates turning reverse-engineering explanations into checkable decisions. The post says the real REA JavaScript analyzer was run, tracing reviewSignal() to inspectGuards() and locating ageMs > 400 at guards.mjs line 4, followed by HOLD / STALE_PRICE at line 5. Reported local checks return REVIEW at 399 and 400 milliseconds and HOLD at 401 and 800 milliseconds, emphasizing the boundary between strictly greater than and greater than or equal to. The author says the video edits together real CLI results and six local checks, without a live Claude session. REVIEW only means passing this example's check and does not submit orders; static tracing alone does not establish runtime behavior either. The complete module and all six outputs were not obtained, so this is an author-reported analysis test on a self-made sample, not a commercial trading-tool audit or a rerun by this collection.

October 15, 23:56 source; candidate snapshot: 2 likes, 10 views. Six checks is the author's count; the post lists only four timing-input results.

## Sources

- [Author's call locations, boundary results and demonstration limitations](https://x.com/i/status/2110761684411572247)

[中文](../rea-js-stale-price-boundary-demo.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
