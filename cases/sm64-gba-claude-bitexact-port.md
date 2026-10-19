# sm64-gba：Claude 适配既有人类反编译成果，用逐帧 oracle 保持 GBA 运动逻辑

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-19
阶段：进行中

10月19日12:13（北京时间），@riabcevv 转述 Kodoque 的 sm64-gba 项目，纠正‘Claude 写了 GBA 版 Super Mario 64’的说法：运动逻辑来自人类完成的 n64decomp/sm64，AI 的工作是适配、优化和构建严格的对照。补查找到 Kodoque1/sm64-gba 公开仓库，而不是把发帖中的简写当作准确 GitHub 账号。README 明确说代码、测试框架和工程笔记由 Claude Opus 5.5 编写，开发者确定目标与取舍；未确认 REA。

目标是在16.78 MHz、无FPU的ARM7 GBA预算内，保持运动与碰撞结果逐位一致。项目将未修改的反编译代码作为严格IEEE参考，给主机、ARM与GBA构建相同输入，比较每帧状态；README报告23组脚本、53,139帧，两个故意错误构建均须失败，并用1200万次直接碰撞查询补充回放。四关可玩演示的683帧位置回放报告逐位一致；这些覆盖不能证明所有游戏行为正确。

10月19日04:56北京时间的提交 e45fdfadfc1582a5cdb46d3ef7223bfd0385fa8f 补充 mGBA/NanoBoyAdvance 双模拟器、记录到存档RAM的bench ROM及随机上电内存检查。项目报告1228帧巡游在两模拟器分别99.9%/99.8%达到30 FPS；这是固定路线，不是全游戏帧率保证。GitHub测试运行39172132182在06:25北京时间创建，查询时completed/success；这核实的是项目CI状态，本合集没有执行代码、重跑oracle或操作GBA。

尚未在真实GBA测试。演示没有敌人、金币、平台或门，使用简化画面、替代跟随相机与自适应分辨率。默认是碰撞网格和中性人偶；可从用户自备ROM导入模型与场景素材，但不分发原ROM。它是建立在人类反编译上的有限范围移植与验证工程，不是AI重新发现原始源码、全游戏完成或在原掌机通关。补充仓库与CI均属较早工程证据，不当成本窗口新候选。

10月19日候选快照2赞、69浏览、0转发；传播快照不代表测试覆盖或硬件兼容性。

## 来源

- [候选：riabcevv区分人类反编译与Claude适配](https://x.com/i/status/2112034312769900668)
- [公开README：范围、oracle、性能与实机限制](https://github.com/Kodoque1/sm64-gba/blob/e45fdfadfc1582a5cdb46d3ef7223bfd0385fa8f/README.md)
- [10月19日04:56补充提交：双模拟器与上电内存检查](https://github.com/Kodoque1/sm64-gba/commit/e45fdfadfc1582a5cdb46d3ef7223bfd0385fa8f)
- [公开测试运行39172132182：查询时成功](https://github.com/Kodoque1/sm64-gba/actions/runs/39172132182)

[English](en/sm64-gba-claude-bitexact-port.md) | [返回目录](../README.zh-CN.md)
