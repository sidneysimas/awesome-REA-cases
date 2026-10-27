# chardet 7：Claude辅助重写编码检测库，兼容API与许可争议需分开看

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-25
阶段：分析测试

2026年10月25日14:48:01（北京时间），Srimugunthan Dhandapani（@Srimugunthan_D）以Python编码检测库chardet为具体例子，讨论Claude Code重写是否构成clean-room：转述维护者重写、原作者反对与约1%相似度辩护。ArtCraft和REA只作为争论背景，不是该作者另做的实验。补查原帖确认署名与完整正文。

随后静态阅读chardet/chardet的865f09baa68378850af723db73707fb1bf3e084d提交README（提交于10月24日23:26:34北京时间，早于候选）。它明确Dan Blanchard在2026年用Claude从头重写chardet 7，并以相同包名和公开API替代5.x／6.x；实现描述为13阶段检测流水线，结合BOM、magic number、结构探测、字节合法性筛选和bigram统计模型。目标是重建编码识别功能并降低替换成本，不是取得原始源码。

需要更正二手许可表述：候选说从LGPL转MIT，该固定README及许可标识实际为0BSD。README称后续代码不派生自原版，这是项目方立场，不是本合集法律结论；未取得原作者完整异议、相似度工具和约1%的测试口径。训练可能接触公开源码既不能证明具体输出侵权，也不能保证clean-room合法性。

README报告3138文件上99.7%准确率、编译版比6.0.0快359倍，属于项目自己的测试主张；未下载语料、安装依赖、执行目标代码或复跑基准，不能将其当独立验收、全部输入等价或法院认证。保留analysis-test，REA未提及。

候选快照1赞、29浏览、0转发；后续热度不倒填。
3138文件、99.7%与359倍为固定README的项目测试数据；约1%相似度仅候选转述，未重跑。
候选MIT说法与固定README的0BSD不符；许可标签不是重写法律独立性的裁定。

## 来源

- [候选及原帖补查：Srimugunthan的chardet clean-room讨论，2026-10-25](https://x.com/i/status/2114247590850261264)
- [补充项目README：Claude重写、API、0BSD与测试口径，固定10月24日提交](https://github.com/chardet/chardet/blob/865f09baa68378850af723db73707fb1bf3e084d/README.md)

[English](en/chardet7-claude-encoding-detector-rewrite-license-dispute.md) | [返回目录](../README.zh-CN.md)
