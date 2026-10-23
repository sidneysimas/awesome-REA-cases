# Radian Browser：在Orbe基础上用Claude与REA研究Arc手势和界面

分类：应用与客户端 · REA
记录日期：2026-10-24
阶段：进行中

2026年10月23日23:57:01（北京时间），Abdullah Sultan（@amsultan2010）介绍Radian Browser：希望保留Arc的Spaces、命令栏和垂直标签体验，发布macOS/Electron beta，并称支持导入Arc设置。23:54:26的同作者回复补充：Claude在他的Mac上通过REA与Hopper分析Arc，手势部分因此不难。两帖共同构成这个目标的证据，不另拆一个手势案例。

补读公开README发现重要归属与方法边界：Radian是MIT许可Orbe的早期fork，大部分现有功能来自Orbe；自己的工作包括英文菜单、品牌，以及对Arc 1.170布局、颜色与动画的重新测量。README称通过观察运行行为逐帧匹配，不读取Arc代码或复用资产；这与回复中Hopper分析的说法存在未解释的张力，不能将其写成已核验的clean-room保证，也不能说全部浏览器功能由AI从零恢复。

README列macOS 13以上、Apple Silicon优先，尚无Intel构建，发布包未获Apple公证；账号、同步与AI功能目前不提供。原帖把同步、MCP和移动端作为未来方向，不算已实现。轻量、节电、与Arc完全相同以及Arc停运日期均是作者或项目叙述，本次不作独立背书。补充README所查提交e2bd86722d294ab6848072df654a7427c17d4561时间为2026-10-23 16:04:46 UTC，即北京时间次日00:04:46，晚于严格窗口，仅用于补充归属和限制，不冒充窗口内发布。未下载、运行浏览器或核验功能等价。

候选来源2026-10-23，北京时间；补充README提交2026-10-24 00:04:46，北京时间，晚于窗口。
进行中；观察匹配与Hopper分析的关系未澄清，未独立运行。

## 来源

- [作者发布Radian beta，2026-10-23](https://x.com/i/status/2113660978172723603)
- [作者回复：Claude、REA与Hopper分析Arc手势，2026-10-23](https://x.com/i/status/2113660326185218328)
- [补充项目README：Orbe归属和平台限制，窗口后提交](https://github.com/amsultan2010/radian-browser/blob/e2bd86722d294ab6848072df654a7427c17d4561/README.md)

[English](en/radian-browser-arc-rea-rebuild.md) | [返回目录](../README.zh-CN.md)
