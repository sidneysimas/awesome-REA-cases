# awesome-openclaw-skills：结构与维护调研

查询日期：2026-10-12。参考仓库快照：`ad6cb6c88a4859aecdcb414edeb11d3065610c6d`。

## 观察到的组织形式

- README 提供简介、使用方法、目录和按领域分组的链接清单。
- `categories/` 提供各分类的独立 Markdown 页，方便直接阅读与分享。
- 条目采用“名称 + 链接 + 简短用途”格式，目标是发现资源，而非托管资源本身。
- `CONTRIBUTING.md` 给出发布前提、来源限制、描述长度、重复项处理、PR 标题与安全要求。
- 维护通过 Issues / PR 完成；此次看到近期连续合并的投稿记录。
- `.github/workflows/pr-check.yml` 在 PR 打开、修改与同步时检查 PR 描述中是否存在 ClawHub 链接；缺失时留言并失败。

## 不能夸大的部分

自动检查只证明 PR 描述存在符合模式的链接，不会独立执行 skill，也不会证明安全状态或社区使用情况。指南中的质量要求仍需要人工审阅。

此次 README、分类页和贡献指南之间存在口径不一致：例如分类页里仍有 clawskills.sh 链接，而贡献规则要求使用 ClawHub；页面声明的条目数也不应直接当作逐项核对后的总数。不能据此推断其未公开的同步脚本、爬取服务或维护后台。

## 本项目采用的形式

- 保留 README 入口、分类列表、短描述、来源链接和 PR 人工审阅。
- 案例比 skill 链接需要更多背景，因此为每条提供独立案例页。
- 用结构化 JSON 生成中英文 README、分类页与案例详情，避免多份计数与内容不同步；按项目现行要求不生成 HTML。
- 将工具归属与成果阶段分开标注。全部条目进入主目录，但未完成、待验证与相关项目不冒充完成成果。
- CI 验证本项目能自动检查的字段和生成一致性，不冒充来源验证。

## 原始来源

- [仓库 README（固定快照）](https://github.com/VoltAgent/awesome-openclaw-skills/blob/ad6cb6c88a4859aecdcb414edeb11d3065610c6d/README.md)
- [贡献规则](https://github.com/VoltAgent/awesome-openclaw-skills/blob/ad6cb6c88a4859aecdcb414edeb11d3065610c6d/CONTRIBUTING.md)
- [PR 自动检查](https://github.com/VoltAgent/awesome-openclaw-skills/blob/ad6cb6c88a4859aecdcb414edeb11d3065610c6d/.github/workflows/pr-check.yml)
- [分类页示例](https://github.com/VoltAgent/awesome-openclaw-skills/blob/ad6cb6c88a4859aecdcb414edeb11d3065610c6d/categories/gaming.md)

本项目只参考组织方法，未复制其目录内容、图片、条目或营销文案。
