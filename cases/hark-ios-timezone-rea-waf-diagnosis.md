# Hark iOS对话加载故障：REA定位timezone与WAF冲突的作者报告

分类：应用与客户端 · REA
记录日期：2026-10-28
阶段：待验证

2026年10月28日10:28:53（北京时间），xxxxxx（@xxx_cccv）报告Hark iOS端加载不出对话，称原因是请求会话时带timezone参数，被Cloudflare WAF拦截，而网页不带所以正常。作者感谢REA逆向分析，建议用Loon或圈X重写请求、去掉该参数，并附配置图。补查确认署名与图片附件，未核验图片具体配置。

目标是在不重写整个客户端的情况下理解移动端与网页的请求差异，恢复会话读取。没有Hark版本、完整请求/响应、WAF日志、规则、配置文本或修复后对照；因果与解决办法都是作者报告，不是本合集确认的Cloudflare规则缺陷或所有用户通用修复。不推断绕过身份认证、获取他人会话或Hark服务端已修复。REA明确参与分析，未给所用模型；与研究Hark Agent框架的既有案例不是同一故障目标。未访问账户、发送重写请求或运行客户端，保留unverified。

候选快照0赞、310浏览、0转发；WAF归因与去参数修复未独立测试。

## 来源

- [Hark iOS timezone故障与REA归因，2026-10-28](https://x.com/i/status/2115269542159224846)

[English](en/hark-ios-timezone-rea-waf-diagnosis.md) | [返回目录](../README.zh-CN.md)
