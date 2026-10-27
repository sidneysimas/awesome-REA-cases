# tsrs：AI辅助TypeScript编译器Rust移植的转述与公开兼容性边界

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-22
阶段：进行中

2026年10月22日02:00:34（北京时间）的候选将tsrs描述为Cloudflare发布、由AI生成的TypeScript编译器Rust重实现，转述最高8倍编译速度与70%内存下降。它是将既有类型检查和语言服务迁移到新实现的具体项目，不是泛泛软件终结观点；候选作者身份未确认，AI参与及该两项性能数字仍归因于此转述。

补充静态查到oxc-project/tsrs，其README链接Cloudflare公告，感谢Max Schwenk完成移植、Owner.com赞助初始工作与TypeScript团队支持。因此不将全部作者归于Cloudflare。10月27日10:09:31北京时间的654a7115ad4c85fae72ee363c6d60b4986aebf81提交晚于候选及本轮窗口，仅作后续核对：文档称替代TypeScript 7编译器与语言服务，稳定版对7.1达到100%一致性仍是目标，而非已经普遍等价。

默认模式保持固定上游检查行为，包括检查器数量和文件顺序影响诊断的已知问题；尚未发布的fast模式改变调度、缓存和惰性实例化，可能使诊断及退出状态改变，性能取决于项目。README明确它是TypeScript派生作品、Apache-2.0许可，不能写成无代码来源的clean-room克隆。未取得候选时AI工作日志、模型与原始性能口径，未运行编译器、安装依赖或复跑基准；状态保持in-progress，不独立确认8倍或70%。REA未提及。

候选快照0赞、14浏览、0转发；8倍与70%为二手说法，未独立测量。
补充README晚于本轮窗口，只限制当前叙述，不冒充10月22日或窗口内状态；AI具体分工未由所读README确认。

## 来源

- [往期候选：tsrs的AI重实现与性能转述，2026-10-22](https://x.com/i/status/2112967292866711968)
- [后续补充固定README：作者、兼容性、fast模式与许可，2026-10-27](https://github.com/oxc-project/tsrs/blob/654a7115ad4c85fae72ee363c6d60b4986aebf81/README.md)

[English](en/tsrs-typescript7-rust-ai-port-report.md) | [返回目录](../README.zh-CN.md)
