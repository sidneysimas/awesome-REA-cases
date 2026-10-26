# animation-reverse-engineering：Claude Code按帧拆解参考动效再实现交互

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-26
阶段：相关项目

往期待补审候选于2026年10月25日18:50（北京时间）介绍animation-reverse-engineering为逐帧拆解并重写视频的Skill，与同帖motion2code为两个独立项目。公开仓库搜索定位scriptscrypt/animation-reverse-engineering；所读README对应最新062cf5047b7c02c9c2e3c2cd7d85c70bdb410e49，提交时间2026年7月31日15:26:21 UTC，是更早的补充项目文档，不当本轮发布日期。

项目让Claude Code从X视频、Dribbble作品或屏幕录制研究动画时间、顺序和缓动，再实现交互。文档给出采集、探测、接触表和局部帧堆叠的dissect.sh流程，references细分采集、分析、framer-motion移植与验证；要求每项时间与缓动决定能追溯到测量帧，并用相同帧做截图对照，避免仅凭观感猜测。README列两个完整案例，分别为文字扫动时间轴与延时摄影scrubber交互。

这是有公开工作流与示例的AI参考行为重建工具，而非二进制反编译器。文档仍把更多移植目标、自动差异量化、像素保真评分及弹簧/贝塞尔拟合列为扩展方向，不能写成现成功能。作者强调学习动作技术而非一比一复制品牌身份，不据此作法律保证。REA未提及。本合集未安装Skill、运行采集脚本、观看示例或测量还原程度，不确认production一词代表独立验收。

与motion2code为独立项目；文档含两个案例，测量与截图验证未由本合集重跑。
自动差异量化、像素评分及曲线拟合仍是扩展方向；REA未确认。

## 来源

- [往期待补审：逐帧动效重建Skill清单，2026-10-25北京时间](https://x.com/i/status/2114308490848338261)
- [补充公开README，固定062cf50，2026-07-31 UTC](https://github.com/scriptscrypt/animation-reverse-engineering/blob/062cf5047b7c02c9c2e3c2cd7d85c70bdb410e49/README.md)

[English](en/scriptscrypt-animation-reference-frame-dissection-skill.md) | [返回目录](../README.zh-CN.md)
