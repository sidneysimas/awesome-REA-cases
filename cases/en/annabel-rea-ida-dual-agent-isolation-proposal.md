# REA/IDA dual-agent isolation: a planner receives specifications while a specialist keeps raw analysis

Category: Applications and clients · REA
Record date: 2026-10-29
Stage: Needs verification

At 12:43:05 Beijing time on October 29, 2026, Annabel (@annabel_2580) proposes a dual-agent workflow for context-exposure concerns when using Claude with REA. The main planner receives cleaned conclusions; a specialist keeps the REA/IDA session locally, with an alternative model or in a separate workspace. She compares a fully local open-model loop with retaining a strong planner, explicitly questioning whether a /rename split still leaves enough context to trigger filtering during real reversing.

At 13:13:42 the same day, @themegamind24 proposes a similar arrangement: local models or Kimi inspect binaries in a separate git worktree and return sanitized specifications. The post claims complete account safety without an isolation test, data-flow audit, actual target or enforcement comparison. It supplies architecture ideas, not that guarantee. Worktrees separate files, not automatically networks, permissions or model inputs.

At 17:18:59 and 17:19:55 within this window, Cloud Whisperer (@joyfulframes) adds experience in another discussion: submitting IDA decompilation snippets to his main Claude account allegedly led to restrictions, and returning extensive assembly or decompilation features can still expose layered workflows to cloud review. He also says he tried local open models with REA, found complex binary reasoning much weaker and often limited to simple samples, and suggests applying similar layering to Ghidra and Binja. These are personal accounts without named models, samples, revisions or benchmarks, not conclusions about every local model or proof of the cause of restrictions.

Supplementary reading of that discussion's October 27, 22:14:41 parent identifies MinLiBuilds's Dario planner/Sam analyst, worktree and concise-specification proposal. This is older context, not a new candidate, and does not make Annabel or Cloud Whisperer its originator. The parent also promotes subscription packages and asserts safety without validation; promotions are not evidence.

This is a collection of workflow ideas and risk experience, not completed target reconstruction or tested security isolation. Enforcement causality is not independently established, cleaned specifications can still leak content, and service terms and model restrictions remain applicable. This collection checked attribution and text only, without deploying the design, evading filters, testing accounts or running samples.

Earlier snapshots retained: first post 1 like, 29 views; second post 5 likes, 110 views, 2 reposts.
New candidate snapshots: risk post 3 likes, 147 views; local-model post 2 likes, 10 views.
No named target, model benchmark, data-flow audit or controlled account experiment; worktrees are not air gaps.

## Sources

- [Annabel proposes dual agents and questions effective isolation, October 29, 2026](https://x.com/i/status/2115665704586543549)
- [themegamind24 adds worktrees, local models/Kimi and an unsupported safety claim, same day](https://x.com/i/status/2115673409342345495)
- [Cloud Whisperer reports restrictions after IDA snippets and returned-context risks, October 29, 2026](https://x.com/i/status/2115735137615069308)
- [Cloud Whisperer reports reasoning limitations with local models and REA, same day](https://x.com/i/status/2115735371472637963)
- [Supplementary older parent: MinLiBuilds's Dario/Sam proposal, October 27, 2026](https://x.com/i/status/2115084773907656892)

[中文](../annabel-rea-ida-dual-agent-isolation-proposal.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
