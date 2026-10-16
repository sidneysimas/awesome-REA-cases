# Claude Chrome：把本地浏览器协议桥接到云浏览器

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-12

Paul Klein IV 希望 Claude Code 不只操控同机 Chrome，也能使用远端浏览器。他研究 Claude Chrome 的 native messaging：消息使用四字节长度前缀和 JSON，承载导航、截图和点击等工具调用。随后做服务拦截浏览器连接，把命令转成 CDP，送往 Browserbase 云浏览器。线程提供演示与插件入口；它展示的是为 AI 工具做浏览器互通，不证明 AI 本身完成了全部逆向。

发帖：2025-12-29（UTC）｜@pk_iv
热度快照（2026-10-12）：2,263 赞｜395,773 浏览｜181 转发

## 来源

- [作者原帖](https://x.com/pk_iv/status/2005694082627297735)
- [公开实现](https://github.com/browserbase/claude-code-plugin)

[English](en/claude-chrome-remote.md) | [返回目录](../README.zh-CN.md)
