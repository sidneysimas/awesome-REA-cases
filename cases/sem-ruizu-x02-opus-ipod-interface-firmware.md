# Ruizu X02：Sem称Opus提取固件、重做iPod式菜单并加入小游戏

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-26
阶段：待验证

2026年10月26日17:38（北京时间），Sem（@smgdkngt）报告让Opus把廉价Ruizu X02 MP3播放器改得像iPod 3G。原界面图标网格、翻译不全，左右键滚动而上下键返回，使用不便；作者称Claude重做Chicago字体、iPod菜单、带填充进度条的Now Playing屏幕与彩色iPod风格，并改成上下滚动、左返回、右和中键选择。

作者报告AI通过USB恢复模式从NAND读取整个固件，理解加密更新格式、UI资源、字体和按键映射。原厂升级器拒绝修改固件，因此AI编写ARM刷写payload；对原应用的补丁先在Unicorn模拟器测试。另用C从零编写Tetris、Flappy Bird及六岁儿童学习游戏，在21 KB RAM内运行，并用Mac模拟器运行相同代码。学习内容据称有376个词、OpenMoji图片、Andika字体，支持荷兰语和英语。作者说自己负责真机测试并反馈显示问题照片。

补查原帖确认作者、完整流程与附图存在，但未识别图片内容，也未获得固件版本、源码、NAND镜像、Unicorn日志或真机演示验证。各屏幕修改、刷写和游戏效果均是作者报告，不是本合集复现；REA未提及。不下载或执行payload、不操作播放器，状态为unverified。

21 KB RAM、376词、Unicorn预检与真机测试均为作者报告；固件版本、源码与日志未取得。

## 来源

- [Sem报告Opus改装Ruizu X02固件及游戏，2026-10-26](https://x.com/i/status/2114652825099587639)

[English](en/sem-ruizu-x02-opus-ipod-interface-firmware.md) | [返回目录](../README.zh-CN.md)
