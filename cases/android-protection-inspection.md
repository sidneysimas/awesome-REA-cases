# Android App：用 Claude Code 识别根检测与证书固定

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-12
阶段：待验证

Ian Kerins 转述 Ibrahim 的近期研究：在网页数据访问困难时考虑移动 App 路线，用 JADX 阅读代码、Burp Suite MCP 与 Claude Code 查明某个 App 的 root 检测、Magisk 检测和 SSL pinning（证书固定）。具体 App 未具名，也未提供复现代码；目标是理解客户端保护与数据访问路径，不是已证明绕过保护或比浏览器方案更快。仅记录分析报告，不提供绕过步骤。

发帖：2026-10-12T16:19:17+08:00（北京时间）
热度快照（2026-10-12）：0 赞｜17 浏览｜0 转发

## 来源

- [本周期 AMA 转述](https://x.com/IanJKerins/status/2109559519584088093)

[English](en/android-protection-inspection.md) | [返回目录](../README.md)
