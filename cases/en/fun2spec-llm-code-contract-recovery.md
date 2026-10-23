# Fun2Spec: recovering C++ postconditions with LLMs, with a reported Spec-Agent extension

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-24
Stage: Related project

At 00:50:35 Beijing time on October 24, 2026, Julien Vanegue (@jvanegue) calls recovering specifications from code the dual of verification, citing Fun2spec: Code Contract Synthesis At Scale and describing Spec-Agent as an extension to separation logic with fuzzing in the loop. The goal is to supply checkable behavioral contracts for existing implementations, not to recover lost original source.

The public bloomberg/fun2spec README explicitly uses LLMs to generate postcondition specifications for C++ functions, presenting Bloomberg Development Environment (BDE) and the BlazingMQ message queue as two case studies. Its result CSV records function names, generated postconditions and counts of executions where a condition holds or fails. Such test feedback is not a mathematical proof over arbitrary inputs. The documented default model is microsoft/Phi-3-mini-128k-instruct, with return-type filtering for int, pointer or all.

The supplementary README is fixed at afcc146242d2a2c966cadf632b2775cc47c552ae, a July 6, 2026 commit preceding this window. It lists the paper as published at FSE 2026 in July. This confirms the method, case studies and result fields, not a newly released experiment in this window. Spec-Agent's separation-logic and fuzzing extension remains the candidate author's description; its paper and implementation details were not obtained. No tool was run, dependencies installed, contracts independently checked or accuracy measured. REA is not mentioned. This is recorded as a related research project.

Candidate: October 24, 2026, 00:50:35 Beijing time; supplementary repository commit: July 6, 2026, before the window.
Fun2Spec documentation read; Spec-Agent is author-described only. No independent contract generation or checking.

## Sources

- [Julien Vanegue on Fun2spec and Spec-Agent, October 24, 2026](https://x.com/i/status/2113674455503212738)
- [Supplementary Fun2Spec README: LLM method, two case studies and CSV fields, July 6, 2026 commit](https://github.com/bloomberg/fun2spec/blob/afcc146242d2a2c966cadf632b2775cc47c552ae/README.md)

[中文](../fun2spec-llm-code-contract-recovery.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
