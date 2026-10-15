# Flutter App：从安装包识别运行时和编译结构

分类：应用与客户端 · REA
记录日期：2026-10-12

Flutter 是跨平台 App 开发框架，发布后的 Dart 逻辑常被提前编译到原生库中，不能像普通脚本一样直接阅读。贡献者分析 APK 内的 libapp.so 和 libflutter.so，提取 snapshot hash、构建标识、区段和包路径线索，以确认分析的是哪套运行时、数据位于哪里。讨论中测试了 Flutter Gallery、PocketDhamma、Flutter McSweepy 和 cone 等真实 App。这是为后续分析确定入口，尚非完整 Dart 源码恢复。

## 来源

- [PR 与真实应用测试](https://github.com/morluto/rea/pull/1582)

[English](en/flutter-aot.md) | [返回目录](../README.md)
