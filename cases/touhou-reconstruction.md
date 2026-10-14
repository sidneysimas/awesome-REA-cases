# 东方系列：用 Agent 重建旧游戏，并迁移到新平台

分类：游戏与游戏保存 · REA
记录日期：2026-10-12

Touhou Reconstruction Factory 是 N0zoM1z0 将多个东方游戏重建项目的工具与工作流程整理到一起的项目。TH08 指《东方永夜抄》（Imperishable Night）；原材料里的另一个代号是 TH095，即《东方文花帖》（Shoot the Bullet），不是 TH09；TH04 则是《东方幻想乡》。这些都是东方 Project 的游戏。作者用 Agent 分析原可执行文件，逐函数恢复 C++，再编译并对照原二进制，目标是得到可运行、可继续维护的代码。项目记录中，TH08 已有 Linux 和浏览器可玩版本；TH095 已有可玩的 Windows 重建版；TH04 的 DOS 版有作者人工游戏测试记录，现代 64 位移植仍在开发。TH08 延续了 GensokyoClub 的已有工作，TH04 参考了 ReC98；历史项目也使用专用工具，不能把全部成果都归因于 REA。



2026-10-14 的第三方长文综述另称，TH08 项目 1,107 个游戏自身函数中有 1,106 个与原版机器码一致；同文指出这项约两周的工作接续此前人工研究，且另有 1,119 个库函数仅 260 个达到相同标准，整个可执行文件并未精确还原。这是第三方转述，非项目作者在该帖的直接确认；不将全部成果归因于 REA。

第三方综述转述（2026-10-14）：报告 TH08 游戏函数机器码匹配情况；非项目作者直接确认。

## 来源

- [案例文章 PR](https://github.com/morluto/rea/pull/1475)
- [方法与项目证据](https://github.com/morluto/rea/blob/main/website/evidence/touhou-reconstruction-method.md)
- [TH08 项目](https://github.com/N0zoM1z0/th08)
- [TH095 项目](https://github.com/N0zoM1z0/th095)
- [TH04 项目](https://github.com/N0zoM1z0/th04)
- [第三方长文综述：TH08 对照数据（转述，非项目作者确认）](https://x.com/i/status/2110211900051210691)

[返回目录](../README.md)
