# mugen-unleashed: reconstructing the 2013 M.U.G.E.N engine in C, with Claude credited in a commit

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-28
Stage: In progress

At 15:30:46 Beijing time on October 28, 2026, a list-update post recommends mugen-unleashed as a C recovery of M.U.G.E.N from its 2013 executable, noting that AI disclosure is in a commit trailer rather than the README. Supplementary inspection of zxmarcos/mugen-unleashed finds initial commit eea065966ab4c6557f811d707ec05221ba0f7ae9, dated October 23 at 12:01:46 Beijing time, authored by Marcos Medeiros and explicitly carrying 'Co-Authored-By: Claude Opus 5.5'. The earlier commit supplies method attribution, not a new current-window experiment.

M.U.G.E.N is a 2D fighting-game engine using character and stage data. The project targets Elecbyte's mugen.exe 1.1.0 Beta 1 P1 built on August 11, 2013, rebuilding a native Windows x86 program to keep using one's own game data. The README claims all game functions are reconstructed in C and differentially checked against the original binary. Debug and optimized builds reportedly produce identical mugen.log output for the title screen, quick VS, AI-vs-AI, character-select demo, options, storyboards, disabled sound/music and the missing-character error dialog, deliberately preserving quirks and bugs. These are project testing claims, not reproduction by this collection or proof of equivalence for every observable behavior, image, sound and timing.

Static dependencies Lua 5.1.4, libpng 1.2.38, GLEW 1.5.4 and minizip 0.15 reportedly use original source at the same versions. Running still requires legally obtained original data and Elecbyte.MUGEN.libs dynamic libraries. The README says GitHub Actions builds each push, but no successful run was verified and no artifact downloaded or executed. Public source/documentation is not Elecbyte permission: the README states original copyright, no official affiliation and no grant beyond applicable law. In-game AI in the README is not used as model evidence. Claude's contribution is not quantified and REA use is unconfirmed. Retained as in progress.

Candidate snapshot: 0 likes, 70 views, 0 reposts. Nine stars and 274 files are the candidate list's figures, not this collection's live statistics.
Static commit/README inspection only, without running targets or installing dependencies. Successful CI and per-function logs were not verified.

## Sources

- [Candidate list introduces mugen-unleashed and AI credit, October 28, 2026](https://x.com/i/status/2115345512325099569)
- [Public zxmarcos/mugen-unleashed repository](https://github.com/zxmarcos/mugen-unleashed)
- [Out-of-window supplement: October 23 initial commit and Claude co-author credit](https://github.com/zxmarcos/mugen-unleashed/commit/eea065966ab4c6557f811d707ec05221ba0f7ae9)
- [Pinned README: target, differential-test scope and rights boundary](https://github.com/zxmarcos/mugen-unleashed/blob/eea065966ab4c6557f811d707ec05221ba0f7ae9/README.md)

[中文](../zxmarcos-mugen-unleashed-claude-c-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
