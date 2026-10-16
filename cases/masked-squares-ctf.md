# DownUnderCTF：从校验程序中找出正确输入

分类：算法与功能重建 · REA
记录日期：2026-10-12

DownUnderCTF 是网络安全解题比赛，masked squares flag checker 是其中一道校验题：程序接受一串输入，但不直接告诉你正确答案。贡献者用 REA + Ghidra 从输入提示追到校验函数，恢复掩码、求和常量和方程，再用 Python/Z3 求解。项目记录显示，求出的输入被原程序接受，改动一个字符后则被拒绝。逆向在这里用于把隐藏的校验规则还原成可求解的约束。

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/1077)
- [证据记录](https://github.com/morluto/rea/blob/main/website/evidence/ctf-masked-squares.md)

[English](en/masked-squares-ctf.md) | [返回目录](../README.zh-CN.md)
