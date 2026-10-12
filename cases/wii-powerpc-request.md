# GameCube / Wii：从实际 Wii 分析提出 PowerPC 支持

分类：游戏与游戏保存 · 未确认使用 REA
记录日期：2026-10-12

GameCube 和 Wii 是任天堂主机，游戏程序使用 PowerPC 处理器与 DOL 格式。Issue 作者称已在 REA 之外用 Ghidra headless 分析一款未具名 Wii 游戏，希望把函数、调用者和数据检查接入 REA。讨论提出先支持通用 PowerPC ELF，再处理 DOL。现有证据是实际外部研究与明确接入需求，不是 REA 已完成某款 Wii 游戏重建。

## 来源

- [原始 Issue](https://github.com/morluto/rea/issues/1741)

[返回目录](../README.md)
