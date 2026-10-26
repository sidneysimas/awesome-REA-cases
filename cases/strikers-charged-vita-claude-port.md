# Mario Strikers Charged：人类真机测试、Claude协作的PS Vita移植

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-26
阶段：进行中

2026年10月25日15:30（北京时间），yibie在同一资源更新中另介绍Mario Strikers Charged的PS Vita原生移植，并称从19处提交trailer识别AI参与。补查公开仓库CBOC-Vita-Lab/strikers-charged-vita，目标是让Wii足球游戏在Vita上运行：项目描述把游戏代码重建为Vita处理器代码、为图形芯片重写渲染器，并适配按键、触控、声音和存档，不是流式游玩或整机模拟器。这些是项目实现说明，本合集没有真机验证。

README致谢明确由Claude及其他AI助手编码、人类指导和真机游玩测试，建立在yannicksuter/mscharged-decomp既有反编译、vitaGL与VitaSDK之上，不能把前人工作全部归为本次AI原创反编译。10月24日04:50:42 UTC的e80d886提交带Claude Opus 5.5共同署名，报告把带表情的面部蒙皮移到GPU、减少重复解码，并称回放时渲染线程每帧ARM指令少16%、游戏线程少3%；这是项目测量口径，不是本合集基准。REA使用未获确认。

补读固定4fbe675提交（10月25日03:43:38 UTC）的README，1.1版自报轻场景最高60fps、通常30fps，进球回放与庆祝约20至25fps，普通操作延迟约0.1秒；不能把最高60fps当全程锁定。项目仍列已知问题、不同场景性能差别及后续工作。它要求用户自备Wii USA Rev 1游戏数据，不在本合集提供游戏、安装包或运行指导。

这是往期待补审项目，补充公开提交和文档早于10月26日00:00至04:00窗口，只用于确认项目身份、AI分工与具体限制。原帖6星、4146文件和19处trailer未重数，不作为能力验证。未安装依赖、执行代码、下载游戏资产或独立测试移植的原生执行、帧率、输入与存档；状态保留进行中。当前README已明确AI协作，不沿用原帖仅凭trailer才可知道AI参与的概括。

进行中；基于既有mscharged-decomp、vitaGL和VitaSDK，人类指导与项目真机测试不等于本合集独立复现。
1.1性能为项目自报且因场景而异；REA使用未知，不分发原游戏数据。

## 来源

- [往期候选：yibie介绍Vita移植，2026-10-25北京时间](https://x.com/i/status/2114258253253329233)
- [补充项目README与AI/人工分工，固定4fbe675，2026-10-25 UTC](https://github.com/CBOC-Vita-Lab/strikers-charged-vita/blob/4fbe6759ea0f255364666534551aee7fb3676549/README.md)
- [GPU面部蒙皮实现及Claude共同署名，2026-10-24 UTC](https://github.com/CBOC-Vita-Lab/strikers-charged-vita/commit/e80d886e2f7b262defb22f9ffb1a535e174f560a)

[English](en/strikers-charged-vita-claude-port.md) | [返回目录](../README.zh-CN.md)
