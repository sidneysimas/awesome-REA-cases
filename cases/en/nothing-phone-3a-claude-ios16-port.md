# Nothing Phone 3a: a reported Claude Code-assisted iOS 16 bring-up

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At 20:24 Beijing time on October 20, 2026, Sajid Khan (msfbeast007) reports porting the iPhone X's iOS 16 to a Nothing Phone 3a. Claude Code reportedly wrote drivers and XNU kernel patches and read crash logs, while the human held the phone, flashed it and took photographs. The author describes about two days from a locked bootloader to the lock screen, then lists the home screen, Settings, Control Center, touch, buttons and all eight cores as working. Swiping up or using the Essential Key reportedly returns home. The target is cross-hardware OS adaptation rather than an Android theme, but authenticity remains an author report.

The author explicitly says Wi-Fi, Bluetooth, calls, sound, camera, App Store and GPU support do not work. Rendering uses the CPU, most security is disabled and the port is not a daily driver. The post credits dipa-studio's ios-sweet and says no iOS files are distributed. It also mentions ongoing exploration of macOS on a Snapdragon laptop without reporting a result. Its legal interpretation is not adopted as this collection's legal conclusion.

Supplementary reading of the public ios-sweet README, at a repository commit dated October 20 at 00:44 Beijing time with a document status date of October 18, confirms an upstream account of XNU with iOS 16.7.16 userland on Redmi Note 10 Pro, UFS/HFS+, touch drivers and extensive security limits. It warns that userdata is erased. That document reports only six A55 cores and inability to leave apps; it does not verify the Nothing branch's eight cores or home gesture. The two devices and development states must not be conflated. Nothing-specific source, boot logs and independent device tests were not obtained; REA is not stated.

## Sources

- [Sajid Khan's Claude Code porting report for Nothing Phone 3a](https://x.com/i/status/2112520362382811236)
- [Supplementary upstream: ios-sweet README with October 18 status, not a Nothing device test](https://github.com/dipa-studio/ios-sweet/blob/11da58bd050672960c0a83b5bef2176047eea479/README.md)

[中文](../nothing-phone-3a-claude-ios16-port.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
