# Windows loader：REA 与 Codex 的不运行样本分析

分类：应用与客户端 · REA
记录日期：2026-10-18
阶段：分析测试

10月18日07:21（北京时间），Fedele Mantuano（@fedelemantuano）介绍一次 Windows loader 分析，提出不运行恶意软件也能得到什么信息的问题。他称使用 REA、Ghidra 和 Codex，发现硬编码服务器以及内存中加载载荷的行为。loader 是负责装入后续载荷的程序；这里的目标是理解样本结构和潜在通信/加载路径，而不是让其实际联网执行。

可用原帖未给样本哈希、恶意软件家族、函数地址、服务器值、完整证据链或反编译结果，文章只有短链且未取得正文。因此这只是作者报告的静态分析，不将硬编码地址等同当前活跃服务，也不将可能的载荷路径升级为已经观测到的执行。未下载或运行样本，未做独立复现。

候选快照0赞、36浏览；结论为作者报告的静态发现，无动态验收。

## 来源

- [Fedele Mantuano：REA/Ghidra/Codex 静态 loader 分析](https://x.com/i/status/2111598581421670782)

[English](en/windows-loader-rea-codex-static-analysis.md) | [返回目录](../README.zh-CN.md)
