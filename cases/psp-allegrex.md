# PSP：让 REA 支持掌机程序的静态分析

分类：硬件与设备互通 · REA
记录日期：2026-10-12

PSP 是索尼的 PlayStation Portable 掌机，使用名为 Allegrex 的处理器。用户希望 REA 能分析这一平台的程序，贡献者因此接入 Ghidra 的 Allegrex 扩展，使 Agent 可以获取函数、汇编和伪代码。验证使用自行编译的 PSP 测试程序，核查已知函数和调用关系。解决的是“通用逆向工作流不认识这个平台”的问题，不是已经复刻某款商业 PSP 游戏。

## 来源

- [应用需求](https://github.com/morluto/rea/issues/1330)
- [接入实现](https://github.com/morluto/rea/pull/1599)

[返回目录](../README.md)
