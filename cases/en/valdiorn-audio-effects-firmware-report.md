# Guitar effects: emulate the original firmware, then compare a standalone C++ library

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-17
Stage: Needs verification

At 13:33 Beijing time on October 17, @RealYDT recounts guitar-effects maker valdiorn's experience. Supplementary Hacker News research located the original comment, dated October 15 at 15:19:19 UTC, or 23:19 Beijing time. It predates this candidate window and is used only as a traced source. valdiorn says they run a small professional-audio company and are building an Eventide H90-like multi-effects processor with reverb, delay and chorus algorithms. The H90 is the intended product benchmark, not an established decompilation target.

They report studying three main competitors' products in the preceding 72 hours, including Strymon Big Sky, and say Opus 5.5 handled the relevant decompilation with one prompt in three hours. The method was to ask Claude to build an emulator executing original firmware/ROM, rather than merely generate similar-sounding effects, then convert the logic into a standalone C++ library and compare results against the emulator. They say all sounded excellent. For Lexicon 224, Claude reused code it found on GitHub from a week earlier; the entire Ursa Major range allegedly took 20 minutes. These figures cannot be added into a reproducible overall project duration, nor can reused code be credited as independently recovered by the model.

The original comment confirms the gist of the retelling but publishes no emulator, C++ library, firmware versions, test vectors or numerical/listening comparison logs. The referenced Lexicon repository was not identified. There is no evidence of bit-exact equivalence, complete competitor-product coverage or a shipped product. The commenter expresses concern and says they will not box and resell competitors' algorithms; the research account does not establish commercial permission. This collection ran no firmware or code, and REA use is unconfirmed.

Original comment: October 15, 2026, 23:19 Beijing time; the in-window candidate is an October 17 retelling.
Author-reported emulator comparisons and listening, not a publicly reproducible test or proof of commercial rights.

## Sources

- [In-window Chinese retelling](https://x.com/i/status/2111329818914791727)
- [Supplementary original: valdiorn's method, timing and limits](https://news.ycombinator.com/item?id=50104955)

[中文](../valdiorn-audio-effects-firmware-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
