# Windows 计算器：还原百分号在不同运算中的规则

分类：算法与功能重建 · REA
记录日期：2026-10-12

Windows 计算器的百分号会随当前运算改变含义。贡献者想解释这一行为，先发现 calc.exe 只是启动器，再用 REA 检查 CalcViewModel.dll 中的运算分支，并对照微软公开源码，恢复加减与乘除使用不同规则的逻辑，做成小型交互演示。函数定位由分析者辅助完成；公开源码和网页演示有交叉检查，但没有完成原 Windows GUI 输入验证。

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/1272)
- [分析证据](https://github.com/morluto/rea/blob/main/website/evidence/calculator-and-dino.md)

[English](en/windows-calculator-percent.md) | [返回目录](../README.zh-CN.md)
