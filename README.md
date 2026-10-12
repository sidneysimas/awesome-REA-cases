# Awesome REA Cases

**中文（默认）** | [English](README.en.md)

**软件不支持、设备不兼容、源码丢失——有人开始用 AI 把它们改成自己想要的样子。**

这里收集 REA 与其他 AI 辅助逆向的真实用途：让旧游戏重新可维护，让买来的硬件跨平台工作，把现有软件的能力接进自己的产品。

**每天 6 次追踪公开案例，持续更新。首页由维护者逐条阅读、亲自挑选与编辑，不是自动排名，也不展示全部收录。**

[浏览全部案例](INDEX.md) · [游戏](categories/games.md) · [硬件](categories/hardware.md) · [应用](categories/apps.md) · [算法](categories/algorithms.md)

## 新近值得看

### [不重做 Shapr3D，让它在 Linux 上运行](cases/wine-uwp-shapr3d.md)

作者报告用 Claude 辅助研究 Windows 商店应用所需接口，扩展 Wine 兼容层，并公开实现。值得看的是补上原应用的运行条件，而不是做一个外观相似的替代品。**其他 AI 逆向；非官方 beta，未由本合集实测。**

### [不复刻 Preview，直接给现有应用加 AI 侧栏](cases/preview-ai-sidebar.md)

研究团队展示在 macOS 预览应用的副本上增加 AI 功能，并公开概念验证项目。这个方向把问题从“重新开发整款软件”变成“改造已经在用的软件”。**待验证；未确认使用 REA，生成应用仅供个人实验。**

### [戴上 AR 眼镜，用手势调空调](cases/ar-air-conditioner-control.md)

演示转述称，先研究官方 App 的控制请求，再把开关、调温接到 AR 眼镜。新意在于换一种使用入口，而非重做家电 App。**REA · 待验证：设备型号、协议和代码未公开，不代表兼容任意家电。**

## 这些案例值得先点开

### [Universal Modder：把 Minecraft 的内容放进 GTA V](cases/universal-modder.md)

让 Claude 分析引擎和素材格式，再修改内容、进入游戏测试。创意很直观，原帖热度快照超过 1.4 万赞；它展示的是跨游戏 Mod，不是完整反编译游戏。**其他 AI 逆向。**

### [LG 电视上的 Plex 太慢，于是重做客户端](cases/lg-plxnative.md)

开发者用 Ghidra + Claude Code 研究电视原生媒体栈，做出 Rust/OpenGL 客户端。作者报告用户选择界面从约 30 秒缩到约 3 秒——逆向服务于一个明确的体验问题。**其他 AI 逆向；性能为作者报告。**

### [只有 DOS 二进制，能找回可维护的代码吗？](cases/firefighter-rust.md)

Firefighter 的作者报告从旧程序恢复 Pascal 逻辑，再转写成 Rust。比起重新画一个相似界面，这个目标更接近软件保存：把还能运行的旧程序变成还能继续维护的代码。**其他 AI 逆向。**

### [Apple TV 的遥控器，也可以接到 Linux](cases/siri-remote-linux.md)

研究蓝牙协议，让 Linux 理解遥控器的触控、按键和麦克风数据，并提供开源实现。封闭生态里的配件，变成自己电脑能使用的输入设备。**未确认使用 REA。**

### [从混淆前端重建 Claude Slides 编辑器](cases/claude-slides.md)

Codex + REA 分析前端脚本，Claude Code 整理工程，公开截图和代码提交。适合想看“读代码之后具体做出了什么”的读者。**REA；功能完整度为作者报告。**

### [17 个 Agent，三个月重建《现代战争 2》代码](cases/mw2-decompilation.md)

作者报告游戏可以运行，83% 的函数达到字节级匹配。值得看的是并行协作和原二进制对照，不是“一晚重做大作”的故事。**其他 AI 逆向；代码未公开，未由本合集独立复现。**

## 想继续找？

首页只是精选。所有通过收录筛选的案例、进行中的项目和具体 idea 都保留在[完整目录](INDEX.md)，按用途分类；没上首页不等于没价值。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向工具。本合集也收录其他 AI 辅助逆向，以及为 AI 工具实现互通的项目。

## 贡献与边界

欢迎[提交案例、补充验证或纠错](CONTRIBUTING.md)。首页优先选择具体、鲜明、值得读的项目；热度只是推荐线索，不是成果证明。选编规则见[维护方法](MAINTENANCE.md)。

非 REA 官方项目。内容据作者与项目记录整理，未由本合集独立复现。仅提供原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利，研究或复现前请确认相应授权。
