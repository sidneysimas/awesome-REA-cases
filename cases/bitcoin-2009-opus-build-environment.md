# Bitcoin 2009：Opus 辅助恢复构建环境，而不是恢复源码

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-20
阶段：分析测试

10月20日02:42（北京时间），@itsarcvale转述@t4t5用Opus 5.5重建2009年bitcoin.exe，并建议核对自己的钱包构建。补查作者10月19日03:12原帖及同秒续帖，确认目标是从已有公开源码恢复未知的历史构建环境，不是AI反编译出未公开源码。作者报告EXE与历史发行文件SHA256相同。

补读t4t5/bitcoin-0.1-rebuilt固定提交344f88083abf301af107fb9de120ee9350f1415b（10月19日14:36，北京时间，早于本轮）README：项目恢复Windows XP/MinGW gcc 3.4.5、不同阶段binutils、wxWidgets及Berkeley DB环境，用Docker/Wine构建、WinRAR 3.51打包，报告6,440,960字节EXE及2,132,686字节RAR匹配历史哈希。这是项目结果，不是本合集计算或运行所得。

名为bitcoin-0.1.0的档案实际对应1月10日0.1.1时代更新，不是1月8日首发文件；作者不知道有可验证的首发存本。三个原始时间戳为构建输入，缺它们会差335字节；RAR时间与NTFS压缩属性也由原档案提供，脚本修改后者并重算头校验。libeay32.dll和mingwm10.dll未从源码重建，运行环境是Wine而非XP。未执行构建、下载历史目标或访问钱包，不推广为所有钱包可复现或已排除所有供应链风险。

候选快照11赞、357浏览、2转发；补查较早作者原帖2084赞、271269浏览、119转发。均为10月20日观察的传播快照，不是技术复现。

## 来源

- [本轮Arcvale转述及钱包构建核对建议](https://x.com/i/status/2112252966971301962)
- [较早作者原帖：Opus辅助环境重建](https://x.com/i/status/2111898332658544835)
- [较早作者续帖：版本身份与构建考古](https://x.com/i/status/2111898334893842717)
- [较早固定提交README：结果、输入与DLL边界](https://github.com/t4t5/bitcoin-0.1-rebuilt/blob/344f88083abf301af107fb9de120ee9350f1415b/README.md)

[English](en/bitcoin-2009-opus-build-environment.md) | [返回目录](../README.zh-CN.md)
