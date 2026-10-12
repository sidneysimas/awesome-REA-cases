# LG 电视：重做更快的 Plex 客户端

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-12

Plex 是用于浏览和播放个人影音库的软件。开发者觉得 LG 电视上的 Plex 客户端太慢，便用 Ghidra + Claude Code 研究电视原生媒体栈，做出 Rust/OpenGL 客户端 PlxNative。作者报告，同一台电视的用户选择界面从约 30 秒降到约 3 秒，并支持 4K、Dolby Vision 和 Atmos。逆向用于弄清如何调用电视自身的播放能力，而非只重画 Plex 界面。性能为作者报告；X 热度对应传播帖。

热度：7,268 赞｜26.4 万浏览｜483 转发
发帖：10 月 8 日｜非 REA

## 来源

- [看 X 热门帖](https://x.com/VaibhavSisinty/status/2108103450995417177)
- [开发者原始介绍](https://www.reddit.com/r/ClaudeCode/comments/1x043yp/i_used_claude_code_to_reverseengineer_an_lg_tv/)

[返回目录](../README.md)
