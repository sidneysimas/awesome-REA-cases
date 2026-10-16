# 贡献指南

[English homepage](README.md) | [简体中文首页](README.zh-CN.md)

欢迎提交具体的 REA / AI 辅助逆向案例。修改 `data/cases.json`，然后运行 `python3 scripts/build.py` 生成详情、分类页和完整总目录。首页由维护者亲自判断与编辑，不由生成器覆盖。

## 收录要求

- 讲清楚具体软件、设备、游戏或算法是什么，首次出现的代号和术语给出背景。
- 写清楚作者为什么逆向、具体做了什么，以及报告了什么结果。不要添加猜测用途、泛泛启发或抽象总结。
- 至少一个公开来源；优先作者原帖、源码、验证记录和真实演示。明确区分作者自述、项目测试与独立复现。
- `rea` 使用 `REA`、`other-ai` 或 `unknown`，不确定就不要猜。
- 所有条目统一进入完整总目录 `INDEX.md` 和分类页。`status` 使用 `case`（普通条目，不表示独立验证）、`unverified`（待验证）、`in-progress`（进行中）、`analysis-test`（分析测试）或 `related-project`（相关项目）。未获首页推荐不影响完整收录。
- 同项目追加来源，不重复开条目；不同目标有不同成果时可单独收录。
- 仅发布原创摘要与链接，不提交原软件、受版权保护的资产、凭据、私人材料或未经授权的数据。
- 热度与工时只写有来源的值；热度必须注明快照日期。不要求每个案例都有热度。

## 数据格式

所有必需字段及示例见 `data/cases.json`。每条的 `en` 必须恰好包含 `title`、`summary`、`description`、`metadata`、`source_labels`：前三项为非空英文字符串，`description` 完整翻译中文详情，不能用一句摘要替代；`metadata` 与中文 `metadata` 逐项对应、数量相同（原列表为空时也为空）；`source_labels` 与 `sources` 逐项对应、数量相同，两种列表中的元素均须为非空字符串。URL 只保存在 `sources`，不在 `en` 重复。保留作者归属、日期、数量单位、阶段与全部证据边界，不将转述、静态分析或 idea 升级为已验证成果。

新增或实质修改记录时同步维护完整中英文内容，再生成 `cases/<id>.md`、`cases/en/<id>.md`、两种语言分类页及总目录。中英文详情互链，英文入口直接指向英文详情与 `categories/en/`。生成器校验翻译完整性，缺译时失败，不回退中文或摘要；`--check` 同时检查两种语言详情的过期或孤立文件。中文贡献与维护文档在英文导航中明确标注语言。

不设置 Top N 或固定收录数量。分类使用 `games` / `hardware` / `apps` / `algorithms`。维护者另综合近期传播热度与阅读价值，亲自维护英文默认首页 `README.md` 与中文首页 `README.zh-CN.md` 的近期精选 Top 10、紧凑经典案例、带截止时间的总数及分类数量目录；不使用自动评分或排序算法。

`README.en.md` 仅为静态兼容入口，不作为第三份选编目标；生成器不写入任何一份 README。

English maintenance: update all five `en` fields with every new or changed record, keeping full evidence caveats and aligned metadata/source labels. Keep URLs only in `sources`, regenerate both reading paths, and edit the selected README content by hand.

1. 新增或更新记录，保留已有 ID。
2. `python3 scripts/build.py`
3. `python3 scripts/build.py --check`
4. `python3 -m unittest discover -s tests -v`
5. 提交 PR。标题示例：`Add case: siri-remote-linux`。

PR 描述写明：公开来源、目标、作者操作、结果证据、是否使用 REA。更新已有记录时说明更正原因。维护者人工审阅通过后合并；CI 通过不代表案例已被复现。

如链接失效，优先补作者的新链接或有时间戳的公开归档，保留来源变更说明，不悄悄改写历史结果。
