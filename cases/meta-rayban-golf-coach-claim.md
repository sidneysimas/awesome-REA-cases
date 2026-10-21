# Meta 眼镜推杆教练：HCI／jadx 研究与 AR 方案的未核实宣称

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

2026年10月20日22:25（北京时间），0xCodez 的传播帖声称 Opus 5.5 用一条提示词、20分钟把 Meta Ray-Ban 眼镜变成推杆教练。叙述先抓蓝牙 HCI 并用 jadx 分析 Meta AI，再让四个 tmux Agent 分别处理视频、视觉、物理与UI，称手机画什么镜片就显示什么。紧随的完整提示词指定 Ray-Ban Meta 2 与Android，要求用 tshark 解析日志、核对 Meta Device Access Toolkit，先在录制视频上测试再接眼镜。

方案用单目SLAM、Depth Anything V2、球直径42.67mm与球洞108mm标定，生成5cm网格；以1cm高差画等高线，用YOLO识别目标，RK4按1ms步长搜索让球停在洞后17英寸的路线，再用MediaPipe手指操作菜单。低于100ms端到端延迟是提示词验收目标，不是测量。作者说视频是练习果岭且比赛禁坡度读取；10月20日22:46的中文转述也只是同一宣传，不是复现。

补读 Meta Android DAT 官方 README（10月10日02:23北京时间提交），其明确把 Display 功能限定为 Meta Ray-Ban Display 眼镜；提示词中的 Ray-Ban Meta 2 不能仅凭蓝牙或反编译就视为具备镜片显示能力。未取得具体硬件核定、代码、覆盖层传输协议、深度精度或真机延迟测试。保留为具体目标与未核实方案，不确认20分钟完成或AR投影可用，不与语音助手替代客户端混同。

## 来源

- [0xCodez 推杆教练功能与20分钟宣称](https://x.com/i/status/2112550881950396884)
- [同串完整提示词：HCI、视觉、物理与UI验收目标](https://x.com/i/status/2112550885452623952)
- [补充技术边界：Meta官方DAT README的Display设备范围](https://github.com/facebook/meta-wearables-dat-android/blob/f4371bc9f90249d51eb07d7f8a61e8d829294f16/README.md)

[English](en/meta-rayban-golf-coach-claim.md) | [返回目录](../README.zh-CN.md)
