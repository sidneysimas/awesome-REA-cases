# Google Home本地接口：marfinxx称Claude审计Eureka并改本地控制

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-27
阶段：待验证

2026年10月27日21:00:02（北京时间），marfinxx（@marfinxx）称Claude Code/Opus5.5检查Google Home的8008端口和Cast日志，无密码取得路由器及四邻居网络BSSID/MAC、蓝牙配对线索、运行时间、Eureka配置token与固件日志，并将夜间Nest显示屏唤醒归因于20kHz超声。未给型号、响应样本、信号测量或时间线；接口字段不能直接证明访客完整历史、六英尺定位或全屋布局。

作者称三分钟关闭超声提示而保留离线唤醒、将灯和插座改接本地Matter/Thread、生成Script Editor YAML和回滚JSON，延迟1500ms降至18ms。没有设置差异、兼容清单、脚本或前后测量，不认可生产可用、零风险或普遍适用；所附提示词混有检查和写入，不能因写着read-only认定安全只读。

原帖补查确认作者与全文。按局域网行为研究/改造的unverified报告收录，不认定固件完整反编译或已证隐私泄漏，REA未提及；未访问设备、扫描网络或执行提示词。

候选快照28赞、537浏览、1转发；三分钟、20kHz和1500到18ms未经独立核验。

## 来源

- [marfinxx的Claude/Google Home主张，2026-10-27](https://x.com/i/status/2115065987959529951)

[English](en/google-home-claude-eureka-audit-report.md) | [返回目录](../README.zh-CN.md)
