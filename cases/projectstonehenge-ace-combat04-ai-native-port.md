# ProjectStonehenge：AI协作将Ace Combat 04逐函数转为PC原生C++

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-26
阶段：进行中

2026年10月26日06:18（北京时间）的候选介绍Onaga00的ProjectStonehenge，把PS2飞行战斗游戏Ace Combat 04: Shattered Skies移植到Windows。补查公开仓库固定4412348ed9d3532627a8d3f3b16951f308cf33e9的README；提交日期为10月25日14:50:32 UTC，早于窗口，仅用于确认目标与方法。项目基于北美版SLUS-20152，说明将原PS2 ELF逐函数翻译为C++，不是模拟器封装，也不是自动静态重编译。

AI Disclosure明确研究笔记、大部分代码与研究工具由Anthropic模型在人类监督下编写；没有量化审计其代码比例，也没有指明模型版本或REA。项目致谢以Ghidra为研究数据库、bethington/ghidra-mcp驱动分析、Emotion Engine插件，参考PCSX2调试行为与存档布局及ps2sdk符号资料；不能把这些前人工作归为AI原创。

项目列可选60/120/144/240/360FPS渲染上限，靠渲染与逻辑解耦、插值实现，物理和AI仍以原59.94Hz推进。故“最高360FPS”不是本合集测出的持续性能，也不意味着逻辑加速。README还描述最高4096×3584内部渲染、4K输出、FXAA/SMAA、SDL3键盘手柄输入，以及PCSX2文件夹记忆卡双向交换，但后者明确为beta。272个原版不可达函数及未用场景的保留是项目声明；默认仍不可达，探索界面待做。

当前要求Windows10/11、Vulkan1.2与用户自有北美版光盘数据，Linux、VS模式、Mod和更多优化仍在路线图。本合集仅静态阅读公开文档，未下载游戏、构建代码、跑测试或验证所谓与原版完全相同的行为；按进行中收录，不把公开代码、功能表或支持高帧率当独立复现。

原生C++逐函数移植，非自动静态重编译；AI分工为项目披露，REA未确认。
360FPS为可选渲染上限，逻辑59.94Hz；存档互通beta、Linux计划中，未独立运行。

## 来源

- [窗口候选：ProjectStonehenge的PC移植介绍，2026-10-26北京时间](https://x.com/i/status/2114481803796861088)
- [补充项目README及AI Disclosure，固定4412348，2026-10-25 UTC](https://github.com/Onaga00/ProjectStonehenge/blob/4412348ed9d3532627a8d3f3b16951f308cf33e9/README.md)

[English](en/projectstonehenge-ace-combat04-ai-native-port.md) | [返回目录](../README.zh-CN.md)
