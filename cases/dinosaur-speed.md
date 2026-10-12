# Dinosaur：解释网页跑酷游戏如何逐渐加速

分类：游戏与游戏保存 · REA
记录日期：2026-10-12

t-rex-runner 是类似 Chrome 离线小恐龙的网页跑酷游戏。这次分析针对 HTTP 网页版本，而非浏览器内置的 chrome://dino。贡献者用 REA 阅读脚本，定位初始速度、加速度及更新分支，再用独立 Playwright 控制器在原页面验证更新次数与速度的关系，做成可交互演示。逆向用于回答一个具体玩法问题：“它什么时候加速、每次加多少？”10 月 12 日蓝哥AI 另报告在本机用 REA + Codex 生成复刻版，并发布原版、官方案例版与自制版的并排对比视频；这是新增重建操作的作者报告，不是本合集完成行为等价验证。

补充发帖：2026-10-12T18:41:50+08:00（北京时间）
补充帖热度快照（2026-10-12）：6 赞｜525 浏览｜0 转发

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/1203)
- [原始观察与实验](https://github.com/morluto/rea/blob/main/website/evidence/calculator-and-dino.md)
- [本周期本机复刻与并排对比](https://x.com/0xlangeai/status/2109595393260761111)

[返回目录](../README.md)
