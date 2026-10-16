# Claude Code：用 Muse + REA 阅读大型压缩代码

分类：应用与客户端 · REA
记录日期：2026-10-12

Claude Code 是终端中的 AI 编程工具。huangserva 让 Muse 自动安装 REA，分析 Claude Code 约47MB的压缩代码，并用视频展示过程。作者称得到分析结果，但没有公开恢复了哪些模块；这是 Agent 接入逆向工具阅读大型代码包的报告，不是已复刻 Claude Code。

另一帖自述用 REA 研究语言设置，发现 Claude 默认读取系统设置而非所设选项；没有过程或复测，不能外推至所有版本和配置。10月15日另一作者又提出先搜 GitHub issue，再逆向 CLI 与 Desktop，给开发提供反馈和实现参考；未指定功能或产物、未确认 REA，不混作 huangserva 已完成的工作。

10月16日17:03（北京时间），@botkooper 另称 Opus 没读文档，而选择反编译正在使用的 Claude Code 二进制。这是不同作者对工具选择的观察，未给版本、恢复模块、分析产物或 REA 使用证据，不能据此认定逆向已被解决，也不混同于此前的 Muse/REA 工作。

热度：576 赞｜11.4 万浏览｜56 转发
发帖：10 月 10 日｜REA
补充发帖：2026-10-13T23:18:00+08:00（原帖所示时间）
补充证据为发帖者自述，未独立复核。
2026-10-16 17:03（北京时间），@botkooper 另称 Opus 没读文档，而选择反编译正在使用的 Claude Code 二进制。该独立作者只报告工具选择，未给版本、分析产物、成功恢复的模块或 REA 使用证据；不与此前 Muse/REA 工作混同。

## 来源

- [看 X 热门帖](https://x.com/servasyy_ai/status/2108846931183378537)
- [本窗口：发帖者自述用 REA 检查 Claude Code 语言设置](https://x.com/i/status/2110027278570635457)
- [10 月 15 日另一作者的 CLI/Desktop 功能研究计划（未实现）](https://x.com/i/status/2110550597527339230)
- [10月16日 @botkooper：Opus 选择分析正在使用的 Claude Code 二进制](https://x.com/i/status/2111020085330481582)

[English](en/claude-code-analysis.md) | [返回目录](../README.zh-CN.md)
