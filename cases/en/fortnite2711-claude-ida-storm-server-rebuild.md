# Fortnite 27.11 storm logic: Claude uses an IDA dump through MCP to infer server behavior

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-28
Stage: In progress

At 22:38:58 Beijing time on October 28, 2026, an author says they are reversing Fortnite 27.11, the November 2023 OG version. Many functions are described as stripped: storm logic stopped being stored in full on the client after season 15, although related client functions remain. Rather than manually trial-and-error the server infrastructure, the author gives Claude MCP access to that version's IDA dump and asks it to attempt storm behavior.

They claim frequent first-pass success and roughly 90% less server-programming time, followed by bug checks and rewriting when necessary. No code, input/output comparisons, timing baseline or online validation is supplied. Inferred code is not recovered original private-server source, and neither first-pass success nor a general 90% speedup is established. This is more specific than the existing generic Fortnite reader idea, but no evidence links their authors/projects, so it is retained separately. REA is not mentioned; no game was run here.

Candidate snapshot: 0 likes, 16 views, 0 reposts. Ninety percent is claimed time saved, not feature coverage.

## Sources

- [27.11 author's IDA/MCP/Claude storm-implementation account, October 28, 2026](https://x.com/i/status/2115453274664948001)

[中文](../fortnite2711-claude-ida-storm-server-rebuild.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
