# Hycli：研究网站接口，为 AI Agent 做可复用 CLI 与 MCP 操作

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-19
阶段：相关项目

10月19日01:54（北京时间），@hybirdssss称把博客、社区等网站研究成供AI Agent复用的CLI，以比Playwright浏览器更少的token操作，并复用登录会话及限制过量抓取。补查GitHub确认Hybirdss/Hycli公开仓库。10月19日补读的main README作为补充项目说明，不倒推其全部功能在发帖时已实现。

README描述根据文档、API schema、公开JavaScript和浏览器观察的请求形状准备带类型CLI/MCP动作，三个AI worker分管读取搜索、工作流与账户证据，失败读操作反馈后修订定义，保留仍可用的旧定义。默认只读，写操作需在本地dashboard开启并对单次具体请求批准；未知效果要求审阅，写入不自动重试。任意浏览器点击序列、multipart上传、二进制下载不在当前合同内；截图注明示例或合成本地服务，不当真实站点兼容性验证。

这些是作者和文档描述，未连接账户、运行目标或重跑CI。没有Playwright对照token基准，安全边界未独立审计，也不承诺任意网站都可自动化；只有授权目标适用。REA未明示，按面向AI的接口研究相关项目收录。

## 来源

- [Hybirdss的网站CLI与AI Agent项目原帖](https://x.com/i/status/2111878567542030824)
- [补充公开仓库：Hycli README与边界](https://github.com/Hybirdss/Hycli)

[English](en/hycli-website-cli-agents.md) | [返回目录](../README.zh-CN.md)
