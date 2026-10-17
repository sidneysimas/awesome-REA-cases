# Open Scrantic: rebuilding the Johnny Castaway screensaver engine with REA and Claude Code

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: In progress

At 22:45 Beijing time on October 17, 2026, Glauber Lima (@glauberlima) explains that REA handled reverse engineering, Claude Code the implementation, and he directed and reviewed the work. The target is Sierra/Dynamix's Windows 3.1 screensaver Screen Antics: Johnny Castaway, preserving its nostalgic island character and day-by-day story on modern Windows, macOS and Linux. The parent at 22:42 reports rebuilding it in Rust from disassembly; the 22:43 reply states MIT licensing and that original files are not distributed.

Reading the public glauberlima/open-scrantic README confirms the Open Scrantic project name and explicit AI disclosure: disassembling SCRANTIC.SCR, recovering resource formats and TTM/ADS script semantics, and implementing the Rust engine, tests and documentation, with developer comparisons against the original. The architecture separates resource decoding, story planning, script scheduling, frame rendering and sound. Users still need their own SCRANTIC.SCR, RESOURCE.MAP and RESOURCE.001. The loader accepts only a known original executable build, not arbitrary versions.

The project documents deliberate deviations, including full-frame redraw instead of dirty rectangles and using SCRANTIC.INI rather than recreating the original settings dialog. 'Same behavior' is not a claim of complete frame-by-frame or byte-for-byte identity. Supplementary reading checks commit 2bdbd87af4cd9641dd33739ba4681c0273f095aa from 22:14 on October 17 and a corresponding GitHub CI success. This is project build-check evidence, not this collection's hardware reproduction or acceptance of every story path. Public documentation and workflows were read; no assets were downloaded and no target was compiled or run.

Candidate and parent thread published October 17, 2026, 22:42–22:45 Beijing time; repository reading checks project identity and AI disclosure.
Commit 2bdbd87 is dated October 17, 2026, 22:14 Beijing time, with corresponding CI success; no independent build or execution.
Engine reimplementation only; original assets are required, with known-build restrictions and deliberate behavioral deviations.

## Sources

- [Candidate: author's REA, Claude Code and human-review disclosure](https://x.com/i/status/2111468525286002699)
- [Supplementary parent: three-platform Johnny Castaway Rust rebuild](https://x.com/i/status/2111467934082363521)
- [Same thread: MIT license and original files required](https://x.com/i/status/2111468253394485547)
- [Public repository: AI disclosure, implementation and compatibility boundaries](https://github.com/glauberlima/open-scrantic)
- [October 17, 2026 documentation commit](https://github.com/glauberlima/open-scrantic/commit/2bdbd87af4cd9641dd33739ba4681c0273f095aa)
- [Project CI records (mutable; matching commit successful when checked)](https://github.com/glauberlima/open-scrantic/actions/workflows/ci.yml)

[中文](../johnny-castaway-rust-rea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
