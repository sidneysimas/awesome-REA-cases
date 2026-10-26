# Railroad Tycoon II：REA与专职AI Agent辅助的Rust重实现

分类：游戏与游戏保存 · REA
记录日期：2026-10-26
阶段：进行中

2026年10月25日15:30（北京时间），yibie在资源目录更新中介绍Railroad Tycoon 2的Rust逆向重写，称从提交trailer发现AI参与。补查公开仓库确认目标为pedryvo/rrt2-decomp：研究1998至2001年的Railroad Tycoon II Platinum可执行文件，在保留等距视角和玩法的同时适配现代分辨率。此条来自往期待补审窗口，不作为10月26日00:00至04:00新抓取成果。

补充静态阅读的README说明，项目经REA MCP调用Ghidra，由不同专职AI Agent分担工作，从字符串、导入和数据表定位子系统，先写含地址、常量及伪代码的规格，再编写Rust实现。原函数通过Unicorn运行，与Rust结果逐位比较；整局行为则让原程序在Wine中推进同一存档，与重实现逐字段比较。10月23日23:03:18 UTC的0d26aca提交有Claude Opus 5.5共同署名，内容涉及报表、图表与CSV导出；这支持存在AI协作，不量化AI代码比例。

项目README自报2945个函数、616个已写规格、304个函数逐位验证，以及131个存档推进对照用例全部一致；这些是项目报告，不是本合集重跑结果，不能推成全部游戏语义或函数都已恢复。文档仍标pre-alpha，文件格式、模拟、UI和联机均有部分完成项，路线图与后续实现进度也不完全同步；Windows/macOS构建明确称作者尚未测试。因此按进行中收录，不称完整游戏重建已经验收。

原帖说README不提AI，但当前补读文档已明确专职AI Agent与REA，应以实际读到的文档更正这一概括。8星、421文件和20处trailer仅为原帖快照，本合集未重新统计。项目要求合法持有原游戏数据，不随本记录分发。补充仓库材料早于本轮窗口，用于身份与方法核对；未安装依赖、下载游戏资产、执行项目代码或独立验证画面、性能及存档结果。

往期待补审收录；进行中，项目自报差分结果未独立运行，README仍有未同步的路线图。
当前README明确REA与AI Agent；不沿用原帖README未提AI的概括，不把共同署名量化为AI代码比例。

## 来源

- [往期候选：yibie介绍两个独立游戏项目，2026-10-25北京时间](https://x.com/i/status/2114258253253329233)
- [补充项目README，固定提交0d26aca，2026-10-23 UTC](https://github.com/pedryvo/rrt2-decomp/blob/0d26aca502ec36730c6b261713f71cda890319d5/README.md)
- [公开报表实现提交及Claude Opus 5.5共同署名，2026-10-23 UTC](https://github.com/pedryvo/rrt2-decomp/commit/0d26aca502ec36730c6b261713f71cda890319d5)

[English](en/rrt2-decomp-rea-rust-reimplementation.md) | [返回目录](../README.zh-CN.md)
