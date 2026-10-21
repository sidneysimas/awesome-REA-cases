# vLLM Rust API：Claude／Codex 辅助修复静默忽略参数的兼容差异

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-21
阶段：待验证

2026年10月21日02:07（北京时间），帖子描述 vLLM 将 API 服务改写为 Rust 时的兼容问题：prompt_embeds、return_weight_versions 等不支持的请求字段被接受后静默忽略，调用方却收到正常响应。目标是让重实现与 Python 服务的实际边界一致，而非只复刻成功路径。

报告称当天一批由 Claude 与 Codex 等 AI 编程 Agent 共同署名的修复，会以包含参数名的错误拒绝这些字段，并限制 logit_bias、验证 cache_salt、把 JSON 嵌套限制为64层、对齐 Python 服务的错误形状。此处按 AI 辅助行为兼容修复报告收录，不称闭源二进制反编译。没有取得提交、测试结果或版本号；共同署名不能证明全部研究由 AI 独立完成，列出的行为未经本合集重跑，REA未明示。

## 来源

- [vLLM Rust 服务参数与错误兼容修复的帖子报告](https://x.com/i/status/2112606625986965598)

[English](en/vllm-rust-api-parity-agent-fixes.md) | [返回目录](../README.zh-CN.md)
