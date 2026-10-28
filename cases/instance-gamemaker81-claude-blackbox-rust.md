# Instance：按黑盒规格用Claude重建GameMaker8.1的Rust编辑器与引擎

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-28
阶段：进行中

2026年10月28日18:24（北京时间）的候选转述HN上的Instance项目：作者从GameMaker8.1入门编程，后来用Claude Opus5.5按黑盒观察写出的规格，在Rust中重建旧引擎与IDE。报道说主体一上午完成、剩余怪癖磨了三周，包括事件顺序、随机数算法和sound_isplaying落后实际音频的行为；这些是报道的工时和模型归因，不是本合集测量，标题一上午不能代替三周的完整工作口径。

补读groverburger/instance公开README与CLEANROOM.md，仓库称从文档、.gmk/.gm81工程数据和黑盒观察写spec，再由实现者按spec编码，禁止反汇编、反编译或调试YoYo Games二进制及复制资产。README列可视化编辑器、GML解释器、3D、粒子、TCP/IP多人和包括32位在内的DLL调用，完整IDE与player可编译WebAssembly，浏览器示例包括Spelunky Classic；不是在网页里反编译原游戏。项目解释Spelunky用的是Derek Yu公开工程的修改版，以内置声音替代supersound.dll；示例游戏不受引擎MIT许可统一覆盖。

所读仓库master为10月27日提交cac87f1f4b166e07b729c181c96f1b4e0888df97，早于本轮报道，只作项目背景。文档声明Windows、macOS与浏览器支持，Linux尚不支持、源码构建可能可用；未独立构建、运行网页、DLL或黑盒测试，也没有完整行为覆盖率。代码与规格公开不证明全套GameMaker等价，更不认证报道所谓一人加模型便法律合规的净室团队；法律边界须单独评估。REA未被指明。

候选快照0赞、155浏览、0转发；一上午、三周与Opus5.5按二手报道，未复测。

## 来源

- [Instance／Claude黑盒重建的二手报道，2026-10-28](https://x.com/i/status/2115389109187367266)
- [补充：公开Instance仓库](https://github.com/groverburger/instance)
- [10月27日固定README：功能与平台边界](https://github.com/groverburger/instance/blob/cac87f1f4b166e07b729c181c96f1b4e0888df97/README.md)
- [项目净室输入与隔离政策](https://github.com/groverburger/instance/blob/cac87f1f4b166e07b729c181c96f1b4e0888df97/CLEANROOM.md)

[English](en/instance-gamemaker81-claude-blackbox-rust.md) | [返回目录](../README.zh-CN.md)
