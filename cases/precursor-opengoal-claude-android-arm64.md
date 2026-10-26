# Precursor：Claude辅助把OpenGOAL的Jak三部曲带到Android ARM64

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-24
阶段：进行中

候选是yibie在2026年10月24日15:30:21（北京时间）的项目合集。补读Precursor公开README后，目标比合集中的单作概述更明确：这是OpenGOAL的非官方、非营利fork，尝试让PS2的Jak 1、Jak 2、Jak 3在Android ARM64原生运行。OpenGOAL团队已有的反编译、GOAL编译器、运行时与素材工具是基础，不能归功于本次AI，也不代表该团队认可、制作或支持此fork。

作者thebardockgames负责方向、真机测试与发布；README称Claude通过Claude Code编写和审查相当部分端口代码、诊断与文档，提交使用AI-assisted和Co-Authored-By标记。具体工作包括GOAL编译器ARM64后端、C++与GOAL调用桥、OpenGL ES 3.2渲染器，以及SDL3、cubeb音频和手机端提取编译launcher。不能由AI参与推定整个OpenGOAL或原始反编译由AI完成。

项目报告Jak 1可到标题、intro、菜单、新游戏和初期游玩，约60FPS，支持触控与音频；Jak 2到intro、标题、城市与监狱，碰撞可用但仍有crash；Jak 3到菜单、新游戏和第一段完整过场，随后白屏。作者称设备端ARM64回归测试通过，却明确三作均未从头到尾验证；这些不是本合集真机测试或独立帧率测量。需要用户合法自备PS2游戏，仓库不附游戏资产。补充文档固定在04ee88b20636b0975e4f7d1552f2c828f25b2671，提交于10月23日（北京时间），只用于核实背景和状态，不冒充本窗口候选；未安装APK、编译或运行游戏。

约60FPS、三作启动与设备回归通过为项目报告；三作都未端到端验证，Jak 3白屏仍未解决。
AI贡献限该fork的端口、launcher与诊断等；OpenGOAL原始成果与团队独立归属。

## 来源

- [yibie介绍Precursor，2026-10-24](https://x.com/i/status/2113895858207105458)
- [补充一手：Precursor固定提交README，2026-10-23，北京时间](https://github.com/thebardockgames/Precursor/blob/04ee88b20636b0975e4f7d1552f2c828f25b2671/README.md)

[English](en/precursor-opengoal-claude-android-arm64.md) | [返回目录](../README.zh-CN.md)
