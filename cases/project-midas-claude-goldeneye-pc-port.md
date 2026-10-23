# Project Midas：在GoldenEye既有N64反编译上使用Claude辅助制作PC移植

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-23
阶段：进行中

往期候选原发2026年10月18日09:04:22（北京时间）。Graslu00回复有关复古游戏反编译的讨论，称项目由两位程序员在AI辅助下开发，并有玩家和Mod作者密集测试；补查同串当日14:32:01回复，作者明确称为Project Midas。这些是社区解释，不等于本合集验证测试质量或人员投入。

随后找到murkantor/Project-Midas的公开README，将目标识别为GoldenEye（GE）的进行中PC移植：建立在既有N64反编译之上，面向Windows与Linux，从用户自己的美版卡带映像读取游戏数据。README明确承认Claude参与，致谢n64decomp/007等前人工作；不能将PC移植写成AI独自完成原始反编译、恢复原始源码或零人工成果。未说明Claude具体负责哪些函数、模型版本或使用REA。

窗口外补充材料固定于4b5ca71e93554d6a86b5d08a0ef1bea3fc0258a7，提交日期2026-10-22T20:15:25Z，晚于候选，不能倒推为10月18日已有全部功能。该版本仍将合作、联网和Mod加载列为进行中，普通构建仅载入原版卡带；也记录部分Linux系统关卡只显示大块空白三角形的问题。MIT仅适用于移植代码，不涵盖反编译游戏代码或游戏资产。

本合集只读取公开文档，没有获取卡带、构建、运行、播放验证或独立重测。社区关于认真测试的评价和README中的可运行说明分别保留归因；状态为in-progress，不保证兼容性或发行完成。

候选2026-10-18T09:04:22+08:00；识别项目的回复同日14:32:01。
补充README提交2026-10-22T20:15:25Z，晚于候选，不把后续功能倒填；未构建或运行。

## 来源

- [往期候选：Graslu00解释两人AI辅助及玩家测试](https://x.com/i/status/2111624394703560854)
- [同串回复：明确项目名Project Midas](https://x.com/i/status/2111706851121275300)
- [补充项目README：Claude声明、既有反编译及移植限制](https://github.com/murkantor/Project-Midas/blob/4b5ca71e93554d6a86b5d08a0ef1bea3fc0258a7/README.md)

[English](en/project-midas-claude-goldeneye-pc-port.md) | [返回目录](../README.zh-CN.md)
