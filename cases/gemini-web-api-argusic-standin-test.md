# Gemini Web To API：Agent 仅对替身服务做安装测试

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-18
阶段：分析测试

10月18日06:30（北京时间）的候选介绍 ntthanh2603/gemini-web-to-api，并报告 Argusic Agent 在干净机器上、无人协助地测试固定提交3633170：安装至首次启动2分钟，全程18分钟，未遇错误，评分92/100。引述的 Agent 结语称安装 Go 1.27.2 后构建成功，4981端口 /health 返回HTTP 200，9套测试、85余子测试通过；虚假 cookies 的 Gemini 认证按预期失败。帖子明确所有测试只对替身服务，未访问真实 Gemini。

补读该固定提交的公开 README，确认这是用网页会话 cookies 将 Gemini 网页接口桥接为 OpenAI、Claude、Gemini 兼容 REST 接口的 Go 项目，并明确警告账号风险及可能不符合 Google 条款。此补充文档是固定版本的用途说明，不是窗口内新增实测。未执行项目、安装其依赖或使用账号。这里记录 Agent 检查逆向接口实现的有限结果，不能把构建与替身通过当成真实 Gemini 认证、生成、配额处理或长期稳定性通过；也未证明原协议逆向由 AI 完成，REA 未确认。592星是候选的项目介绍值，不另作实时核实。

2分钟、18分钟、92/100及9套85余子测试为报告值；只测替身服务，无真实Gemini验收。
补充文档提交3633170的作者及提交时间均为2026-09-14 05:07:02 UTC；仅用于确认项目用途，不是10月18日新增实测。

## 来源

- [Argusic 安装与替身测试报告](https://x.com/i/status/2111585716195004425)
- [补充：9月14日固定提交3633170的项目说明](https://github.com/ntthanh2603/gemini-web-to-api/blob/3633170/README.md)

[English](en/gemini-web-api-argusic-standin-test.md) | [返回目录](../README.zh-CN.md)
