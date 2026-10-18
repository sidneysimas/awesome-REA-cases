# An offline Linux reverse-engineering workspace: separating Codex from private files

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: In progress

At 06:41 Beijing time on October 18, Johan Slåttavik (@JohanSlattavik) says REA is interesting but they do not want AI tools to have unrestricted access to their computer. They are building an isolated Linux machine where Codex can use REA, Ghidra and JADX without networking or access to private files. The intended use is to retain an agent's reverse-engineering toolchain while narrowing its access to the personal host and data.

This is an environment under construction. No repository, virtualization or sandbox mechanism, file-transfer method, Codex inference connection or isolation tests are provided. In particular, how Codex works with the no-network requirement is unexplained. It must not be expanded into a verified offline-model system or secure sandbox, and no successful analysis of a particular binary is reported.

Original candidate snapshot: 1 like, 98 views; isolation properties are the author's plan, not security-validated here.

## Sources

- [Johan Slåttavik's isolated Linux workspace development report](https://x.com/i/status/2111588450969231812)

[中文](../codex-rea-offline-linux-isolation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
