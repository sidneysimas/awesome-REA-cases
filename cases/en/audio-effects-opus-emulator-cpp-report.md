# BigSky and Ursa Major: an Opus account of firmware emulation followed by C++ reconstruction

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At exactly 16:00 Beijing time on October 20, included in this window, @mylifcc relays an audio-hardware operator's account of using Claude to investigate competitors' algorithms. The original HN comment, posted by valdiorn at 23:19 Beijing time on October 15, says they run a guitar-pedal and audio-effects company and are building a processor similar to Eventide H90, competing on reverb, delay and chorus algorithms. They claim to have investigated three competing products, including Strymon Big Sky, over the preceding 72 hours, with one Opus 5.5 prompt taking three hours; the entire Ursa Major range allegedly took twenty minutes. All timings and scope are self-reported, without a product list or usage invoices.

Their described method first has Claude build an emulator executing original firmware/ROM, then converts it to a standalone C++ library and compares against the emulator, aiming to avoid merely similar-sounding effects. The author says they listened to all results and found them excellent, but publishes no model outputs, firmware versions, C++ libraries, test signals, error thresholds or sample-by-sample logs. Neither 100% native equivalence nor independent replication follows. They explicitly say the Lexicon 224 portion found and reused someone else's existing code, rather than every result being recovered from scratch by this prompt.

The relay thread also names joelanders/reflecticon-224. Its README at an October 13 commit confirms a browser/plugin emulator for Lexicon 224/224X/224XL using user-supplied ROMs, with documentation still in progress. It establishes neither valdiorn's BigSky/Ursa Major results nor the relay's complete schematic-to-Verilog story. The HN comment and repository are out-of-window supplementary material, not newly collected posts or new development in this window. This collection executed no firmware, downloaded no target ROMs and performed no listening tests. Algorithm rights and permission for commercial copying cannot be inferred from a research account.

## Sources

- [This window's 16:00 candidate relay of audio-algorithm research](https://x.com/i/status/2112453769220780514)
- [October 15 original HN comment: valdiorn's method, timing and attribution](https://news.ycombinator.com/item?id=50104955)
- [Same-author 16:00:01 follow-up outside the window: emulator, C++ and reuse](https://x.com/i/status/2112453770357481754)
- [Out-of-window reflecticon-224 README: user-supplied ROMs, not BigSky validation](https://github.com/joelanders/reflecticon-224/blob/37fde47f6cf94d4f4f96f3c233382e2c43a70354/README.md)

[中文](../audio-effects-opus-emulator-cpp-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
