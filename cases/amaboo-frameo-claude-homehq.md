# AMABOO Frameo 相框：Claude Code 参考已有项目改作 Home HQ 屏幕

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-17
阶段：待验证

10月17日08:20（北京时间），@InvestingVault 转述荷兰用户 @j3lte 参考 @wesbos 的相框改造，让 Claude 阅读 Wes 的 GitHub 仓库，把 AMABOO 10.1英寸 Frameo 相框改作 Home HQ kiosk，并提交记录设置的 PR。正文给出从 Beta Program 启用 ADB、先备份固件、禁用两个自动更新器、设 Home HQ 为主屏，再禁用 Frameo 应用的过程；备份据称压缩后约800 MB。该设备内置浏览器够新，无需替换。作者提醒禁用 Frameo 后等约10秒再重启，否则原应用会回来，并称另一位相同板型用户也遇到。

这是 AI 辅助的旧硬件适配与配置转述，不是重新恢复 Frameo 源码或确认新的协议逆向。来源明确称没有刷固件、更改可撤销；本合集未核对 PR、测试备份恢复或运行设备，不保证其他板型同样适用，也不把约800 MB和10秒扩大为通用规格。

Claude Code 参考已有项目；未确认 REA，未复测可逆性或相同板型行为。

## 来源

- [AMABOO 相框配置与重启时序的转述](https://x.com/i/status/2111250941886226471)

[English](en/amaboo-frameo-claude-homehq.md) | [返回目录](../README.zh-CN.md)
