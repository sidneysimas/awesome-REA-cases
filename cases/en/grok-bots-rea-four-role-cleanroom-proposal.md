# Four REA roles on Grok Bots: a proposal for observation, specification, isolated rebuilding and verification

Category: Applications and clients · REA
Record date: 2026-10-25
Stage: Related project

At 06:45:34 Beijing time on October 25, 2026, francescofaenzi proposes adapting the Claude Code/REA four-role workflow to Grok Bots' shared cloud computer for a small interoperability feature in owned or authorized software. Only the Analyst uses REA and the target, producing evidence.md with observations, inferences and unknowns. A Spec Writer produces behavior-only SPEC.md and tests without addresses, offsets or decompiled names. A Rebuilder writes fresh code from the specification alone. A Verifier compares original and rebuild on identical inputs, returning divergences as tests rather than patches. An optional Team Lead coordinates the sequence and repeats failures for roughly three rounds at most.

The fully reread original includes lab/ and clean/ folders, bot descriptions, an MCP registration example, separate Ghidra/Hopper/IDA requirements for native analysis and stronger environment isolation where available. It supplies no named analyzed app, run report, match rate or code; search ranking is only an example request. Role instructions and folder conventions on a shared computer are not operating-system-enforced isolation, nor guarantees of legal clean-room compliance, no data leakage or restricted tool permissions. This is retained as a concrete engineering proposal, not a deployed Grok integration. No registration command was executed and neither REA nor original targets were installed or run.

Source: 06:45:34 Beijing time; full original reread, without acceptance comparisons on a specific target.

## Sources

- [francescofaenzi's full proposal: four-role Grok Bots/REA workflow, October 25, 2026](https://x.com/i/status/2114126178806079784)

[中文](../grok-bots-rea-four-role-cleanroom-proposal.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
