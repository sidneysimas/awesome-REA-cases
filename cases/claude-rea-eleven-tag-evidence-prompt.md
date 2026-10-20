# 11 标签逆向提示词：引擎检查、证据分层与负例验收

分类：应用与客户端 · REA
记录日期：2026-10-20
阶段：相关项目

10月20日13:22（北京时间），@xmyttle（Myttle）介绍自己写的11标签提示词，供接入REA的Claude Code使用。用户填功能、应用和路径三个槽位，模板用goal、role、scope、engine_check、inputs、evidence、spec、verify、report、rules和start约束调查。具体目的是防止先猜结论再补解释：先确认目标所需工具，对每项结论标OBSERVED、INFERRED或UNKNOWN，并要求提交检查器必须拒绝的测试。

作者限定自有或获准软件，排除DRM、许可或反作弊绕过；开始时先输出引擎检查及三步计划，等用户批准。此为具体流程idea及提示词介绍，不是工具自动保证授权或正确性。帖子没有命名被测App、给出一次完整执行或负例拒绝日志，本合集也没有运行模板，不能把“不允许猜”当成已证明零幻觉；REA为被搭配的工具，不代表官方模板。

## 来源

- [Myttle的11标签提示词设计与授权边界](https://x.com/i/status/2112414005293985823)

[English](en/claude-rea-eleven-tag-evidence-prompt.md) | [返回目录](../README.zh-CN.md)
