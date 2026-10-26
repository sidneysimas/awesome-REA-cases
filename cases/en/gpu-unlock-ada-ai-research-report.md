# GPU-Unlock-Ada: an AI reverse-engineering report and public Ada tensor-throughput research

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-25
Stage: Needs verification

At 12:20:50 Beijing time on October 25, 2026, HKEPC reported JustAResearch using AI-assisted reverse engineering to study GeForce RTX 40 tensor-compute restrictions. It described GPU-Unlock-Ada as requiring neither vBIOS flashing nor a modified NVIDIA driver and listed benchmarks from the 4090 through 4060 Ti. The AI attribution in this entry comes from that report: no inspectable model conversation or clear evidence of REA use was found, and journalistic attribution is not independent project validation.

Supplementary reading on October 26 examined the public JustAResearcher/gpu-unlock-ada README. HEAD at lookup was d28c485418c3d9d034cd4bac19200bc33dd3453b, committed October 26 at 04:21 UTC. This is out-of-window documentation, not evidence already contained in the October 25 candidate. The README describes a Linux kernel module applying an SM speed-select override before the stock driver starts, followed by FLR and driver handoff. The AD102 payload and debug-booter analysis come from TOTORONG/AD103_win_unlocker; the Linux module and packaging derive from Zagitta/gpu-unlock. Upstream work is not attributed entirely to JustAResearch or AI.

The project reports RTX 4090 FP16-to-FP32-accumulate throughput increasing from 165.6 to 331.6 TF/s and BF16 from 165.5 to 330.6 TF/s. It also cites a matched owner run at the same 450W cap: FP16 instruction throughput of 160.4 to 320.4 TF/s and BF16 of 159.7 to 320.2. Real cuBLAS GEMM median FP16 gains were 12–34%; BF16 gained 16–20% at two shapes and was essentially unchanged at 4096³. A modified 48GB 4090 showed no benefit in an 8K-prefill quantized MoE serving workload, at 0.983×. These are project and owner records, not benchmarks rerun for this collection.

The media's universal full-series and broadly doubled matrix-performance framing is therefore not adopted. Public documentation requires per-card experimental opt-in for many Ada PCI IDs; some have only one tested board and laptop results differ. INT8, dp4a and scalar FP32 often remain near baseline. FP8 requires distinguishing instruction issue rate from application GEMM, accumulation mode and power limits, rather than inferring acceleration of every AI workload from one metric. Compatibility, extended stability and safety are not independently confirmed. No firmware or Windows tool was downloaded, module loaded, target code executed or local driver changed.

AI involvement is attributed by media, with REA unconfirmed; public documentation and owner benchmarks are not independent reproductions by this collection.
2× instruction throughput is not 2× inference; reuses TOTORONG's payload and Zagitta's module, and per-card experimental support is not universal Ada coverage.

## Sources

- [HKEPC's AI reverse-engineering report on GPU-Unlock-Ada, October 25, 2026](https://x.com/i/status/2114210551413059771)
- [GPU-Unlock-Ada README at a fixed commit, supplementary reading on October 26](https://github.com/JustAResearcher/gpu-unlock-ada/blob/d28c485418c3d9d034cd4bac19200bc33dd3453b/README.md)
- [GPU-Unlock-Ada project entry and support scope, supplementary reading on October 26](https://github.com/JustAResearcher/gpu-unlock-ada)

[中文](../gpu-unlock-ada-ai-research-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
