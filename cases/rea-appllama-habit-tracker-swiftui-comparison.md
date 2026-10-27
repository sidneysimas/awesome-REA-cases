# 习惯追踪Today页：REA与Appllama辅助SwiftUI重建的三组耗时自述

分类：应用与客户端 · REA
记录日期：2026-10-28
阶段：分析测试

2026年10月28日00:50:01（北京时间），一则推广帖用同一提示Build the Today screen of a habit tracker (SwiftUI)，报告Claude5.5 Opus单独34.7秒，加REA19.6秒，加REA与Appllama11.0秒，称视频并排展示三次运行。背景是让模型先研究真实参考应用，再编码而非凭记忆画界面。

作者说REA读取105 arm64参考App的14屏及onboarding→today→streaks流程，标OBSERVED、INFERRED、UNKNOWN；Appllama研究12个同类热门应用的96屏，再经xcodebuild及iPhone17 Pro模拟器验证。105 arm64的具体身份不明，不补造应用名。这些规模、时长与验证均为帖子主张，未取得运行配置、代码、计时边界、重复次数或功能/视觉对照。不能泛化为三倍工程效率、完整习惯应用或独立通过测试；本合集未运行工具。

候选快照17赞、740浏览、3转发；34.7/19.6/11.0秒为宣传帖口径。

## 来源

- [REA/Appllama习惯追踪器三组展示，2026-10-28](https://x.com/i/status/2115123864762020103)

[English](en/rea-appllama-habit-tracker-swiftui-comparison.md) | [返回目录](../README.zh-CN.md)
