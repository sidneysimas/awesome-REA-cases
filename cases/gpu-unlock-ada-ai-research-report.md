# GPU-Unlock-Ada：AI逆向报道与Ada张量吞吐解锁的公开研究

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-25
阶段：待验证

2026年10月25日12:20:50（北京时间），HKEPC报道JustAResearch借AI逆向研究GeForce RTX 40张量算力限制，称GPU-Unlock-Ada无须刷vBIOS或修改NVIDIA驱动，并列4090至4060 Ti的基准结果。本条的AI参与归因来自这篇报道；未找到可审的模型对话或明确REA使用证据，不能把记者归因升级为项目独立验证。

10月26日补读JustAResearcher/gpu-unlock-ada公开README，检索时HEAD为d28c485418c3d9d034cd4bac19200bc33dd3453b，提交时间为10月26日04:21 UTC；这是窗口外补充文档，不当作10月25日原帖已含的证据。README说Linux内核模块在原版驱动启动前执行SM speed-select覆盖，经过FLR再交接给驱动。AD102载荷和debug-booter分析来自TOTORONG/AD103_win_unlocker，Linux模块与封装来自Zagitta/gpu-unlock；不把上游成果全部归给JustAResearch或AI。

项目报告RTX4090的FP16→FP32累加吞吐由165.6至331.6 TF/s、BF16由165.5至330.6 TF/s。README另引一位机主的匹配测试：450W相同功耗上限下，FP16指令吞吐160.4至320.4 TF/s、BF16为159.7至320.2；真实cuBLAS GEMM的FP16中位提升12–34%，BF16两个形状提升16–20%，4096³基本不变。改装48GB 4090的量化MoE服务8K prefill为0.983倍，无收益。这些是项目和机主记录，本合集未重跑。

因此不照收媒体的全系列通用与矩阵运算普遍翻倍结论。公开文档要求许多Ada PCI ID逐卡实验opt-in，部分只测一张卡，笔记本结果也不一致；INT8、dp4a和标量FP32多项保持基线。FP8还需区分指令issue rate与应用GEMM、累加模式及功耗，不能由一个指标推定所有AI负载加速。硬件兼容、长时间稳定性与安全性未独立确认；没有下载固件/Windows工具、加载模块、执行目标代码或更改本机驱动。

AI研究归因为媒体报道，REA未确认；公开文档和机主基准不是本合集独立复现。
2×指令吞吐不等于2×推理；复用TOTORONG载荷与Zagitta模块，逐卡实验支持不代表全Ada覆盖。

## 来源

- [HKEPC的AI逆向GPU-Unlock-Ada报道，2026-10-25](https://x.com/i/status/2114210551413059771)
- [GPU-Unlock-Ada固定提交README，10月26日补查](https://github.com/JustAResearcher/gpu-unlock-ada/blob/d28c485418c3d9d034cd4bac19200bc33dd3453b/README.md)
- [GPU-Unlock-Ada项目入口与支持范围，10月26日补查](https://github.com/JustAResearcher/gpu-unlock-ada)

[English](en/gpu-unlock-ada-ai-research-report.md) | [返回目录](../README.zh-CN.md)
