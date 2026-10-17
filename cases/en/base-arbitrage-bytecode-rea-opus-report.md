# Base arbitrage contract: an unverified REA/Opus bytecode report

Category: Algorithms and feature recovery · REA
Record date: 2026-10-17
Stage: Needs verification

At 06:18 Beijing time on October 17, @mal0r1key says REA decompiled EVM bytecode from an unverified contract on Base, after which Opus 5.5 explained ETH/USDC arbitrage between Uniswap and Aerodrome, a pre-trade net-edge check, flash borrowing and repayment within one block, then rewrote it in 41 lines of Solidity. Here 'unverified' means the explorer lacks verified source, not that this collection endorses contract safety. The author claims every finding has a bytecode offset and alleges $1,248,530 profit over 296 days, $4,218 per day, about $11.40 per trade and roughly 15 trades per hour. These are unverified promotional figures, not confirmed investment performance.

The conversation does not contain the promised contract address, offsets, rewritten code, transaction records or a replay. The text juxtaposes sizing at 30% of the shallower pool with the constant 0x1e and 30 basis points of slippage. A numeric constant alone cannot establish units and business meaning, and the source supplies no code context resolving that ambiguity. Only the concrete bytecode-investigation narrative is collected, not confirmation of strategy completeness, profits, loss prevention or a deployable trading bot. No contract or tests were executed.

No address, offsets, code or transaction replay were found in the conversation; profits and a 41-line rewrite remain author claims.
30% position sizing and 30-basis-point slippage have different units; a constant alone does not establish meaning.

## Sources

- [Original Base-arbitrage bytecode analysis and profit claims](https://x.com/i/status/2111220274226217276)

[中文](../base-arbitrage-bytecode-rea-opus-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
