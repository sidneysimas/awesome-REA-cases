# Codex 浏览器：找出网页唤起评论框的链路

分类：应用与客户端 · REA
记录日期：2026-10-12

宝玉想弄清 Codex / ChatGPT App 内置浏览器的网页标记如何进入对话输入框，以便自己的网页接入这一交互。他让 Codex + REA 查 Electron 代码，自己配合发送消息，再做测试网页。作者报告可通过 document.oai.annotation.request() 弹出评论框并填充内容，但不能直接把评论附加进输入框。案例结果是找到并部分验证一条交互接口，不是完整实现自动发消息。

发帖：2026-10-11（UTC）｜@dotey
热度快照（2026-10-12）：252 赞｜29,085 浏览｜32 转发

## 来源

- [作者原帖](https://x.com/dotey/status/2109417222724600172)

[English](en/codex-browser-annotations.md) | [返回目录](../README.md)
