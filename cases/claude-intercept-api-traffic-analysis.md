# Claude Intercept：把授权 HTTP/S 抓包交给 Claude Code 分析

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-16
阶段：相关项目

往期10月16日19:30（北京时间）的候选在 Ship Systems 项目介绍中列出 Claude Intercept，称可查看解密后的电脑流量和未文档化 API，由 William Haesemeyer 参与制作。此前因 AI 角色与项目地址不明而待补证；现补查到名称和作者匹配的 whaesemeyer/claude-intercept，公开 README 明确定位为 Claude Code 配套 HTTP/S 中间人代理。项目描述本地抓包、实时面板、SQLite 存储、/intercept skill，以及 api-docs、summary、full 等导出方式，让 Claude 研究请求模式与 API，而非只凭产品名推定 AI 参与。

该 README 为本次补充阅读，不当作原候选时点已独立测试的功能。它要求为授权设备配置代理与信任本机 CA，并说明某些证书固定域名会失败、面板绑定0.0.0.0不能放在不可信网络；停止代理后若不关闭系统代理还会影响联网。因此不采用原帖“所有流量都可解密”的泛化。本地存储也不等于送入云模型的内容不会外发。README 许可为 CC BY-NC 4.0，不能把宣传中的开源等同无限商业许可。项目用途和 AI 接口可由文档核对，实际拦截、权限安全、隐私与分析质量未验证；未安装、改代理、导入证书或访问任何凭据，未确认 REA 参与。

补审原窗口为10月16日16:00–20:00，不计作本轮新帖。
仅检查公开文档；CC BY-NC 4.0、证书固定与局域网暴露限制按项目说明保留。

## 来源

- [往期候选：Ship Systems 对 Claude Intercept 的介绍](https://x.com/i/status/2111057177200738632)
- [补充公开 README：Claude Code 集成与安全边界](https://github.com/whaesemeyer/claude-intercept)

[English](en/claude-intercept-api-traffic-analysis.md) | [返回目录](../README.zh-CN.md)
