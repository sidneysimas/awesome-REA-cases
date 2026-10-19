# Co-op Anything：给 Agent 的单机游戏联机改造与旧 Mod 修复流程

分类：游戏与游戏保存 · REA
记录日期：2026-10-19
阶段：相关项目

10月19日12:10（北京时间），@Bing_Bryan_BRN 介绍Co-op Anything：让Claude Code/Codex研究引擎、写同步、用Bot驱动游戏客户端测试，再打包Steam中继联机。补查cranebeaker/coop-anything公开README确认它是MCP服务器与工程playbook，MCP负责从安装目录识别引擎、查230多个联机Mod目录并读取流程；二进制分析可搭配REA。它不是本身就能完成所有逆向的单一模型。

两条路线分别是审计并修复已有停更Mod，或从零研究游戏状态、挂钩、玩家敌人与世界同步、切关和存档。README列Deus Ex的HX Mod修复包、Dungeon Keeper/KeeperFX、Fallout: New Vegas和Ocarina of Time等项目链接，并区分未测试、玩家报告、自动客户端测试与通关等级。这些是项目文档中的实例与质量标记，不在此分别新增未经审查的候选案例。

项目计划使用真实客户端Bot测试、Steam relay及免端口转发分发，要求参与者各自持有游戏，不触碰反作弊与他人在线服务。每个游戏的适配、稳定性与发布程度仍不同；README的‘任何游戏都可行’不视为已验证兼容保证。没有安装依赖、运行MCP、开游戏或核验双端同步，本条是公开工作流相关项目而非无人值守联机成功证明。仓库为本轮补充背景，不冒充候选帖子。

## 来源

- [候选：Co-op Anything联机改造介绍](https://x.com/i/status/2112033640419045529)
- [公开项目：MCP、两条路线与质量等级](https://github.com/cranebeaker/coop-anything)

[English](en/coop-anything-agent-multiplayer-workflow.md) | [返回目录](../README.zh-CN.md)
