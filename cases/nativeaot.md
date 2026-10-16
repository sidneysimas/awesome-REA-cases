# .NET NativeAOT：从原生二进制恢复 C# 信息的诉求

分类：应用与客户端 · REA
记录日期：2026-10-12
阶段：进行中

NativeAOT 会把 .NET 程序提前编译为原生机器码，不能再按普通 .NET 程序集直接读出 C#。用户希望 REA 恢复相关信息；部分元数据支持已加入，但现有材料不能证明恢复了原 C# 工程，Windows 工作流也有边界。这是一条能力需求和进展记录。

## 来源

- [原始记录](https://github.com/morluto/rea/issues/744)
- [相关实现](https://github.com/morluto/rea/pull/748)

[English](en/nativeaot.md) | [返回目录](../README.zh-CN.md)
