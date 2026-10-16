# REA 6.4.0：Windows 下的 .NET 与 Electron 样本测试

分类：应用与客户端 · REA
记录日期：2026-10-15
阶段：分析测试

本轮长帖以第一人称描述在 Windows + Node 24 下测试 npm REA 6.4.0，未装 ILSpy/dnSpy；另一个候选注明测评来自论坛作者“神奇的人鱼”，因此不把传播账号自动当作原测试者。帖子称检查约 200 个 .NET Framework 程序集：1701 方法的样本可解，System.DirectoryServices.dll 的 2094 方法样本失败，System.Activities.dll 出现元数据完整而成员不可用的差异。作者将其归因于 JSON 中间表示的 64 MiB 预算，并报告文档中的 --type 在该 npm 版本不可用。这是特定版本与样本的实测报告，不把约 2000 方法当成所有程序集固定阈值；原文对 Windows 能力比例的数字不一致，本条不沿用该比例。

同帖称用 AI 构造 Electron 风格样本，包含 BrowserWindow、IPC handler、原生 .node 插件及条件动态 require；REA 输出 24 个语义节点和 33 条边，能定位 IPC 与原生插件，并把无法静态判断的依赖标为 unknown。续帖另报告 Trap.dll 中的写文件静态构造函数未执行，以及对仅差一个常量的两个程序集准确定位变更方法。目标是检验静态结构分析、资源限制和版本比较，而不是复刻整款商业软件。样本、命令原始输出和完整测试环境未由本合集独立核验；不能据单一 Trap.dll 测试保证所有工具链绝无副作用。

版本口径：npm 6.4.0，Windows + Node 24；测试为帖子报告。
两条候选各 1 赞，属于同一测评的主帖与续帖，非独立重复实验；不沿用星数、代码行数或安全性绝对宣称。

## 来源

- [本轮长帖：Framework 与 Electron 样本测试](https://x.com/i/status/2110563764886266167)
- [本轮续帖：Trap.dll 与程序集变更比较](https://x.com/i/status/2110565455039799441)

[English](en/rea-640-windows-managed-electron-test.md) | [返回目录](../README.zh-CN.md)
