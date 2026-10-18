# Neural decompilation research: specialized models, variable names and types

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-18
Stage: Related project

At 12:40 Beijing time on October 18, a Japanese survey frames research in terms of closed-source protection and describes recovering readable programs from instructions, inferring missing names and types, and synthesizing substitutes from input/output observations. It cites Towards Neural Decompilation and Coda from 2019, LLM4Decompile from 2024, DIRTY from 2022 and IReEn from 2021. Their concrete purposes are learned decompilation, more readable decompiler output and functional reconstruction from black-box observations, not a commercial application rebuilt by the poster.

Supplementary reading of the primary LLM4Decompile page on ACL Anthology confirms a November 2024 paper by Hanzhuo Tan, Qi Luo, Jing Li and Yuqun Zhang, with 1.3B–33B models. End directly decompiles, while Ref refines Ghidra output. Its abstract reports over 100% relative improvement in re-executability over GPT-4o and Ghidra on HumanEval and ExeBench, and a further 16.2% improvement for Ref over End. These are the paper authors' benchmark claims, not a 100% absolute success rate or recovery of an entire closed application. No evaluation was independently run here. The paper is historical supplementary evidence outside the candidate window, not a new result from this run.

The survey also quotes DIRTY name/type recovery at 66.4%/75.8% and about 78% for IReEn on Karel; those figures were not checked against each original paper. The benchmarks do not establish its generalizations about nearly reversible compilation, ineffective obfuscation or near-zero analysis cost, which are not adopted. REA involvement is unconfirmed, and nothing here establishes lossless recovery of original comments or design intent by current general-purpose models.

October 18, 2026 survey candidate snapshot: 7 likes, 746 views; the 2024 paper is traced background, not an in-window experiment.
DIRTY and IReEn numbers are survey quotations only; for LLM4Decompile only the primary abstract was checked, without rerunning tests.

## Sources

- [October 18 Japanese neural-decompilation survey](https://x.com/i/status/2111678828599021657)
- [Historical supplement: LLM4Decompile EMNLP 2024 abstract and metadata](https://aclanthology.org/2024.emnlp-main.203/)

[中文](../neural-decompilation-research-survey.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
