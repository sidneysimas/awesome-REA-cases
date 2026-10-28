# EasyClick APK: Goge reports local Qwen recovering self-written encrypted JS in 44m 58s

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-28
Stage: Analysis test

At 14:18:49 Beijing time on October 28, 2026, Goge (@niandwo) reports local-model tests with an AMD R9700 32G, DDR5 64G, Strata 0.1.52 and Qwen3.8-next-flash-iq3_s at a 256K context. The reverse-engineering target is an Android automation-script app previously written with easyclick. The setup uses opencode and basic reversing skills, explicitly without the REA toolkit. The agent finds jadx and OrbStack on the Mac, starts a debugging container and plans to load the APK's native decryption library, open an IEC2 script package and export js/main.js. The author sees this progress at 17m 29s and ultimately reports complete, accurate recovery of his own JS logic at 44m 58s. Original-post lookup confirms attribution and four screenshot attachments, not the code depicted.

The aim is testing long-context tool use and protection of scripts in a self-owned app, not compromising another person's account. No original APK, original/recovered code comparison, hashes, repeatable tests or complete agent log is supplied; completeness and accuracy are the author's assessment. Container-image and JDK downloads cause waiting, so 44m 58s is not pure inference time or a general speed guarantee. About 80 tokens/s at 240K context, roughly 15% slower than an RTX3090 setup, and at least 1.5 times faster than llama.cpp running Qwen3.8-27B Q5 on the same hardware are separately reported inference comparisons, not reversing accuracy. Generating a shooter in 6m 27s is likewise not this recovery result. No target dependencies were installed, APK executed or decryption library run here. Retained as a reported analysis test.

Candidate snapshot: 7 likes, 349 views, 0 reposts. 17m 29s is a progress point; 44m 58s is the author's total including download waits.

## Sources

- [Goge's local Qwen inference and EasyClick script-recovery report, October 28, 2026](https://x.com/i/status/2115327409520267434)

[中文](../goge-qwen-easyclick-apk-js-recovery.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
