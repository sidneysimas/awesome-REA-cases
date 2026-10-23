# Caleb Gross: using an LLM to prioritize decompiled firmware functions for review

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-23
Stage: Analysis test

At 16:08:04 Beijing time on October 23, 2026, Black Hat's official @BlackHatEvents account recaps research presented by Caleb Gross at Black Hat USA 2026. The target is deciding where human review should start among thousands of decompiled firmware functions without symbols, not automatically finding every vulnerability. Rereading the original confirmed the official publisher and wording. The advertised December 7-10 London conference dates are not treated as experiment dates.

The post says Gross had an LLM rank functions by how likely they were to hide a bug, more than doubling precision compared with simply asking the model. This is a concrete AI-assisted reverse-engineering triage experiment: decompiled functions are the input, and a priority order for vulnerability review is the output. REA, model, firmware product, sample size, precision denominator and baseline prompt are unspecified. Recall, newly discovered vulnerability counts and generalization to all firmware cannot be inferred.

This review checked only the candidate and official original post, not a full conference video or paper. It did not run the ranking, inspect labels or recompute metrics. More than twice the precision remains a conference organizer's reported result, not a measurement by this collection. The research is recorded as an analysis test with explicit inputs, outputs and a comparison target.

Source: October 23, 2026, 16:08:04 Beijing time; the experiment's date is unspecified.
More than twice the precision is reported in an official conference summary, not recomputed. REA is not mentioned.

## Sources

- [Official Black Hat post: Caleb Gross's firmware-function ranking and reported precision, October 23, 2026](https://x.com/i/status/2113542962533605863)

[中文](../caleb-gross-llm-firmware-function-ranking.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
