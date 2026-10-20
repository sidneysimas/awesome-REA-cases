# Android API Extraction Skill：从界面调用链追到 HTTP 接口

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-20
阶段：相关项目

10月20日05:10（北京时间），@mobileossfinds介绍Android Reverse Engineering & API Extraction这一Claude Code Skill，沿Activity／Fragment、ViewModel、repository追踪至HTTP调用。补取原帖图片替代文字确认仓库是SimoneAvogadro/android-reverse-engineering-skill，不是已收录的newliver666/apk-reverse。

补读公开master分支README，项目使用jadx及可选Fernflower／Vineflower分析APK、XAPK、JAR、AAR，要求Java JDK 17+；组织安装包预检、Manifest结构检查、Retrofit／OkHttp等接口提取和Kotlin元数据名称恢复。文档也列Ktor、Apollo GraphQL与Koin相关模式，以及Windows PowerShell实验性支持。用途是授权分析中整理接口及其调用路径，不是已恢复某款商业App的后端。

GitHub元数据给出的最近推送为10月12日16:15（北京时间），是早于本轮的补充项目背景，不冒充新发布。README关于典型App约100%恢复特定Kotlin类名的说法未附本次可核对样本，本合集不将它泛化为所有R8混淆都可还原。未安装Skill、下载APK、提取凭据或执行项目脚本；仅确认文档与项目身份。

## 来源

- [Niko的调用链Skill介绍与仓库截图](https://x.com/i/status/2112290204320981036)
- [项目README：工作流与实验性平台支持](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md)

[English](en/android-api-extraction-claude-skill.md) | [返回目录](../README.zh-CN.md)
