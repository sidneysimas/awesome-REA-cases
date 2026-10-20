# MagicSwipe：Opus 研究 Magic Mouse，让 iPad 通用控制支持手势

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-20
阶段：进行中

10月20日07:46（北京时间），saikumar（@saikumar2729）称Opus 5.5在一次会话中研究Magic Mouse经Universal Control控制iPad时缺失的双指手势：从Apple私有MultitouchSupport框架读取触摸，再经Karabiner开源虚拟HID驱动发送Globe组合键。作者报告左右滑切应用、上滑或双指双击开App Switcher、下滑回主屏，并仅在指针位于iPad时启用。标签提到REA，但正文没有明确REA的实际步骤，按其他AI辅助研究记录。

补读公开MagicSwipe固定提交f8379a0e6f2aa3af9d22f0846f482321b3417876（10月19日09:45，北京时间，早于本轮）的README与app/main.m。源码可见私有触摸回调、Universal Control的notify状态位0x2/0x1、手势识别和发给keyd的命令；README说明普通CGEvent或AppleScript按键不被转发，需HID级输入，必要时先用虚拟鼠标按钮4转移键盘焦点。不是恢复连续拖动的原生触控板手势，而是替换成键盘快捷键。

项目报告测试macOS 27、蓝牙产品ID 0x0269的Magic Mouse及iPad。安装需管理员权限和Karabiner DriverKit 8.5.0（协议7），部分辅助进程以root运行；私有接口可能随系统更新失效，滑动会轻微滚动下层页面，双击则不会。提交注明Claude Opus 5.5共同署名，但不等于独立运行验证。本合集只读公开文档与源码，未安装驱动、执行目标代码或实测设备。

候选快照2赞、17浏览、0转发；传播很早期，不代表兼容性验证。

## 来源

- [saikumar的Opus手势研究与演示帖](https://x.com/i/status/2112329554731630682)
- [较早固定提交README：测试配置、权限与限制](https://github.com/sai2729/MagicSwipe/blob/f8379a0e6f2aa3af9d22f0846f482321b3417876/README.md)
- [同提交手势识别与Universal Control状态源码](https://github.com/sai2729/MagicSwipe/blob/f8379a0e6f2aa3af9d22f0846f482321b3417876/app/main.m)

[English](en/magic-mouse-ipad-opus-virtual-hid.md) | [返回目录](../README.zh-CN.md)
