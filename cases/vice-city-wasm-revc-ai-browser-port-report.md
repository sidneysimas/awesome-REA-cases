# Vice City浏览器版：基于reVC既有逆向引擎的AI辅助移植转述

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-22
阶段：待验证

2026年10月22日17:24:40（北京时间），Shivansh Gupta（@shivanshgupta36）介绍oalanicolas的GTA: Vice City浏览器移植：继承reVC Web/wasm-revc的C/C++逆向引擎，用Emscripten编为WebAssembly，经WebGL2渲染、OpenAL处理音频并适配触屏，在iPhone Safari本机执行，不是云游戏。原帖明确归功reVC及WebAssembly社区多年成果，不能说AI从零反编译原游戏。

据其转述，游戏逾1.5GB资产按需加载，使用VFS、HTTP Range、Web Workers、预取缓存和异步I/O；主城市归档分为1,250个、每块至多256KiB的独立压缩块，传输量从约327MB降到183MB，所称44.22%是来源报告，不是本次复算。作者称项目桌面基准约59.95fps，自己的iPhone截图计数58至60fps，不保证所有设备持续60fps。

AI分工也为该作者转述项目文档：Codex负责引擎集成、排障和测试，Claude负责菜单与UI，Gemini参与优化且包括另一个3D资产查看器。约73.5亿token是多个工作流的日志合计，包含大量缓存上下文读取，不是73.5亿生成token，不直接推成本或全部属于游戏移植。

本次读取候选全文并补查作者身份，没有取得所链技术文章、精确提交、资产授权或可复核性能日志，也没有运行游戏或下载游戏资产。按基于既有逆向成果的AI辅助移植转述保留unverified，REA未被提及；浏览器可运行的说法不构成资产再分发许可。

来源原发2026-10-22T17:24:40+08:00；59.95fps、58至60fps、44.22%及73.5亿token均为来源转述，未经本合集复算或测量。

## 来源

- [Shivansh Gupta：Vice City浏览器移植、前人贡献与AI分工长文](https://x.com/i/status/2113199849936142390)

[English](en/vice-city-wasm-revc-ai-browser-port-report.md) | [返回目录](../README.zh-CN.md)
