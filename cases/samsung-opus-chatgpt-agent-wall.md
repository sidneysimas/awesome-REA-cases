# Samsung 电视显示六个 Claude Agent：Opus 研究本地遥控，ChatGPT 语音开墙

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-22
阶段：待验证

2026年10月22日01:25（北京时间），Codez（@0xCodez）报告让Opus 5.5研究自己的Samsung电视如何接受局域网命令，再用ChatGPT语音打开六个Claude Code窗口的显示墙。笔记本运行tmux中的六个Agent，并以网页供电视浏览器显示；电视和笔记本同Wi-Fi，首次连接由用户在电视上Allow。作者称所示设备运行Smart Hub，并声称适用于多数Tizen电视，但没有给型号、固件或兼容矩阵，不把它当作普遍支持。

同串完整提示词说明要研究WebSocket8002本地遥控接口，以samsungtvws打开URL，用tmux的3×2布局与ttyd端口7681提供带口令的局域网页。提示词要求不root、不刷固件、不侧载，只改笔记本端，先保存状态与撤销方法。语音触发拟用只有open_claude_wall一个无参数工具的MCP，经受令牌保护的Cloudflare Tunnel接到ChatGPT自定义连接器；如果套餐或语音模式不能调用则退回笔记本本地唤醒词。这些是提示词中的实现要求，不能据此证明连接器、口令、撤销或安全隔离已被实际验证。

作者称找到loophole，但正文使用既有本地遥控库和需用户配对的API，没有漏洞编号、未知协议捕获或绕过认证证据；不将其升级为Tizen漏洞或AI在电视本机运行。没有公开仓库、运行日志或语音连接器测试，视频附件的存在不等于本合集独立复现。归因是Opus/Claude与ChatGPT；虽然末尾推广逆向文章，不能据此确认实际调用REA。

主帖候选快照78赞、6086浏览、1转发；来源更新2026-10-22T01:25:45+08:00。

## 来源

- [Codez：Samsung电视、笔记本六Agent与语音控制报告](https://x.com/i/status/2112958529988669742)
- [作者同串完整提示词：接口、网页与连接器的要求和回退](https://x.com/i/status/2112958534363021398)

[English](en/samsung-opus-chatgpt-agent-wall.md) | [返回目录](../README.zh-CN.md)
