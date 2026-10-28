# OpenRemoteAssistant：RC003-MS遥控器麦克风接入Mac与Windows的预发布项目

分类：硬件与设备互通 · 未确认使用 REA
记录日期：2026-10-28
阶段：相关项目

2026年10月28日18:29（北京时间）的比较帖将OpenRemoteAssistant与MI-AO、SayAll区分：只适配小米RC003-MS，Mac/Windows都是开发测试预发布；Windows10有开发机记录，Windows11未实测，需VB-CABLE，由输入法转写。作为同帖列出的独立设备互通相关项目保留，不把另两项的Codex或Whisper方法套给它。

补读ru-gong/OpenRemoteAssistant公开README：用途是将小米蓝牙遥控器2Pro的按键与麦克风接电脑作语音输入、语音编程和web coding，应用本身不做语音转文字。Mac0.2.10（Apple Silicon/macOS26）用Swift/SwiftUI、CoreBluetooth/CoreAudio及OpenRemoteAudio虚拟麦克风；Windows0.3.1 x64用C#/.NET9、WinRT BLE与NAudio，VB-CABLE为可选另许可组件。Windows10 build19045的开发测试记录不代表干净系统或全设备验收，两平台独立发版，Win版不替代Mac版。

文档明确RC003-MS设备自报RC003，其他遥控器不承诺兼容；使用须保持助手运行，Windows关窗退出，Mac可驻留菜单栏。Mac不保存录音，Windows默认不存、可选本地WAV。源码GPL-3.0-only，第三方组件保留许可。候选与README都未说明模型参与协议研究；AI是用途背景，不能认定AI辅助逆向已成立。未独立安装、录音、配对或测系统兼容性，REA与模型未知。

共享候选快照1赞、18浏览、0转发；Windows10开发记录非Windows11或全平台验收，AI逆向参与未知。

## 来源

- [候选：OpenRemoteAssistant预发布范围与输入法边界，2026-10-28](https://x.com/i/status/2115390370095800483)
- [补充：OpenRemoteAssistant公开README，10月28日读取](https://github.com/ru-gong/OpenRemoteAssistant)

[English](en/openremoteassistant-rc003-computer-microphone.md) | [返回目录](../README.zh-CN.md)
