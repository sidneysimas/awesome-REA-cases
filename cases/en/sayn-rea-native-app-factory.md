# sayn: build a personal Android app from Play Store features and an APK spec

Category: Applications and clients · REA
Record date: 2026-10-20
Stage: In progress

At 22:20 Beijing time on October 19, @EShishniashvili introduces sayn: connect a phone, pick a Play Store app or describe an idea, and have Claude Code or Codex generate a personal native app, also learning from negative store reviews. Gym, habit-tracking, conversion and language-learning tools motivate the proposal. The author claims many paid utilities can be replaced in 5–10 minutes; shared memory across generated apps is still planned. Timing and replacement capability are claims without acceptance records for named generated examples.

Supplementary reading of Ersho/sayn commit 5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc (October 19 at 19:20 Beijing time, before the candidate window), its README and backend/vibe/codex.py and playstore.py confirms the design: a local FastAPI/Vite dashboard, an Expo/React Native template, signed APK builds and ADB installation. Store descriptions, screenshots and reviews are the default reference. Optional APK mode pins REA 6.7.0 with JADX and prompts the agent to inspect activities, navigation and data models, write inspiration/spec.md, then implement. An APK download failure falls back to store material, so not every generated app involves reversing. The inspected code uses prompt constraints on the same agent that analyzes and builds, not an isolated clean-room team. Prohibitions on copying code, names or assets are project rules, not a legal guarantee.

The README specifies Windows/Linux x64, about 10 minutes for the first build and 5–7 minutes thereafter. Local operation still sends agent conversations to the model provider. The workflow API returned no Actions runs. This collection did not install dependencies, download a target APK, build an app or connect a phone. Static reading does not establish functional equivalence, privacy isolation, replacement of arbitrary subscriptions or five-minute delivery.

October 19 candidate snapshot: 0 likes, 15 views and 0 reposts. Low engagement does not exclude a concrete project; not a performance test.

## Sources

- [Author introduces sayn, REA integration and planned shared memory](https://x.com/i/status/2112187204676018577)
- [Earlier public README commit: architecture, timing and platform scope](https://github.com/Ersho/sayn/blob/5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc/README.md)
- [Same commit's codex.py: REA configuration and spec-before-build prompts](https://github.com/Ersho/sayn/blob/5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc/backend/vibe/codex.py)
- [Same commit's playstore.py: optional APK mode and failure fallback](https://github.com/Ersho/sayn/blob/5471b9606daf8bd5105e6b8b767f3ba2e5c4edcc/backend/vibe/playstore.py)

[中文](../sayn-rea-native-app-factory.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
