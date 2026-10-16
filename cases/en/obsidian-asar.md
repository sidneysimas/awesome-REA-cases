# Obsidian ASAR: large-package analysis

Category: Applications and clients · REA
Record date: 2026-10-12
Stage: Analysis test

Obsidian is a local note-taking app whose desktop JavaScript can be packaged in an ASAR archive. A user analyzed a real package of about 24 MB with REA and, following fixes, confirmed that REA 6.0.0 with JSONL completed the original target in 86 seconds. The discussion establishes that large-package analysis can run, but shows no note-taking feature rebuilt from the results, so this is classified as an analysis test rather than completed feature reconstruction.

On 2026-10-15, another poster reports analyzing Obsidian with REA. They say a native-binary hash mismatch caused integrity verification to block the first run; after adjusting parameters, JavaScript-layer analysis finished in seconds and exposed file-reading and system-interface call paths. Their attempt to analyze the native binary failed, and Ghidra, Hopper and IDA were not configured. The poster explicitly notes that static analysis alone, unresolved dynamic IPC and code that has not been run do not establish behavior. The post also mentions an unnamed large package taking about a minute, but neither its identity nor its results justify including it in this Obsidian case. This collection did not reproduce these steps.

Follow-up posted: 2026-10-15T00:29:18+08:00; author report, not independently retested.
Report limited to Obsidian JavaScript static analysis; native-binary analysis failed and dynamic behavior was not established.

## Sources

- [Original record](https://github.com/morluto/rea/issues/746)
- [This window: author reports Obsidian JavaScript static analysis and blocked native-layer analysis (not independently retested)](https://x.com/i/status/2110407610134663474)

[中文](../obsidian-asar.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
