# WoW WotLK 客户端：为 Azerothcore 与 LLM 玩家代理做 cleanroom 重实现

分类：游戏与游戏保存 · 未确认使用 REA
记录日期：2026-10-21
阶段：进行中

2026年10月21日08:45（北京时间），Shannon Sands（max_paperclips）称正在 cleanroom 逆向并重实现 WoW 的 WotLK（巫妖王之怒）客户端，报告可配合最新 Azerothcore 使用。背景是已有服务端与传统 playerbot 模组很好，但需要开放、易修改的客户端，让部分角色由完整LLM代理控制，和人类组队、组公会及参加战场。

作者设想加入轻量无头实例、机器人视角的WASM查看器、验证器与日志钩子，以及像人类一样控制一队playerbot的接口，用于评估和生成数据。现有模组能让LLM处理对话，不等于所设想的完整自主角色已经实现。原帖没有仓库、客户端版本或兼容测试，未说明AI是否参与客户端逆向，REA也未明示；AI在本条首先是客户端的目标用户。本合集未运行游戏或核验cleanroom隔离及资产来源，作者表示必要时愿重做资产不是已经完成。

## 来源

- [Shannon Sands：WotLK客户端与LLM代理环境计划](https://x.com/i/status/2112706696846143972)

[English](en/wotlk-cleanroom-client-llm-playerbots.md) | [返回目录](../README.zh-CN.md)
