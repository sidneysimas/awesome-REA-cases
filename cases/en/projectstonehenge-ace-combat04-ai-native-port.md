# ProjectStonehenge: an AI-assisted function-by-function native C++ port of Ace Combat 04

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-26
Stage: In progress

The candidate posted at 06:18 Beijing time on October 26, 2026 introduces Onaga00's ProjectStonehenge, a Windows port of the PS2 combat-flight game Ace Combat 04: Shattered Skies. Supplementary reading used the public README at fixed commit 4412348ed9d3532627a8d3f3b16951f308cf33e9, dated October 25 at 14:50:32 UTC, before the window, to establish identity and method. It targets North American SLUS-20152 and describes translating the original PS2 ELF function by function into C++, not an emulator wrapper or automatic static recompilation.

Its AI Disclosure credits Anthropic models working under human supervision for research notes, most code and research tools. That proportion was not audited, and neither a model version nor REA is specified. Credits name Ghidra as the research database, bethington/ghidra-mcp to drive analysis, an Emotion Engine plugin, PCSX2 as a debugger/behavior and save-layout reference, and ps2sdk for symbol references. Prior work must not be attributed to original AI research.

The project lists selectable 60/120/144/240/360 FPS render caps using decoupled rendering and interpolation, while physics and AI retain the original 59.94 Hz. Up to 360 FPS is therefore not independently measured sustained performance or accelerated game logic. The README also describes internal rendering up to 4096×3584, 4K output, FXAA/SMAA, SDL3 keyboard/gamepad input and two-way PCSX2 folder-memory-card interchange; the latter is explicitly beta. Preserving 272 originally unreachable functions and unused scenes is a project statement. They remain unreachable by default, with an exploration interface still planned.

Current requirements are Windows 10/11, Vulkan 1.2 and the user's own North American game-disc data. Linux, VS mode, modding and further optimization remain on the roadmap. This collection only read public documentation statically; it downloaded no game, built no code, ran no tests and did not verify exact-original behavior. The entry remains in progress. Public code, feature lists and high-frame-rate support are not independent reproduction.

Native function-by-function C++ port, not automatic static recompilation; AI involvement is project-disclosed and REA is unconfirmed.
360 FPS is a selectable render cap with 59.94 Hz logic; save interchange is beta and Linux planned. Not independently run.

## Sources

- [Window candidate: ProjectStonehenge PC-port introduction, October 26, 2026 Beijing time](https://x.com/i/status/2114481803796861088)
- [Supplementary project README and AI Disclosure at fixed commit 4412348, October 25, 2026 UTC](https://github.com/Onaga00/ProjectStonehenge/blob/4412348ed9d3532627a8d3f3b16951f308cf33e9/README.md)

[中文](../projectstonehenge-ace-combat04-ai-native-port.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
