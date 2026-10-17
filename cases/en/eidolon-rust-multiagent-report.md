# Eidolon: a multi-agent binary-to-Rust comparison report

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-18
Stage: Needs verification

At 22:07–22:08 Beijing time on October 17, 2026, Rovshan (@mrboldpineapple) reports giving AI a 64 KB-class demoscene .exe to test end-to-end reverse engineering: unpacking, extracting shaders and animation curves, recovering the music synthesizer and rewriting it in Rust. The follow-up identifies the original as Eidolon by Poo-Brain and calls it the Revision 2017 PC 64k winner; that identity and award were not separately checked in this review.

The author says a coordinator split the work among agents handling unpacking, synth recovery, Rust porting and per-frame SHA-256 checks. He lists GPT-6 Astra, GPT-6.1 Sol and Claude Opus 5.5, with about 760M tokens. He reports roughly 40 hours, matching all 27,000 frames and every audio sample, and shrinking from 60,928 to 48,128 bytes, described as 21% smaller. Matching means the claimed rendered pictures and sound, not a Rust executable byte-identical to the original .exe. Model names, time, tokens and figures retain the posts' conventions.

The main post has a short link, but its destination content, source code, comparison logs, frame hashes and audio records were not obtained. Neither the figures nor end-to-end success are independently verified. REA is not mentioned and no target code was run here.

Sources published October 17, 2026, at 22:07 and 22:08 Beijing time.
About 40 hours, 760M tokens, 27,000 frames and 60,928→48,128 bytes are author reports without obtained comparison logs.
Original-work identity/award, model labels and output equivalence were not independently verified; REA is unconfirmed.

## Sources

- [Author's main post: unpacking, Rust rewrite and claimed output equivalence](https://x.com/i/status/2111459038823157986)
- [Author's follow-up: target, models, delegation and size figures](https://x.com/i/status/2111459359867699273)

[中文](../eidolon-rust-multiagent-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
