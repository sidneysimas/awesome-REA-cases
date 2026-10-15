# Urban Terror：把桌面多人射击游戏移植到浏览器

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-12

Urban Terror 是基于 Quake III 系技术的多人射击游戏。levelsio 此前尝试通过 ioquake3 引擎和 WebAssembly 将它搬进浏览器，但游戏一直跑不起来。新一轮尝试中，模型定位到引擎结构体和游戏字节码之间的数据布局差异；修正后，作者报告游戏能在浏览器运行并接入多人服务器，附有试玩视频。逆向用于弄清阻碍移植的底层兼容性，而非从零恢复整款游戏。

热度：479 赞｜11.1 万浏览｜11 转发
发帖：10 月 3 日｜非 REA

## 来源

- [看 X 热门帖](https://x.com/levelsio/status/2106150888289009666)

[English](en/urban-terror-web.md) | [返回目录](../README.md)
