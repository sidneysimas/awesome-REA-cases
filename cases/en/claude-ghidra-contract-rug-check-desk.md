# A pre-buy contract check desk: Claude/Ghidra sell-path analysis and a corrected proxy flag

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-21
Stage: Needs verification

At 19:50 Beijing time on October 21, 2026, a publisher describes a first-night rug-check desk: a Claude agent connected to Ghidra MCP reads contract bytecode, withholding the buy button until all red-flag checks pass. Reported checks include retained minting authority, non-whitelisted users unable to sell, unlocked liquidity and adjustable fees. The author claims seven of nine contracts were blocked but names only six examples; the other three must not be invented or a complete accuracy rate inferred.

The author also reports VIBEINU was incorrectly flagged as a dangerous upgradeable proxy and recognized as a standard OpenZeppelin pattern after an implementation comparison was requested. This shows findings still need review, and a standard proxy pattern itself does not establish safety. The post includes a textual excerpt of GOBLINX2's sell branch and claims the video shows a decompiler panel at 0:12, but supplies no network, contract addresses, block height, plugin configuration, original logs or repository. These names and tool results cannot independently be tied to real contracts. REA is not stated; the Ghidra MCP name alone does not establish support for the chain's bytecode. The author acknowledges limits against social engineering and later liquidity withdrawal. Passing these checks is not investment safety or a guarantee against honeypots; no contracts were analyzed or trades made here.

Source update: 2026-10-21T19:50:24+08:00; 7/9 is the author's count, with only six named examples and no addresses or independent rerun.

## Sources

- [Publisher's Claude/Ghidra rug-check desk, sell-branch excerpt and false-positive correction](https://x.com/i/status/2112874139279130962)

[中文](../claude-ghidra-contract-rug-check-desk.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
