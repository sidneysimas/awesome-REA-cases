# Amazon Prime tvOS：研究 IPA 的 Universal Link，让自己的 App 跳到节目页

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-17
阶段：待验证

2026年10月17日19:51（北京时间），Xiao（@im_xiaoxiao）报告用“RAE+ghidra”分析Amazon Prime的tvOS IPA，找到了该应用支持的Universal Link格式，称自己的App现在可以直接跳到对应动画节目的播放页。逆向用于发现跨应用深链接接口，不是解密视频、绕过订阅或重建整个Prime客户端。原帖写的是RAE而非REA，工具身份没有进一步确认，因此不自行纠正其拼写并据此标为REA实测；正文同时明确出现Codex参与工作环境。

作者还报告RAE或Ghidra中的某一方每分钟消耗10G磁盘，最终占满电脑，导致Codex无法执行，自己手动分析磁盘占用才定位问题。故障归属、10G的单位口径与增长机制未核实，不扩展为Ghidra或REA的普遍缺陷。帖子没有公开链接格式、IPA版本、代码、操作视频或跳转验证记录，所称成功仅是作者自述；不能推断所有节目或tvOS版本兼容。本合集补查原帖确认作者与完整文字，未执行IPA或独立复现。

来源发布：2026-10-17 19:51，北京时间；原文工具名RAE，不自动改为REA。
跳转成功及每分钟10G磁盘消耗均为作者报告，无公开实现与测试记录。

## 来源

- [Xiao 的 Prime tvOS 深链接研究与磁盘故障自述](https://x.com/i/status/2111424789827228006)

[English](en/prime-tvos-universal-link-ghidra-report.md) | [返回目录](../README.zh-CN.md)
