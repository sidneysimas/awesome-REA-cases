# re3 / GTA III：用 Opus 给既有逆向游戏增加 NPC Agent 层

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

10月20日14:55（北京时间），@vladrezdev（Vlad Rez）称Claude Opus 5.5在既有GTA III逆向项目re3中加入System 1 / System 2式NPC层：输入激活作弊码后，附近角色成为Agent。TypeSafe Jev负责步行、跑、战斗、聊天与驾驶等决策，GPT-4.1-mini生成对话和想法，并在Jev不确定或无端攻击等重大动作时接管。

作者描述游戏每秒通过本地HTTP把街道快照发送给Python桥，桥返回动作、言语与思考；角色有姓名、性格、城市计划、事件与信任记忆。作者举例可请NPC开车送医院，见证攻击的角色可能还击或打公用电话报警。帖子带多个视频，但本合集未完整观看、运行或取得源码、延迟和多人稳定性测试；每秒一次是作者所述交换频率，不是实测性能。收录为AI扩展既有逆向代码的具体项目，不将re3原始反编译归功于Opus，不认定所有叙述行为均已验证；未确认使用REA。

## 来源

- [Vlad Rez：re3的Jev/GPT NPC层与本地桥说明](https://x.com/i/status/2112437552183701557)

[English](en/re3-gta3-jev-npc-agent-layer.md) | [返回目录](../README.zh-CN.md)
