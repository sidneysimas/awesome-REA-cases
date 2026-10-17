# Decepticon Reverser: REA/Ghidra static evidence in authorized security investigations

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: Related project

At 01:28 Beijing time on October 18, 2026, @chaitanyamkj introduces Decepticon, describing REA/Ghidra integration in its Reverser, 16 specialists and 102/104 XBOW results. Supplementary reading of BitterSecurity/Decepticon's README and reversing document confirms an authorized-scope security-investigation system, not an Adobe reconstruction tool. Main then corresponded to commit 0647e8bd24110960a8c8e3654a8a944647bee3d0, dated October 17 at 19:34 Beijing time. Repository materials check implementation boundaries rather than becoming another in-window candidate.

The document specifies REA 6.3.0 and Ghidra 12.1.4. For a binary already in the workspace, the Reverser checks status, discovers that session's tools and schemas and invokes selected tools. Before returning results, the gateway preserves original Evidence and an integrity manifest tied to the analyzed bytes. This does not replace Ghidra's decompiler or imply other providers are installed. The document explicitly says static results do not prove runtime paths executed and do not preserve a user-edited Ghidra project; unavailable workloads fall back to local radare2 and triage tools.

The README does publish project scores of 102/104 overall and 7/8 hard XBOW challenges. They are not this collection's reruns, arbitrary-target compromise rates or REA reversing accuracy. Multi-agent orchestration, databases and a sandbox describe system architecture, not proof that a particular binary was successfully recovered. This collection only read documentation; it started no agent, executed no attack, installed no dependencies and ran no target.

Candidate: October 18, 2026, 01:28; supplementary repository commit: October 17, 2026, 19:34 Beijing time.
Project documentation specifies REA 6.3.0/Ghidra 12.1.4 and Evidence retention; static analysis does not establish runtime execution.
XBOW 102/104 overall and 7/8 hard are project pentesting results, not independently rerun or reversing-accuracy measurements.

## Sources

- [Window candidate: introduction to Decepticon and Reverser](https://x.com/i/status/2111509697211806150)
- [Public repository and project benchmark account](https://github.com/BitterSecurity/Decepticon)
- [Pinned commit: REA integration and static-analysis boundaries](https://github.com/BitterSecurity/Decepticon/blob/0647e8bd24110960a8c8e3654a8a944647bee3d0/docs/features/rea-reversing.md)

[中文](../decepticon-reverser-rea-project.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
