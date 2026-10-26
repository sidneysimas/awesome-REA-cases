# Windows HLP：bitplane报告AI辅助解析器、转换器、库与TUI

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-24
阶段：待验证

2026年10月24日17:05:27（北京时间），davidsong（@bitplane）列举AI帮助完成的项目，其中一项是Windows HLP解析器、转换器、库与终端界面。目标是恢复旧帮助文件的读取与转换能力；过程艰苦为作者描述，无实际工时。未点名模型或REA。

补读winhlp公开README，最后修改于2026-09-26，早于本窗口。它明确是基于Manfred Winterhoff、Ben Collver、Paul Wise等人的helpdeco源码派生的纯Python实现，以GPLv2发布，不能描述成从零黑盒恢复。文档列WinHelp 3.0、3.1、Windows 95和MediaView .mvb，输出JSON或可浏览HTML，终端可搜索与导航；约6500真实帮助文件验证及helpdeco文本对照为项目报告。

本合集未运行程序或对照脚本，未核查语料或输出完整性；保留未验证，不把支持清单当所有历史文档可无损转换，也不将前人的helpdeco成果归于本次AI。

基于既有helpdeco源码，非从零黑盒恢复；约6500文件验证为项目声明，未独立执行。

## 来源

- [bitplane的Windows HLP项目自述，2026-10-24](https://x.com/i/status/2113919789886218477)
- [补充winhlp README，最后修改2026-09-26](https://github.com/bitplane/winhlp/blob/9e84faf7f3beb232b96685f56af761f824928b0b/README.md)

[English](en/bitplane-ai-windows-hlp-reader.md) | [返回目录](../README.zh-CN.md)
