# Slice vault investigation: Sonnet locates external-return accounting in decompiled bytecode

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-21
Stage: Analysis test

The candidate at 15:42 Beijing time on October 21, 2026 is MentemDeus asking whether coffiasse used Claude to decompile bytecode. Supplementary parent and author replies identify a closed-source vault contract associated with Slice. The 15:22 parent reports approximately $41,000 lost and describes the protocol using a caller-supplied external contract's return value directly for internal accounting, potentially allowing the vault to be drained. The author says they had to work through decompiled bytecode and free Claude Sonnet 5.5 located the vulnerable function in under two minutes. At 15:55 they answer yes to Claude's decompilation role. Both supplementary posts fall within the window and explain the candidate reply; they are not additional candidates.

This supports a specific author-reported AI-assisted contract investigation, not proof that the model independently discovered the real attack, completely recovered the contract or executed an exploit. No contract address, chain, transaction hash, complete inputs/outputs or test script was obtained for verification here. Approximately $41,000 and under two minutes remain author claims, not an independently recomputed on-chain loss or benchmark. REA is not stated. No wallet was connected, transaction submitted or target executed.

## Sources

- [Window candidate: MentemDeus asks about Claude bytecode decompilation](https://x.com/i/status/2112811815931437188)
- [Supplementary parent: coffiasse reports Slice vault accounting and Sonnet analysis](https://x.com/i/status/2112806669654925542)
- [Same author confirms Claude decompilation at 15:55](https://x.com/i/status/2112814939555717393)

[中文](../slice-vault-sonnet-decompiled-bytecode.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
