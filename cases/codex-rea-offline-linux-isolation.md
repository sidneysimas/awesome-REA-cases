# 离线 Linux 逆向工作机：隔离 Codex 与私人文件

分类：应用与客户端 · REA
记录日期：2026-10-18
阶段：进行中

10月18日06:41（北京时间），Johan Slåttavik（@JohanSlattavik）说 REA 很有意思，但不愿给 AI 工具自由访问自己的电脑，因此正在搭建一个隔离 Linux 工作机，让 Codex 使用 REA、Ghidra 和 JADX，同时无网络、不能访问私人文件。具体用途是保留 Agent 逆向工具链，又缩小工具对个人主机和数据的访问面。

这是正在建设的环境方案，未给仓库、虚拟化或沙盒机制、文件传递方法、Codex 推理连接方式或隔离测试。特别是无网络与 Codex 如何配合尚未解释，不能自行补成已验证的离线模型系统或安全沙盒；没有报告对具体二进制的分析成功。

原帖候选快照1赞、98浏览；隔离属性是作者计划，未进行安全验证。

## 来源

- [Johan Slåttavik 的隔离 Linux 工作机建设报告](https://x.com/i/status/2111588450969231812)

[English](en/codex-rea-offline-linux-isolation.md) | [返回目录](../README.zh-CN.md)
