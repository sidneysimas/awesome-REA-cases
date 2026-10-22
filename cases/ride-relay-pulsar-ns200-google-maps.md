# Ride Relay：OpenCode与DeepSeek把Google Maps转向提示送到Pulsar NS200仪表

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-22
阶段：待验证

待补审候选原发于2026年10月22日15:55:21（北京时间），属于12:00至16:00窗口，不计为16:00至20:00新抓取。Manovikram K（@manov_ik）称用OpenCode与DeepSeek V4.1 Flash Free构建和调试Android应用，结合逆向与蓝牙协议，已在实车工作。

本次补查同串15:55:17的根帖和15:55:19的功能说明，确认目标为Bajaj Pulsar NS200摩托车仪表。官方Bajaj应用已有导航，但作者想使用Google Maps，因此让OpenCode帮助研究官方应用，做独立的Ride Relay。它读取Google Maps导航通知，提取转向方向与距离，转为仪表期待的蓝牙数据包再发送；作者称无需root或修改官方APK。它是通知到仪表的桥接，不是将整个Google Maps移植进车机，也不是电单车项目。

来源未给协议字段、抓包、仓库正文、固件版本、通知权限配置、兼容车款列表或实车日志；Free是作者采用的模型名称/档位，不是可持续免费保证。作者附Use at your own risk，结果仅为自报实车可用。REA未被提及，本合集未安装应用、连接车辆或验证骑行安全。

候选原发2026-10-22T15:55:21+08:00；补充串原发同日15:55:17、15:55:19，均属往期窗口。

## 来源

- [待补审候选：DeepSeek、OpenCode与实车可用自述](https://x.com/i/status/2113177372178759943)
- [补充同串根帖：Bajaj Pulsar NS200与Google Maps目标](https://x.com/i/status/2113177358220079353)
- [补充同串：Ride Relay的通知与蓝牙桥接](https://x.com/i/status/2113177366969422029)

[English](en/ride-relay-pulsar-ns200-google-maps.md) | [返回目录](../README.zh-CN.md)
