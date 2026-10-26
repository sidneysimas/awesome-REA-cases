# Ricoh GR无线取景器：Codex协作的StickS3固件与分代协议

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-22
阶段：待验证

2026年10月21日至22日，社区帖子介绍Codex辅助的Ricoh GR无线取景器与快门遥控：M5Stack StickS3装在热靴上，横持取景、竖持蓝牙快门，可用M5Burner烧录；一帖称作者把真机串口日志交给Codex排查重连。用途是独立小屏预览与相机遥控，与Ricoh GXR色彩recipe移植idea不同。关于“逆向热靴接口”的转述不能直接当作视频经热靴传输的证据。

10月26日补查找到特征吻合的sky18Dragon/RICOH-GR-Live-View-Shooting，静态阅读10月19日固定提交8c4fc0f的README。项目注明作者与Codex协作开发，M5Burner作者名为TinkerZhang，仓库提供热靴安装结构件。文档说明图像经Wi-Fi的HTTP MJPEG LiveView传输；GR III/IV用BLE配对、WLAN控制及快门，而没有蓝牙的GR II需手动开启Wi-Fi，走官方GR Remote HTTP接口。因此它不是重写整个相机固件，也不能把安装热靴当作图像总线。

该提交文档称GR IIIx、GR IV、GR IV HDF和GR II已实机验证，GR III仍需完整独立回归，GR III HDF/IIIx HDF为缺独立实机证据的实验支持。项目报告Native测试93/93通过、StickS3构建成功、RAM 66,444/327,680字节（20.3%）、Flash 1,455,789/3,342,336字节（43.6%）；这里只核对文档，未重跑测试、编译、烧录或连接相机。自动测试不替代逐型号/固件实机回归。保留unverified状态，区分社区串口调试转述、项目测试自报与本合集静态阅读；旧提交为补充来源，不冒充候选窗口的新发布。

已定位公开项目及Codex协作声明；只静态阅读，逐机型支持和93/93测试均为项目报告。
GR II无BLE，使用官方HTTP接口；GR III/IV另有BLE控制路径，热靴安装不等于图像传输。

## 来源

- [Ricoh GR接口研究转述，2026-10-21](https://x.com/i/status/2112892660251795697)
- [StickS3与烧录方式转述，2026-10-22](https://x.com/i/status/2113242014242287678)
- [Wi-Fi/蓝牙与串口调试流程转述，2026-10-21](https://x.com/i/status/2112738503222349881)
- [10月19日固定提交README：Codex归因、传输路径与测试范围，10月26日补读](https://github.com/sky18Dragon/RICOH-GR-Live-View-Shooting/blob/8c4fc0f768b8a14369b9b2a426d90177d7405efb/README.md)

[English](en/ricoh-gr-codex-sticks3-wireless-viewfinder-report.md) | [返回目录](../README.zh-CN.md)
