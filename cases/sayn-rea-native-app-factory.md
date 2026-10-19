# sayn：从 Play Store 功能与 APK 规格生成自己的 Android App

分类：应用与客户端 · REA
记录日期：2026-10-20
阶段：进行中

10月19日22:20（北京时间），@EShishniashvili 介绍sayn：连接手机，在Play Store选择应用或描述需求，让Claude Code或Codex生成自己的原生App；也参考商店差评改进功能。作者以健身、习惯、格式转换和语言学习工具为背景，称可在5至10分钟内替代许多付费工具，跨App共享记忆仍是下一步。时间与替代能力是作者说法，并无具名生成样本的验收记录。

补查公开Ersho/sayn的5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc提交（10月19日19:20，北京时间，早于候选窗口）README及backend/vibe/codex.py、playstore.py，确认本地FastAPI与Vite控制台、Expo/React Native模板、构建签名APK后ADB安装的设计。默认参考商店文案、截图和评论；可选APK模式固定REA 6.7.0与JADX，提示Agent分析活动、导航和数据模型，先写inspiration/spec.md，再实现。APK获取失败会回退为商店资料，不能把每次生成都称作逆向。源码所见为同一Agent先分析再构建的提示词约束，并非隔离的clean-room团队；不复制代码、名称或资产是项目规则，不是法律保证。

README称支持Windows/Linux x64，首个构建约10分钟、后续约5至7分钟；本地运行仍会把Agent对话发给模型提供商。补查工作流接口未返回Actions运行记录，未安装依赖、下载目标APK、构建App或连接手机。本合集只做静态阅读，不确认功能等价、隐私隔离、任意订阅可替代或5分钟交付。

10月19日候选快照0赞、15浏览、0转发；传播低不影响具体项目收录，非性能验证。

## 来源

- [作者介绍sayn、REA接入及共享记忆计划](https://x.com/i/status/2112187204676018577)
- [较早提交的公开README：架构、时间与平台范围](https://github.com/Ersho/sayn/blob/5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc/README.md)
- [同提交codex.py：REA配置与先规格后构建提示词](https://github.com/Ersho/sayn/blob/5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc/backend/vibe/codex.py)
- [同提交playstore.py：APK可选及失败回退](https://github.com/Ersho/sayn/blob/5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc/backend/vibe/playstore.py)

[English](en/sayn-rea-native-app-factory.md) | [返回目录](../README.zh-CN.md)
