# ReaCut: an independent editor informed by Jianying research

Category: Applications and clients · REA
Record date: 2026-10-15
Stage: In progress

In this review, @zoozoo_ai says they are reverse-engineering Jianying with REA, invites contributors and links Xiangyu-CAS/rea-capcut. This is separate from Mehal's existing CapCut editor. On October 15, repository research and validation documents from October 13 were checked: the author used REA 6.4.0 to inspect macOS Jianying 11.0.12922, passively observe new-project creation and timelines with self-made assets, and distinguish component/string presence from actual behavior. The initial opaque draft cannot directly establish format support. The independent implementation uses its own project format and FFmpeg exports; commercial assets, original binaries and a complete native call graph are not presented as recovered results. Validation records report 293 passes and one skip for missing libx265, plus actual installed-package exports of videos with Chinese text and mixed audio and plugin-protocol tests in an isolated environment. The user confirmed Codex sidebar visibility, but complete host workflows, cross-platform support and initial CI failure retain limitations. Version 0.5.0 is an Apple Silicon preview package with only local ad-hoc signing and no notarization. This collection only read project records; author acceptance is not independent reproduction or all-green cross-platform CI.

Current candidate is a work-in-progress invitation; October 13 documents are retrospective supporting evidence, not newly completed results in this window.

## Sources

- [Author's contribution invitation this review](https://x.com/i/status/2110633692834222460)
- [Project source](https://github.com/Xiangyu-CAS/rea-capcut)
- [October 13 research boundaries (additional source)](https://github.com/Xiangyu-CAS/rea-capcut/blob/main/docs/research/REA_FINDINGS.md)
- [October 13 project-validation records (additional source)](https://github.com/Xiangyu-CAS/rea-capcut/blob/main/docs/VALIDATION.md)

[中文](../reacut-jianying-open-editor.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
