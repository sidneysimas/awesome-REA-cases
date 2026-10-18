# REA 核验引擎：用 CFG、符号路径与运行轨迹交叉检查结论

分类：算法与功能重建 · REA
记录日期：2026-10-18
阶段：待验证

10月18日22:31（北京时间），作者向morluto提出：Ghidra、Hopper、IDA给Agent看二进制的能力，但函数做什么仍需核验，应增加verification engine。在Agent写实现前，用CFG恢复、符号执行路径和运行轨迹确认发现，并设想与angr、radare2、Binary Ninja交叉检查。CFG是控制流图，用来描述基本块及分支关系。

这是针对AI分析可信度的具体工具集成idea，不是已实现的证明器或完整性保证。没有目标样本、跨工具结果、设计文档或实现；不同工具可能共享错误前提，符号路径与运行覆盖也不能保证所有输入正确。文中的质疑不等于已经证明REA没有任何核验能力。

10月18日候选快照1赞、44浏览；未提供实现或基准。

## 来源

- [REA结论与多工具交叉核验引擎的建议](https://x.com/i/status/2111827443979874751)

[English](en/rea-cross-tool-verification-engine-idea.md) | [返回目录](../README.zh-CN.md)
