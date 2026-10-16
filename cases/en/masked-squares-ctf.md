# DownUnderCTF: masked squares checker

Category: Algorithms and feature recovery · REA
Record date: 2026-10-12

DownUnderCTF is a cybersecurity puzzle competition. Its masked squares flag checker accepts an input string without revealing the correct answer. A contributor used REA and Ghidra to trace the input prompt to the validation function, recover masks, sum constants and equations, and solve them with Python/Z3. Project records show the original program accepted the recovered input and rejected it after one character was changed. Reverse engineering converted hidden validation rules into solvable constraints.

## Sources

- [Case PR](https://github.com/morluto/rea/pull/1077)
- [Evidence record](https://github.com/morluto/rea/blob/main/website/evidence/ctf-masked-squares.md)

[中文](../masked-squares-ctf.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
