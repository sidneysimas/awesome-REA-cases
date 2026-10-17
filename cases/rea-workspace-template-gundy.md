# REA Workspace Template：把原件、分析副本与证据分开的工作区

分类：应用与客户端 · REA
记录日期：2026-10-18
阶段：相关项目

2026年10月17日23:05（北京时间），Gundy（@Gundy886）发布REA Workspace Template，针对AI逆向时难以分清直接观察与推测、原件易被修改、跨会话丢失进度的问题。模板以一个目标一个工作区组织target原件、work副本、notes证据与prompts任务；结论标CONFIRMED/GUESS，附源码行号、函数地址或抓包位置；导入生成SHA-256基线，修改在副本进行，并留重命名与交接记录。支持源码、APK、原生、JS/Electron、HAR和未知格式流程，原帖称首轮最多深入30个函数。

补读dobest1024/rea-workspace-template的README和2026年10月17日VALIDATION记录：项目提供Claude Code和Codex的项目级MCP配置；脚手架复制样本而不执行，HAR脚本生成仅保留结构的分析副本。记录称12项标准库测试通过，REA 6.4.0握手healthy，合成JS静态分析以及一条合成POST HAR的脱敏后读取通过。它没有验证真实APK/native目标、真实业务HAR完整匿名化、API客户端联调或重启后的Claude/Codex UI接入。

仓库明确0444与客户端规则不是不可绕过的沙盒，SHA基线本身不是防篡改存储，脱敏仍需人工检查主机、路径与字段名。不可把模板测试变为真实软件成功逆向或强隔离保证。补读源码仓库与文档用于确认可公开查阅的实现和边界；最新提交fc15b9a4ba2a8b40510d19a2dd80209f665711c5发表于同日22:43。本合集未执行模板、安装REA或运行其测试。

候选发布：2026-10-17 23:05；仓库提交22:43，北京时间；验收文档原日期2026-10-17。
12项测试、MCP握手和合成JS/HAR分析为项目内部记录，本合集未重跑。
不承诺真实目标效果、完整匿名化或不可绕过隔离；真实APK/native与客户端UI接入待验证。

## 来源

- [候选：Gundy 发布工作区模板与使用约定](https://x.com/i/status/2111473593305682203)
- [公开模板：项目配置与保护边界](https://github.com/dobest1024/rea-workspace-template)
- [项目验收记录：合成样本与未验证项](https://github.com/dobest1024/rea-workspace-template/blob/fc15b9a4ba2a8b40510d19a2dd80209f665711c5/docs/VALIDATION.md)

[English](en/rea-workspace-template-gundy.md) | [返回目录](../README.zh-CN.md)
