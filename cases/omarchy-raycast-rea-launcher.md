# oma-launcher／oma-cast：REA 研究 Raycast 后为 Omarchy 重建启动器

分类：应用与客户端 · REA
记录日期：2026-10-20
阶段：进行中

10月20日03:34（北京时间），@typecraft_dev称数小时用REA做出Omarchy的Raycast式启动器，支持习惯排序、应用及Omarchy动作统一搜索、别名收藏、键盘操作和实时主题，约40ms打开。补查typecraft-dev/oma-cast，采用窗口结束前9375380fe04dc67fd06752d884ea8cfe9d1eabad提交（10月20日03:20），其中名称仍为oma-launcher，不采用04:03后续改名作窗口内事实。

已读该提交README、RootSearch.js及后端研究笔记相关可读部分。项目要求Omarchy 4、Hyprland 0.56+与omarchy-shell，作为QML插件而非Electron/Node守护进程运行；代码可见应用及菜单候选、别名收藏、frecency和搜索回退。笔记明确目标为Raycast 2.8.2，区分静态观察与推断，记录REA打开原生模块时Hopper超时，部分常量改用objdump读取，不能称所有发现都由REA完成。

设置窗口、Script Commands、剪贴板历史、snippets、quicklinks、计算器、Raycast扩展、窗口管理与rayconfig导入仍在路线图，不是完整Raycast替代。独立clean-room及无Raycast代码资产为项目声明，非法律审核；产品无AI功能不等于开发未用AI。存在单元与smoke测试文件，但Actions接口未返回运行记录，本合集未运行目标测试或桌面。数小时、约400菜单动作与40ms均为作者／项目说法。

候选106赞、1985浏览、3转发；补取原帖130赞、2458浏览、3转发，均为10月20日传播观察而非性能验证。

## 来源

- [typecraft的REA启动器发布](https://x.com/i/status/2112266105200800245)
- [窗口内固定提交README与路线图](https://github.com/typecraft-dev/oma-cast/blob/9375380fe04dc67fd06752d884ea8cfe9d1eabad/README.md)
- [同提交RootSearch实现](https://github.com/typecraft-dev/oma-cast/blob/9375380fe04dc67fd06752d884ea8cfe9d1eabad/plugin/core/RootSearch.js)
- [同提交Raycast静态研究与Hopper超时说明](https://github.com/typecraft-dev/oma-cast/blob/9375380fe04dc67fd06752d884ea8cfe9d1eabad/reference/02-backend.md)

[English](en/omarchy-raycast-rea-launcher.md) | [返回目录](../README.zh-CN.md)
