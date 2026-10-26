# Motion2Code：让编程Agent把参考动效视频重建为可编辑SVG与GSAP

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-26
阶段：相关项目

往期待补审帖子于2026年10月25日18:50（北京时间）在视频工具清单中分别介绍motion2code和animation-reverse-engineering。本轮通过公开仓库搜索找到lovisdotio/motion2code；所读README对应仓库最新提交0f003288997604487df04c1b7a0586900d3e36bb，提交时间为10月20日04:21:50 UTC，属于候选之前的项目材料，不是本轮新发布。它面向希望从参考视频恢复可编辑动效、或把模拟网站录屏做成真实交互网页的编程Agent。

项目要求先每0.25秒抽帧，结合硬切附近帧、接触表、颜色和循环检测研究参考，再以SVG形状和单一GSAP时间轴实现；页面暴露seek(t)以定点渲染。frame_diff生成源视频与代码的并排图及差异分数，check_anim检查页面契约、无嵌入视频/栅格图、运行错误和循环接缝；这些是项目设计与自带检查，不是本合集复现结果。网站方向还使用ScrollTrigger及实际按钮/键盘交互，不只是播放录屏。

README列六个示例：字体、眼睛转场、节日地图、天气雷达、贴纸作品集和播客播放器；说明源视频由MiniMax H3 Max在fal生成，重建由Claude Opus 5.5配合该Skill完成，每目录有源片、HTML和同步比较页。这为具体重建实践提供公开产物入口，但本合集只静态阅读文档，未播放、逐帧检查、运行脚本或验证网页交互。高分辨率和小文件为项目主张，不当性能基准。REA未提及；不与其他视频重建项目合并，也不把清单中的普通剪辑工具一并收录。

往期补审；公开六个AI重建示例及比较页，未独立运行或核验相似度。
参考视频到SVG/GSAP及交互网页；逐帧测量是项目方法，不证明任意视频可精确重建，REA未确认。

## 来源

- [往期待补审：视频工具清单中的两个独立重建Skill，2026-10-25北京时间](https://x.com/i/status/2114308490848338261)
- [补充Motion2Code公开README，固定0f00328，2026-10-20 UTC](https://github.com/lovisdotio/motion2code/blob/0f003288997604487df04c1b7a0586900d3e36bb/README.md)

[English](en/motion2code-svg-gsap-reference-video-rebuild.md) | [返回目录](../README.zh-CN.md)
