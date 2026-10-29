# 哈苏X2D系列：Codex辅助CIM研究、Doom与受限自动对焦扩展

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-29
阶段：进行中

2026年10月29日10:31:00（北京时间），极客开源（@hongseyanqiu）转述Radium Wang（@iamRadiumWang）以Codex分析哈苏CIM固件，在X2D系列探索功能扩展。文案称一代X2D 100C运行Doom，以ARM64引擎、C与Qt/QML连接画面、触屏、快门开火与音效；另称X2D II展示CarPlay与GPT控制对焦/快门，并研究一代原厂保留的连续对焦、人脸/人眼与三档速度路径。前述演示和AI工具归因属于转述，不是本合集实机观察。

补查公开仓库radium-wang/Hasselblad-X-System-CIM-Firmware-Research-Feature-Extensions的3dd59bbe1643397eede926b034c75df795f71006 README，提交于10月28日09:21:18北京时间，早于候选，只作补证。文档明确一代Doom引擎、快门、音效与滑动有受限设备反馈，但公开树无部署后端；一代进入原厂AF-C状态不等于对焦效果验收，AFT/眼部共存与三档选择器只有分开的受限反馈，速度倍率不等于端到端提速。曾把参数80改100的试验减少拉风箱却频繁虚焦，已淘汰。

同一README把二代LiDAR/AF路径与39个仍加密的模型标为离线分析，未做二代实机验收；未看到CarPlay/GPT的独立验证，不能拿一代证据认证二代演示。库还区分像素位移采集、离线处理和未量化光学收益，记录三轮界面响应试验未确认改善并恢复原厂。它说明公开源码、测试和脱敏结论不含厂商固件、模型、库或安装后端；实验性Mac/Windows一键工具另有仓库，首代固件4.2.0范围不应扩大。

项目注明前人x2d-cim-notes及derrickyau9提取研究的贡献。原始代码主体MIT，Doom模块GPL-2.0-or-later、Shimeji模块GPL-3.0-or-later；这些不授权厂商材料。本合集只静态读README，没有运行离线套件、安装工具、刷写相机或测光学效果。按进行中固件研究收录，REA未提及，不宣称所有隐藏功能已解锁或修改安全。

候选快照0赞、45浏览、0转发；补充仓库提交为10月28日，非本窗口新候选。
AI使用与二代CarPlay/GPT来自转述；固定README支持一代有限反馈，不是完整功能、全机型或安全验证。

## 来源

- [极客开源转述Radium Wang的Codex/哈苏研究，2026-10-29](https://x.com/i/status/2115632462437171618)
- [补充：10月28日固定README，实机/离线/未验证的逐项边界](https://github.com/radium-wang/Hasselblad-X-System-CIM-Firmware-Research-Feature-Extensions/blob/3dd59bbe1643397eede926b034c75df795f71006/README.md)

[English](en/radium-hasselblad-cim-codex-feature-research.md) | [返回目录](../README.zh-CN.md)
