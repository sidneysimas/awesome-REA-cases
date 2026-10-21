# PES 2021／Football Life：Claude 与 REA 辅助重建跨平台大师联赛存档编辑器

分类：游戏与游戏保存 · REA
记录日期：2026-10-21
阶段：进行中

2026年10月21日07:57（北京时间），Felipe Mikeias（felipemikeias）称用 Claude 与 REA 研究 PES 2021／Football Life 的存档编辑器，再重建开源跨平台项目。用途是编辑足球游戏大师联赛存档中的转会预算、工资预算、球迷数和经理姓名，而不是重建整款游戏。

补查公开仓库 pes21-ml-editor，所读 dfa862df 提交于10月19日01:51（北京时间），早于本轮候选。仓库简介将其称为 preview；README 列出 Rust 核心、egui 桌面端与 show／set／decrypt／encrypt CLI，声明支持 Windows、Linux、Intel／Apple Silicon macOS。项目明确致谢公共领域 pesXdecrypter、zlac 的 PES 2021 密钥以及 Devil Cold52 的 PES 2021 ML Money Tool 字段位置；不能把这些前人研究归于 Claude。

项目文档称只有原样重加密逐字节一致才允许编辑，只改所选字段，先备份，以原子写入和失败恢复保护文件，游戏同时写存档时拒写。它们是项目设计声明，不是本合集运行所得。补查 GitHub Actions，当前提交的10月19日运行39151490045为 completed／failure；较旧提交有成功记录，不能称当前版本 CI 通过或三平台均验证。未下载运行目标或修改存档，AI 各步贡献、游戏版本兼容及实际保存结果未独立核定；只用于自有离线存档并保留备份。

验证边界：公开源码与安全保存文档不等于当前构建通过；dfa862df 对应 CI 运行失败，本合集未编辑存档。

## 来源

- [Felipe Mikeias：Claude／REA 与跨平台存档编辑器发布](https://x.com/i/status/2112694820657393735)
- [项目 README：dfa862df，功能、安全保存与前人研究致谢](https://github.com/felipemikeias/pes21-ml-editor/blob/dfa862df2f2f7f077ebd16d0d4b0da4b507b0e7c/README.md)
- [该提交的项目 CI：10月19日运行失败](https://github.com/felipemikeias/pes21-ml-editor/actions/runs/39151490045)

[English](en/pes2021-football-life-claude-rea-editor.md) | [返回目录](../README.zh-CN.md)
