# rea-engine: Rebuild Windows TicTacToe from its binary

分类：游戏与游戏保存 · REA
记录日期：2026-10-15

The author says rea-engine retains the original REA MCP and adds ILSpy, preview Ghidra 12.1.2, and pinned, hash-checked Frida, Z3, LIEF, and Capstone. The reported workflow combines static and Frida runtime evidence with rebuild, test, and repair. The author reports reconstructing Windows TicTacToe from its binary alone, with 19,683/19,683 board states matching byte for byte. This is a first-person report, not independently reproduced. The post explicitly credits morluto/rea for the original project.

First-person project report
Result not independently reproduced
October 15 follow-ups reiterate bundled tooling, Frida tracing and Z3 checks, then claim byte-for-byte output comparisons for rebuilds. These are author claims, not a demonstrated universal guarantee or a reason to generalize the TicTacToe result.

## 来源

- [Author's first-person report on rea-engine and TicTacToe reconstruction](https://x.com/i/status/2110506338706985158)
- [Author's follow-up on bundled tools, runtime tracing and Z3](https://x.com/i/status/2110622062918144222)
- [Author's follow-up on byte-for-byte comparison claims](https://x.com/i/status/2110641814545764484)

[返回目录](../README.md)
