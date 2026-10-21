# vLLM Rust API: reported Claude/Codex fixes for silently ignored request fields

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-21
Stage: Needs verification

At 02:07 Beijing time on October 21, 2026, a post describes a compatibility problem in vLLM's Rust API-server rewrite: unsupported request fields such as prompt_embeds and return_weight_versions were accepted then silently ignored while callers received normal responses. The purpose is to match the Python server's actual boundaries, not merely its happy path.

The reported wave of fixes, coauthored by AI coding agents including Claude and Codex, rejects those fields with parameter-naming errors, limits logit_bias, validates cache_salt, caps JSON nesting at 64 levels and matches the Python error shape. This is an AI-assisted behavioral-compatibility report, not closed-source binary decompilation. Commits, test results and version numbers were not obtained. Coauthorship does not establish independent AI investigation, the listed behavior was not rerun here, and REA is not stated.

## Sources

- [Post reporting vLLM Rust request-field and error-compatibility fixes](https://x.com/i/status/2112606625986965598)

[中文](../vllm-rust-api-parity-agent-fixes.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
