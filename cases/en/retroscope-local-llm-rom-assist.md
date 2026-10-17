# RetroScope: a local-LLM assistant for ROM instruction references

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-17
Stage: In progress

At 13:44 Beijing time on October 17, 2026, なごみ (@141_80_call) reports implementing RetroScope, a local-LLM analysis assistant. The concrete workflow feeds breakpoint-time registers, ROM and instructions to Python and picks out other instructions referring to a target address, helping inspect address relationships in an existing program rather than relying solely on model guesses. The author explicitly says searching only works with absolute addresses so far, accuracy remains inadequate, and mentions Ghidra-like tools as a comparison.

The source includes a screenshot but no public repository, model identity, full data flow, target ROM name or accuracy measurement. It does not establish relative-address handling, complete control flow, automatic decompilation or replacement of Ghidra. This is a named tool in progress, with the local LLM's role limited to the author's description. No software was installed or run, and REA use is unconfirmed.

Absolute-address search only; no published accuracy or runnable artifact, not independently verified.

## Sources

- [Author's RetroScope implementation update](https://x.com/i/status/2111332462811087061)

[中文](../retroscope-local-llm-rom-assist.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
