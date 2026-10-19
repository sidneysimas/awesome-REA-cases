# 《织梦岛》：Claude Code 参与 PC 移植的待验证转述

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-19
阶段：待验证

原综述称《织梦岛》几乎全靠Claude Code重编译到PC。10月15日14:17候选补充LASRecomp项目名及特殊操作会崩溃的边界。随后补查peiikai/LASRecomp公开README，确认目标为2019年Switch版v1.0.0，项目自称静态重编译为Windows、macOS和Linux原生应用；作者明确称几乎全部代码、工具、逆向和文档由Claude Code完成，人类指挥、测试和审阅。该次文档为beta：macOS限Apple Silicon，Linux ARM标实验且未实机测试，已列出查看特定梳妆台和返回标题界面会崩溃等问题。项目不含游戏文件、素材或字体，需用户合法提供原作。本合集未编译或运行，不量化AI贡献比例、不保证完整行为对等；保留已有ID与早期来源，公开文档为此前追溯补证。

10月19日22:45（北京时间）的LEO开源推荐综述再次介绍LAS Recomp，称首次启动在本地完成重编译、支持21:9与按键映射、内置randomizer，macOS使用MetalFX，Windows/Linux用Vulkan，beta地牢偶有黑块。文中列自编译需求为AVX2 CPU、Vulkan1.3、clang、SDL3与Python3.12，并提到iOS fork。新增细节仅为综述转述，不是本合集再次核验当前仓库或跨平台测试；不能将其星数、转引视频热度或显示功能当作稳定性验收。

10月15日转述快照：144赞、24723浏览、16转发；此前公开README确认项目及AI自述，未独立运行。
10月15日18:04新转述称锁60 FPS、内部渲染最高4倍、超过60帧会出问题。本轮重读公开README仅确认可调内部渲染与beta/崩溃限制，未从该文档确认60 FPS或4倍上限；精确值保持转述口径，不当作当前跨平台实测。

## 来源

- [早期游戏移植综述分享帖](https://x.com/i/status/2110565293802274865)
- [本轮LASRecomp转述与崩溃边界](https://x.com/i/status/2110615951075168686)
- [公开项目说明与已知问题（10月15日补查）](https://github.com/peiikai/LASRecomp)
- [10月15日18:04帧率及分辨率设置转述](https://x.com/i/status/2110673058986066332)
- [10月19日LEO开源推荐：LAS Recomp功能与beta限制转述](https://x.com/i/status/2112193333892362570)

[English](en/links-awakening-claude-pc-port-report.md) | [返回目录](../README.zh-CN.md)
