# Dinosaur: the acceleration rule

Category: Games and preservation · REA
Record date: 2026-10-12

t-rex-runner is a browser runner similar to Chrome's offline dinosaur game. This analysis targets an HTTP web version, not the browser's built-in chrome://dino. A contributor used REA to read scripts and locate the initial speed, acceleration and update branches, then used an independent Playwright controller on the original page to verify the relationship between update counts and speed and build an interactive demonstration. Reverse engineering answers a specific gameplay question: when does it accelerate, and by how much each time? On October 12, 蓝哥AI also reported generating a local replica with REA and Codex and posted a side-by-side video of the original, the official case version and the self-made version. This is an author report of additional reconstruction work, not behavioral-equivalence verification performed by this collection.

Follow-up posted: 2026-10-12T18:41:50+08:00 (Beijing time)
Follow-up engagement snapshot (2026-10-12): 6 likes | 525 views | 0 reposts

## Sources

- [Case PR](https://github.com/morluto/rea/pull/1203)
- [Original observations and experiments](https://github.com/morluto/rea/blob/main/website/evidence/calculator-and-dino.md)
- [This review: local reconstruction and side-by-side comparison](https://x.com/0xlangeai/status/2109595393260761111)

[中文](../dinosaur-speed.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
