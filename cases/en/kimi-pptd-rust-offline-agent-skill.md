# Kimi Slide / PPTD: a modified Rust compiler for offline agent slide editing and export

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At 07:36 Beijing time on October 20, shiquda (@shiquda123321) says they compared seven public agent slide skills and preferred one reverse-engineering Kimi Slide. The author describes PPTD as declarative YAML page descriptions compiled into PDF, PPTX, PNG and other outputs, addressing LLM difficulties editing OOXML directly. A previously found version depended on a reverse-engineered official frontend exporter and could not export PPTX.

The author says they spent recent days extending a public Rust PPTD compiler, adding specification-related functionality and adapting the skill for fully offline use. They also report converting PPTX from other sources back into PPTD for editing. The specific purpose is agent-friendly slide creation and format interoperability, not reversing Kimi's model.

The post supplies two short URLs and screenshots, but no confirmed repository, commit dates, test files or specification-coverage table was obtained here. The seven-skill comparison is a personal assessment without same-task scores. Offline operation, PPTX round trips and added functionality remain author reports. Nothing was installed or run, and lossless preservation of animation, fonts or layout is not established. REA is not explicit.

## Sources

- [shiquda's account of Rust PPTD compiler extensions and an offline skill](https://x.com/i/status/2112326934139203659)

[中文](../kimi-pptd-rust-offline-agent-skill.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
