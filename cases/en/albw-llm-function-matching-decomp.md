# A Link Between Worlds: LLM function reconstruction with separate hack counts and checker exemptions

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-22
Stage: In progress

At 15:42 Beijing time on October 22, 2026, yibie introduces an LLM-assisted per-function decompilation of The Legend of Zelda: A Link Between Worlds. To trace this candidate, this review read the public README, docs/LESSONS.md, tools/fn.py and commit ee841b32311d39154be05bc978a45170e918e0b3 in 7akeem0/albw-decomp-ai. The original commit is dated October 15 at 08:10:28 Beijing time, before this window: supplementary project evidence, not code newly released on October 22. Its co-authorship includes Claude Opus 5.5; REA use is not stated.

The goal is individual C/C++ functions compiled with the original compiler for the USA 3DS release, supporting further investigation and preservation, not a completed PC port. The README reports 16,544 source-included matches out of 25,986 functions (63.7%): 15,662 defined by the project as honest (60.3%) and 882 relying on hacks such as weak declarations, scheduling barriers, inline assembly or unused locals (3.4%). Another 127 previously matched entries lack source: 92 lost sources, 26 unredistributable third-party-library sources, six prebuilt middleware/SDK entries and three duplicate interior addresses. Methods also include a custom machine-code-to-C translator, source permuters and harvesting similar functions; not every result is attributed to LLMs acting alone.

This review only read the checker statically. It compiles a candidate, parses its ELF object and compares instruction words, but accepts differences for several relocations, absolute literal addresses, linker inlining and branches outside the function range. Thus the README's byte-exact and MATCH refer to a project-specific checking convention, not equality of every raw byte, and do not prove identical call targets, whole-program linking or runtime semantics. Honest only means avoiding the listed source hacks, not an independent security audit.

LESSONS retains failures: lifting machine code and locally repairing it matched only 18/233 random unmatched medium functions, 1/119 large functions and 0/30 huge functions; 250 pairs yielded no reusable rewrite rules. The author attributes the remaining difficulty to shared-header forms such as inlined constructors, setters and temporary strings. These are project-reported tests, not independently rerun results. Rechecking requires a legally obtained game code.bin and ARM Compiler 4.1 build 1049. The repository supplies neither game assets nor compiler and has no license file. This collection downloaded or executed no target, installed no dependencies and compiled no game. The 63.7% is not playable-game completion or recovery of all original source.

Candidate date: 2026-10-22T15:42:53+08:00; supplementary code originally dated 2026-10-15T08:10:28+08:00.
63.7%, 60.3% and 3.4% are README figures; MATCH includes linking/relocation exemptions and was not independently recomputed.

## Sources

- [Candidate: yibie on per-function reconstruction and hack counts](https://x.com/i/status/2113174237251084670)
- [Supplementary: README at the original commit](https://github.com/7akeem0/albw-decomp-ai/blob/ee841b32311d39154be05bc978a45170e918e0b3/README.md)
- [Supplementary: project lessons and failure measurements](https://github.com/7akeem0/albw-decomp-ai/blob/ee841b32311d39154be05bc978a45170e918e0b3/docs/LESSONS.md)
- [Supplementary: checker and its accepted differences](https://github.com/7akeem0/albw-decomp-ai/blob/ee841b32311d39154be05bc978a45170e918e0b3/tools/fn.py)
- [Supplementary: original commit date and Claude co-authorship](https://github.com/7akeem0/albw-decomp-ai/commit/ee841b32311d39154be05bc978a45170e918e0b3)

[中文](../albw-llm-function-matching-decomp.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
