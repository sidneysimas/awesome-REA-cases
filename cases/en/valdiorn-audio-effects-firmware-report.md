# Guitar effects: emulate the original firmware, then compare a standalone C++ library

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-18
Stage: Needs verification

At 13:33 Beijing time on October 17, @RealYDT recounts guitar-effects maker valdiorn's experience. Earlier supplementary Hacker News research located the original comment, dated October 15 at 15:19:19 UTC, or 23:19 Beijing time. This is historical traced evidence, not a new October 18 experiment. valdiorn says they run a small professional-audio company building an Eventide H90-like multi-effects processor for reverb, delay and chorus. H90 is the intended product benchmark, not an established decompilation target.

They report studying three main competitors over the preceding 72 hours, including Strymon Big Sky, saying Opus 5.5 handled relevant decompilation with one prompt in three hours. Claude first builds an emulator running original firmware/ROM rather than merely generating similar sounds, then converts logic to a standalone C++ library and compares against the emulator; all allegedly sounded excellent. Lexicon 224 reused code Claude found on GitHub from a week earlier, while the whole Ursa Major range allegedly took 20 minutes. The timings cannot be added into one overall project duration or reused code credited as independent model recovery. The original supplies no emulator, library, firmware versions, vectors or numerical/listening logs. The Lexicon repository is unverified, with no evidence of bit-exact equivalence, complete coverage or a shipped product. The author says competitors' algorithms will not be boxed and resold; research is not commercial permission.

A new article at 15:27 on October 18 retells the HN three-unit/72-hour and BigSky reverb claims, also saying a hobbyist used Opus 5.5 for a Lexicon 224XL firmware emulator on GitHub. It provides no repository or tests. 224XL is the new article's wording and is not silently equated to the original comment's 224 implementation. Prices such as a USD 69 clone pedal and roughly USD 5,000 collectible original frame a brand-value argument, not this project's cost or reverse-engineering measurements, and are not adopted as technical results. This is additional circulation, not a new experiment or independent confirmation. This collection ran no firmware or code, and REA use is unconfirmed.

Original comment: October 15, 2026, 23:19 Beijing time; the October 17 and 18 posts are retellings, not two independent experiments.
Author-reported emulator comparisons and listening, not a publicly reproducible test or proof of commercial rights.
October 18 article candidate snapshot: 3 likes, 1,386 views; the Lexicon 224XL repository and operation remain unverified.

## Sources

- [October 17 Chinese retelling](https://x.com/i/status/2111329818914791727)
- [Supplementary original: valdiorn's method, timing and limits](https://news.ycombinator.com/item?id=50104955)
- [October 18 recirculation: effects algorithms and brand value](https://x.com/i/status/2111720688038072631)

[中文](../valdiorn-audio-effects-firmware-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
