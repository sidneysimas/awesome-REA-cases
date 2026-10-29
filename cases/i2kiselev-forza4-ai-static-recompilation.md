# Forza Motorsport 4：AI辅助静态重编译，公开限定硬件的帧率对照

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-29
阶段：进行中

2026年10月29日19:44:22（北京时间），The Gaming Emporium报道i2kiselev的Forza Motorsport4静态重编译。补读仓库固定提交0be771c68af81af5d74ca2e2c6284ec6b6642207的README及guide/performance.md，提交时间为同日09:13:11Z，即本候选窗口内17:13:11。文档明确代码、脚本、文档与游戏二进制逆向使用AI辅助，但没有给具体模型或REA使用证据。

项目通过ShiftGlue把原PowerPC代码预先转成C++再编译到x86-64，以Vulkan处理图形，基于arcanite24的Pinyon Shift与ShiftGlue分支，并致谢ReXGlue、Xenia及较早fm4-recomp。新增FM4专用深度、相机与物体运动信息供DLSS/FSR2/FSR3，另有键盘、游戏内图形菜单、Disc2与DLC。不能把继承的运行时和渲染器写成作者或AI从零完成。

README允许最高5120×2880与240fps上限，但它们不是同一实测结果。项目0.3.0以Ryzen7 5700X3D、32GB DDR4-3600、RTX4070Ti SUPER16GB、Windows10 Pro22H2测Bernese Alps与11台AI车，每项约12秒，三次中位数，关闭升采样、采用Console预设。1x为233fps、2x232、3x156、4x即5K为102；相同机器Xenia Canary固定提交分别为102、88、68、45。项目称快2.3至2.6倍，不能外推到所有赛道、GPU或配置，也不能将显示器170Hz与渲染帧率混为一谈。

项目报告World Tour至Expert、约30场Event List、Free Play、车库、回放和保存测试，未测分屏、方向盘及大多数AMD/Intel GPU。Windows10 2004+ x64为当前入口，Linux和方向盘仍在路线图；Xbox LIVE与Kinect不支持。仅指定PAL/USA1.0 Disc1，Rev1/1.1不支持，自备合法游戏文件并在本机生成，不分发原始资产或预编译游戏。

上述为开发者文档及二手报道，不是本合集性能测量或全面兼容验证。本合集未下载游戏、执行安装器、运行目标测试或重新编译。

候选快照1赞、81浏览、0转发；不使用补查时的传播值。
项目单机短赛道三次中位数：5K102fps，不是5K240fps；未独立复跑。
实验版，自备受支持Disc1；当前Windows，分屏与多数GPU未测试。

## 来源

- [The Gaming Emporium报道FM4重编译与AI辅助，2026-10-29](https://x.com/i/status/2115771724390178926)
- [补充：FM4固定README，2026-10-29 09:13:11Z提交](https://github.com/i2kiselev/fm4-static-recomp/blob/0be771c68af81af5d74ca2e2c6284ec6b6642207/README.md)
- [补充：同提交的测试范围、环境和Xenia对照表](https://github.com/i2kiselev/fm4-static-recomp/blob/0be771c68af81af5d74ca2e2c6284ec6b6642207/guide/performance.md)

[English](en/i2kiselev-forza4-ai-static-recompilation.md) | [返回目录](../README.zh-CN.md)
