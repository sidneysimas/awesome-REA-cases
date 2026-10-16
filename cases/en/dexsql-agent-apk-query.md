# DexSQL: let agents query APK and DEX call relationships with SQL

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-16
Stage: Related project

An October 16 tool roundup recommends LSPosed/dexsql-release for AI agents to query classes, methods, strings and call relationships in Android APK/DEX files using SQL, reducing repeated manual browsing. Supplementary reading of the project README confirms that one executable supplies CLI and MCP interfaces, lets agents combine signatures, strings and call predicates, and exposes Smali. Parsing is local and leaves input unchanged, but whether results reach a model depends on the AI client's settings. The project compares eight query types on a roughly 372 MiB QQ 9.3.55 APK, documenting result-set checks, timeouts and cache conditions, and acknowledges that DexDec was faster for its repeated caller query in that run. These are project benchmarks, not rerun by this collection or proof of automatic original-source recovery. Crucially, core DexSQL is a closed-source binary under DexSQL Binary License 1.0; the installation Skill, documentation and benchmark materials are separately MIT-licensed. A public GitHub repository does not make the whole tool open source. The README is supplementary project documentation, not a new author measurement in this window. This collection did not download or execute the binary.

Evidence: this window's recommendation and supplementary project README; project-reported benchmarks, not executed here.
License distinction: closed-source core binary; public Skill, documentation and benchmark materials under MIT.
Latest supplementary README commit: e9c89eae180895c8ae7b24da01fa219c58233775, 2026-10-15T12:41:41Z; before this window, used only to check project scope and licensing.

## Sources

- [October 16 roundup recommending DexSQL](https://x.com/i/status/2110962000675434613)
- [LSPosed project description, benchmark caveats and licensing](https://github.com/LSPosed/dexsql-release)

[中文](../dexsql-agent-apk-query.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
