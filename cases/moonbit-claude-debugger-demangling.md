# MoonBit：Claude 研究符号改名，让 VSCode 调试更易读

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-16
阶段：待验证

@jonathoda 为语言研究项目寻找代数数据类型、模式匹配、可变性、引用相等、JavaScript 编译与调试等能力，按 Claude 建议尝试 MoonBit 后发现调试输出全是改名符号。10月16日作者称 Claude 逆向 name mangling 算法，写了 VSCode 调试器 customDescriptionGenerator，改善可读性。目标是理解编译器名称编码并改善显示，不是重建 MoonBit 编译器。前面的需求帖仅作窗口外背景；候选未提供生成器代码、符号样例、覆盖率或测试，显示效果与正确性仍是作者报告，本合集未运行。

10月16日候选快照：0赞、27浏览；未公开代码或测试结果。

## 来源

- [作者的符号解码与调试器报告](https://x.com/i/status/2110938121080631767)
- [往期语言研究需求背景](https://x.com/i/status/2110458286290133115)

[English](en/moonbit-claude-debugger-demangling.md) | [返回目录](../README.zh-CN.md)
