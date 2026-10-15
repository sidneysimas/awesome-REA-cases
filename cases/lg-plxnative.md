# LG 电视：重做更快的 Plex 客户端

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-13

Plex 是用于浏览和播放个人影音库的软件。开发者觉得 LG 电视上的 Plex 客户端太慢，便用 Ghidra + Claude Code 研究电视原生媒体栈，做出 Rust/OpenGL 客户端 PlxNative。作者报告，同一台电视的用户选择界面从约 30 秒降到约 3 秒，并支持 4K、Dolby Vision 和 Atmos。逆向用于弄清如何调用电视自身的播放能力，而非只重画 Plex 界面。性能为作者报告；X 热度对应传播帖。 10 月 12 日一条转述微信公众号的长帖新增开发细节：称 LG 修改版 SDL 的结构体尺寸导致重构后崩溃，随后改用 Rust 中间层；又称通过削减着色器动态分支、缩小阴影画布与脏矩形重绘恢复帧率。这些为二手开发过程转述，未从原作者代码或测试记录复核，不把文中性能计数及“无需 Root”扩大为所有电视的结论。

热度：7,268 赞｜26.4 万浏览｜483 转发
发帖：10 月 8 日｜非 REA
开发细节补充帖热度快照（2026-10-13）：1 赞｜345 浏览｜0 转发；原热门帖热度保留 2026-10-12 快照

## 来源

- [看 X 热门帖](https://x.com/VaibhavSisinty/status/2108103450995417177)
- [开发者原始介绍](https://www.reddit.com/r/ClaudeCode/comments/1x043yp/i_used_claude_code_to_reverseengineer_an_lg_tv/)
- [本周期开发细节二手转述](https://x.com/i/status/2109658600394367126)

[English](en/lg-plxnative.md) | [返回目录](../README.md)
