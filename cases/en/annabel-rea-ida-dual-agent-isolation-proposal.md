# REA/IDA dual-agent isolation: a planner receives specifications while a specialist keeps raw analysis

Category: Applications and clients · REA
Record date: 2026-10-29
Stage: Needs verification

At 12:43:05 Beijing time on October 29, 2026, Annabel (@annabel_2580) proposes a dual-agent workflow for context-exposure concerns when using Claude with REA. The main planner receives cleaned conclusions; a specialist keeps the REA/IDA session locally, with an alternative model or in a separate workspace. She compares a fully local open-model loop with the compromise of retaining a strong planner, explicitly questioning whether a /rename split still leaves enough context to trigger filtering during real reversing.

At 13:13:42 the same day, @themegamind24 describes a similar arrangement: a local model or Kimi inspects binaries in a separate git worktree and returns sanitized logic specifications. That post claims the primary account becomes completely safe, but provides no isolation test, data-flow audit, real target or account-enforcement comparison. It supplies architecture ideas, not evidence for that guarantee. Git worktrees separate file workspaces; they do not automatically air-gap networks, permissions or model inputs.

This is a concrete reverse-engineering workflow idea, not a completed target reconstruction. Neither author's causal explanation of platform enforcement is independently supported. Cleaned specifications may still expose content, and service terms and model restrictions continue to apply. Lookup confirmed attribution and text. This collection did not deploy the architecture, evade filters or test accounts, and does not present it as a reliable way around safety policies.

Candidate snapshots: first post 1 like and 29 views; second post 5 likes, 110 views and 2 reposts.
No target program, data-flow audit or account experiment. Worktrees are not air gaps.

## Sources

- [Annabel proposes dual agents and questions effective isolation, October 29, 2026](https://x.com/i/status/2115665704586543549)
- [themegamind24 adds worktrees, local models/Kimi and an unsupported safety claim, same day](https://x.com/i/status/2115673409342345495)

[中文](../annabel-rea-ida-dual-agent-isolation-proposal.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
