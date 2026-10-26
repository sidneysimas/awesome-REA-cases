# libfpv：Claude Code辅助把Betaflight仿真接到SM64与GTA IV，练习FPV飞行

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-24
阶段：相关项目

2026年10月24日13:00:51（北京时间）的候选介绍u/Hammerill的libfpv：借助Claude Code，把真实无人机遥控器接入PC，在Super Mario 64或GTA IV场景练习油门、转弯与穿越，避免损坏实体无人机。明确的AI归因来自候选介绍，而不是本合集对提交或生成代码比例的审计；REA未被提及。

补读hammerill/libfpv公开README，项目通过SimITL在独立1kHz仿真线程运行Betaflight 2025.12，接收遥控器或手柄输入，向游戏交付姿态、相机、OSD和电机声等。游戏提供碰撞几何并绘制结果，库本身没有渲染器，提供C接口；README链接sm64ex-fpv及gtaiv-fpv作为集成例子。每款游戏仍要单独接入，不能写成任意游戏自动安装，也不将SM64既有反编译、Betaflight或SimITL归功于AI。

这是与AI辅助游戏改造有关的公开项目，不是已证实的两款游戏AI反编译案例。README固定在9133485ba325ad10c8be767364e7aa599f36f93d，提交于10月24日06:29:59（北京时间），早于本窗口。1kHz是项目设计说明，不是本合集性能测量；未构建库、启动游戏或使用真实遥控器，物理真实性与训练迁移效果未独立验证。

Claude Code参与由候选归因；1kHz、固件版本与集成架构来自项目文档，未运行验证。
相关项目：不主张AI完成原游戏反编译，也不将仿真等同真实飞行训练效果。

## 来源

- [候选介绍Hammerill、Claude Code与FPV练习，2026-10-24](https://x.com/i/status/2113858235912630778)
- [补充一手：libfpv固定提交README，2026-10-24，窗口前](https://github.com/hammerill/libfpv/blob/9133485ba325ad10c8be767364e7aa599f36f93d/README.md)

[English](en/libfpv-claude-game-flight-training.md) | [返回目录](../README.zh-CN.md)
