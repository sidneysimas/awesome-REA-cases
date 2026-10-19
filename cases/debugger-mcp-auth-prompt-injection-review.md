# 调试器 MCP 风险调查：x64dbg、GhidraMCP 与 IDA Pro MCP

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-20
阶段：相关项目

10月20日03:21（北京时间），帖子以调试器可读内存、修改状态、控制执行为背景，介绍对x64dbg、GhidraMCP与IDA Pro MCP的源码级调查，目标是检查将调试权限暴露给AI Agent后的认证缺陷、工具权限和prompt-injection风险。

正文只给文章短链，没有具体缺陷、版本、CVE、复现或修复提交，也没有说明研究过程是否由AI辅助。按与AI逆向工具安全直接相关的项目收录，不宣称三工具均可被攻破、存在同一漏洞或作者用REA做了审计。未运行调试器或攻击目标。

## 来源

- [调试器MCP源码级安全调查介绍](https://x.com/i/status/2112262924676804726)

[English](en/debugger-mcp-auth-prompt-injection-review.md) | [返回目录](../README.zh-CN.md)
