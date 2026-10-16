# rea-engine: Rebuilding TicTacToe from a Windows game binary

Category: Games and preservation · REA
Record date: 2026-10-15

The author says rea-engine retains the original REA MCP and adds ILSpy, preview Ghidra 12.1.2, and pinned, hash-checked Frida, Z3, LIEF, and Capstone. The reported workflow combines static and Frida runtime evidence with rebuild, test, and repair. The author reports reconstructing Windows TicTacToe from its binary alone, with 19,683/19,683 board states matching byte for byte. This is a first-person report, not independently reproduced. The post explicitly credits morluto/rea for the original project.

First-person project report
An October 15 22:20 post introduces Heaven Skills as execution SOPs drawn from the author's OpenAgent, rea-engine and career-studio-ai builds. It adds workflow context for automated decompilation and verification, not a new TicTacToe test or proof that SOPs eliminate hallucinations; the skill repository was not inspected here.
Result not independently reproduced
October 15 follow-ups reiterate bundled tooling, Frida tracing and Z3 checks, then claim byte-for-byte output comparisons for rebuilds. These are author claims, not a demonstrated universal guarantee or a reason to generalize the TicTacToe result.

## Sources

- [Author's first-person report on rea-engine and TicTacToe reconstruction](https://x.com/i/status/2110506338706985158)
- [Author's follow-up on bundled tools, runtime tracing and Z3](https://x.com/i/status/2110622062918144222)
- [Author's follow-up on byte-for-byte comparison claims](https://x.com/i/status/2110641814545764484)
- [Author's Heaven Skills workflow context](https://x.com/i/status/2110737629465514404)

[中文](../rea-engine-tictactoe.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
