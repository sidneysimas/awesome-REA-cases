# Notion：追清复制文字和图片的内部链路

分类：应用与客户端 · REA
记录日期：2026-10-12

Notion 是文档与知识管理工具，桌面版使用 Electron，页面代码与系统功能之间需要跨进程通信。贡献者想弄清“点复制后，内容如何进入系统剪贴板”，从前端 API 追到 preload 包装层、IPC 消息和主进程接收端。后续真实客户端包分析整理出 copy、copyText、copyImage 三条静态候选路径，连接到 Electron 或浏览器剪贴板接口。成果是解释这一功能的实现链路，并非重建整个 Notion。

A later post further describes copying Notion blocks while preserving text, formatting and block structure, and reports that copied HTML carries a notionvc ID linking it to saved block data. This is a secondary post-level account; the underlying implementation details are not independently verified here.

Additional clipboard/block association details reported 2026-10-13; source is a post, not an independent implementation test.

## 来源

- [最初案例](https://github.com/morluto/rea/pull/961)
- [后续实测](https://github.com/morluto/rea/pull/1874)
- [REA Notion clipboard case details (X post)](https://x.com/i/status/2109842048023212348)

[返回目录](../README.md)
