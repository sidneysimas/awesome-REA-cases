# Game-function matcher: an audit account of wrong constants passing checks

Category: Algorithms and feature recovery · REA
Record date: 2026-10-17
Stage: Analysis test

At 07:42 Beijing time on October 17, @xmyttle recounts three game-function reconstruction relays from an REA blog: GPT-6-Sol to GPT-6.1-Sol, GPT-6.1-Sol to GPT-6 Astra, and GPT-6-Luna-max reportedly achieved matches. Astra is said to have rewired the control-flow graph so the compiler merged branches as in the original. More importantly, the post describes an acceptance limitation: instruction comparison reads a value behind an address only when that value was recorded. A later audit allegedly found accepted functions with wrong constants, such as adding 1.0f instead of the original 32.0f.

This is a specific test-oracle issue for function matching, separate from the CSV-export negative-control experiment. The source does not name a game or provide function lists, comparator code, an audit report or a fix commit. Both the three successes and the wrong constants remain attributed accounts, not independently reproduced defects or a confirmed repair. Feeding known-wrong code to a checker before trusting a green tick explains the proposed test, but does not establish that all byte-matching projects have the same flaw. Nothing was independently run.

Game and functions are unnamed; the original blog and audit code were not checked; 32.0f/1.0f is the source's example.

## Sources

- [Account of three game-function relays and a matcher constant-checking flaw](https://x.com/i/status/2111241506006700380)

[中文](../rea-game-function-matcher-audit-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
