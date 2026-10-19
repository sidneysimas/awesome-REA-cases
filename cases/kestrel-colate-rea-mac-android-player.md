# Kestrel：研究 MuMuPlayer Pro，为 Apple Silicon 做原生 Android 游戏播放器

分类：应用与客户端 · REA
记录日期：2026-10-19
阶段：进行中

10月19日07:59（北京时间），@ColateAi 转述 @iamthehimansh_ 的 Kestrel：为在 Mac 玩 BGMI，使用 Colate Desktop 的 REA mod 研究 MuMuPlayer Pro 的部分架构，再在 Google Android Emulator 上实现原生播放器、输入与键位映射。补读 iamthehimansh/kestrel 公开仓库，README 将构建工具称为 Cana.build 的 REA mod，并明确它基于开源 REA；这里保留候选与仓库的命名差异，不推断产品更名。项目称不包含专有模拟器二进制、反编译源码或受限 Android 镜像。不是从零实现整个 Android 模拟器。

公开提交 5250e2ba（10月19日06:46:09，北京时间）及其研究账本提供单台 Apple Silicon 开发机的实验摘要与公开复测方法；历史数值转录自保留的私有评测文件，不等于公开原始数据或独立复现。pipe 与 ASG 的两次启动、每次三样本对照未建立有意义的帧时间改善，因此未加性能开关。MuMu Android 12/API32 与 Kestrel Android16/API36、绘制尺寸和工作负载不同，不能推出普遍性能倍数。共享内存降低测得的CPU成本和帧龄，但缺少已证明的生产者栅栏；产品选择完整复制帧与单槽 latest-frame mailbox。Metal 显示路径限制在途渲染并保持比例。

作者记录请求4 GiB而既有QCOW2为6 GiB导致快照验证失效；保留实际磁盘容量后，三次恢复约6.36秒，不拿含初始设置的冷启动当提速分母。120 Hz虚拟显示不等于游戏120 FPS。BGMI最初EGL崩溃，关异步swap只消除崩溃但仍黑屏；在该条件保留时选择内置ANGLE后渲染，维护者提供游玩截图并称可玩，不证明其他设置无关。键鼠映射、失焦释放触点、全屏提示、实例管理与CLI有公开实现；预置键位不等于逐款游戏实测。

仓库说明原生播放器需macOS15及Apple Silicon，SDK首次运行下载，App仅ad-hoc签名、未公证，输入仅ASCII，麦克风实际语音聊天未验证，不承诺反作弊接受或商业模拟器性能等价。补查公开CI run 39173792442（10月19日06:48至07:01，北京时间）：Swift构建步骤成功、Test步骤失败，打包脚本测试作业成功；不能称全套CI通过。未执行目标代码、安装包或游戏，本合集只读公开材料。

07:59候选快照0赞、3浏览；补查GitHub时1星。传播很少，不是成熟度证明。

## 来源

- [Colate转述Kestrel研究、实验与预览限制](https://x.com/i/status/2111970389983142116)
- [Kestrel公开仓库与README](https://github.com/iamthehimansh/kestrel)
- [10月19日06:46提交的实验账本](https://github.com/iamthehimansh/kestrel/blob/5250e2ba2ca5d9fbcbb8ad94e7aa1cc7534f6809/docs/research/experiment-ledger.md)
- [同提交的兼容性与证据说明](https://github.com/iamthehimansh/kestrel/blob/5250e2ba2ca5d9fbcbb8ad94e7aa1cc7534f6809/docs/guide/compatibility.md)
- [公开CI：Swift测试失败，打包脚本测试成功](https://github.com/iamthehimansh/kestrel/actions/runs/39173792442)

[English](en/kestrel-colate-rea-mac-android-player.md) | [返回目录](../README.zh-CN.md)
