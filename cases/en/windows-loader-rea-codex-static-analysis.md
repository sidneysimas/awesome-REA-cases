# Windows loader: REA and Codex analysis without running the sample

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: Analysis test

At 07:21 Beijing time on October 18, Fedele Mantuano (@fedelemantuano) introduces a Windows loader analysis by asking what can be learned about malware without running it. He reports using REA, Ghidra and Codex to uncover hardcoded servers and in-memory payload loading. A loader is a program responsible for loading a subsequent payload; the purpose here is to understand sample structure and potential communication/loading paths, not actually connect and execute it.

The available original post provides no sample hash, malware family, function addresses, server values, full evidence chain or decompilation results. The article is only a short link and its text was not obtained. This is therefore the author's reported static analysis. Hardcoded addresses are not established as currently active services, and a possible payload path must not become observed execution. No sample was downloaded or run and no independent reproduction was performed.

Candidate snapshot: 0 likes, 36 views; conclusions are author-reported static findings, not dynamic acceptance results.

## Sources

- [Fedele Mantuano: static loader analysis with REA/Ghidra/Codex](https://x.com/i/status/2111598581421670782)

[中文](../windows-loader-rea-codex-static-analysis.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
