# ArkWeb：让蜘蛛侠在 Gotham 摆荡的双游戏实验

分类：游戏与游戏保存 · 未确认使用 REA
记录日期：2026-10-17
阶段：进行中

10月17日04:04（北京时间），@tezzarc 用 REA + Opus 5.5 话题介绍 ArkWeb。补查确认 luki-1/ArkWeb 公开仓库：它同时运行 Marvel's Spider-Man Remastered 与 Batman: Arkham Knight，把 Gotham 的碰撞分块传入蜘蛛侠的物理世界，再把蜘蛛侠画面叠入 Arkham；战斗时由隐藏的 Batman 执行动作，蜘蛛侠逐帧匹配姿态。README 解释了距纽约约2公里的客体场景、50米瓦片、通过录制运动研究骨架，以及让 Agent 帮助安装和排障的流程。这不是把两款游戏完整反编译成新引擎，也不是只换模型。

仓库的10月1日 PHASE2 笔记记录 PhysX 布局与几何导出，并明确其中 Spider-Man 运行时碰撞实现当时仅构建、尚未运行；较新的 README 自称端到端可工作，但仍标 experimental，列出穿过细建筑、加载区碰撞空洞、照明和战斗手部姿态缺陷。要求 Windows、两款自有 Steam 游戏及特定 Spider-Man 4.0630 版本。10月3日文档提交署有 Claude Opus 5.5 协作标记，支持 AI 参与文档与安装流程，不能证明整个逆向由模型完成；项目材料未确认使用 REA。10月1日至3日材料是窗口外背景补证，10月17日帖子才是候选。这里只阅读文档、目录与提交，未运行 Mod 或独立复现。

项目称实验性端到端运行；本合集只读材料，未运行游戏或验证性能。
AI 安装引导与文档协作可见；REA 与完整 AI 逆向归因未确认。

## 来源

- [10月17日 ArkWeb 技术介绍与 REA 传播帖](https://x.com/i/status/2111186571252687192)
- [ArkWeb 公开仓库与实验性状态说明](https://github.com/luki-1/ArkWeb)
- [10月1日阶段笔记：几何导出与尚未运行的实现](https://github.com/luki-1/ArkWeb/blob/main/PHASE2.md)
- [10月3日 Claude 协作署名的安装引导提交](https://github.com/luki-1/ArkWeb/commit/a936b62f8ba66864aaae24fd2829303197664e1d)

[English](en/arkweb-spiderman-arkham-report.md) | [返回目录](../README.zh-CN.md)
