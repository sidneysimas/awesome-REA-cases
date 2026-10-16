# OpenCodex / Antigravity：用 REA 调查多轮工具调用签名丢失

分类：应用与客户端 · REA
记录日期：2026-10-16
阶段：待验证

10月16日作者报告称，OpenCodex 代理 Gemini/Antigravity 的复杂多轮会话即使缓存和重放历史签名，仍遭遇缺少 thought_signature 的400错误。作者用 REA 查看本地 antigravity_tools（Rust）与 Google language_server（Go）二进制，称发现本地缓存及回退找不到真实签名时客户端使用 skip_thought_signature_validator 占位符；据此在 OpenCodex 的 Antigravity 请求末端加入兜底，允许后续真实签名覆盖。作者称错误消失，但未给补丁、版本、请求日志或测试矩阵。Google 网关硬编码豁免的解释仍是作者归因，客户端静态观察不能直接证明服务端实现，也不代表任意模型或会话兼容。本合集未发送请求或复现。

10月16日候选快照：1赞、108浏览；结果与服务端解释均未独立核验。

## 来源

- [OpenCodex 签名报错与 REA 调查报告](https://x.com/i/status/2110921946418602001)

[English](en/opencodex-antigravity-signature-fallback.md) | [返回目录](../README.zh-CN.md)
