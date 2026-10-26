# crashlens: connecting REA crash triage to coding agents

Category: Applications and clients · REA
Record date: 2026-10-25
Stage: Related project

On October 16, 2026, @rae1101x (Minglei) proposes a crash-triage Skill beside Hermes's reverse-engineer-anything for core dumps, panics and sanitizer reports, describing it as read-only and compatible with pinned rea-agents@6.4.0, and offering a PR. At 19:54 he describes explaining production crashes and bugs when logs are insufficient, calling the project early. A supplementary same-thread 16:13 original already says crashlens was built on REA. It is not an unstarted idea, but an offer to submit a PR and willingness to review it do not establish submission, merge or official release.

At 00:26:57 Beijing time on October 25, the current-window candidate reports Claude Code finding the cause of a native crash without logs, source or debug symbols in one turn instead of four. At 02:05:09 the same author shares the debugging direction with another user. In an after-window reply at 15:10:24, he explains that the one-turn result used a pass that decompiled the failing function and its caller and supplied Claude Code with a report. Connected over MCP, REA also lets the agent drive Ghidra and decompile more functions, but this is slower and useful when the bug lies beyond those two functions. Turns for a pre-generated report do not measure fully autonomous MCP end-to-end runtime or establish a fourfold speedup for all crashes.

The public README was reread. Its latest modification is commit 74c3ace797019d084bbf810f3f1f2ef48adf277b, committed at 11:45:44 Beijing time on October 26, after the window. It is supplementary project/documentation evidence, not proof all current features existed early on October 25. The prototype handles Linux x86-64 cores, multilingual stacks and sanitizer reports, assembling failing frames, context, optional source attribution and input hashes. Current documentation offers a Claude Code plugin and four read-only MCP tools; native cores need REA, with optional Ghidra pseudocode labeled as decompiler output rather than original source. It lists the four-versus-one-turn stripped-binary benchmark and explicitly calls these small test repos, not a study. Binary identity, complete comparison runs and production acceptance were not independently verified. Basic analysis is offline and never runs the target; optional --ai sends a report containing code snippets and logs to Anthropic. Read-only is not a no-egress guarantee. No prototype was installed or executed and no project benchmark was run; its related-project classification and early status are retained.

Earlier candidates: October 16, 2026 at 19:11 and 19:54. New candidates: October 25 at 00:26:57 and 02:05:09. All times Beijing time.
Four turns versus one is an author report using pre-generated failing-function/caller evidence, not a controlled end-to-end comparison of fully autonomous MCP analysis.
The after-window author reply at 15:10:24 on October 25 and README committed at 11:45:44 on October 26 are supplementary only. Hermes integration is unconfirmed; no prototype or benchmark was run.

## Sources

- [Candidate: author's proposed Hermes crash-triage Skill](https://x.com/i/status/2111052456151154858)
- [Candidate: production-debugging vision and early status](https://x.com/i/status/2111063236355498247)
- [Same-thread 16:13 project introduction (supplemental source)](https://x.com/i/status/2111007641715786116)
- [Public crashlens project and README](https://github.com/mingleiw/crashlens)
- [New candidate: four versus one turn for a stripped native crash, October 25, 2026](https://x.com/i/status/2114030898815611097)
- [New candidate: same author's REA debugging direction, October 25, 2026](https://x.com/i/status/2114055611562500158)
- [After-window author clarification: a two-function report differs from driving MCP, October 25, 2026](https://x.com/i/status/2114253225247625532)
- [After-window pinned public README, October 26, 2026](https://github.com/mingleiw/crashlens/blob/74c3ace797019d084bbf810f3f1f2ef48adf277b/README.md)

[中文](../crashlens-rea-crash-triage-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
