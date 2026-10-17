# NJFE：Claude 借前人协议研究，把耳镜变成电脑 USB 检查镜

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-17

10月17日08:29（北京时间）的候选以七项 AI 构建串为入口，补读08:29:51回复识别为 NJFE（Not Just For Ears）。本轮按名称查到 WildweaselMS/NJFE，阅读 README 和提交元数据：项目10月10日已有实现与英文文档，早于本轮窗口，作为补充来源而非新抓取帖子。它让 ESP32-C3 接入 Soulear 耳镜 Wi-Fi，以 i4season UDP 协议接收 JPEG，再经 USB 串口送到 Python 电脑界面，用于电子与机械检查，不必在手机安装原厂 App。

项目称研究、协议实现、桥接固件、电脑工具、测试与文档均在 Claude Code 对话中完成；人负责想法、硬件、真机测试与决策。但 README 明确承认 rbeilvert/otoscope 的既有协议实现是蓝图，不能把传播帖“从手机 App 逆向”的简写改写成 Claude 独自首次破解协议。项目报告 Hopefox Find T／HKV41B 一台设备、Windows 测试、480×480 JPEG 约17 fps，提供照片、录制、旋转与 LED 控制。

这些是项目自报，并非本合集运行：没有安装依赖、刷桥接板或连接相机。相机本身 Wi-Fi 仍开放且协议无认证，隔离桥接不能消除无线近场访问风险；其他相机兼容只是预期。该工具不是医疗器械，不应把电脑画面用于诊断或治疗。

项目报告只测一台 Hopefox Find T；没有本合集独立复现。
GPL-3.0-or-later，协议实现源自 GPL otoscope；未确认 REA。

## 来源

- [本轮候选：AI 构建汇总入口](https://x.com/i/status/2111253121204994318)
- [补读同串：NJFE 耳镜具体项目](https://x.com/i/status/2111253320170164278)
- [NJFE README：Claude 参与、前人归因与限制](https://github.com/WildweaselMS/NJFE)
- [10月10日文档提交，早于候选窗口](https://github.com/WildweaselMS/NJFE/commit/992866c6609f8c813f459ff79840cf04d5883f8e)

[English](en/njfe-claude-ear-camera-usb.md) | [返回目录](../README.zh-CN.md)
