# Gears of War 3：AI 辅助静态重编译与图形后端研究

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-17
阶段：进行中

10月17日01:27（北京时间），GloriousEggroll 介绍自己持续数周乃至数月的 Gears of War 3 重编译，称以 SonicDE 的反编译 GPU 后端为基础，不直接依赖 Xenia 的 Xbox 360 图形翻译器，画面升至4K且未用 FSR，帧率改善但战斗仍有掉帧。其对其他移植是否算原生的评价不是本合集的技术判定。补读同作者本窗口02:40的澄清后，应把项目写成静态重编译而非完整反编译：作者称未用 UE3 源码，修改版 ReXGlue 从自备 ISO 中的 default.xex 将 PowerPC 指令机械翻译为可移植 C++，再编译成 x86-64 Linux 程序；并明确承认 Xenia 的内核/系统服务与 XenonRecomp 的分析翻译基础。着色器经 XenosRecomp 转 HLSL，再由 DXC 转 SPIR-V 供 Vulkan 使用，渲染库为 plume。作者03:18又说明自己不是模拟领域专家，没有 AI 可能不会尝试。以上具体工具和性能均为作者说明，未取得或运行源码、ISO、基准与完整兼容测试；不称其恢复了带原名和原结构的源码，也不把视频或4K当作全程稳定帧率。

候选快照（10月17日）：239赞、4,767浏览、21转发；非独立性能验证。
补充回复发布于同一严格窗口；无 UE3 源码、机械翻译与依赖归属均按作者原话保留。

## 来源

- [GloriousEggroll 的 WIP 原帖](https://x.com/i/status/2111146922522402943)
- [同作者澄清 ReXGlue、着色器和运行库路线](https://x.com/i/status/2111165298531270905)
- [同作者说明 AI 促成尝试及个人经验边界](https://x.com/i/status/2111175047033528355)

[English](en/gears3-ai-graphics-recompile.md) | [返回目录](../README.zh-CN.md)
