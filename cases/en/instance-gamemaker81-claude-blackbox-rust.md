# Instance: a Claude-assisted Rust GameMaker 8.1 editor and engine from black-box specifications

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-28
Stage: In progress

The candidate at 18:24 Beijing time on October 28, 2026 recounts Instance from HN: its author learned programming with GameMaker 8.1 and later used Claude Opus 5.5 to reconstruct the engine and IDE in Rust from specifications written through black-box observation. It says the main body took a morning but quirks took three weeks, including event order, the random-number algorithm and sound_isplaying lagging actual audio. Time and model attribution belong to the report, not this collection's measurements; a one-morning headline must not replace the full three-week account.

Supplementary reading of groverburger/instance's public README and CLEANROOM.md finds a stated process of writing specs from documentation, .gmk/.gm81 project data and black-box observations, followed by implementation from specs. Disassembly, decompilation or debugging of YoYo Games binaries and asset copying are prohibited by project policy. The README lists a visual editor, GML interpreter, 3D, particles, TCP/IP multiplayer and DLL calls including 32-bit DLLs. The whole IDE and player can compile to WebAssembly, with Spelunky Classic among browser examples; this is not browser-side decompilation of the original game. The project explains that Spelunky uses a modification of Derek Yu's publicly released project, replacing supersound.dll with built-in sound. Example games are not all covered by the engine's MIT license.

The master revision read is cac87f1f4b166e07b729c181c96f1b4e0888df97 from October 27, predating this report and used only as project background. Documentation claims Windows, macOS and browser support; Linux is unsupported, though a source build may work. This collection did not build the code, run the browser version, DLLs or black-box tests, and obtained no complete behavioral-coverage measure. Public code/specs do not prove total GameMaker equivalence or certify the report's assertion that one person plus a model creates a legally compliant clean-room team; legal boundaries require separate assessment. REA is unspecified.

Candidate snapshot: 0 likes, 155 views, 0 reposts. A morning, three weeks and Opus 5.5 are secondary-report claims, not independently retested.

## Sources

- [Secondary account of Instance/Claude black-box reconstruction, October 28, 2026](https://x.com/i/status/2115389109187367266)
- [Supplementary public Instance repository](https://github.com/groverburger/instance)
- [Pinned October 27 README: features and platform limits](https://github.com/groverburger/instance/blob/cac87f1f4b166e07b729c181c96f1b4e0888df97/README.md)
- [Project clean-room input and separation policy](https://github.com/groverburger/instance/blob/cac87f1f4b166e07b729c181c96f1b4e0888df97/CLEANROOM.md)

[中文](../instance-gamemaker81-claude-blackbox-rust.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
