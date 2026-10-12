# Dinosaur：解释网页跑酷游戏如何逐渐加速

分类：游戏与游戏保存 · REA
记录日期：2026-10-12

t-rex-runner 是类似 Chrome 离线小恐龙的网页跑酷游戏。这次分析针对 HTTP 网页版本，而非浏览器内置的 chrome://dino。贡献者用 REA 阅读脚本，定位初始速度、加速度及更新分支，再用独立 Playwright 控制器在原页面验证更新次数与速度的关系，做成可交互演示。逆向用于回答一个具体玩法问题：“它什么时候加速、每次加多少？”

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/1203)
- [原始观察与实验](https://github.com/morluto/rea/blob/main/website/evidence/calculator-and-dino.md)

[返回目录](../README.md)
