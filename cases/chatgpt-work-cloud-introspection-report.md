# ChatGPT Work Cloud：通过自省提示研究云端 Agent 的工具边界

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-16
阶段：待验证

10月16日的一篇中文帖转述 Simon Willison 对 ChatGPT Work Cloud 的研究：要求系统寻找伦敦带有 Pelican in her piety 象征的地点，整理 JSON 并建站，据称完成了检索、清洗和发布；再通过自省式提示探测可用能力，称发现 44 项 Skills、223 种微型 Tools，以及联网、执行程序、无头 Chrome、跨会话工作区和 Cloudflare Workers/D1/R2 部署能力。目标是理解云端 Agent 如何串联研究与交付，以及它能接触什么数据和网络，不是恢复整个服务的源码。这里记录的是该帖对 Willison 的转述，未取得其原始测试记录或复现上述数字；自省输出也不能自动证明后端的实际权限。帖子提到的私有数据、不可信内容和外发能力同时存在的提示注入风险是安全讨论，不能据此认定发生了泄露；类似 Codex 的审查与沙箱只是帖中猜测，未确认为 Work Cloud 已公开机制。未提及 REA。

来源发布：2026-10-16 16:22，北京时间；二手报告，工具清单与部署测试未独立核验。

## 来源

- [10月16日：转述 Willison 的 Work Cloud 研究](https://x.com/i/status/2111009945865097386)

[English](en/chatgpt-work-cloud-introspection-report.md) | [返回目录](../README.zh-CN.md)
