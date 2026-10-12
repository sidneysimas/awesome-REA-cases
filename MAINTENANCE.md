# 维护方法

## 单一数据源

`data/cases.json` 是唯一需要编辑的案例集合；`cases/*.md`、`categories/*.md`、`README.md`、`LEADS.md`、`docs/index.html` 均由 `scripts/build.py` 生成。脚本仅用 Python 标准库，无服务、数据库或 API 密钥。

## 流程

发现来源 → 确认原作者和目标 → 阅读具体操作与结果 → 去重 / 分类 → 写简短背景与事实 → 验证数据及生成页 → PR 人工审阅 → 合并。

- 不只因帖子热度高就收录；没有完成证据的放 `leads`。
- 旧记录的抓取快照保持历史口径；重新核实后才更新记录日期与热度。
- 优先查阅项目验证记录，状态可变的 PR 不写成永久状态。
- 定期人工检查链接及主要成果声明，建议每月一次；本次没有创建机器人、服务器定时任务或自动发帖。
- 对有争议的声明，注明作者报告或降为线索；纠错走 Issue / PR，不删除证据边界。

## 自动检查

GitHub Actions 在 push、PR、每周及手动触发时验证字段、重复 ID / 来源集、HTTPS 链接格式、生成文件同步及单元测试。只使用只读权限，无第三方服务密钥。

CI **不**确认外部链接可访问，不**复现**软件或独立证明作者成果。特别是 X 的登录、限流和反爬响应，不能当成链接已失效。人工来源核验与自动格式检查必须分开。

## 本地命令

```bash
python3 scripts/build.py
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

## 发布与版权

仓库为公开 Markdown 集合；HTML 在 `docs/index.html`，可下载后直接打开。本次不依赖 GitHub Pages 或外部主机。

MIT 许可只涵盖本项目原创摘要、数据整理与代码，不能用于授权链接中的游戏、软件、源代码或资产。案例的复现需要使用合法获得的目标；本项目不分发这些目标。
