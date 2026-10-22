# LLM4Decompile：从汇编或 Ghidra 伪代码恢复 C 函数的专用模型

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-22
阶段：分析测试

2026年10月22日00:26（北京时间），@isofunds 介绍 LLM4Decompile，提出先恢复旧 C/C++、再让另一模型改写以便维护的用途。这是本轮候选；为核对宣传而补读的项目 README 是早期研究材料，不是本窗口新发布。项目署名 Hanzhuo Tan、Qi Luo、Jing Li 与 Yuqun Zhang，论文标为2024年；固定阅读版本为提交85b364bf093eb2ee4f3687cfe38a203fca89f23e，其提交日期为2026年2月12日。

README说明支持Linux x86_64、GCC O0至O3，将二进制先用Objdump转成汇编，再生成C。LLM4Decompile-End直接从汇编生成函数，LLM4Decompile-Ref则细化Ghidra已生成的伪代码，不能把两种输入条件视作同一实验。公开评估以重新执行并通过预设测试为指标，列HumanEval-Decompile的164个标准库C函数与ExeBench的2621个真实项目函数。模型表分别报1.3B-v1.5为27.3%、1.3B-v2为46.0%、9B-v2为64.9%；2024年9月23日更新另给9B值0.6494。这些是项目报告，不是任意整套应用可恢复比例，也不是小型1.3B模型达到约三分之二。

原帖把进展说成2023年至2024年提升，并将其连到REA研究谱系；当前文档不足证明这种因果。银行与保险系统迁移、StarCoder后续改写只是该帖提出的应用方向，没有具体部署或迁移测试。单GPU16GB、模型文件小于3GB等资源宣传未单独验证。不执行模型或目标代码，不声称独立复现；开源模型与函数级评估是已读的具体产物，而不是已证明自动改造遗留主机系统。

候选来源更新：2026-10-22T00:26:57+08:00；历史项目文档用于核对，不作为窗口内新研究。

## 来源

- [isofunds：LLM4Decompile与旧代码维护用途的介绍](https://x.com/i/status/2112943735394758689)
- [LLM4Decompile固定版本README：模型路线、指标与历史更新](https://github.com/albertan017/LLM4Decompile/blob/85b364bf093eb2ee4f3687cfe38a203fca89f23e/README.md)
- [固定版本提交日期与元数据（2026年2月12日）](https://github.com/albertan017/LLM4Decompile/commit/85b364bf093eb2ee4f3687cfe38a203fca89f23e)

[English](en/llm4decompile-assembly-c-models.md) | [返回目录](../README.zh-CN.md)
