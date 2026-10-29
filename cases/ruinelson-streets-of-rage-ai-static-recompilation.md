# 怒之铁拳：RuiNelson借LLM分析与RageDecompiler把68000逻辑重编译为C++

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-29
阶段：进行中

2026年10月29日17:24:26（北京时间），The Gaming Emporium（@McGroin83）介绍RuiNelson对SEGA1991年Mega Drive游戏Streets of Rage（怒之铁拳）的PC静态重编译。补读主仓库StreetsOfRageProject固定提交d56258e26cddaf385ade8a7d44bc03dd6a5e2e4d的README，并确认重编译子仓库指向主项目文档。主文档致谢Genesis Plus GX作为硬件参考、gsaurus反汇编及注释作为起点，以及Claude、ChatGPT、Grok4.5辅助；不能将前人成果归为AI从零恢复。

RageDecompiler将Motorola68000 ROM例程反汇编并转C++，从入口和中断向量追踪直接调用。间接调用不能仅靠静态遍历覆盖，运行时会报告尚无编译函数的地址，配合aux_addresses台账与推测发现模式反复游玩、记录和重编译。项目保存LLM分析稿、标签与人工重实现，包含压缩/解压和VBlank等待替代。这是逐步恢复目标逻辑，不是证明所有过程均已还原或字节级匹配。

SDL3的MegaDriveEnvironment仍提供VDP、音频、输入等硬件兼容层；消除硬件模拟依赖、可读化全部例程与增强渲染是路线图，不作为已完成成果。文档另给autoplay：从运行宿主读取原RAM布局、用反汇编得出的敌人状态机、时序与碰撞框决策，动作经虚拟手柄输入，不直接写RAM。它是符号规则AI，不是训练的神经网络，也不是LLM实时玩游戏。

报道列Windows/Linux/macOS构建方向，但本合集未编译、运行或验证跨平台与通关。项目要求读者自备有权使用的兼容ROM，不分发原游戏材料；可获得源码不等于获得游戏授权。按公开的进行中重编译研究收录，REA未提及。

候选快照12赞、432浏览、0转发；后续补查不覆盖原快照。
硬件兼容层与间接调用发现仍需保留；符号AI不等于LLM玩家。
只静态阅读公开文档，未构建、执行ROM或复测平台支持。

## 来源

- [The Gaming Emporium介绍RuiNelson的怒之铁拳项目，2026-10-29](https://x.com/i/status/2115736509437329888)
- [补充：StreetsOfRageProject固定README，发现循环、前人和LLM致谢、符号AI](https://github.com/RuiNelson/StreetsOfRageProject/blob/d56258e26cddaf385ade8a7d44bc03dd6a5e2e4d/README.md)
- [补充：重编译子仓库的固定README，10月28日23:32:39Z提交](https://github.com/RuiNelson/StreetsOfRageRecompilation/blob/cb14e06d7c7e8d9c0084bccbc8f54dbde617cbec/README.md)

[English](en/ruinelson-streets-of-rage-ai-static-recompilation.md) | [返回目录](../README.zh-CN.md)
