# ReaCut：研究剪映本地行为，制作独立视频编辑器

分类：应用与客户端 · REA
记录日期：2026-10-15
阶段：进行中

@zoozoo_ai本轮说正在用REA逆向剪映并邀请贡献，链接Xiangyu-CAS/rea-capcut。与已有Mehal的CapCut编辑器不是同一项目。10月15日补查仓库10月13日研究和验证文档：作者用REA6.4.0检查macOS剪映11.0.12922包、被动观察新建项目和自造素材时间线，区分组件/字符串存在与真实行为，首轮不透明草稿不能直接认定为已支持格式。独立实现使用自己的项目格式和FFmpeg导出，不把商业素材、原二进制或完整原生调用图作为已恢复成果。验证记录报告293项通过、1项缺libx265跳过，以及隔离环境下实际安装包导出中文、混音视频和插件协议测试；Codex侧栏可见获用户确认，但完整宿主流程、跨平台与首次CI失败尚有边界。v0.5.0仅本地ad-hoc签名的Apple Silicon预览包，未公证。本合集仅阅读项目记录，不把作者验收升级为独立复现或跨平台CI全绿。

本轮候选为进行中邀请；10月13日文档是追溯补证，不是本窗口新完成结果。

## 来源

- [本轮作者贡献邀请](https://x.com/i/status/2110633692834222460)
- [项目源码](https://github.com/Xiangyu-CAS/rea-capcut)
- [10月13日研究边界（补充来源）](https://github.com/Xiangyu-CAS/rea-capcut/blob/main/docs/research/REA_FINDINGS.md)
- [10月13日项目验证记录（补充来源）](https://github.com/Xiangyu-CAS/rea-capcut/blob/main/docs/VALIDATION.md)

[返回目录](../README.md)
