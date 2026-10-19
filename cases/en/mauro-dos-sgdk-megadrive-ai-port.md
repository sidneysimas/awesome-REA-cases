# Mauro's Mega Drive port: AI converts a DOS game to C, with manual memory and graphics adaptation

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-19
Stage: In progress

At 10:03 Beijing time on October 19, Mauro Xavier (@MXRetroDev) answers a joke describing his project as a one-prompt Rust port, explicitly denying using Rust or REA. He took the original DOS floppy-disk version, asked AI to reinterpret and convert as much code as possible to C using SGDK, a Mega Drive development framework, then requested asset conversion and integration. The goal is running the game on a stock Mega Drive without enhancement chips, not emulating it on a modern machine.

His earlier 06:42 post in the same conversation reports a complete start-to-finish playthrough without a single crash, while graphics and performance still need work. That post asks readers to identify the game from screenshots; the readable text obtained this round does not name it. No title is guessed from images, but the concrete engineering account is retained. The earlier post is supplementary background, not a new candidate in this window.

The author says 64 KB of RAM and 64 KB of VRAM caused numerous problems requiring manual adjustments. AI helped write Python tools to pre-render selected polygonal entities at specified positions, then assembly routines for software zooming of those sprites. With over 190 camera views, manual work on Mega Drive colors and dithering remains. He stresses that handing all adaptation to AI would not yield the same result: AI did much of the work, but this is not an unattended-success claim.

No source, ROM version, build record, frame-rate measurements or independent playthrough was obtained. Claude or any particular model is not inferred. Completion and crash-free play are attributed only to the author; neither the game nor target code was run here.

## Sources

- [Candidate: Mauro clarifies SGDK/C and the division of AI and manual work](https://x.com/i/status/2112001737896673737)
- [Supplementary 06:42 original: stock Mega Drive and playthrough report](https://x.com/i/status/2111951070188765668)

[中文](../mauro-dos-sgdk-megadrive-ai-port.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
