# Civilization civd: AI-assisted reconstruction with project hash checks after a four-byte startup correction

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-21
Stage: In progress

At 23:22 Beijing time on October 20, 2026, Xiao Tan (tvytlx) recounts AI-assisted reconstruction of the original 1991 DOS Civilization. At 13:08 and 13:09 on October 21, two candidates by Jimmy Young (jimmyyangrz) name Steve Melia and discuss the old toolchain, inferred names and memory constraints. Supplementary inspection locates the public sjmelia/civd repository, correcting the earlier evidence boundary of four unexplained differing bytes without identified code. Source, a technical book, build rules and project CI are now inspectable, but this collection still has not independently reproduced the build.

Pinned commit 6dff0891 is dated October 20 at 03:02 Beijing time, before this candidate window. Its README credits models from OpenAI, Anthropic and Google for code and documentation, followed by editing and build verification, and explicitly builds on prior OpenCiv1 work. The earlier account also acknowledges possible training-data exposure to that prior code, so this is not established from-scratch work uninfluenced by existing implementations. Names, comments and some types are inferred; matching bytes do not recover MicroProse's original source. The project links the modern-platform reciv reconstruction, whose runtime behavior was not checked here.

The same commit's build notes and justfile use Microsoft C 5.1, MASM 5.10, LINK 5.01 and MAKE 4.07. CONTROL.C and CITYMGT.C use loadfix -192 to constrain compiler memory, because available memory and identifier spelling affect emitted layout. Raw linker output remains CIVRAW.EXE. CRTEDIT checks length, CRC and expected bytes, changes the four destination bytes of one far call, then checks the result as CIV.EXE. The call changes from runtime environment initialization to an immediately returning empty_hook; why the original bypasses initialization remains unknown. These four bytes are an explicit post-link correction, not four still-unmatched bytes in the final artifact.

After a clean build, just verify checks repository-pinned SHA-256 hashes for raw linker output, final CIV.EXE 474.05, the MCGA graphics driver, AdLib sound driver and MISC.EXE. GitHub Actions run 39505519022 corresponds to 6dff0891 and was created on October 21 at 06:05 Beijing time, before this window. Its verify job and tool-installation/verification/documentation step succeeded, and the workflow explicitly invokes just verify. These are the project's pinned-hash and CI evidence, not this collection obtaining the original and independently comparing hashes or testing gameplay.

Jimmy's candidate additionally reports 120 source files including 44 C and seven assembly files, intermittent work over months and subscription tiers around GBP15 per month from three providers with unused quota. Those remain secondary claims, without an independent file count or billing audit, not a measured total project cost or exact labor time. REA is not stated. The goal is readable implementation and game-history preservation, not Civilization VI strategy AI. No target was executed, old compiler installed or legal provenance of assets and source determined here.

## Sources

- [Retained source: Xiao Tan's toolchain and four-byte-difference account](https://x.com/i/status/2112565000372101178)
- [October 21, 13:08 Jimmy names Steve Melia and the DOS Civilization reconstruction](https://x.com/i/status/2112773003981594700)
- [Same author at 13:09 on file counts, inferred names and memory constraints](https://x.com/i/status/2112773213134745743)
- [Supplementary older commit 6dff0891 README: AI credits and reconstruction limits](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/README.md)
- [Same-commit build notes: memory and the four-byte call correction](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/book/src/architecture/toolchain_clues.md)
- [Same-commit justfile: clean build and pinned-hash checks](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/justfile)
- [October 21, 06:05 successful project CI for that commit](https://github.com/sjmelia/civd/actions/runs/39505519022)
- [Same-commit workflow: commands actually run by the verify job](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/.github/workflows/build.yml)

[中文](../civilization-dos47405-ai-reconstruction-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
