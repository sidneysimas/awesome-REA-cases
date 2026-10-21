# Co-op Anything：给 Agent 的单机游戏联机改造与旧 Mod 修复流程

分类：游戏与游戏保存 · REA
记录日期：2026-10-21
阶段：相关项目

10月19日12:10（北京时间），@Bing_Bryan_BRN 介绍Co-op Anything：让Claude Code/Codex研究引擎、写同步、用Bot驱动游戏客户端测试，再打包Steam中继联机。补查cranebeaker/coop-anything公开README确认它是MCP服务器与工程playbook，MCP负责从安装目录识别引擎、查230多个联机Mod目录并读取流程；二进制分析可搭配REA。它不是本身就能完成所有逆向的单一模型。

两条路线分别是审计并修复已有停更Mod，或从零研究游戏状态、挂钩、玩家敌人与世界同步、切关和存档。README列Deus Ex的HX Mod修复包、Dungeon Keeper/KeeperFX、Fallout: New Vegas和Ocarina of Time等项目链接，并区分未测试、玩家报告、自动客户端测试与通关等级。这些是项目文档中的实例与质量标记，不在此分别新增未经审查的候选案例。

项目计划使用真实客户端Bot测试、Steam relay及免端口转发分发，要求参与者各自持有游戏，不触碰反作弊与他人在线服务。每个游戏的适配、稳定性与发布程度仍不同；README的‘任何游戏都可行’不视为已验证兼容保证。没有安装依赖、运行MCP、开游戏或核验双端同步，本条是公开工作流相关项目而非无人值守联机成功证明。仓库为本轮补充背景，不冒充候选帖子。

10月21日22:17（北京时间）候选转述：Deus Ex依赖Sebastian Kaufel（Hanfling）的HX 0.9.89.4（最后版本称为2019年6月），用独立HXFix包修切图崩溃、结局对话及门禁笔记丢失，不修改或重新分发HX；称有40余真实客户端测试，仍为Beta。10月22日补读公开README，确认独立包、Steam中继及真实客户端测试的项目说明，但未核对候选时点的测试数量或运行测试。文档仍列结尾字幕占位及对话警告，不把能合作玩战役等同于无已知缺陷。
同一候选将Dungeon Keeper归于KeeperFX、STALKER归于Shadow of COOP补丁、Ocarina of Time归于Ship of Harkinian及联机分支，并把Fallout New Vegas列为约35%的开发者预览；这些为10月21日转述口径，未逐项目验证或另建案例。需要自有合法游戏／ROM，Steam Spacewar AppID 480只是中继测试通路，不是商业发布认证。所称499星明确是10月19日上午旧快照，不充当当前热度；本候选1赞、125浏览、0转发。

## 来源

- [候选：Co-op Anything联机改造介绍](https://x.com/i/status/2112033640419045529)
- [公开项目：MCP、两条路线与质量等级](https://github.com/cranebeaker/coop-anything)
- [10月21日转述：HXFix、Beta与其他游戏阶段](https://x.com/i/status/2112911054606917774)
- [补充项目文档：Deus Ex HXFix与Steam中继](https://github.com/cranebeaker/deus-ex-coop)

[English](en/coop-anything-agent-multiplayer-workflow.md) | [返回目录](../README.zh-CN.md)
