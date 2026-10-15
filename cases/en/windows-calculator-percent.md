# Windows Calculator: recovering percentage rules

Category: Algorithms and feature recovery · REA
Record date: 2026-10-12

The percent key in Windows Calculator changes meaning depending on the current operation. A contributor sought to explain this behavior, first finding that calc.exe is only a launcher, then using REA to inspect operation branches in CalcViewModel.dll and compare them with Microsoft's public source. The recovered logic uses different rules for addition/subtraction and multiplication/division, illustrated in a small interactive demo. The analyst assisted function identification. Public source and the web demo were cross-checked, but input validation in the original Windows GUI was not completed.

## Sources

- [Case PR](https://github.com/morluto/rea/pull/1272)
- [Analysis evidence](https://github.com/morluto/rea/blob/main/website/evidence/calculator-and-dino.md)

[中文](../windows-calculator-percent.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
