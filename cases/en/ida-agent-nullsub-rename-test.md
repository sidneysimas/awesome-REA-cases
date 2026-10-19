# IDA agent self-test: ten nullsubs individually renamed and restored

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-20
Stage: Analysis test

At 00:19 Beijing time on October 20, @mornpeak describes selecting ten nullsubs in an IDB and having an agent loop over individual rename calls. They report 10/10 renamed and 10/10 restored in under one second overall, with warm calls taking milliseconds. The target is AI-connected IDA symbol manipulation and undo, not recovery of a particular program's logic.

The October 19 parent at 23:53, before this window, describes a personally expanded 98-tool version versus official IDA MCP. Its colloquial batch-renaming claim is clarified here as a loop. Hundreds of symbols processed in groups and an IDA Undo review are plans, not scale tests. No plugin repository, logs, model or timing method is available; REA is unconfirmed and multi-agent IDB stability cannot be inferred.

## Sources

- [mornpeak's ten-symbol rename/restore self-test](https://x.com/i/status/2112216965372940463)
- [Earlier parent: 98 tools versus official MCP](https://x.com/i/status/2112210641796870462)

[中文](../ida-agent-nullsub-rename-test.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
