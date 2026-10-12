# Android ApiDemos：从 APK 追到具体 Java 方法

分类：应用与客户端 · REA
记录日期：2026-10-12

ApiDemos 是 Appium 用来展示和测试 Android 功能的示例 App。贡献者用其真实发布 APK 验证 REA + headless JADX：读取安装包和清单、查找类、查看成员、提取选中方法的 Java/smali，以及追踪谁调用它。还单独核查了 ContextCompat.startActivities 的重载选择。目的是让 Agent 能从安装包准确定位到特定实现；原 APK 未执行，这是静态分析实例，不是复刻整款 App。

## 来源

- [原始 PR 与验证](https://github.com/morluto/rea/pull/738)

[返回目录](../README.md)
