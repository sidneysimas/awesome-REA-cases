# wine-uwp：让 Shapr3D 等 Windows 商店应用在 Linux 运行

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-12
阶段：待验证

Wine 是在 Linux 运行 Windows 软件的兼容层，UWP/MSIX 商店应用还需要应用包模型、WinRT 和界面合成接口。DesignGears 报告 Claude 完成多数逆向和编码，自己负责指导与测试，做出 wine-uwp；原帖与 README 列出 Shapr3D、纸牌、媒体播放器和计算器。后续同周期帖介绍基于该运行时的 Shapr3D for Linux，称建模、登录、云同步及 STL/PDF 导出可用，仍为非官方 beta。项目运行微软原有界面框架，不是重写整个 Shapr3D 或 Windows；本合集只核对公开材料，未运行应用。

发帖：2026-10-12T14:24:27+08:00、14:30:30+08:00（北京时间）
运行时帖热度快照（2026-10-12）：2 赞｜70 浏览｜0 转发
Shapr3D 帖热度快照（2026-10-12）：1 赞｜23 浏览｜0 转发

## 来源

- [本周期运行时作者帖](https://x.com/DesignGears/status/2109530620321788301)
- [本周期 Shapr3D 作者帖](https://x.com/DesignGears/status/2109532140907921698)
- [兼容层实现与应用状态](https://github.com/designgears/wine-uwp)
- [Shapr3D 包装项目与 beta 说明](https://github.com/designgears/shapr3d-linux)

[返回目录](../README.md)
