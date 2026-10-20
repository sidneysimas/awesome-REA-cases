# Kimi Slide / PPTD：Rust 编译器二开，让 Agent 离线编辑与导出幻灯片

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

10月20日07:36（北京时间），shiquda（@shiquda123321）称比较7个公开的Agent幻灯片Skill，认为逆向Kimi Slide的方案最好。作者解释PPTD以声明式YAML描述页面，再经编译器输出PDF、PPTX、PNG等，以缓解LLM直接编辑OOXML的困难；此前找到的版本依赖逆向官方前端导出器，PPTX导出不可用。

作者称这几天在公开Rust PPTD编译器上二次开发，补充符合PPTD规范的功能并优化Skill，可完全离线使用，还支持把其他来源PPTX反转为PPTD再编辑。目标明确是Agent可用的幻灯片创作及格式互通，不是Kimi模型逆向。

帖子给两个短链与截图，未取得可确认仓库、提交日期、测试文件或规范覆盖表。7个方案的比较是个人评估，没有同题评分；离线可用、PPTX往返和新增功能均为作者报告，未安装或运行，不保证动画、字体、布局与原文件无损。REA未明示。

## 来源

- [shiquda的PPTD编译器二开与离线Skill报告](https://x.com/i/status/2112326934139203659)

[English](en/kimi-pptd-rust-offline-agent-skill.md) | [返回目录](../README.zh-CN.md)
