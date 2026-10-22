# LLM4Decompile: specialized models recovering C functions from assembly or Ghidra output

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-22
Stage: Analysis test

At 00:26 Beijing time on October 22, 2026, @isofunds introduces LLM4Decompile and proposes recovering legacy C/C++ before another model rewrites it for maintenance. This post is the window candidate; the project README consulted to check the promotion is older research material, not a release within this window. The project credits Hanzhuo Tan, Qi Luo, Jing Li and Yuqun Zhang and cites a 2024 paper. The inspected revision is 85b364bf093eb2ee4f3687cfe38a203fca89f23e, committed on February 12, 2026.

The README describes Linux x86_64 and GCC O0 through O3, first disassembling binaries with Objdump and then generating C. LLM4Decompile-End generates functions from assembly, whereas LLM4Decompile-Ref refines pseudocode already produced by Ghidra. These input conditions are not the same experiment. Evaluation defines re-executability as execution that passes predefined tests and lists HumanEval-Decompile's 164 standard-library C functions and ExeBench's 2,621 real-project functions. The model table reports 27.3% for 1.3B-v1.5, 46.0% for 1.3B-v2 and 64.9% for 9B-v2; the September 23, 2024 update separately gives the 9B value as 0.6494. These are project-reported figures, not the fraction of an arbitrary complete application recovered, nor evidence that the small 1.3B model reaches roughly two-thirds.

The post dates the improvement to 2023–2024 and connects it to REA's research lineage; the inspected documentation does not establish that causal story. Bank and insurance-system migration and subsequent StarCoder rewriting are proposed applications, without a specific deployment or migration test. Claims about a single 16GB GPU and a model file below 3GB were not separately verified. Neither models nor target code were executed here, and no independent reproduction is claimed. Open models and function-level evaluations are the inspected artifacts, not demonstrated automatic modernization of legacy mainframes.

Candidate source update: 2026-10-22T00:26:57+08:00; older project documentation was used for checking, not treated as new research within the window.

## Sources

- [isofunds introduces LLM4Decompile and legacy-code maintenance uses](https://x.com/i/status/2112943735394758689)
- [Pinned LLM4Decompile README: model routes, metrics and historical updates](https://github.com/albertan017/LLM4Decompile/blob/85b364bf093eb2ee4f3687cfe38a203fca89f23e/README.md)
- [Pinned revision date and metadata, February 12, 2026](https://github.com/albertan017/LLM4Decompile/commit/85b364bf093eb2ee4f3687cfe38a203fca89f23e)

[中文](../llm4decompile-assembly-c-models.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
