# 米遥MI-AO：Codex协作研究遥控器BLE，把按住说话送入Mac任务

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-28
阶段：进行中

2026年10月28日18:29（北京时间）的候选将MI-AO、SayAll和OpenRemoteAssistant分开介绍：米遥把小米蓝牙语音遥控器2 Pro接到Mac，按住语音键录音，松开后本地Whisper转写，再提交当前Codex任务。候选明确只有项目方报告固件2671的端到端验证，不是遥控器本身运行模型。三项目各自成条，不互借兼容性或测试。

补读fanxeon/mi-ao公开README，作者FanXeon@Poemcoder明确Codex作为AI工程协作者参与代码、测试、文档与调试；协议基于Google ATV Voice over BLE调研，不是独占协议的从零发现。链路是BLE ATVV v0.4/v1.0、IMA/DVI ADPCM、16kHz PCM/WAV、本地whisper.cpp与Codex辅助功能树；只有唯一可用输入区才自动发送，其他情况回退复制。文档报告小米2Pro固件2671、ATVV1.0、16kHz/120B验证，未覆盖其他遥控器。

所读文档为V2/0.2.2、macOS14+、source-first beta，无Windows/Linux支持，用户本机构建ad-hoc签名App。文档同时保留0.2.2菜单栏与连接策略待安装版真机验收，以及长时间、多显示器、登录启动和部分按键压力验收；不要把核心语音链路通过扩大为所有功能已验证。录音与文字本地保存不是不留数据；转写本地也不改变文本随后交Codex处理的边界。源码MIT，REA未提及。本合集未安装、配对、读BLE或发送Codex任务，硬件测试均为项目报告。

共享候选快照1赞、18浏览、0转发；不当任一项目独立热度。
已报告设备为2Pro固件2671；0.2.2部分安装版验收仍待完成。

## 来源

- [三种小米遥控器AI输入方案的候选比较，2026-10-28](https://x.com/i/status/2115390370095800483)
- [补充：MI-AO公开README、Codex归因与硬件边界，10月28日读取](https://github.com/fanxeon/mi-ao)

[English](en/fanxeon-mi-ao-xiaomi-remote-codex.md) | [返回目录](../README.zh-CN.md)
