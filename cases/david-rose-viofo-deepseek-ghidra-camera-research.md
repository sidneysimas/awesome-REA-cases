# Viofo行车记录仪：David Rose用DeepSeek/Ghidra排除USB实时视频方案

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-28
阶段：分析测试

2026年10月28日02:38:09（北京时间），David Rose（@drose101）回顾车载相机方案：单全局快门USB相机夜间模糊，170度鱼眼被挡且在comma世界模型里让预测更差，于是想用现有Viofo记录仪的优秀夜间画面，通过USB取实时视频。他说在DeepSeek帮助下用Ghidra反编译固件，发现USB webcam模式坏了，内部内存缓冲只每两秒更新一张快照，因此放弃。作者对Claude/Gemini的负面评价未给具体拒绝记录，不扩成模型能力排名。

最终采用向下长焦与向上倾的Sony STARVIS2低光相机，共用3D打印壳、固定到遮阳板钢支架。此为替代路线的背景，不是Viofo已修好或自动驾驶已安全。没有Viofo型号、固件、函数、USB捕获或原始计时，不泛化全部记录仪同样故障；两秒与预测变差是作者报告，REA未提及。本合集未运行固件、接相机或道路测试。

候选快照1赞、28浏览、0转发；两秒快照与方案失败均按作者归因。

## 来源

- [David Rose的相机迭代与DeepSeek/Ghidra调查，2026-10-28](https://x.com/i/status/2115151080577286246)

[English](en/david-rose-viofo-deepseek-ghidra-camera-research.md) | [返回目录](../README.zh-CN.md)
