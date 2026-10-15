# macOS 预览：对比有无 REA 的功能重建

分类：应用与客户端 · REA
记录日期：2026-10-12

Preview（预览）是macOS自带的图片和PDF工具。Mahesh把重建它作为有无REA的对照，称纯Claude更快，REA版在缩放、分享、旋转、标注和保存上更接近原作。10月15日候选中文文章进一步叙述两条路线：REA侧解析CommonToolbar.plist、MainMenu.nib和私有selector，编写Swift实现并报告47项自测通过；另一侧依靠AppKit常识生成18个Swift文件并修复自身Bug，交付更快。该文没有给出可重放源码与统一系统测试，属于这次对照的补充叙述，不是本合集或第三方独立复现；不采纳星数、私有类推断或速度差为普遍结论。

发帖：2026-10-11（UTC）｜@maheshboda006
热度快照（2026-10-12）：5 赞｜494 浏览｜1 转发

## 来源

- [作者原帖](https://x.com/maheshboda006/status/2109154423712977359)
- [10月15日中文过程叙述（非独立复现）](https://x.com/i/status/2110613996382654771)

[English](en/preview-rebuild.md) | [返回目录](../README.md)
