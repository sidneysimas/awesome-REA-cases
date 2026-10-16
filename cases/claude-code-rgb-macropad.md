# GAMEKB-K17 宏键盘：用 Claude Code 逆向配置协议

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-15

Denis Darkin（@dvdarkin）报告用不到 40 美元的 16 键 RGB 宏键盘辅助日常 AI 编程，以 /model、/clear、yes 回车和 continue 回车等固件宏替代重复输入。他称用 Claude Code 逆向键盘配置协议，不再依赖厂商网页。补查公开仓库 gamekb-k17 的 README，目标为 GAMEKB-K17 / HCY-K017（USB 0816:0220）；项目从厂商 WebHID 配置器研究协议，提供按键映射、宏、RGB 与布局配置。文档说明配置写入键盘闪存后读回核验，断开配置程序后仍保存在设备内，并附协议文档。仓库自述 Windows 已测，其他 hidapi 平台未测；本合集只阅读文档，没有安装、运行工具或连接硬件，不把项目自测升级为独立复现。

发帖：2026-10-15 09:22（北京时间）
候选快照：7 赞｜399 浏览｜0 转发
仓库创建于 2026-10-15；README 平台测试范围为项目声明。

## 来源

- [作者本轮 Claude Code 辅助逆向报告](https://x.com/i/status/2110541828097462605)
- [公开实现及配置/协议文档（本轮补查）](https://github.com/dvdarkin/gamekb-k17)

[English](en/claude-code-rgb-macropad.md) | [返回目录](../README.zh-CN.md)
