# 贡献指南

欢迎提交具体的 REA / AI 辅助逆向案例。只需修改 `data/cases.json`，然后运行 `python3 scripts/build.py`。

## 收录要求

- 讲清楚具体软件、设备、游戏或算法是什么，首次出现的代号和术语给出背景。
- 写清楚作者为什么逆向、具体做了什么，以及报告了什么结果。不要添加猜测用途、泛泛启发或抽象总结。
- 至少一个公开来源；优先作者原帖、源码、验证记录和真实演示。明确区分作者自述、项目测试与独立复现。
- `rea` 使用 `REA`、`other-ai` 或 `unknown`，不确定就不要猜。
- 所有条目统一进入主目录。`status` 使用 `case`（普通条目，不表示独立验证）、`unverified`（待验证）、`in-progress`（进行中）、`analysis-test`（分析测试）或 `related-project`（相关项目）。
- 同项目追加来源，不重复开条目；不同目标有不同成果时可单独收录。
- 仅发布原创摘要与链接，不提交原软件、受版权保护的资产、凭据、私人材料或未经授权的数据。
- 热度与工时只写有来源的值；热度必须注明快照日期。不要求每个案例都有热度。

## 数据格式

所有必需字段及示例见 `data/cases.json`。每条必须包含 `en.title` 与 `en.summary`，用于生成英文 README；不设置 Top N 或固定收录数量。分类使用 `games` / `hardware` / `apps` / `algorithms`。

1. 新增或更新记录，保留已有 ID。
2. `python3 scripts/build.py`
3. `python3 scripts/build.py --check`
4. `python3 -m unittest discover -s tests -v`
5. 提交 PR。标题示例：`Add case: siri-remote-linux`。

PR 描述写明：公开来源、目标、作者操作、结果证据、是否使用 REA。更新已有记录时说明更正原因。维护者人工审阅通过后合并；CI 通过不代表案例已被复现。

如链接失效，优先补作者的新链接或有时间戳的公开归档，保留来源变更说明，不悄悄改写历史结果。
