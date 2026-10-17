# LeanREA: an 8 KB CLI skill benchmarked against REA on Notion, a native addon and Go

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-17
Stage: Analysis test

At 11:09 Beijing time on October 17, @aicodeking announced LeanREA, an 8 KB skill guiding agents to use CLI tools directly rather than MCP. A name search found aicodeking/leanrea. Supplementary reading of its README, bench/BENCHMARK.md and commit metadata confirmed the initial repository commit at 10:53 that day; the benchmark document labels itself October 16. Four tasks cover the microphone/meeting-detection chain in Notion app.asar; mac_utils.node exports, TCC permission checking and its single-instance lock; build/dependency information from a stripped gh binary; and recovering the lock's socket path, wire protocol and peer authentication from disassembly alone.

The project used Claude Code 2.1.301 headless, Sonnet 5.5 and macOS arm64, comparing LeanREA, no skill, and REA 6.5.0 MCP plus its own skill with three repetitions per task per arm, 36 runs altogether. Detailed totals over 12 runs per arm are: LeanREA 388 seconds, $2.17, 55 turns, 2.40 million tokens, score 74/75; REA 627 seconds, $3.36, 124 turns, 5.93 million tokens, 75/75; no skill 479 seconds, $2.21, 81 turns, 3.11 million tokens, 67/75 with one refusal. The advertised 38% less time, 35% lower cost and 56% fewer turns are project aggregates, not measurements by this collection. 'Same accuracy' is imprecise: LeanREA once named an existing v1 IPC channel instead of v2.

Answers were regex-graded against author-written keys. The document discloses a corrected regex false negative for the bare model's Go version string. There was one model, one machine and three repetitions per cell; full native analysis engines were not installed, so this cannot be generalized to Ghidra/Hopper/IDA or APK work. The README additionally says jadx was absent. REA used deferred tool search; the 400.7k context figure belongs only to a separate probe loading every tool with search disabled, not default cost in the 36-run comparison. Readers ask whether Electron dependency-install approval delays and matched batching/output caps were counted; no author answer was obtained. Public benchmark and raw-metric paths make this more inspectable than a promotional sentence, but this collection did not execute the repository, models or targets, and does not infer that LeanREA universally replaces REA.

Announcement candidate snapshot (2026-10-17): 31 likes, 557 views, 2 reposts; changing view counts during rereading do not overwrite it.
Author benchmark, not independent reproduction; 74/75 differs from 75/75, and 36 runs are not 36 distinct targets.

## Sources

- [LeanREA announcement and 36-run comparison claim](https://x.com/i/status/2111293595529703853)
- [Public project README](https://github.com/aicodeking/leanrea)
- [Full benchmark and caveats in the initial commit](https://github.com/aicodeking/leanrea/blob/a07ed0ebf1c585d9db535f91a91ef555b8920b90/bench/BENCHMARK.md)
- [Reader question: were installation-approval delays timed?](https://x.com/i/status/2111299719888884167)
- [Reader question: matched batching and output caps](https://x.com/i/status/2111298045421953535)

[中文](../leanrea-cli-skill-benchmark.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
