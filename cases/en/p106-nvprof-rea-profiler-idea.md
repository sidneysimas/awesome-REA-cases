# P106 mining GPU: an REA and homemade-profiler idea after nvprof refuses support

Category: Hardware and interoperability · REA
Record date: 2026-10-23
Stage: Needs verification

At 18:05:05 Beijing time on October 23, 2026, a post reports NVIDIA nvprof displaying “nvprof does not support NVIDIA Crypto Mining Processors” on the author's P106 mining rig. The practical problem is analyzing GPU work on a machine whose device category is rejected by the official profiling tool.

The author proposes making a profiler with CUDA events and asks “Time to REA: Reverse Engineer Anything?” This names a device, tool and compatibility idea, not a completed nvprof patch. The post does not specify which file REA would inspect and provides no model, code, timing output or performance comparison.

It is recorded as an unverified preliminary plan. Bypassed device detection, restored official profiling, access to hardware counters and equivalence between CUDA events and nvprof are not inferred. This review read only the candidate; it did not access the rig, download drivers or run device tests.

Source: October 23, 2026, 18:05:05 Beijing time; an idea only, with no completion or timing validation.

## Sources

- [Candidate original: nvprof on P106, CUDA events and an REA idea](https://x.com/i/status/2113572410175688822)

[中文](../p106-nvprof-rea-profiler-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
