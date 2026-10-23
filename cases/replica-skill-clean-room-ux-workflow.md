# Replica skill：从公开页面与自有账号观察应用，再按规格重建的11技能项目

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-23
阶段：相关项目

往期候选原发2026年10月22日19:46:43（北京时间），介绍replica-skill的11技能流程。本次找到Jakeschincariol/replica-skill并阅读公开README与replica-recon/SKILL.md，确认项目由Jake Schincariol制作，面向Claude用户从应用的可观察功能和流程制作自己的实现。REA未提及，不把名字中的逆向等同二进制分析。

技能依次处理观察地图、架构、设计系统、逐屏实现、后端、测试、原版对照、用户差评、品牌、发布文案与部署，交接材料保存在项目replica目录。recon要求先限范围、逐页记录空白／加载／错误／权限状态，给推断数据模型标证据和置信度，把内容库、社交网络及许可证等列为不可复制部分。它限定公开文档、截图、商店说明及用户自己的账号，明确禁止读取目标JavaScript包、反编译二进制、记录网络请求以复制端点或绕过付费墙；这与通用REA扫描路线不同。

README用预约工具示例说明18屏、7流程、86功能分、91布局分与140条评论等预期交付；这是说明性示例，不是已复现项目或实测得分。项目列出六个标准库Python辅助工具，用于布局、功能覆盖、评论、对比度、品牌残留及商店文案检查，但本合集未运行工具或测试。文档中的洁净室、品牌清理与不编造要求是工作流意图，不是运行时隔离或法律合规保证；克隆任意App的宣传不能视作验证结果。

补充资料固定于77c9436fb3d18c3d58169efb8caf4fe906b0dc51，提交日期2026-10-03T12:07:14Z，早于候选，只作为往期项目证据，不冒充本轮新发布。README标MIT；候选17.4% fork率未核验，也不把19天未推送解释为项目失效。保留为related-project，没有安装插件、执行目标代码或部署产品。

候选2026-10-22T19:46:43+08:00，为往期补审；补充项目提交2026-10-03T12:07:14Z。
11技能与六工具来自项目文档；预约工具数字为示例，17.4% fork率未核，工具未运行。

## 来源

- [往期候选：replica-skill流程介绍](https://x.com/i/status/2113235600098890142)
- [项目README（固定提交）](https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/README.md)
- [replica-recon：输入、证据与禁止读取目标代码的规则](https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/replica-recon/SKILL.md)

[English](en/replica-skill-clean-room-ux-workflow.md) | [返回目录](../README.zh-CN.md)
