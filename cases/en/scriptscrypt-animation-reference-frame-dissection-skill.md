# animation-reverse-engineering: Claude Code dissects reference motion frame by frame and ports interactions

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-26
Stage: Related project

The previously deferred candidate posted at 18:50 Beijing time on October 25, 2026 introduces animation-reverse-engineering as a skill for dissecting and rewriting reference video frame by frame, separately from motion2code in the same list. Public repository search identified scriptscrypt/animation-reverse-engineering. The README read corresponds to latest commit 062cf5047b7c02c9c2e3c2cd7d85c70bdb410e49, dated July 31, 2026 at 15:26:21 UTC: earlier supplementary project documentation, not a release in this window.

The project has Claude Code investigate timing, order and easing from X videos, Dribbble work or screen recordings, then implement interactions. Documentation describes dissect.sh acquisition, probing, contact sheets and cropped frame stacks, with references covering acquisition, analysis, framer-motion porting and verification. Every timing/easing decision is meant to trace to measured frames, with screenshot verification against those frames rather than visual guesswork. The README lists two complete studies: a text-sweep timeline and a timelapse-scrubber interaction.

This is an AI reference-behavior reconstruction tool with a public workflow and examples, not a binary decompiler. Documentation still lists additional port targets, automatic difference measurement, pixel-fidelity scoring and spring/Bezier fitting as extension directions, not existing features. The author emphasizes studying motion technique rather than cloning branded identity; that is not a legal guarantee. REA is not mentioned. This collection did not install the skill, execute acquisition scripts, watch examples or measure reconstruction accuracy. Production wording is not treated as independent acceptance testing.

A separate project from motion2code; documentation includes two studies. Measurement and screenshot checks were not rerun by this collection.
Automatic difference measurement, pixel scoring and curve fitting remain extension directions; REA is unconfirmed.

## Sources

- [Previously deferred candidate: frame-level motion-reconstruction skill list, October 25, 2026 Beijing time](https://x.com/i/status/2114308490848338261)
- [Supplementary public README at fixed commit 062cf50, July 31, 2026 UTC](https://github.com/scriptscrypt/animation-reverse-engineering/blob/062cf5047b7c02c9c2e3c2cd7d85c70bdb410e49/README.md)

[中文](../scriptscrypt-animation-reference-frame-dissection-skill.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
