# Samsung电视语音遥控：Codez称Opus研究局域网API后接入Grok Bot

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-22
阶段：待验证

2026年10月22日22:07:18（北京时间），Codez（@0xCodez）称用Opus 5.5研究自己的Samsung电视，让Grok Bot充当语音入口，达到说一句话即可打开Netflix并浏览的效果。其具体方案是由Claude Code根据电视信息研究同一家庭网络内的遥控接口，编写只包含打开Netflix、移动、选择三项操作的小遥控，再作为插件接入Grok Bot；电视端需用户允许连接。

这里的目标是把已有的局域网遥控能力接到语音Agent，不是移除电视DRM、替换固件或破解Netflix。作者称近几年多数Samsung、LG与Google TV都可用，但没有给具体电视型号、固件、协议、插件代码、提示词正文、测试日志或跨品牌演示，不能把宣传范围当成实测兼容表。

本次补查原帖确认作者与视频附件信息，未播放核验视频、连接电视或运行插件。没有声明使用REA；Opus的逆向角色和运行效果均来自作者自述，保留unverified。

作者原发2026-10-22T22:07:18+08:00；三项工具与多数品牌兼容均为原帖说法，未独立验证。

## 来源

- [Codez：Opus研究Samsung遥控与Grok Bot插件自述](https://x.com/i/status/2113270979476545573)

[English](en/codez-samsung-opus-grokbot-netflix-remote.md) | [返回目录](../README.zh-CN.md)
