# SayAll：把小米蓝牙遥控器改接电脑语音输入的相关项目

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-28
阶段：相关项目

2026年10月28日18:29（北京时间）的同一比较帖介绍SayAll：以Mac为主，Windows首个preview支持小米遥控器2与2Pro，语音输入仅支持微信输入法。它与MI-AO的本地Whisper直送Codex不是同一链路，而是让遥控器成为电脑语音输入设备。候选没有作者逆向日志，按设备互通与AI开发相关项目保留。

补读HD838A/remote-mic-app公开README，SwiftUI Mac应用将BLE语音遥控器变无线麦克风，需兼容虚拟麦克风或BlackHole等回环设备，并由所选输入软件负责识别；Windows预览仍以基本功能为主。文档说明AI开发工具token用于持续开发，不能因此断言AI发现了协议或参与每一段实现。项目最初fork自nijez/open-voice-bridge，兼容麦克风命名和USB transport方案参考MiRemoteVoice，驱动从BlackHole源码派生，不抹去前人工作。Mac代码/驱动GPL-3.0-only，品牌图像另有授权，iOS另属私有仓库。

文档将多步动作、按App方案和记录回眸/只读MCP列为候选或仍需真实环境验收，不把配置入口当全面验证。回眸默认关闭，不保存音频；第三方AI客户端可能上传已读取的文字。当前README另列不同平台与芯片要求及部分会员功能，不认定所有功能免费或通用。未独立验证性能、公证、设备范围或Windows语音路径，也未安装驱动或配对；REA未指明。

共享候选快照1赞、18浏览、0转发；AI开发参与不等于已证实AI辅助协议逆向。

## 来源

- [候选：SayAll与另两种遥控器输入链路比较，2026-10-28](https://x.com/i/status/2115390370095800483)
- [补充：SayAll源码README、来源与测试边界，10月28日读取](https://github.com/HD838A/remote-mic-app)

[English](en/sayall-xiaomi-remote-voice-bridge.md) | [返回目录](../README.zh-CN.md)
