# CREBench: 432 cryptographic binary tasks, from algorithm identification to flag recovery

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-23
Stage: Analysis test

A candidate posted at 13:38:54 Beijing time on October 23, 2026 introduces CREBench, saying GPT-5.4 scored 64.04, 28 points behind human experts. Public repository search located wangyu-ovo/CREBench. Its README identifies it as the official code repository for the COLM 2026 paper CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering, crediting Baicheng Chen, Yu Wang, Ziheng Zhou, Xiangru Liu, Juanru Li, Yilei Chen and Tianxing He. REA is not mentioned.

The goal is not breaking modern cryptographic primitives but evaluating what models can recover from compiled programs containing cryptographic logic. Four levels cover algorithm identification, key or IV extraction, wrapper-level code reimplementation and flag recovery. The README specifies 48 algorithms; hardcode_plain, fragmented_build and weak_prng_seeded key modes; and O0, O3 and constxor difficulties, totaling 432 challenges. It documents single-run and pass@k evaluation, parallel and resumable runs, and per-challenge scores, conversations and metrics. Ghidra, a Docker sandbox, Codex and multiple model integrations are documented.

The inspected repository's latest commit was 9fc4016538a0bab8c230732a9f788a61ed43addf, dated August 20, 2026, 13:01:15 UTC. This is supplementary inspection of older public material; the candidate's claim of a release five hours earlier is not treated as the repository's original release date. The 64.04 score and 28-point gap appeared only in the candidate, not verified against paper tables or evaluation artifacts, and remain attributed secondary claims rather than measurements by this collection. No challenge binary was downloaded, no dependencies installed and no evaluation run. Documented evaluation procedures do not establish independent reproduction.

Candidate: October 23, 2026, 13:38:54 Beijing time; supplementary repository commit August 20, 2026, 13:01:15 UTC. Retrieval is not the original publication date.
The README confirms 432 tasks and four levels; 64.04 and the 28-point gap are candidate claims only, not rerun.

## Sources

- [Candidate: CREBench scale, four levels and reported model scores](https://x.com/i/status/2113505421021323523)
- [Supplementary first-party CREBench README pinned to the August 20, 2026 commit](https://github.com/wangyu-ovo/CREBench/blob/9fc4016538a0bab8c230732a9f788a61ed43addf/README.md)

[中文](../crebench-432-crypto-re-benchmark-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
