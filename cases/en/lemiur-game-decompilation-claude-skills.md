# Game Decompilation Skill for Claude: packaging byte matching, failure diagnosis and merge review as skills

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-27
Stage: Related project

At 15:30 Beijing time on October 27, 2026, yibie's list update recommends Game Decompilation Skill for Claude. Supplementary reading covers lemiur/Game-Decompilation-Skill-For-Claude's README at commit eedfe281d4fab7d8cdaf98b9f72f6a6ac4db04be, timestamped October 26 at 03:28:55 Beijing time, before the candidate window. It checks project purpose, not a release in this window.

The project supplies Claude Code with game matching-decompilation methodology: matcher reconstructs and matches functions; wall-identifier diagnoses stalled matches; helper-recovery restores inlined helpers; permute performs bounded permutation searches; decomp-code-rules checks readability and fake matches; orchestrator coordinates parallel worktree tasks and reviewed merges. Each game repository supplies commands and conventions through AGENTS.md, overriding skill defaults. The aim is readable source that produces matching bytes under the original compiler, not recovery of a unique original source.

The README explicitly supplies no toolchain. Users need the original compiler/linker or exact equivalents, a legally held retail binary, a unit-level build/comparison setup, and optionally disassembly, diff, permuter and objdiff tools. Native porting is a separate step after matching. Claims that PS1/PS2 projects are manageable while PS3/360 work may take months are author experience, not schedule guarantees. Named classic games illustrate the method, not games completed by this skill. This collection read documentation only, without installing skills, spawning agents or executing targets. Included as a related project; REA use is unconfirmed.

Candidate snapshot: 1 like, 65 views, 0 reposts. The post's 116-star project snapshot was not independently checked.
Skill methodology and gates do not establish success rates; no game's byte matching was run or verified here.

## Sources

- [Candidate: Claude game skills in yibie's list update, October 27, 2026](https://x.com/i/status/2114983062060904506)
- [Supplement: pinned October 26 README and toolchain requirements](https://github.com/lemiur/Game-Decompilation-Skill-For-Claude/blob/eedfe281d4fab7d8cdaf98b9f72f6a6ac4db04be/README.md)

[中文](../lemiur-game-decompilation-claude-skills.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
