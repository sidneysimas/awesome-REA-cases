# chardet 7: a Claude-assisted encoding-detector rewrite, API compatibility and a separate licensing dispute

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-25
Stage: Analysis test

At 14:48:01 Beijing time on October 25, 2026, Srimugunthan Dhandapani (@Srimugunthan_D) uses Python encoding-detector library chardet to question whether a Claude Code rewrite is clean-room work, relaying a maintainer rewrite, the original creator's objection and a defense based on about 1% similarity. ArtCraft and REA are debate context, not additional experiments by this author. Original-post lookup confirms attribution and complete text.

Supplementary static reading uses chardet/chardet README at commit 865f09baa68378850af723db73707fb1bf3e084d, committed at 23:26:34 Beijing time on October 24, before the candidate. It explicitly says Dan Blanchard rewrote chardet 7 from scratch using Claude in 2026, retaining the package name and public API as a replacement for 5.x/6.x. The implementation is described as a 13-stage pipeline combining BOM detection, magic numbers, structural probing, byte-validity filtering and bigram statistical models. The goal is to reconstruct encoding detection and reduce switching costs, not recover original source.

The secondary licensing account needs correction: the candidate says LGPL to MIT, whereas the pinned README and license label say 0BSD. The README's claim that later code is not derivative is the project's position, not this collection's legal conclusion. The original creator's full objection, similarity tool and basis for about 1% were not obtained. Possible exposure to public source during training neither proves infringement in a particular output nor guarantees lawful clean-room status.

The README reports 99.7% accuracy on 3,138 files and a compiled version 359 times faster than 6.0.0. These are project-generated test claims. No corpus was downloaded, dependencies installed, target code executed or benchmarks rerun; they do not establish independent acceptance, equivalence on all inputs or court certification. Retained as analysis-test; REA is not mentioned.

Candidate snapshot: 1 like, 29 views, 0 reposts. Later engagement is not backfilled.
3,138 files, 99.7% and 359x are project test figures in the pinned README. About 1% similarity appears only in the candidate's retelling and was not rerun.
The candidate's MIT account conflicts with 0BSD in the pinned README. A license label does not adjudicate the rewrite's legal independence.

## Sources

- [Candidate and original lookup: Srimugunthan's chardet clean-room discussion, October 25, 2026](https://x.com/i/status/2114247590850261264)
- [Supplementary project README: Claude rewrite, API, 0BSD and tests at a pinned October 24 commit](https://github.com/chardet/chardet/blob/865f09baa68378850af723db73707fb1bf3e084d/README.md)

[中文](../chardet7-claude-encoding-detector-rewrite-license-dispute.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
