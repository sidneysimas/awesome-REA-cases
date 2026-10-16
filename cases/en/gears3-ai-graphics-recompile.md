# Gears of War 3: AI-assisted static recompilation and graphics work

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-17
Stage: In progress

At 01:27 Beijing time on October 17, GloriousEggroll described weeks or possibly months of work on a Gears of War 3 recompile, saying it uses the decompiled SonicDE GPU backend as a base rather than directly relying on Xenia's Xbox 360 graphics translator. The author reports improved frame rates with a 4K upscale and no FSR, but remaining combat drops. Their opinion about whether other ports are native is not this collection's technical judgment. Reading the same author's 02:40 clarification within the window changes the description to static recompilation, not full decompilation: no UE3 source was used; a modified ReXGlue translates PowerPC instructions in default.xex from the user's ISO into portable C++, compiled into an x86-64 Linux program. The author explicitly credits Xenia kernel/system services and XenonRecomp analysis and translation foundations. XenosRecomp converts shader binaries to HLSL, then DXC compiles to SPIR-V for Vulkan; plume provides renderer libraries. At 03:18 the author adds that they are not an emulation expert and probably would not have attempted this without AI. Tool details and performance remain author statements. This collection did not obtain or run source, an ISO, benchmarks or full compatibility tests. The project is not described as recovering original names and source structure, and a video or 4K setting does not establish sustained stable frame rates.

October 17 candidate snapshot: 239 likes, 4,767 views, 21 reposts; not independent performance validation.
Supplementary author replies are within the same strict window; no UE3 source, mechanical translation and dependency credits are retained as author statements.

## Sources

- [GloriousEggroll's original WIP post](https://x.com/i/status/2111146922522402943)
- [Author's ReXGlue, shader and runtime clarification](https://x.com/i/status/2111165298531270905)
- [Author's AI motivation and limits of personal expertise](https://x.com/i/status/2111175047033528355)

[中文](../gears3-ai-graphics-recompile.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
