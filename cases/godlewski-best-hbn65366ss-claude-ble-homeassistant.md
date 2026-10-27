# BEST HBN65366SS抽油烟机：Claude协作抓包纠正GATT缓存误判，接入Home Assistant

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-27
阶段：进行中

2026年10月27日02:50:08（北京时间），Steve Godlewski（@stevegodlewski）报告用AI研究BEST抽油烟机、接入Home Assistant。补查作者串称基于前人工作且已推送上游；公开godlewski/esphome-best-hood-hbn65366ss README明确与Claude Code共同研究、编写配置和文档，并逐步在自有设备测试。补充源码和日志是10月24日至25日的研究材料，不冒充本轮新抓取帖子。

目标为Best by Broan HBN65366SS，固件4.2.2／1.1.20，以ESP-WROOM-32运行ESPHome，经本地BLE替代厂商云端控制路径。作者复用WheapLabs的唤醒广播和无bond加密配对，不把前人难点归自己首创。最初ESP32看不到灯光档位和延时关闭特征，误判该型号没有功能；静态搜索BEST Kitchen Android应用Hermes bundle后仍未完成反编译映射。最后用Android 12手机关闭网络并单独连接设备抓Bluetooth HCI，再解析ATT，看到54个特征和应用对21026/21050的写入。ESP-IDF默认缓存40个，配置CONFIG_BT_GATTC_MAX_CACHE_CHAR为100后恢复缺失特征，日志明确保留并纠正原误判。

项目报告风扇四速、灯光四档、SmartSense、延时关闭与本体按键状态双向同步。21050写0是立即停风扇，不是取消延时继续运行；延时自然结束时长仍待检查。只测试一台HBN65366SS，ESP32占BLE时手机App改走云端，不说两者同时用BLE。抓包原文件因含网络名未发布，有解析器与脱敏日志，不能称独立复现。

补查WheapLabs PR #5确认godlewski提交的缓存修正于10月25日00:53:33 UTC合并；PR报告ESPHome 2026.10.0配置校验与自有设备运行，未测试未修改文件在HBN1306SS/WCS1306SS上。原仓库28e1e1d772c55d9f94bb485854cb75e9608c2b0e的README和日志可追溯。未运行配置、抓包或设备；REA未提及，保持进行中作者实测实现，不作通用安全认证。

候选快照4赞、101浏览、0转发；补充GitHub资料原日期早于本窗口。
54是该设备特征数，40是默认缓存上限，100是修正配置；不代表100功能或100设备验证。

## 来源

- [本轮候选：Steve报告BEST接入HA，2026-10-27北京时间](https://x.com/i/status/2114791707011379640)
- [补充作者串：基于前人并推送上游，2026-10-27北京时间](https://x.com/i/status/2114791712199729238)
- [补充公开README：Claude参与与单设备边界，2026-10-24提交](https://github.com/godlewski/esphome-best-hood-hbn65366ss/blob/28e1e1d772c55d9f94bb485854cb75e9608c2b0e/README.md)
- [补充构建日志：GATT误判、HCI抓包及修正，2026-10-24](https://github.com/godlewski/esphome-best-hood-hbn65366ss/blob/28e1e1d772c55d9f94bb485854cb75e9608c2b0e/docs/LOG.md)
- [补充上游PR #5：缓存修正及项目测试，2026-10-25合并](https://github.com/WheapLabs/ESPHome-Best-Hood/pull/5)

[English](en/godlewski-best-hbn65366ss-claude-ble-homeassistant.md) | [返回目录](../README.zh-CN.md)
