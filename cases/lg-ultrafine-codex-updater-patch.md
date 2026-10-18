# LG UltraFine：Codex 修补 Screen Manager 更新器的内存错误

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-19

10月19日02:25（北京时间），@hirbod说2017年的LG UltraFine在升级macOS 27.0.1后黑屏、USB异常，而LG Screen Manager固件更新器反复崩溃。他称给Codex Astra读IPS崩溃报告，定位double-free，用30行Python修补并本地签名，15分钟后显示器恢复。这些工时与脚本行数是初帖说法，不是当前公开脚本的统计。03:14同作者补充Screen Manager 3.05的Gist并警告刷错可能变砖。

补读公开Gist：创建于10月19日02:59:51、更新于03:32:33（北京时间），均在当前窗口内。文档称jamesxsc在2026年3月5日已报告该内存错误，帮助缩小调查方向；作者说未下载或复用前人的补丁二进制或代码，自己的脚本来自已安装程序与崩溃报告。分析描述416字节分配缩至52字节时忽略realloc返回值，旧指针可能失效；补丁跳过多余resize，保留最终free与传输，不是禁掉错误检查或修改显示器固件签名。公开脚本静态可见精确程序哈希、UUID和原字节检查，只修改独立副本的ARM64指令，保留沙箱权限、检查原App及辅助程序不变，并验证本地签名；不自动启动App或刷固件。

作者记录的配置是M3 Max、macOS 27.0.1 build 26A434、Screen Manager 3.05、原代UltraFine 5K 27MD5KA/27MD5KB家族，产品ID 0x5B11；准确零售后缀未定。作者称隔离函数模拟强制移动分配时复现旧指针错误，修补版以五块发送256字节且仅释放一次；实机scaler更新达100%、最终CRC通过，相机、音频与hub已是最新版。该模拟不是整台显示器仿真，另一dfu-util辅助程序崩溃也不是同一诊断。其他型号、构建和Intel切片未验证，本地签名不是LG认可或Apple公证。本合集只读文档与代码，未执行补丁或刷机；不能保证无变砖风险。

10月19日02:25候选快照21赞、673浏览；不是独立设备验证。

## 来源

- [Hirbod的UltraFine故障与Codex修补自述](https://x.com/i/status/2111886343282274799)
- [同作者Screen Manager 3.05补充与风险提示](https://x.com/i/status/2111898752164532359)
- [公开Gist：诊断、精确构建补丁与作者测试记录](https://gist.github.com/hirbod/2928e9a04c3290ddc66ce23221291b87)

[English](en/lg-ultrafine-codex-updater-patch.md) | [返回目录](../README.zh-CN.md)
