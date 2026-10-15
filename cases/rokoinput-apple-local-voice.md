# 洛克输入法：研究 Typeless 后用苹果端侧能力做本地输入

分类：应用与客户端 · REA
记录日期：2026-10-15
阶段：进行中

@slashui因担心输入法收集个人信息，用REA研究国外语音输入工具，作者串将其与Typeless比较，并公开bassnova42/rokoinput。与已有whisper.cpp/Ollama版REATypeless不同，本项目使用苹果Speech框架和InputMethodKit，不带第三方ASR或大模型。10月15日补查README：0.4.0才强制端侧识别，不支持则停止而非回退云端；系统准备语言资源可能联网，设备与语言有条件，不能沿用帖子中Mac不挑机型的笼统说法。文档也明确文字历史默认开启、明文且不自动过期，可关闭但不会自动删除旧记录。只有源码与本地构建脚本，未独立验证真实麦克风、全局快捷键和流量；自定义许可仅限个人非商业使用，不称MIT或自由商用开源。

候选快照：3赞｜432浏览；读取公开文档，不代表实机验收。

## 来源

- [作者报告与回复](https://x.com/i/status/2110610758212145408)
- [公开源码及隐私、版本边界](https://github.com/bassnova42/rokoinput)

[English](en/rokoinput-apple-local-voice.md) | [返回目录](../README.md)
