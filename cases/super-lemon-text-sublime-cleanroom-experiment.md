# Super Lemon Text：Claude Code按行为描述重建Sublime式Rust编辑器

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-29
阶段：进行中

2026年10月29日03:03:09（北京时间），Lemonator32称受AI逆向游戏讨论启发，做了Sublime Text的clean-room重实现实验。同作者回复将其命名为Super Lemon Text。按名称补查到lemonator32/super-lemon-text；固定提交67de7002e8f96f1cd7c8c68e7c99f3e897db9b1f的README称这是Claude Code按行为描述制作的Rust编辑器，没有接触原软件代码、二进制或自带内容。这是行为重建，不是反编译得到Sublime源码；隔离方法与法律合规未独立审计。

项目自报Windows上M0–M8完成，涵盖编辑、多选、设置、标签/分栏、会话/项目、语法、导航、构建与独立进程Python插件；macOS/Linux、打包、性能门禁与打磨仍待完成，原作者已停止开发、开放接续。测试覆盖文档区分自动、手工与忽略测试，并列UTF-16、拼写检查、部分键位、图像预览等未完项目，日语IME与死键脚本未运行。README的500毫秒启动、16毫秒输入和60fps是性能目标，不能当本合集测量。

补查API确认该精确提交有2026-10-29 01:13:55开始且结论success的CI记录；这是项目CI状态，不证明全面功能等价、所有测试未跳过或本合集复现。仓库10月24日已创建，当前提交在10月29日01:13:52，均早于候选帖子；不把发帖时间当开发开始。未执行目标或下载依赖。

候选快照0赞、11浏览、0转发；补充仓库和CI用于核实实现与测试边界，不是额外窗口候选。

## 来源

- [Lemonator32的Sublime重建实验，2026-10-29](https://x.com/i/status/2115519757319544858)
- [同作者补充项目名Super Lemon Text](https://x.com/i/status/2115519759299031484)
- [固定提交README：Claude Code、clean-room与未完成状态](https://github.com/lemonator32/super-lemon-text/blob/67de7002e8f96f1cd7c8c68e7c99f3e897db9b1f/README.md)
- [同提交测试覆盖及未运行/未完成项目](https://github.com/lemonator32/super-lemon-text/blob/67de7002e8f96f1cd7c8c68e7c99f3e897db9b1f/docs/test-coverage.md)
- [精确提交的成功CI记录，非本合集复现](https://github.com/lemonator32/super-lemon-text/actions/runs/40733708962)

[English](en/super-lemon-text-sublime-cleanroom-experiment.md) | [返回目录](../README.zh-CN.md)
