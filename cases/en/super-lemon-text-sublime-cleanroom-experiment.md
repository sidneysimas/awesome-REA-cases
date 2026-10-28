# Super Lemon Text: Claude Code rebuilds a Sublime-style Rust editor from behavior

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-29
Stage: In progress

At 03:03:09 Beijing time on October 29, 2026, Lemonator32 reports a clean-room Sublime Text reimplementation experiment inspired by discussion of AI game reversing. A same-author reply names it Super Lemon Text. A name search found lemonator32/super-lemon-text. The README at commit 67de7002e8f96f1cd7c8c68e7c99f3e897db9b1f says Claude Code built the Rust editor from behavioral descriptions without access to the original code, binaries or bundled content. This is behavioral reconstruction, not decompiled Sublime source; isolation and legal compliance were not independently audited.

The project reports Windows milestones M0–M8 complete: editing, multiple selections, settings, tabs/splits, sessions/projects, syntax, navigation, builds and out-of-process Python plugins. macOS/Linux, packaging, performance gates and polish remain unfinished. The original author has stopped development and invites continuation. Coverage documentation distinguishes automated, manual and ignored tests, listing unfinished UTF-16, spell checking, some key bindings and image previews; Japanese IME and dead-key scripts were never run. The README's 500 ms startup, 16 ms input and 60 fps are performance goals, not measurements by this collection.

An API check confirms successful CI for that exact commit, started at 01:13:55 Beijing time on October 29. Project CI does not establish complete parity, absence of skipped tests or independent reproduction here. The repository was created October 24 and the current commit dates to October 29 at 01:13:52, both before the candidate; the post date is not the development start. No target code or dependencies were executed.

Candidate snapshot: 0 likes, 11 views, 0 reposts. Supplementary repository and CI checks establish implementation and test boundaries, not additional window candidates.

## Sources

- [Lemonator32's Sublime reconstruction experiment, October 29, 2026](https://x.com/i/status/2115519757319544858)
- [Same author names Super Lemon Text](https://x.com/i/status/2115519759299031484)
- [Pinned README: Claude Code, clean-room method and unfinished status](https://github.com/lemonator32/super-lemon-text/blob/67de7002e8f96f1cd7c8c68e7c99f3e897db9b1f/README.md)
- [Same-commit test coverage and unrun/unfinished work](https://github.com/lemonator32/super-lemon-text/blob/67de7002e8f96f1cd7c8c68e7c99f3e897db9b1f/docs/test-coverage.md)
- [Successful exact-commit CI, not reproduction by this collection](https://github.com/lemonator32/super-lemon-text/actions/runs/40733708962)

[中文](../super-lemon-text-sublime-cleanroom-experiment.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
