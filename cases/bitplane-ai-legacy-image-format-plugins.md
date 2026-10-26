# Amiga .info与旧图像格式：bitplane报告给Pillow等补充读取支持

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-24
阶段：待验证

davidsong（@bitplane）在2026年10月24日17:05:27（北京时间）的AI成果清单中，报告为Pillow、MediaInfo、ImageMagick等添加Amiga .info格式支持，另列Pillow插件处理Windows MetaFiles、ZX Spectrum dump加载画面、Atari DEGAS、AMOS abk及netpbm的40多种格式。用途是让现有图像工具读取历史文件，而不是重新生成图片。

作者明确Windows MetaFiles工作尚不包含EMF，不应扩大支持范围。帖子未给样本、解析规则、测试或上游PR，AI归因只到清单整体，没有具体模型与REA证据。补读amigainfo的公开README，最后修改于2026-03-16、早于本窗口，确认它是读取、保存及转换五代图标的独立Python包，含Pillow插件，不等于上游已经合并。

这里记录作者格式兼容工作，不确认三个上游均已集成、覆盖所有文件变体或通过恶意输入安全测试；未安装插件或打开目标文件。

EMF明确未支持；40多种netpbm格式及上游支持均据作者，未核验PR或样本。补充amigainfo文档列五代图标及Pillow插件，是独立包而非上游合并证明。

## 来源

- [bitplane的旧图像格式与Pillow插件清单，2026-10-24](https://x.com/i/status/2113919789886218477)
- [补充amigainfo README，最后修改2026-03-16](https://github.com/bitplane/amigainfo/blob/627948384e2cc47e7f36477c91fb9aafd3abec0a/README.md)

[English](en/bitplane-ai-legacy-image-format-plugins.md) | [返回目录](../README.zh-CN.md)
