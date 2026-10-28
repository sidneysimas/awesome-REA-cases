# Ginux: Codex builds a Linux-userspace-compatible kernel under human architecture and acceptance gates

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-28
Stage: In progress

At 18:11:05 Beijing time on October 28, 2026, corleone jack (@jackcorleone19) recounts Gregory Kurtzer's Ginux: one Codex task over 11 days produced about 139,000 lines for an independent Linux binary-interface implementation, not a Linux fork, booting Rocky Linux 10 to systemd. The HDAE division assigns architecture, constraints, milestones, acceptance and stopping decisions to a human, with implementation, booting, testing and diagnosis by the agent. Included as AI-assisted compatibility reconstruction, not recovery of original Linux source or an inferred decompilation of Linux.

Supplementary October 28 reading of gmkurtzer/ginux's public README describes a Rust-first x86-64 kernel booting directly through UEFI, with Linux userspace inside native domains rather than a Linux host kernel. The document credits one persistent OpenAI Codex task using GPT-5.6 Sol over 11 days, retaining about 139,000 implementation and test lines. It explicitly identifies October 23 commit d11c126a048a51fe7eb9c4105f31760add1027ea as the paper's evaluated checkpoint, not all later repository changes. This review read documentation only, without inspecting or rerunning the paper's measurements.

The README reports selected Alpine and Rocky programs on a Q35/OVMF QEMU configuration with Intel IOMMU and virtio, and Rocky 10 systemd reaching multi-user.target. Of 375 Linux 6.12 syscall numbers, 82 are complete, 245 partial and 48 policy-denied: exhaustive classification is not complete conformance. Aggregate make test is not fully passing; a post-execve system-supervisor lifecycle probe remains a recorded failure. Hardware, isolation, persistence, networking and security validation remain incomplete, with no independent audit, physical-hardware coverage or production replacement guarantee. Eleven days, line count and a single boot path do not establish arbitrary Linux-program compatibility. REA is unspecified. This collection did not compile, boot or install target dependencies.

Candidate snapshot: 0 likes, 14 views, 0 reposts. Eleven days and 139,000 lines are project figures including tests.
The 82/245/48 syscall classification and systemd boot are documented states, not independent tests or distribution-wide compatibility.

## Sources

- [corleone jack recounts Ginux/Codex research, October 28, 2026](https://x.com/i/status/2115385859633475649)
- [Supplementary public Ginux README, validation limits and research account, read October 28](https://github.com/gmkurtzer/ginux)

[中文](../ginux-codex-linux-abi-kernel-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
