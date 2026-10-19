# UFOX：把本地 APK 反编译与脚本分析接给 AI Agent 的 MCP 项目

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-19
阶段：相关项目

10月19日17:01与17:04（北京时间），@ksr03y（orvian）介绍给AI编码Agent使用的MCP接口。补读16:57的父帖确认项目叫UFOX APK Decompiler，宣称快速、本地处理且无需上传服务器；用途是让Agent以程序方式调用Android反编译器，而不是人工来回搬运分析内容。

17:04的同作者回复还说AI可以编写并运行自己的JavaScript分析脚本，组合ELF、Capstone与Unicorn建立工作流。ELF是二进制文件格式，Capstone用于反汇编，Unicorn用于CPU仿真；这里记录的是作者宣传的工具组合，不据此断定所有能力都在APK路径实现，也不把脚本运行当本合集已做的操作。

本轮只读到作者串，未取得展开后的MCP文档、源码、样本输出、安装或验证记录，没有测试本地性、无上传承诺与分析正确性。不声称该工具已恢复某个App的功能，未确认REA。父帖是补充项目身份的较早材料，两条候选各保留判断。

## 来源

- [候选：UFOX给AI Agent的APK反编译MCP](https://x.com/i/status/2112106736844976401)
- [候选：JavaScript与ELF／Capstone／Unicorn组合](https://x.com/i/status/2112107730874114322)
- [补充父帖：UFOX名称与本地无上传宣传](https://x.com/i/status/2112105862244524310)

[English](en/ufox-mcp-apk-analysis.md) | [返回目录](../README.zh-CN.md)
