# SuperGhidra：常驻Ghidra/MCP与可重编译C的项目转述

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-29
阶段：相关项目

2026年10月29日09:19:57（北京时间），Dopax（@tensorstaff）在盘点中将SuperGhidra列为10月新项目，介绍减少Agent重复启动Ghidra headless的常驻守护进程/MCP，以及可编译C改写、MSVC RTTI/MFC布局与Z3检查，列164星。它与Kuna是独立工具，不是一项目标重建成果。

补读yuatemycat/SuperGhidra公开README，文档分开只读Ghidra oracle、JSON写覆盖层、独立Python类恢复与另仓MCP桥。真实Ghidra反编译需Ghidra11/12、OpenJDK21及PyGhidra；不要把独立无JVM原型等同完整反编译。README明确原型在四个DLL的154导出中仅11能反编译、其中7能编译；复杂分支、浮点和未处理指令可能失败。C后处理报告1300函数22.62%通过、留出测试25.26%，不等于任意程序行为等价。

文档给Z3 P-code等价检查与布局义务门禁，但本合集未检查证明条件、运行回归或审计全部代码。README标AGPL-3.0-or-later；性能表和星数仍为项目/盘点主张，未重测。10月29日静态补读只核对功能与限制，不保证安全并发、语义保持或REA集成。

同帖快照0赞、23浏览、0转发；164星为作者标注的10月29日GitHub统计，未独立查询。

## 来源

- [Dopax的SuperGhidra功能介绍，2026-10-29](https://x.com/i/status/2115614583184638042)
- [补充项目README：运行模式与原型局限，10月29日静态读取](https://github.com/yuatemycat/SuperGhidra/blob/master/README.md)

[English](en/superghidra-daemon-mcp-recompilation-report.md) | [返回目录](../README.zh-CN.md)
