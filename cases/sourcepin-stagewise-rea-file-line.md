# sourcepin：用 REA 研究 stagewise，把网页元素先定位到源码再交给模型

分类：应用与客户端 · REA
记录日期：2026-10-21
阶段：进行中

2026年10月21日06:19（北京时间），Aayush Swami（Aayushswamidev）称用 REA 研究 stagewise 后制作 sourcepin：用户点击自己开发中的网页元素、描述修改，工具先找出源码位置，再让 AI 读写该文件。作者称精确快照加定位需86毫秒。

补查 sourcepin 的6c72ecef提交（10月21日05:27，北京时间）：v0.1 README 与研究笔记说明目标是开源 stagewise 的43c6b252版本，不是无源码恢复。作者直接读源码，并用 REA 6.7.0 生成静态模块／IPC 图和功能追踪；全仓图因1397项资源限制而不完整，聚焦追踪也有部分覆盖。工具通过 React 19 开发构建的 fiber._debugStack 与 Next.js 错误覆盖层接口定位，再检查该行标签；不支持的配置退到静态 JSX 匹配或文本候选，区分 exact、likely 和未知，不声称都精确。

README 报告自制小应用29个元素定位正确，测试环境为 macOS／Chrome、Next.js＋React 19开发模式webpack；Turbopack未测，Vue／Svelte不支持。所读公开 bench JSON 记录同一 gpt-oss-120b 经 OpenRouter 的五个请求，有映射／无映射共十行都正确，工具调用合计10对15、模型步数15对21。文档将整轮平均时间均记为13.4秒，因此不能把步数减少写成整体加速。另与 stagewise 的单次运行使用不同测试页面，Electron截图与headless Chrome设置也不同，不是公平大基准。

公开 AGPL-3.0 代码与证据可读，作者称从零写成且未复制 stagewise 代码；本合集未安装或重跑，未独立验证86毫秒、定位率、安全隔离或代码来源。

## 来源

- [Aayush Swami：stagewise研究与sourcepin发布](https://x.com/i/status/2112670162105376938)
- [sourcepin README：6c72ecef，映射、测量与限制](https://github.com/aayushswami123/sourcepin/blob/6c72ecef36e7f7a713e8f7d2b49ff2c9a6e09908/README.md)
- [静态研究笔记：REA部分图与源码追踪](https://github.com/aayushswami123/sourcepin/blob/6c72ecef36e7f7a713e8f7d2b49ff2c9a6e09908/docs/rea/01-source-map.md)
- [项目五请求映射开关对照原始JSON](https://github.com/aayushswami123/sourcepin/blob/6c72ecef36e7f7a713e8f7d2b49ff2c9a6e09908/docs/rea/evidence/bench-openrouter-gpt-oss-120b.json)

[English](en/sourcepin-stagewise-rea-file-line.md) | [返回目录](../README.zh-CN.md)
