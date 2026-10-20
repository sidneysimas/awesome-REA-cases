# xbox-boot-re: reconstructing the original Xbox boot animation from one BIOS

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-20
Stage: In progress

At 15:30 Beijing time on October 20, a candidate directory update introduces bennyborn/xbox-boot-re: recover the original Xbox boot animation's green blob, chamber, logo and sound from one 1 MB BIOS and build a standalone renderer. The README pinned to commit 12a3396 explicitly attributes most analysis, specification and reconstruction to Opus 5.5 in Claude Code, with a human continuously choosing directions and reviewing the work, not an unattended process. Its input is a Complex 4627 Retail (1.0) modified BIOS dumped from the author's own modified console, not an unmodified retail dump. Other BIOS versions are not covered.

The project reports bit-for-bit matching of timing, camera, geometry, blob, textures and GPU command streams against recorded xemu runs, and word-for-word matching of the sound sequencer and DSP program. Audio voice synthesis instead approximates insufficiently documented hardware using xemu's interpretation; this does not establish native-exact audio throughout or final-pixel equivalence. The reconstruction is a C core targeting native hosts and wasm32. A WebGPU frontend adds free-camera, wireframe and Next Gen reinterpretations, not a complete Xbox emulator. Specifications, vectors and test code are public. The build and Pages-deployment CI for this commit, started at 05:08 Beijing time on October 16, succeeded. This establishes a successful project pipeline, not this collection rerunning BIOS comparisons or hardware validation.

The original commit is dated October 16 at 05:06 Beijing time: historical supplementary material prompted by this window's candidate, not newly completed October 20 development. The README states that its data directory contains Microsoft's geometry, samples and tables; AI reconstruction does not change those rights. Repeating the research requires a legally obtained BIOS. This collection read documents, test layout and CI status only; it did not download a BIOS, execute target code or watch the complete demonstration.

October 20 candidate snapshot: 0 likes, 46 views. Its 26-star directory figure is a third-party snapshot, not independently counted.

## Sources

- [October 20 candidate directory introduction](https://x.com/i/status/2112446312104825271)
- [October 16 pinned README: AI attribution, matching scope and data rights](https://github.com/bennyborn/xbox-boot-re/blob/12a3396aa77f72c8d2fd94c0988c7e11539b47e7/README.md)
- [Same-commit core documentation: interfaces, test layout and unreconstructed states](https://github.com/bennyborn/xbox-boot-re/blob/12a3396aa77f72c8d2fd94c0988c7e11539b47e7/docs/core.md)
- [Successful project build and Pages deployment, not independent replication](https://github.com/bennyborn/xbox-boot-re/actions/runs/38807512169)

[中文](../xbox-boot-re-claude-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
