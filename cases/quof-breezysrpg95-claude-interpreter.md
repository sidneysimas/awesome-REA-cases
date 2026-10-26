# BreezySRPG95：Quof用Claude反汇编旧运行器，制作战棋游戏替代客户端

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-25
阶段：进行中

2026年10月25日12:56:56（北京时间），Quof（@Mr_Quof）说明，自己参考REA仓库，使用Claude Code CLI反汇编原可执行文件并编写客户端。补读同日12:56:55父帖确认项目是BreezySRPG，用来运行シミュレーションRPGツクール95（Sim RPG Maker 95）制作的战棋游戏：把替代运行器放入合法取得的游戏目录，改善旧游戏在现代电脑上的操作体验。作者只说参考REA，未证明实际连接REA MCP。

同串作者介绍键盘操作、加速、跳过敌方回合、高分辨率、无边框窗口、事件中存档及敌方行动范围，并明确这是仅有几个人测试过的早期beta。10月26日补查公开Quof/BreezySRPG95仓库，固定到10月25日提交cad576ddcec2ea92ef6e3a82bb40068b096c8ba4的README，项目称不修改游戏文件，列出えるまに、ＯtoＺ、昴の騎士及闇鍋企画前后篇为已测游戏。README另说明原有1至8号存档可互通，而9至100号槽位仅替代客户端支持；事件中存档被旧程序读取时回到回合菜单。

父帖和仓库仅为候选的方法说明补充目标与兼容性，不是额外候选。未下载发行程序、运行游戏或验证反汇编质量；功能和已测游戏均为作者／项目自述，不保证所有SRPG Maker 95游戏兼容，也不是恢复原始源码的证明。

早期beta，仅数人试用；未独立运行。
参考REA不等于确认调用REA；存档互通有槽位和事件状态限制。

## 来源

- [Quof的Claude Code反汇编方法说明，2026-10-25](https://x.com/i/status/2114219639274340689)
- [同日父帖：BreezySRPG身份与用途](https://x.com/i/status/2114219633192411382)
- [同日作者：功能与早期beta限制](https://x.com/i/status/2114219636686516718)
- [补充：10月25日提交的项目README](https://github.com/Quof/BreezySRPG95/blob/cad576ddcec2ea92ef6e3a82bb40068b096c8ba4/README.md)

[English](en/quof-breezysrpg95-claude-interpreter.md) | [返回目录](../README.zh-CN.md)
