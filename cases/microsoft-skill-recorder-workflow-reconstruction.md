# Microsoft Skill Recorder：由录屏与操作事件重建可复用Agent技能

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-25
阶段：相关项目

2026年10月25日12:25:54（北京时间），TechVerser（@realfxw）介绍Microsoft Skill Recorder，把人完成任务的一次操作记录转为可重复执行的Agent技能。这里重建的是应用操作工作流，而非反编译应用二进制；作为更广义AI辅助行为重建的相关项目收录。

10月26日补读microsoft/skill-recorder公开README，固定到9月21日提交b05d59036182e897e1a60e90651e775cf5f97e8d。项目描述本地捕获屏幕、窗口切换、浏览器路径、剪贴板预览、可选录制终端和语音讲解，以GitHub Copilot CLI重建任务意图与有序步骤，供用户编辑，再生成SKILL.md或定时／触发Automation。它优先调用原生CLI/API工具而非回放固定点击坐标；将一次表单示例泛化为批处理是项目设计目标，不是本合集完成的实验。

隐私边界不能省略：录制、存储、帧提取和可选Whisper转录在本机进行，但点击Analyze后会把事件时间线、提取图像、转录文本与受限终端输出发到GitHub云端处理。敏感信息检查和技能预览不等于安全保证。README以macOS为主要目标，并说明Windows 11 x64/ARM64支持。未安装程序、录屏或执行生成技能，未独立核验跨平台能力、泛化准确率及数据脱敏效果；帖子中的平台兼容说法不扩展为已验证集成。

相关行为重建工具，不是二进制反编译案例；未安装或运行。
本地录制不等于离线分析；Analyze上传数据，预览与扫描不保证安全。

## 来源

- [TechVerser介绍Skill Recorder，2026-10-25](https://x.com/i/status/2114211826493714625)
- [补充：9月21日提交的微软项目README](https://github.com/microsoft/skill-recorder/blob/b05d59036182e897e1a60e90651e775cf5f97e8d/README.md)

[English](en/microsoft-skill-recorder-workflow-reconstruction.md) | [返回目录](../README.zh-CN.md)
