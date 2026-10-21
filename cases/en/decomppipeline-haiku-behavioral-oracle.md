# DecompPipeline: constrained Haiku and a behavioral oracle for Dreamcast functions

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-21
Stage: In progress

At 15:30 Beijing time on October 21, 2026, yibie's directory update introduces GeneralAtrox/DecompPipeline, asking whether a small model, Haiku, can decompile game functions under a rigid process. Supplementary inspection pins commit 70b248a5, dated October 19 at 09:20 Beijing time, before this window and used only for background and implementation checks. The current target is Dreamcast SH-4, with a separate workspace per game and no game data in the repository.

The README describes locked-down claude -p sessions reading assembly, Ghidra output and context before writing C. A machine supplies PASS/FAIL rather than accepting an agent's success claim. Ghidra p-code emulates the original function on 96 default inputs: 48 development and 48 hidden vectors. Checks cover return values, bytes at memory addresses the original writes, call targets/order/arguments and additional SH-4 register state; callees are mocked. Candidates compile with MSVC. Thus byte-exact refers to byte results of tested behavior, not original instructions reproduced with the original compiler. Documentation also provides coverage and mutation checks; passing finite inputs is not proof of complete semantic equivalence.

The pinned core/oracle_stamp.py confirms a harness stamp covering scripts, facts, function address, vector counts, hints, catalog and binary fingerprint among its inputs. current also checks callee records against the callees' own harness signatures. This addresses stale fixtures masquerading as current evidence, but a stamp proves neither judge correctness nor real-game compatibility. No end-to-end run record was obtained for this review, and no target was executed or dependencies installed. The directory post's 17 stars is its publication snapshot, not an independent count here. Use of the REA tool is not stated.

## Sources

- [yibie's DecompPipeline directory update and input-stamp note](https://x.com/i/status/2112808681918337410)
- [October 19 pinned README: Haiku workflow, 96 vectors and behavioral-verdict limits](https://github.com/GeneralAtrox/DecompPipeline/blob/70b248a5ade720b469716c39ec6da0db0953f5a4/README.md)
- [Same-commit core/oracle_stamp.py: inputs and callee-signature checks](https://github.com/GeneralAtrox/DecompPipeline/blob/70b248a5ade720b469716c39ec6da0db0953f5a4/core/oracle_stamp.py)

[中文](../decomppipeline-haiku-behavioral-oracle.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
