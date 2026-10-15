# 游戏与游戏保存

[返回主目录](../README.md)

- [Universal Modder：用 AI 给现有游戏做 Mod](../cases/universal-modder.md) — 分析游戏代码与文件格式，制作跨游戏内容 Mod。 **[其他 AI 逆向]**
- [Firefighter：把老 DOS 游戏恢复成可维护的 Rust 代码](../cases/firefighter-rust.md) — 从旧 DOS 二进制恢复 Pascal，再转写为 Rust。 **[其他 AI 逆向]**
- [《现代战争 2》：用多 Agent 重建游戏代码](../cases/mw2-decompilation.md) — 多 Agent 反编译游戏，以原二进制核对恢复函数。 **[其他 AI 逆向]**
- [Urban Terror：把桌面多人射击游戏移植到浏览器](../cases/urban-terror-web.md) — 定位引擎与字节码布局差异，将游戏移植到浏览器。 **[其他 AI 逆向]**
- [DX-Ball：恢复老打砖块游戏的声像算法](../cases/dx-ball-sound-pan.md) — 还原打砖块游戏按位置分配左右声道的函数。 **[REA]**
- [《东方幻想乡》：恢复环形弹幕的角度计算](../cases/th04-bullet-ring.md) — 恢复《东方幻想乡》环形弹幕的角度计算。 **[REA]**
- [东方系列：用 Agent 重建旧游戏，并迁移到新平台](../cases/touhou-reconstruction.md) — 重建东方系列代码，验证并迁移到可玩平台。 **[REA]**
- [Dinosaur：解释网页跑酷游戏如何逐渐加速](../cases/dinosaur-speed.md) — 读网页脚本，实验验证跑酷游戏的加速规则。 **[REA]**
- [Unity / Valheim：游戏程序集分析需求](../cases/unity-valheim.md) — 真实游戏分析需求，原游戏目标复测仍缺少证据。 **[REA · 进行中]**
- [《荒野大镖客 2》：写导出器移入波巴·费特](../cases/boba-fett-rdr2.md) — Claude 研究游戏素材格式，迁移角色并制作喷气背包等玩法。 **[其他 AI 逆向]**
- [GameCube / Wii：从实际 Wii 分析提出 PowerPC 支持](../cases/wii-powerpc-request.md) — 已有 Ghidra 研究经验，REA 内部支持仍是需求。 **[未确认使用 REA · 进行中]**
- [《航空霸业2》：用 REA + Kimi 反编译老游戏](../cases/aerobiz-2-decompilation.md) — 研究 KOEI 1993 年航空经营游戏的编译程序。 **[REA · 待验证]**
- [《超级马里奥阳光》：AI 参与说法下的原生 PC 移植](../cases/super-mario-sunshine-pc.md) — 传播帖称 AI Agent 参与反编译并将 GameCube 游戏移植到 PC。 **[未确认使用 REA · 待验证]**
- [《红色警戒 2》：为强化学习重写游戏引擎](../cases/red-alert-2-rl-engine.md) — 参考 Chrono Divide，用 Opus 与测试集重建单位行为。 **[其他 AI 逆向 · 待验证]**
- [《不可思议的机器》：用 Claude 重建浏览器版](../cases/incredible-machine-browser.md) — 作者报告 Opus 分析 Sierra 老游戏、重做素材并在浏览器运行。 **[其他 AI 逆向 · 待验证]**
- [《街头霸王 III》：用 AI 重构反编译后的 C 代码](../cases/sfiii-codescene-refactoring.md) — 在既有开源反编译代码上用 CodeHealth MCP 与轨迹回放约束重构。 **[其他 AI 逆向 · 相关项目]**
- [经典射击游戏：AI 辅助浏览器移植的传播报告](../cases/classic-shooters-browser-report.md) — 传播帖列出多款网页移植，但缺少项目对应与 AI 贡献证据。 **[未确认使用 REA · 待验证]**
- [Nanolathe：重新实现《横扫千军》游戏引擎](../cases/nanolathe-total-annihilation.md) — 用公开研究重实现 Total Annihilation，AI 具体贡献仍待核实。 **[其他 AI 逆向 · 待验证]**
- [手游交互：用 Codex + REA 对应脚本与运行活动](../cases/mobile-game-interaction-evidence.md) — 一边分析脚本文件，一边观察手游交互的计算活动。 **[REA · 进行中]**
- [Star Fox / Sonic CD：AI 原生移植的待验证传播](../cases/arwing-littleplanet-ai-port-report.md) — 传播帖关联三个原生移植仓库，但不等于 AI 完整反编译。 **[其他 AI 逆向 · 待验证]**
- [Dark Sun: Shattered Lands：用 REA 研究并移植老游戏的计划](../cases/dark-sun-shattered-lands-port-idea.md) — 提出从 GOG 游戏到 REA 分析，再用攻略帮助移植 Unity/three.js 的路线。 **[REA · 待验证]**
- [Armed and Dangerous：用 Ghidra 与 AI 探索重制路线](../cases/armed-and-dangerous-remaster.md) — 作者报告以 Ghidra 反编译并用 AI 编写 C 函数，正在比较运行时替换与 Bevy 重写路线。 **[未确认使用 REA · 进行中]**
- [Fort Apocalypse：用 Codex 与 Ghidra 移植到 Android](../cases/fort-apocalypse-android-port.md) — 作者称使用 Codex 和 Ghidra 将 C64 游戏 Fort Apocalypse 移植到 Android。 **[其他 AI 逆向 · 待验证]**
- [Minecraft × Plants vs. Zombies：REA 辅助的可玩混合作品报告](../cases/minecraft-pvz-rea-mashup.md) — 一则 quote 帖称试用 REA 逆向后制作出可玩的 Minecraft 与植物大战僵尸混合作品。 **[REA · 待验证]**
- [《三国志14》：将修改器功能组合成 MCP 的报告](../cases/three-kingdoms-mod-mcp.md) — 作者称分析《三国志14》修改器与风灵月影，并组合成可批量操作的 MCP。 **[未确认使用 REA · 待验证]**
- [Virtua Fighter 2.1 / 3 TB：AI 辅助反编译进行中](../cases/virtua-fighter-ai-decompilation.md) — AI coding agents 辅助恢复两款 SEGA 格斗游戏的可读 C/C++ 逻辑；项目仍在进行。 **[未确认使用 REA · 进行中]**
- [Dragon Ball Budokai：AI 逆向与浏览器移植的待验证报告](../cases/dragon-ball-budokai-browser.md) — 传播帖称 AI 逆向《龙珠》游戏并实现可在浏览器运行的 60 fps 版本；项目与 AI 贡献未核实。 **[未确认使用 REA · 待验证]**
- [Friday Night Funkin’：基于反编译成果制作 Claude 辅助的新玩法](../cases/friday-night-funkin-claude-gameplay.md) — 作者称基于近期反编译成果，用 Claude 制作含新输入、画面与界面的玩法版本。 **[未确认使用 REA · 待验证]**
- [rea-engine: Rebuild Windows TicTacToe from its binary](../cases/rea-engine-tictactoe.md) — The author reports building rea-engine atop original REA, adding a tooling layer, and reconstructing a Windows TicTacToe game from its binary; all 19,683 board states reportedly match byte for byte. **[REA]**
- [《星之卡比》：REA 逆向进行中的作者报告](../cases/kirby-rea-in-progress.md) — 作者称星之卡比逆向到一半，未公布具体版本或产物。 **[REA · 进行中]**
- [《织梦岛》：Claude Code 参与 PC 移植的待验证转述](../cases/links-awakening-claude-pc-port-report.md) — 移植综述称《织梦岛》几乎依靠 Claude Code 重编译上 PC，未提供本帖内可核验产物。 **[其他 AI 逆向 · 待验证]**
- [《博德之门3》：探索 Agent 增强 Mod 的 idea](../cases/bg3-agent-modding-idea.md) — 发帖者提出把 BG3 作为 Agent 增强目标，询问是否受反编译难度限制。 **[未确认使用 REA · 待验证]**
