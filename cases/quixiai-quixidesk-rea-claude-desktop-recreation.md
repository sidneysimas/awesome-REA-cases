# QuixiDesk：Eric Hartford以REA研究Claude Desktop，重建可换模型的Rust客户端

分类：应用与客户端 · REA
记录日期：2026-10-27
阶段：进行中

2026年10月27日09:08（北京时间），Eric Hartford（@QuixiAI）称用morluto的REA逆向Claude Desktop，做出可使用本地或云模型的开源替代品。同日10:50作者明确项目名为QuixiDesk，与T3 Code无关。它也不同于本合集此前收录的Open Claude UI界面细节研究，不能合并成同一作者或实现。

补充阅读QuixiAI/QuixiDesk固定72c9d8836f69cdc7d02372b84b1cf7054bdf2658提交的README及Cargo.toml；该提交时间为10月27日13:34:46北京时间，晚于本候选窗口，仅用于发布后的项目背景核查，不冒充窗口内已实现的功能快照。项目称用REA映射1400多个IPC通道及macOS原生helper协议，以tao／wry和WKWebView替代Electron／Node.js，重建Rust工作空间。README宣称17种模型provider、11种界面语言、内置浏览器／电脑操作与统一任务聊天视图；Cargo清单确认存在Rust工作空间成员声明，不证明这些功能都已实现。

目标是保留桌面交互并解除单一模型供应商限制，而不是复制Claude模型权重。文档要求macOS14或更高、cargo1.80或更高及Xcode命令行工具，不能据此宣称Linux或Windows已可用。README的full feature parity、零配置和安全文件访问均是项目主张；本合集没有编译、运行、逐通道检查或进行权限审计。作者串有人质疑开源链接和工具权限配置，作者请后者提交issue；这些意见不构成已确认漏洞，也不能当功能等价证明。按in-progress收录公开重建项目。

候选首帖快照122赞、4022浏览、13转发；不以补查后的热度替换。
1400多个通道、17种provider与11种语言为项目声明；只读文档和清单，未独立验证兼容、权限或性能。

## 来源

- [Eric Hartford自述REA逆向Claude Desktop，2026-10-27](https://x.com/i/status/2114886957603991752)
- [作者澄清QuixiDesk名称及与T3 Code无关，2026-10-27](https://x.com/i/status/2114912658306814150)
- [补充：窗口后13:34提交的QuixiDesk README](https://github.com/QuixiAI/QuixiDesk/blob/72c9d8836f69cdc7d02372b84b1cf7054bdf2658/README.md)
- [补充：同提交Rust工作空间清单](https://github.com/QuixiAI/QuixiDesk/blob/72c9d8836f69cdc7d02372b84b1cf7054bdf2658/Cargo.toml)

[English](en/quixiai-quixidesk-rea-claude-desktop-recreation.md) | [返回目录](../README.zh-CN.md)
