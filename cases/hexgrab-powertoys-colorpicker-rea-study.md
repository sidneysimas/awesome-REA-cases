# hexgrab：Claude/REA研究PowerToys取色器，九项论断中一项只对了一半

分类：应用与客户端 · REA
记录日期：2026-10-29
阶段：分析测试

2026年10月29日16:50:03（北京时间），Mukesh Murugan（@iammukeshm）报告用一天通过Claude Code与REA研究Microsoft PowerToys Color Picker，不先读源码，再写自己的.NET10取色器hexgrab。补读同作者仓库固定提交511c58078776af4fb0d2e3601e098f98e9f90c9a的README及docs/rea-findings.md；提交时间10月12日22:35:07Z，研究文档标10月12日，属于早于本窗口的补证，不把此次发帖当实际开发日。

研究针对PowerToys0.98.0的托管ColorPickerUI.dll与原生ColorPicker.dll，文档记REA6.4.0、Ghidra12.1.4。作者先调查托管类型、调用边界，再在原生DLL中查字符串、交叉引用与伪代码，导出证据。首次字符串命中只是日志包装，需上溯调用者；Ghidra的带库名前缀导入也使一次名称查引用失败。作者随后以公开源码评分：九项中八项完全正确；所谓原生模块拥有热键仅部分正确，实际是runner注册、模块响应，runner未在分析目标内。这是作者对有限论断的评分，不是通用准确率或本合集独立对照。

hexgrab公开实现Win+Shift+H取屏幕像素并复制HEX，采用定时轮询以捕捉静止鼠标下的动画颜色，并重试剪贴板；刻意不复制PowerToys修改系统光标方案的设计。项目称无NuGet依赖、含注释不足750行C#，只提供HEX，暂无历史、放大镜或设置。公开端到端脚本描述热键、点击吞掉、取消、回车、钩子卸载与颜色变化检查，但本合集没有运行。

README只称一台显示器、125%缩放实测，混合DPI多屏未实机验证；发行文件未签名，不能据有下载入口保证安全。作者称未复制PowerToys代码，公开源码只用于评分；这是其归因与许可说明，不是法律保证。本合集未下载可执行文件、安装目标依赖或复现桌面测试。

候选快照12赞、630浏览、2转发；一天为作者工时说法，源码提交与研究早于窗口。
8/9完全正确，1项部分正确；源码评分和桌面测试未独立重跑，发行未签名、混合DPI多屏未实测。

## 来源

- [Mukesh报告PowerToys研究与hexgrab，2026-10-29](https://x.com/i/status/2115727855669641216)
- [补充：10月12日固定提交的hexgrab README、实现范围与限制](https://github.com/iammukeshm/hexgrab/blob/511c58078776af4fb0d2e3601e098f98e9f90c9a/README.md)
- [补充：PowerToys0.98.0的REA研究与九项作者评分，10月12日](https://github.com/iammukeshm/hexgrab/blob/511c58078776af4fb0d2e3601e098f98e9f90c9a/docs/rea-findings.md)

[English](en/hexgrab-powertoys-colorpicker-rea-study.md) | [返回目录](../README.zh-CN.md)
