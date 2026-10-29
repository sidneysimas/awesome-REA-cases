# Streets of Rage: RuiNelson combines LLM analysis and RageDecompiler to recompile 68000 logic into C++

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-29
Stage: In progress

At 17:24:26 Beijing time on October 29, 2026, The Gaming Emporium (@McGroin83) introduces RuiNelson's PC static recompilation of SEGA's 1991 Mega Drive game Streets of Rage. Supplementary reading obtained the main StreetsOfRageProject README at commit d56258e26cddaf385ade8a7d44bc03dd6a5e2e4d and confirmed that the recompilation submodule directs readers to it. The main document credits Genesis Plus GX as a hardware reference, gsaurus's disassembly and annotations as a starting point, and Claude, ChatGPT and Grok 4.5 for assistance. Prior work is not attributed to AI recovering everything from scratch.

RageDecompiler disassembles Motorola 68000 ROM routines and translates them into C++, following direct calls from entry and interrupt vectors. Indirect calls cannot be covered by static traversal alone. Runtime reports addresses lacking compiled functions, feeding an aux_addresses ledger and speculative discovery loop of playing, recording and recompiling. The project keeps LLM analysis manuscripts, labels and manual reimplementations, including compression/decompression and VBlank-wait replacements. This is incremental recovery, not proof that all procedures are recovered or byte-matched.

The SDL3-based MegaDriveEnvironment still supplies VDP, audio, input and related hardware compatibility. Removing emulated-device dependencies, making every routine readable and enhancing rendering remain roadmap items. The documented autoplay reads the host's original RAM layout and uses recovered enemy state machines, timings and hitboxes to choose actions through a virtual controller, without directly writing RAM. It is symbolic rule-based AI, not a trained neural network or a live LLM game player.

The report lists Windows/Linux/macOS build directions, but this collection did not compile, run or validate cross-platform behavior or a complete playthrough. Users must provide a compatible ROM they are entitled to use; original game material is not distributed. Public source does not grant game rights. Included as public, in-progress recompilation research; REA is unspecified.

Candidate snapshot: 12 likes, 432 views, 0 reposts. Later lookup does not replace it.
Hardware compatibility and indirect-call discovery remain relevant; symbolic AI is not an LLM player.
Public documents were read statically; no builds, ROM execution or platform retests.

## Sources

- [The Gaming Emporium introduces RuiNelson's Streets of Rage project, October 29, 2026](https://x.com/i/status/2115736509437329888)
- [Supplementary: pinned StreetsOfRageProject README on discovery, prior work, LLM credits and symbolic AI](https://github.com/RuiNelson/StreetsOfRageProject/blob/d56258e26cddaf385ade8a7d44bc03dd6a5e2e4d/README.md)
- [Supplementary: recompilation submodule README, commit dated October 28, 23:32:39Z](https://github.com/RuiNelson/StreetsOfRageRecompilation/blob/cb14e06d7c7e8d9c0084bccbc8f54dbde617cbec/README.md)

[中文](../ruinelson-streets-of-rage-ai-static-recompilation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
