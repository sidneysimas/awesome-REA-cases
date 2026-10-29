# SuperGhidra: a report of persistent Ghidra/MCP and recompilable C

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-29
Stage: Related project

At 09:19:57 Beijing time on October 29, 2026, Dopax (@tensorstaff) lists SuperGhidra as an October project, describing a persistent Ghidra headless daemon/MCP to reduce agent cold starts, recompilable C rewriting, MSVC RTTI/MFC layouts and Z3 checks, with 164 stars. It is a distinct tool from Kuna, not a completed target reconstruction.

Supplementary reading of yuatemycat/SuperGhidra's public README separates the read-only Ghidra oracle, JSON write overlay, standalone Python class recovery and a separate MCP bridge repository. Actual Ghidra decompilation requires Ghidra 11/12, OpenJDK 21 and PyGhidra; the zero-JVM standalone prototype is not a full decompiler. The README explicitly reports only 11 of 154 exports across four DLLs decompiling, with seven compiling; complex branches, floating point and unhandled instructions can fail. C post-processing reports 22.62% compilation across 1,300 functions and 25.26% on a held-out split, not arbitrary-program behavioral equivalence.

The document describes Z3 P-code equivalence checking and layout-obligation gates, but this collection did not inspect proof assumptions, run regressions or audit all code. The README labels the project AGPL-3.0-or-later. Performance tables and stars remain project/roundup claims, not retested measurements. Static reading on October 29 checks features and limits only, without guaranteeing concurrent-operation safety, preserved semantics or REA integration.

Same-post snapshot: 0 likes, 23 views, 0 reposts. The author attributes 164 stars to October 29 GitHub statistics; not independently queried here.

## Sources

- [Dopax's SuperGhidra feature description, October 29, 2026](https://x.com/i/status/2115614583184638042)
- [Supplementary project README: operating modes and prototype limits, statically read October 29](https://github.com/yuatemycat/SuperGhidra/blob/master/README.md)

[中文](../superghidra-daemon-mcp-recompilation-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
