# jshook：给AI Agent按需搜索与加载逆向工具的MCP工作区

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-26
阶段：相关项目

2026年10月26日01:56（北京时间），Dan Kornas（@DanKornas）介绍jshook，针对AI Agent逆向Web应用时一开始就塞入大量MCP schema、占用上下文的问题，先开放可搜索的小工具面，调查需要时再升级至workflow或full配置。作者是在介绍项目，不据此归为仓库开发者。

补充查到公开仓库vmoranv/jshookmcp，其README与候选的search-first、profile-aware及AGPL-3.0描述一致。读取的固定提交abbbd40e49435c71859718c0f6ecf791a9af3e4b提交于10月25日17:12:19北京时间，早于候选窗口；用来说明项目设计，不当本轮新发布。文档描述Chromium/Camoufox的CDP驱动、WebSocket/HTTP/GraphQL与Burp桥接、JavaScript反混淆与source map重建、WASM反汇编、Frida/Ghidra/IDA等原生分析桥接，以及可热加载插件和声明式工作流。

README把search元数据估为约3K tokens，full的735工具约109K tokens，并明确测量日期为10月10日、需随目录增长重测。这是项目自报的配置开销，不是独立模型效率基准；本记录不据此声称检出率更高、无source map时恢复成功或任意应用可逆向。没有指定真实目标的分析/重建验收记录，本合集只静态阅读介绍和文档，没有安装、接浏览器、调用目标工具或运行测试；REA不是此项目的已确认引擎。按相关AI逆向工具项目收录。

相关工具项目，未运行；候选介绍者不等于仓库作者，REA引擎未确认。
约3K/109K tokens及735工具是README注明10月10日测量的自报快照，不是独立效果基准。

## 来源

- [Dan Kornas介绍jshook搜索优先工作区，2026-10-26北京时间](https://x.com/i/status/2114415785720623360)
- [补充公开项目README，固定提交abbbd40，2026-10-25](https://github.com/vmoranv/jshookmcp/blob/abbbd40e49435c71859718c0f6ecf791a9af3e4b/README.md)

[English](en/jshookmcp-search-first-re-workspace.md) | [返回目录](../README.zh-CN.md)
