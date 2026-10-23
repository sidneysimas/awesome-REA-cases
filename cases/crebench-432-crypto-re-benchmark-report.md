# CREBench：432个密码二进制任务，从算法识别到flag恢复

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-23
阶段：分析测试

2026年10月23日13:38:54（北京时间）的候选介绍CREBench密码逆向基准，称GPT-5.4得64.04、比人类专家低28分。本次通过公开仓库检索找到wangyu-ovo/CREBench并阅读README，确认其自称为COLM 2026论文《CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering》的官方代码仓库。作者列为Baicheng Chen、Yu Wang、Ziheng Zhou、Xiangru Liu、Juanru Li、Yilei Chen与Tianxing He。REA未提及。

目标不是破解现代密码原语，而是评测模型对含密码逻辑的已编译程序能恢复多少信息。四级任务分别是算法识别、密钥或IV提取、封装层代码重实现、flag恢复。README给出48种算法、hardcode_plain/fragmented_build/weak_prng_seeded三种密钥模式与O0/O3/constxor三种难度，共432题；提供单次与pass@k评测、并行与恢复运行、逐题分数、对话和指标产物的说明。文档提及Ghidra与Docker沙盒，以及Codex和多个模型的接入。

所读仓库最新提交为9fc4016538a0bab8c230732a9f788a61ed43addf，提交时间2026年8月20日13:01:15 UTC；这是旧公开材料的补充核对，不采纳候选的“5小时前发布”为仓库首发日期。64.04和28分差距只在候选中出现，未从论文表格或评测产物复核，因此仅保留为该帖转述，不作本合集基准测量。本次未下载题目二进制、安装依赖或运行评测；README列有评测流程不等于结果已独立复现。

候选2026-10-23 13:38:54，北京时间；补充仓库提交日期2026-08-20 13:01:15 UTC，不将检索日当首发日。
432题和四级定义由README确认；64.04及低28分仅为候选转述，未重跑。

## 来源

- [候选：CREBench规模、四级任务与模型成绩转述](https://x.com/i/status/2113505421021323523)
- [补充一手：CREBench官方仓库README，固定于2026-08-20提交](https://github.com/wangyu-ovo/CREBench/blob/9fc4016538a0bab8c230732a9f788a61ed43addf/README.md)

[English](en/crebench-432-crypto-re-benchmark-report.md) | [返回目录](../README.zh-CN.md)
