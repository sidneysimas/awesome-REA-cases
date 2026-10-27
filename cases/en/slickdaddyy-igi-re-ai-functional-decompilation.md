# IGI-RE: an AI-assisted Project I.G.I. rewrite checked with Unicorn for behavior, not byte identity

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-27
Stage: In progress

At 15:30 Beijing time on October 27, 2026, yibie recommends IGI-RE, intended to preserve Innerloop Studios' 2000 Project I.G.I.: I'm Going In. Supplementary reading covers slickdaddyy/IGI-RE's README at commit 088950a517a18bfbb15c7dc6b28b09564f85c7d4, dated October 26 at 16:00:39 Beijing time, before this window. The author explicitly discloses AI coding tools in development, debugging and testing, without naming a model or REA. A list name alone does not establish REA involvement.

The project rewrites IGI.exe function by function in readable C. Ghidra locates functions; dinput.dll redirects original functions to rewrites. Unicorn runs original machine code and rewritten versions from identical states and compares returns, memory writes, stack cleanup and call order. Floating-point code is tested under the game's x87 rounding modes, followed by scripted mission/frame comparisons. This is functional decompilation, not a requirement to compile identical bytes. The README reports 5,376/5,376 functions rewritten and named, 90,078 passing differential tests in 425 files, all 14 missions checked beside the original, and a standalone igidecomp.exe built from source. These are project claims, not tests by this collection or formal equivalence over every input.

The target is a specific EU release (also described as Chinese in the document) of IGI.exe plus legally held game assets; other releases are unsupported. The linked Microsoft C runtime is not decompiled and is replaced by system msvcrt.dll. It runs on Windows or Linux with Wine; documentation says Wine 11 is used for development/live tests and notes that the target includes a no-CD modification. Credits acknowledge existing IGIPatch names, disc-check notes and other tools, so foundational work is not all attributed to AI. No build, dependency installation, gameplay or test rerun was performed here. Included as in progress for its concrete implementation and inspectable methodology.

Candidate snapshot: 1 like, 65 views, 0 reposts. Eight stars and 1,142 files are the post's figures, not validation of functionality or AI contribution.
5,376 functions, 90,078 tests, 425 test files and 14 missions are pinned-README reports, without an independent rerun or proof over all inputs.

## Sources

- [Candidate: yibie introduces IGI-RE, October 27, 2026](https://x.com/i/status/2114983062060904506)
- [Supplement: pinned October 26 README, AI disclosure and verification scope](https://github.com/slickdaddyy/IGI-RE/blob/088950a517a18bfbb15c7dc6b28b09564f85c7d4/README.md)

[中文](../slickdaddyy-igi-re-ai-functional-decompilation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
