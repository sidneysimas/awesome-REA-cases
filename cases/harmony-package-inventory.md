# 鸿蒙 App：识别安装包结构与组件

分类：应用与客户端 · REA
记录日期：2026-10-12

HAP 是鸿蒙应用的安装包格式。贡献者使用开源 harmony-next-pipeline 1.0.1 的真实发布包，验证 REA 如何识别 HAP、HSP 与 App Pack，列出组件路径、内容哈希和运行时线索，并对照 CLI 与 MCP 的结果。目的是先回答安装包里有什么、后续可以分析哪里；没有解码 Ark 字节码、验证签名或证明应用运行行为。

## 来源

- [原始 PR 与真实 HAP 记录](https://github.com/morluto/rea/pull/1447)

[English](en/harmony-package-inventory.md) | [返回目录](../README.md)
