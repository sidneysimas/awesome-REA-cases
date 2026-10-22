# Vice City in the browser: a report of an AI-assisted port built on the existing reVC reverse-engineered engine

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-22
Stage: Needs verification

At 17:24:40 Beijing time on October 22, 2026, Shivansh Gupta (@shivanshgupta36) describes oalanicolas's GTA: Vice City browser port. It inherits the C/C++ reverse-engineered reVC Web/wasm-revc engine, compiles it with Emscripten to WebAssembly, renders through WebGL2, uses OpenAL for audio and adapts touch input. It reportedly executes on the iPhone in Safari rather than using cloud gaming. The post explicitly credits years of reVC and WebAssembly community work; this is not AI decompiling the original game from scratch.

The account describes over 1.5 GB of on-demand assets using a virtual filesystem, HTTP Range requests, Web Workers, prefetching/caching and asynchronous I/O. The main city archive is divided into 1,250 independently compressed blocks of up to 256 KiB, reportedly reducing transfers from about 327 MB to 183 MB. The stated 44.22% is a source figure, not independently recalculated here. It cites a project desktop benchmark near 59.95 fps and the poster's iPhone screenshots at 58-60 fps, without guaranteeing sustained 60 fps on all devices.

AI responsibilities are also relayed from project documentation: Codex for engine integration, debugging and testing; Claude for menus/UI; Gemini for optimization including a separate 3D asset viewer. Approximately 7.35 billion logged tokens cover multiple workflows and extensive cached-context reads. They are not 7.35 billion generated tokens and do not directly establish cost or exclusive attribution to the game port.

This review read the full candidate and additionally fetched author information, but did not obtain the linked technical article, exact commit, asset permissions or inspectable performance logs. It ran no game and downloaded no game assets. This remains an unverified secondary account of AI-assisted porting based on prior reverse engineering. REA is not mentioned, and reported browser operation does not authorize redistribution of the game's assets.

Source originally posted 2026-10-22T17:24:40+08:00; 59.95 fps, 58-60 fps, 44.22% and 7.35 billion tokens are source-reported and were not independently recalculated or measured here.

## Sources

- [Shivansh Gupta's account of the Vice City browser port, prior contributions and AI responsibilities](https://x.com/i/status/2113199849936142390)

[中文](../vice-city-wasm-revc-ai-browser-port-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
