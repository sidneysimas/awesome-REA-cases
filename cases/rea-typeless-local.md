# Typeless：用 REA 做本地语音输入替代品

分类：应用与客户端 · REA
记录日期：2026-10-13
阶段：待验证

一位 Mac 用户报告，因 Typeless 免费额度下降，使用 Claude Code 通过 REA 分析该 Electron 语音输入应用，并制作名为 REATypeless 的本地替代品。作者称分析发现原应用客户端处理快捷键、录音与粘贴，语音识别和文本处理依赖服务器；其替代实现改用 whisper.cpp large-v3-turbo 量化模型和 Ollama/Qwen2.5 3B，并加入润色、翻译及选中文本改写功能。帖子报告约 2.9GB 常驻内存，以及五秒语音约两至三秒出字等体验，但未提供代码或独立功能/性能测试，因此这些结果均为作者自述；不能据此认定完整复刻 Typeless。

Another poster reports using Claude Code over half a day to build Saydra, a Windows voice-input alternative. Claimed features include local offline SenseVoice recognition (about 0.3 seconds), optional Groq Whisper large-v3, Qwen text polishing, translation, and selected-text rewriting. The poster says Chris used REA to reverse engineer Typeless; this is a retelling, not evidence that the poster personally used REA, nor independent confirmation of Chris's identity or original project details. Saydra's features and performance are unverified.

作者报告已完成个人 Mac 上的本地应用；未公开代码，未独立验证功能或性能。
原帖注明仅供个人学习与技术研究，不分发、不售卖。
2026-10-14: Another developer reports building Windows alternative Saydra with Claude Code; REA use is attributed to @Chris62771610 and is not independently verified.

## 来源

- [作者的 REA 分析与本地替代品报告](https://x.com/i/status/2109971905336037671)
- [Saydra author's report and retelling of Chris's REA work](https://x.com/i/status/2110386418929594439)

[返回目录](../README.md)
