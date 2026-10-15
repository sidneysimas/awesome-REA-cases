# REA 6.4.0: Windows .NET and Electron sample tests

Category: Applications and clients · REA
Record date: 2026-10-15
Stage: Analysis test

A long post in this review describes firsthand testing npm REA 6.4.0 on Windows with Node 24 and without ILSpy/dnSpy. Another candidate attributes the review to forum author 神奇的人鱼, so the account circulating it is not automatically treated as the original tester. The post says about 200 .NET Framework assemblies were checked: a sample with 1,701 methods decoded, System.DirectoryServices.dll with 2,094 methods failed, and System.Activities.dll had complete metadata but unavailable members. The author attributes this to a 64 MiB JSON intermediate-representation budget and reports that the documented --type option was unavailable in that npm version. These are tests of a specific version and samples, not a universal threshold of about 2,000 methods. The original gives inconsistent Windows-capability percentages, so that percentage is omitted.

The same post says AI constructed an Electron-style sample with BrowserWindow, IPC handlers, a native .node addon and conditional dynamic require. REA output 24 semantic nodes and 33 edges, located IPC and the native addon, and marked statically indeterminable dependencies unknown. A follow-up says a file-writing static constructor in Trap.dll was not executed and a changed method was correctly located between two assemblies differing only in one constant. The target is testing static structural analysis, resource limits and version comparison, not cloning commercial software. Samples, raw command output and the full environment were not independently checked by this collection. One Trap.dll test cannot guarantee every toolchain is free of side effects.

Version scope: npm 6.4.0, Windows + Node 24; tests are post-reported.
Two candidates have 1 like each and are the main and follow-up posts of the same review, not independent repeated experiments; star counts, line counts and absolute safety claims are not adopted.

## Sources

- [Long post this review: Framework and Electron sample tests](https://x.com/i/status/2110563764886266167)
- [Follow-up this review: Trap.dll and assembly-change comparison](https://x.com/i/status/2110565455039799441)

[中文](../rea-640-windows-managed-electron-test.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
