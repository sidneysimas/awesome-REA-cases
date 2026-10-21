# Neverball 到 KaniVolcanoEngine：REA 先提规格，LLM 再用 Rust 引擎重建

分类：游戏与游戏保存 · REA
记录日期：2026-10-21
阶段：待验证

2026年10月21日22:47（北京时间），Otinpan（@otinpan512）介绍KaniVolcanoEngine与REA结合的实验：先用REA研究Neverball可执行文件，生成覆盖游戏逻辑及关卡结构的规格，再让LLM基于该规格，在自己的Rust游戏引擎KaniVolcanoEngine里重建游戏。这里报告的是可执行文件到规格再到另一引擎的路径，不是只看截图仿界面。

补查原帖确认作者及两段视频附件，但本合集未完整检查演示，也没有取得目标版本、规格、重建源码、随机或物理行为对照、关卡覆盖率及构建记录。公开GitHub项目名检索未找到可确认仓库，不能推断它未公开。作者所称重建不能扩展为全部关卡、完全相同物理或原始源码恢复，LLM具体型号也未说明。未运行目标或引擎。

## 来源

- [Otinpan：Neverball可执行文件、REA规格与Rust引擎重建](https://x.com/i/status/2112918638345039936)

[English](en/neverball-rea-kanivolcanoengine.md) | [返回目录](../README.zh-CN.md)
