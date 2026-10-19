# Android CarPlay AI box：把四个 Claude 终端显示到停车后的车机屏幕

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-19
阶段：相关项目

10月19日21:16（北京时间）的回复提供完整方案提示词：使用自有Ottocast、Carlinkit Tbox或类似Android CarPlay AI box，先研究iPhone渲染与车机显示的边界，再把笔记本上四个Claude Code进程组成tmux网格，经有密码的本地ttyd网页由盒子浏览器展示。动机是在车机屏幕查看和切换Agent，工具配置预期使用ADB、同一热点及屏幕授权，而非逆向或越狱iPhone。

提示词要求先确认确有Android盒子，否则停止；备份设置、保存撤销命令，不触碰CarPlay服务、导航、倒车影像、CAN总线及其他安全应用，只在停车时操作，不root或刷固件。这些是设计约束，不是已经通过的安全测试。没有盒子型号实测、源码、录像或运行日志，四Agent终端展示是验收目标而非完成结果，REA未明示。与BMW iDrive任意App推广是不同技术前提，不能替其证明五分钟突破白名单。

## 来源

- [Android AI box展示Claude终端的完整方案提示词](https://x.com/i/status/2112170918914977851)

[English](en/android-carplay-box-claude-terminal-idea.md) | [返回目录](../README.zh-CN.md)
