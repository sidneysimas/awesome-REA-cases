# OpenAntiGrav：以Pulse为参照，用Rust重建WipEout多作共享引擎

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-23
阶段：进行中

2026年10月23日18:09:05（北京时间），Aman（@mdaman010）介绍WipEout Pulse的AI辅助重实现OpenAntiGrav。本次补读其原串，并通过公开仓库检索定位topaxi/OpenAntiGrav，读取README、开发文档及CLAUDE.md相关段落。Aman是推荐者，不冒充项目维护者；仓库为Claude Code提供研究与验证规则，未给AI贡献百分比或提及REA。

README将项目定义为Studio Liverpool反重力竞速引擎的Rust clean-room重实现，而不是反编译源码的逐行翻译。Pulse（PSP/PS2）是参考目标；Pure、HD/Fury、2048与Omega Collection共享架构。做法是观察原二进制行为，附证据与置信度后从头实现；开发文档列Ghidra/GhidraMCP、PSP Allegrex处理器模块以及PPSSPP、PCSX2、RPCS3和Vita3K等行为参照。CLAUDE.md说明依赖真实游戏数据的ground-truth测试不在CI自动运行，不能从普通CI推定原作一致性。

README内部状态表标注2026-10-14：Pulse已有菜单到比赛、各模式、带奖牌解锁的战役、记录与ghost，部分物理和武器与原作核对，但Zone仍部分完成，不宣称整场逐tick一致；其他作品的战役或比赛仍有部分与未完成项。文档列分屏等功能，但本次没有逐项核对所有模式，候选的LAN说法亦未复测。平台方面，README说仅Linux原生运行，Windows通过Wine；Mac与iOS未在真机运行，Android状态另有文档。因而不沿用候选对所有平台“运行良好”的概括。

补充README固定于2026-10-22 19:41:30 UTC的提交e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd；这是候选之前的公开项目材料，不是本窗口新发布。未下载游戏、安装依赖、构建或运行浏览器版，也未独立比较物理。项目要求自备合法游戏，不分发游戏内容；按进行中保存项目记录，不把公开文档或测试条目当独立复现。

候选2026-10-23 18:09:05，北京时间；补充提交2026-10-22 19:41:30 UTC。
状态与测试为项目自述；未运行游戏、测试或验证全部平台。

## 来源

- [候选：Aman介绍OpenAntiGrav、玩法与平台限制，2026-10-23](https://x.com/i/status/2113573415844241533)
- [补充一手：固定提交README，状态表日期2026-10-14](https://github.com/topaxi/OpenAntiGrav/blob/e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd/README.md)
- [补充项目开发文档：Ghidra、模拟器行为参照与Claude规则](https://github.com/topaxi/OpenAntiGrav/blob/e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd/docs/overview/developing.md)
- [补充项目Claude Code规则：ground-truth测试与CI的区别](https://github.com/topaxi/OpenAntiGrav/blob/e9c9f74c4ba0f1dbecbc3fe2f3f01e7da05c8fcd/CLAUDE.md)

[English](en/openantigrav-wipeout-rust-reimplementation.md) | [返回目录](../README.zh-CN.md)
