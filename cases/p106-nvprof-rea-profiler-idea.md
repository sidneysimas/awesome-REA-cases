# P106矿卡：nvprof拒绝支持后，作者提出REA与自制profiler方向

分类：硬件与设备互通 · REA
记录日期：2026-10-23
阶段：待验证

2026年10月23日18:05:05（北京时间），发帖者说自己在P106矿卡机器上调用NVIDIA nvprof，遇到“nvprof does not support NVIDIA Crypto Mining Processors”的提示。背景是希望分析这台机器上的GPU工作，而官方分析工具拒绝该设备类别。

作者表示准备使用CUDA events做自己的profiler，并以“Time to REA: Reverse Engineer Anything?”提出逆向方向。它是一个具名设备与具名工具的兼容性idea，而非已完成的nvprof补丁；原文没有明确说明REA将分析哪份文件，也没有模型、代码、计时输出或性能对照。

按unverified记录初步计划。不推断已解除设备检测、恢复官方profiler、取得硬件计数器或证明CUDA events与nvprof等价；本次只阅读候选，没有访问矿机、下载驱动或运行设备测试。

来源2026-10-23 18:05:05，北京时间；仅idea，无完成或计时验证。

## 来源

- [候选原帖：P106上的nvprof提示、CUDA events与REA设想](https://x.com/i/status/2113572410175688822)

[English](en/p106-nvprof-rea-profiler-idea.md) | [返回目录](../README.zh-CN.md)
