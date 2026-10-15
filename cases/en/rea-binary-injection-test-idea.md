# REA analysis: a binary prompt-injection test idea

Category: Algorithms and feature recovery · REA use unconfirmed
Record date: 2026-10-13
Stage: Needs verification

riyoway proposes placing AI-directed instructions in target strings, resources or dead code to observe whether LLM reverse-engineering tools such as REA treat them as instructions and contaminate analysis. The aim is to assess indirect prompt-injection boundaries in AI reverse-engineering workflows. Initially the author only considered an experiment, with no sample, test or success evidence. This collection did not create or execute an injected target, and the proposal is not presented as an effective defense.

Later test (author report): the author used REA 6.5.0's JavaScript analyzer on a self-made toy Electron app without connecting an agent and searched reports for nine harmless markers. Six appeared in different report sections. Comments and package.json description did not appear; some strings, object keys, IPC names, URLs and filenames did. Slices containing only summary/statistics/limitations and window settings lacked the markers, while the window slice still showed nodeIntegration enabled and contextIsolation disabled. The author consequently recommends checking numbers and flags first and treating slices with names or URLs as target text. This shows only which sample text enters static-analysis output, not that a model follows instructions, and cannot be generalized to other commands or apps.

Posted: 2026-10-12T23:42:14+08:00 (Beijing time)
Engagement snapshot (2026-10-13): 1 like | 14 views | 0 reposts
REA 6.5.0; author's self-made toy Electron app; no agent connected and no test of model obedience to embedded text.
At 20:30 on October 15, another user proposed embedding text in their own software requiring a model to repeat interjections many times as interference against AI reverse engineering. This adds only a concrete idea, not new results from the earlier experiment's author, and establishes neither agent obedience nor an effective defense. Candidate snapshot: 36 likes and 1,450 views, recorded October 16.

## Sources

- [Author report from this review](https://x.com/i/status/2109670989319868863)
- [Author's REA 6.5.0 toy-app static-analysis test (model obedience untested)](https://x.com/i/status/2110441399279604113)
- [Another user's embedded-prompt interference idea (untested)](https://x.com/i/status/2110709861042503706)

[中文](../rea-binary-injection-test-idea.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
