# Codex cursor: recovering drawing geometry for a Windows pointer

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-17
Stage: Needs verification

At 01:10 Beijing time on October 17, Ananth (@Ananth7e) wanted the Codex computer-use pointer as their default Windows cursor and asked Opus 5.5 to inspect its compiled executable. The author says Ghidra crashed because the C drive was full, after which Claude switched to Python, pefile and Capstone, disassembled the drawing function, recovered geometry, curves and colors, rebuilt the cursor, installed it in Windows and backed up the old settings. The goal was one visual element, not rebuilding Codex. Reading the original conversation confirmed the author and a posted image, but this collection did not inspect its pixels or obtain extraction scripts, binaries, cursor files or tests. No author validation establishes animation, hotspots at different display scales or click accuracy; commenters' questions do not establish implemented features. Nothing was independently executed and REA use is unconfirmed.

October 17 candidate snapshot: 34 likes, 1,789 views, 1 repost; not functional validation.
Installation and settings backup are author reports; pixels, animation and hotspots were not independently checked.

## Sources

- [Ananth's original cursor-recovery post and conversation](https://x.com/i/status/2111142820207837308)

[中文](../codex-cursor-windows-opus.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
