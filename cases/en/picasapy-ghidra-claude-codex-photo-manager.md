# PicasaPy: Virág Attila rebuilds Picasa 3.9 with Ghidra, Claude and Codex

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-28
Stage: In progress

At 03:13:47 Beijing time on October 28, 2026, Virág Attila (@sanchomuzax) introduces PicasaPy as an open-source Python/Qt rewrite of Picasa 3.9, reverse-engineered with Ghidra and built with Claude and Codex, saying it already runs. The matching author's public repository confirms a Python, PySide6 and Qt Quick photo-management/editing project intended to continue a local Picasa-style workflow after Google's discontinued development. Its README says shared .picasa.ini files support reading and writing non-destructive edits, but later Picasa writes may overwrite external changes: not conflict-safe live synchronization. The feature list is project documentation, not individually tested functionality here.

Research documents were read at fixed commit cd9a25459d73abe244f24ed07ff61b60bca32ca7. The methodology targets Picasa 3.9.141.259 using strings, RTTI, resources and Ghidra leads. The parity document gives an initial October 13 inspection date with later revisions, separates statically reachable QML paths from real clicks and effect outputs, and retains missing/placeholding controls, platform differences and retired online services as non-goals. Its 108/138 menu-path figure is a particular static snapshot, not a complete functional click-pass rate. The initial document date is not the date of every revision.

Public CI run 40573684760 records success for that commit, created at 03:57:11 Beijing time on October 28, later than the candidate but inside this window. It is supplementary project validation, not another candidate or an independently rerun build. At lookup, latest commit 2a689c1204df7209d0eb286cba186a6dec395fb6 was dated 04:03:51, after the window, and is not presented as in-window progress; its queued CI is not passing evidence. Retained as an in-progress reconstruction, not original source recovery, complete Picasa effect equivalence, revived Google services or independent reproduction. No dependencies were installed or project code run.

Candidate snapshot: 0 likes, 13 views, 0 reposts. Selection is based on public research material and inspectable project records, not high engagement.
Documents and CI are project evidence, not independently executed here. Post-window latest changes and queued CI are not mixed into in-window results.

## Sources

- [Virág Attila's PicasaPy announcement, October 28, 2026](https://x.com/i/status/2115160045243814263)
- [Public repository and README: project scope and .picasa.ini limitations](https://github.com/sanchomuzax/PicasaPy)
- [Fixed-commit binary-research methodology, including pre-candidate background](https://github.com/sanchomuzax/PicasaPy/blob/cd9a25459d73abe244f24ed07ff61b60bca32ca7/docs/specs/binaris-regeszet-modszertan.md)
- [Fixed-commit layered parity checks and limits, initially dated October 13, 2026](https://github.com/sanchomuzax/PicasaPy/blob/cd9a25459d73abe244f24ed07ff61b60bca32ca7/docs/specs/paritas-ellenorzes.md)
- [Supplement: successful CI for cd9a254, created October 28 at 03:57 Beijing time](https://github.com/sanchomuzax/PicasaPy/actions/runs/40573684760)

[中文](../picasapy-ghidra-claude-codex-photo-manager.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
