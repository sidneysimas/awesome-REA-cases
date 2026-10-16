# DexSQL：让 Agent 用 SQL 查询 APK 与 DEX 的调用关系

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-16
阶段：相关项目

10月16日的工具清单推荐 LSPosed/dexsql-release：让 AI Agent 用 SQL 查询 Android APK / DEX 的类、方法、字符串与调用关系，减少反复人工浏览。补读项目 README 确认同一可执行文件提供 CLI 与 MCP，Agent 可组合签名、字符串和调用条件，并读取 Smali；输入在本地解析且不修改，但结果是否发给模型取决于 AI 客户端设置。项目以约372 MiB 的 QQ 9.3.55 APK 做八类查询对照，列出结果集检查、超时与缓存条件，并承认 DexDec 在该次重复调用者查询中更快。这是项目自己的基准记录，不是本合集复跑，也不证明自动恢复原始源码。特别注意：核心 DexSQL 为闭源二进制，使用 DexSQL Binary License 1.0；安装 Skill、文档和基准材料另以 MIT 发布，不能因有公开 GitHub 仓库就称整个工具开源。README 是补充项目资料，不冒充本窗口作者新测量；本合集未下载或执行二进制。

证据：本窗口推荐帖及补读项目 README；项目自报基准，未执行。
许可区分：核心闭源二进制；公开 Skill、文档与基准材料为 MIT。
补充README最近提交：e9c89eae180895c8ae7b24da01fa219c58233775，2026-10-15T12:41:41Z；早于本窗口，仅用于核对项目范围与许可。

## 来源

- [10月16日工具清单中的 DexSQL 推荐](https://x.com/i/status/2110962000675434613)
- [LSPosed 项目说明、基准边界与许可](https://github.com/LSPosed/dexsql-release)

[English](en/dexsql-agent-apk-query.md) | [返回目录](../README.zh-CN.md)
