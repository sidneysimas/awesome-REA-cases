# An offline Linux reverse-engineering workspace: separating Codex from private files

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: In progress

At 06:41 Beijing time on October 18, Johan Slåttavik (@JohanSlattavik) says REA is interesting but they do not want AI tools to have unrestricted access to their computer. They are building an isolated Linux machine where Codex can use REA, Ghidra and JADX without networking or access to private files. The intended use is to retain an agent's reverse-engineering toolchain while narrowing its access to the personal host and data.

At 09:43 the same account clarifies the current architectural goal in the same conversation: REA, Ghidra and JADX run inside an isolated virtual machine (VM), controlled through AI in VS Code on Linux. Rereading the original confirms that the author and conversation match the earlier record, so this is appended rather than creating another workspace entry. A VM is the intended deployment boundary, not a security property verified by this collection.

The environment remains under construction. No repository, virtualization product, file-transfer method, Codex inference connection or isolation tests are supplied. How the no-network requirement and external control coexist is still unexplained. It must not become a verified offline-model system or secure sandbox, and no successful analysis of a particular binary is reported.

Original candidate snapshot: 1 like, 98 views; isolation properties are the author's plan, not security-validated here.
October 18, 09:43 candidate snapshot: 1 like, 12 views; VM/VS Code is the same author's architecture clarification, without a sample or isolation acceptance test.

## Sources

- [Johan Slåttavik's isolated Linux workspace development report](https://x.com/i/status/2111588450969231812)
- [October 18, 09:43: same author clarifies the isolated VM and Linux VS Code control](https://x.com/i/status/2111634258649608673)

[中文](../codex-rea-offline-linux-isolation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
