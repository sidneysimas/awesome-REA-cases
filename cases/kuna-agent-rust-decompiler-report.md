# Kuna：Dopax介绍面向Agent的Rust反编译器与WASM入口

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-29
阶段：相关项目

2026年10月29日09:19:57（北京时间），Dopax（@tensorstaff）在开源盘点中介绍Kuna，称它是面向Agent的Rust反编译器，由Ghidra移植后继续独立演进。目标是让Agent通过CLI、浏览器WASM或Ghidra后端分析二进制，而不是报告某款软件已完整重建。

补读Noelo-Lab/kuna公开README，确认项目自称Agent自主改进反编译器的实验，要求阶段化设计、自然语言规格和可配置功能，并提供Claude Code/Codex/OpenCode skill。README称浏览器WASM本机处理，原二进制不需上传；Ghidra GUI插件尚不支持全部原生功能，headless不能直接靠GUI插件生效，另列Ghidra12.1.2/REA3.1.0的后端替换项目测试。只确认文档存在，不代表本合集验证隐私或兼容性。

帖子称19MB约三分钟、DecBench优化C榜居前与731星（截至10月29日）；README也有性能宣称，并列83文件675断言的回归语料与多类测试门禁。它们不等于本合集重跑结果，未检查基准配置、具体输入或运行日志，不能推导同条件速度、语义正确率或完整源码恢复。README于10月29日补查，只作候选项目核对；未执行工具，REA分类仍不以一段兼容文档推定本项目由REA构建。

候选快照0赞、23浏览、0转发；731星和性能均为盘点自述，非本合集重测。

## 来源

- [Dopax盘点Kuna与SuperGhidra等项目，2026-10-29](https://x.com/i/status/2115614583184638042)
- [补充项目README：Agent改进目标、接口与回归范围，10月29日静态读取](https://github.com/Noelo-Lab/kuna/blob/main/README.md)

[English](en/kuna-agent-rust-decompiler-report.md) | [返回目录](../README.zh-CN.md)
