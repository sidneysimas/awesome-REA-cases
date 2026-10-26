# jshook: a search-first MCP workspace that loads reverse-engineering tools for AI agents on demand

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-26
Stage: Related project

At 01:56 Beijing time on October 26, 2026, Dan Kornas (@DanKornas) introduced jshook as a response to large MCP schema catalogs consuming an AI agent's context before web-application investigation begins. A small searchable tool surface is exposed first, with promotion to workflow or full profiles when needed. The poster is introducing the project, not established here as its repository developer.

Supplementary lookup found the public vmoranv/jshookmcp repository, whose README matches the candidate's search-first, profile-aware and AGPL-3.0 description. The fixed commit read, abbbd40e49435c71859718c0f6ecf791a9af3e4b, is dated October 25 at 17:12:19 Beijing time, before the candidate window. It explains the design rather than constituting a new release in this window. Documentation describes Chromium/Camoufox CDP control, WebSocket/HTTP/GraphQL and Burp bridges, JavaScript deobfuscation and source-map reconstruction, WASM disassembly, native-analysis bridges including Frida/Ghidra/IDA, hot-reload plugins and declarative workflows.

The README estimates search metadata at about 3K tokens and the full 735-tool profile at about 109K tokens, explicitly dating the measurement to October 10 and asking for remeasurement as the catalog grows. This is project-reported configuration overhead, not an independent model-efficiency benchmark. It does not establish better detection rates, successful recovery without source maps or universal application reversal. No named target's analysis/reconstruction acceptance record was obtained. This collection only read the introduction and documentation, without installing it, attaching a browser, invoking target tools or running tests. REA is not a confirmed engine of this project. It is included as a related AI reverse-engineering tool project.

Related tool project, not run here; the introducing poster is not established as the repository author, and a REA engine is unconfirmed.
About 3K/109K tokens and 735 tools are the README's self-reported snapshot measured October 10, not an independent effectiveness benchmark.

## Sources

- [Dan Kornas introduces jshook's search-first workspace, October 26, 2026 Beijing time](https://x.com/i/status/2114415785720623360)
- [Supplementary public project README at fixed commit abbbd40, October 25, 2026](https://github.com/vmoranv/jshookmcp/blob/abbbd40e49435c71859718c0f6ecf791a9af3e4b/README.md)

[中文](../jshookmcp-search-first-re-workspace.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
