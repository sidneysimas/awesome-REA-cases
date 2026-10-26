# A7C II Tools 3.0：AI逆向报道与QAQLeonard的单机验证边界

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-26
阶段：待验证

2026年10月26日15:09（北京时间）候选称开发者借AI研究Sony A7C II固件，解锁FL2／FL3并导入自定义LUT，以便不换机也使用新的影像风格。15:41候选进一步指名QAQLeonard、A7C II Tools 3.0与固件2.01，并提示副厂电池识别、开机和保修风险。两帖为同一具名相机工具方向，不因功能分别建案例；AI参与仍归于二手报道，未取得原作者对模型、逆向步骤或AI贡献范围的披露，REA未明确提及。

补查准确工具名与作者，找到QAQLeonard/a7c2-fl23-research。静态阅读README对应ef7db116e13e37be91e9af20360dc9bba8d64a9b，提交于10月25日19:23:19北京时间，作为早于候选的补充项目文档。README明确仅支持A7C II（ILCE-7CM2）固件2.01，拒绝其他型号；3.0首次提供正式GUI，修改相机固件中的程序与设置。文档称支持FL2／FL3、自定义Creative Looks、DCP／CUBE离线转为.a7look，带15对DCP／A7Look（11富士、4理光）及可选Lightroom RAW配置插件；RAW插件不改RAW数据。不是相机直接运行任意Log LUT，CUBE须为Sony ST／sRGB输入，S-Log3不能直接使用，内置色彩是拟合近似，不保证与原DCP完全一致。

项目验证表称FL2／FL3、六外观安装及恢复已在作者的一台Windows＋A7C II上写入、回读并重启核验，自定义外观预览／照片及临时声音试听在同机测试。持久自定义快门声只有离线与打包自测，长期真机测试仍进行中；Vertical Display含菜单框正在重写、真机验收待做，macOS虽能打包但真实USB尚未验证。不能把这些功能一概称为已完成或全平台支持，本合集未独立运行测试或看样片。

README引用A7CR／A7R V前人移植、Sony-PMCA-RE等研究，不是从零独立发现所有协议；原项目代码当前为PolyForm Noncommercial 1.0.0，第三方及旧版本另有许可，不泛称MIT开源。文档明确写入成功与回读一致不等于开机安全，可能无法开机、循环重启、丢数据，影响更新、保修与维修，恢复也无保证。副厂电池影响仅候选提及，本合集未验证。基线初代Sony α7 idea为不同机型，保留独立ID；未下载固件、安装依赖、连接相机或刷写，按unverified保留AI归因与独立复现边界。

AI逆向归因来自候选转述，未确认模型或AI贡献范围；原项目仅单台Windows＋A7C II／2.01报告验证，未独立刷机。
macOS USB未验证，持久快门声长期测试进行中，竖屏菜单重写待验收；色彩为拟合近似，回读不保证启动或恢复。

## 来源

- [候选转述A7C II的AI固件研究、FL2／FL3与LUT，2026-10-26](https://x.com/i/status/2114615282480423016)
- [候选补充QAQLeonard、3.0、2.01固件与风险，2026-10-26](https://x.com/i/status/2114623475587698902)
- [补充项目README：ef7db116固定提交，2026-10-25 19:23:19北京时间](https://github.com/QAQLeonard/a7c2-fl23-research/blob/ef7db116e13e37be91e9af20360dc9bba8d64a9b/README.md)

[English](en/sony-a7cii-ai-fl2-fl3-lut-firmware-report.md) | [返回目录](../README.zh-CN.md)
