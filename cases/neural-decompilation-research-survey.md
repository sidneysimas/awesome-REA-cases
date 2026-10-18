# 神经反编译研究：从专用模型到变量与类型恢复

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-18
阶段：相关项目

10月18日12:40（北京时间），一篇日语综述用闭源软件保护为背景，介绍从机器指令恢复可读程序、推断丢失的名称与类型，以及从输入输出合成替代程序的研究。它列出2019年的 Towards Neural Decompilation 与 Coda、2024年的 LLM4Decompile、2022年的 DIRTY，以及2021年的 IReEn。具体研究用途分别是学习反编译、改善反编译结果的可读性、以及在黑盒观察下恢复功能，而非作者自己重建了一款商业应用。

补查 ACL Anthology 的 LLM4Decompile 原论文页面：论文发表于2024年11月，作者为 Hanzhuo Tan、Qi Luo、Jing Li 与 Yuqun Zhang，提供1.3B至33B模型；End路线直接反编译，Ref路线细化 Ghidra 输出。摘要报告在 HumanEval 和 ExeBench 上的可再执行率相对 GPT-4o 与 Ghidra 提升超过100%，Ref相对End再提升16.2%。这些是论文作者的基准主张，不是100%绝对成功率，更不代表整款闭源软件被恢复；未独立运行评测。原论文是窗口之外的历史补充材料，不能冒充本轮新成果。

综述另转述 DIRTY 的变量名66.4%、类型75.8%，及 IReEn 在 Karel 上约78%的结果；这里未逐篇核查这些数字。其关于编译近乎可逆、难读化防御消失、解析成本近零的泛化不由上述基准证明，不予采纳。没有确认 REA 参与，也没有证据说明当前通用模型能无损找回原始注释或设计意图。

2026-10-18综述候选快照7赞、746浏览；2024年论文为追溯补充，不是新窗口实验。
DIRTY和IReEn数值仅综述转述；LLM4Decompile只核对论文摘要，未重跑。

## 来源

- [10月18日神经反编译日语综述](https://x.com/i/status/2111678828599021657)
- [历史补充：LLM4Decompile，EMNLP 2024论文摘要与元数据](https://aclanthology.org/2024.emnlp-main.203/)

[English](en/neural-decompilation-research-survey.md) | [返回目录](../README.zh-CN.md)
