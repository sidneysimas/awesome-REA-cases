# Notion: clipboard paths

Category: Applications and clients · REA
Record date: 2026-10-12

Notion is a document and knowledge-management tool. Its Electron desktop app needs interprocess communication between page code and system features. A contributor investigated how clicking Copy sends content to the system clipboard, tracing the frontend API through a preload wrapper, IPC messages and the main-process receiver. Subsequent analysis of a real client package identified three static candidate paths—copy, copyText and copyImage—leading to Electron or browser clipboard interfaces. The result explains this feature's implementation chain rather than rebuilding all of Notion.

A later post further describes copying Notion blocks while preserving text, formatting and block structure, and reports that copied HTML carries a notionvc ID linking it to saved block data. This is a secondary post-level account; the underlying implementation details are not independently verified here.

Additional clipboard/block association details reported 2026-10-13; source is a post, not an independent implementation test.

## Sources

- [Initial case](https://github.com/morluto/rea/pull/961)
- [Subsequent hands-on test](https://github.com/morluto/rea/pull/1874)
- [REA Notion clipboard case details (X post)](https://x.com/i/status/2109842048023212348)

[中文](../notion-clipboard.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
