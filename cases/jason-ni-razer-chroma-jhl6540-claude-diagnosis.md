# Razer Core Chroma X：Jason Ni让Claude读BadLLP日志，退TB2后称缓解掉线

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-28
阶段：待验证

2026年10月28日03:13:26（北京时间），Jason Ni（@njy1991）回复Razer，称TB3协议下约每秒200个BadLLP错误，负载时超过每分钟30,000直至致命掉线；Claude认为可能是Intel JHL6540控制器固件或芯片问题。补查同日03:03与03:06父串，作者称疫情GPU涨价时购Razer Core Chroma X，激烈游戏会掉线卡死，换三块GPU及多根线仍无效，闲置多年，降为TB2连接后解决，并建议用Claude看链路日志。

这是AI辅助设备协议排障，不是固件已反编译、修补或Intel确认设计缺陷。没有主机/系统/固件版本、原始日志、线材参数、重复负载测试或TB2设置细节，无法独立核验错误率、因果和修复稳定性。全部数值与缓解来自作者；不要把模型的两个假设变成产品缺陷定论，REA未提及。本合集未操作eGPU。

候选快照0赞、10浏览、0转发；200/秒与逾30,000/分钟未经独立测量。

## 来源

- [Jason Ni的BadLLP与Claude诊断候选，2026-10-28](https://x.com/i/status/2115159956689129755)
- [补充父帖：Razer外置显卡盒掉线与TB2缓解，同日03:03](https://x.com/i/status/2115157442531062066)
- [补充父串：建议Claude读取链路日志，同日03:06](https://x.com/i/status/2115158155818586183)

[English](en/jason-ni-razer-chroma-jhl6540-claude-diagnosis.md) | [返回目录](../README.zh-CN.md)
