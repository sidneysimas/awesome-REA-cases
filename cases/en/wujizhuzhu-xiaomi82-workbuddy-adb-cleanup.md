# Xiaomi Master 82 TV: WorkBuddy uses CleanYourTV, a UI tree and a screensaver configuration fix

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-25
Stage: Needs verification

At 15:54:49 Beijing time on October 25, 2026, @Wujizhuzhu reported modifying his Xiaomi TV Master 82-inch Ultra commemorative edition, described as a 2GB-RAM Android 9 device whose sluggish interface had led him to use an external Apple TV. He found agent instructions in the existing open-source CleanYourTV project and had WorkBuddy connect through authorized ADB debugging, ask which apps, casting, voice features and launcher icons to retain, and proceed. This is a different author from the baseline Leo Workbuddy-launcher report and is not merged merely because brand and tool match.

He says it backed up 115 packages and all system settings, then disabled 25 packages in two batches, covering ads, statistics, cloud control, TV management, lock-screen artwork and PatchWall. Reported available RAM rose from a little over 100MB to nearly 700MB and swap use fell from 367MB to 16MB. These are author measurements without raw logs or a standardized before/after protocol. WorkBuddy then fetched an open-source launcher, compiled an APK, installed it, set the default home screen/screensaver, and reportedly fixed the original screensaver pointing to an uninstalled Google clock.

The account also describes ADB screenshots returning zero bytes, prompting UI-tree inspection; a Mac lacking Java, Gradle and Android SDK, with the agent installing the toolchain and resolving a Gradle AEAD error through JVM proxy parameters; and a conflict between automated clicks and the launcher watchdog, temporarily disabling and restoring accessibility. About an hour later the TV had a third-party Bilibili client, Aerial launcher and SmartTube. A network-proxy subscription is also mentioned; no subscription, credentials or configuration was obtained or copied here.

This records AI-assisted understanding of device state, configuration behavior and launcher adaptation. Existing ADB access, disabling packages and compiling an open-source launcher are not described as vulnerability discovery, root, a reverse-engineered firmware rewrite or invention of CleanYourTV. Supplementary reading on October 26 confirmed author and full text. No TV was connected, dependencies installed, recovery/reboot persistence tested, screensaver defect independently checked or memory remeasured. A clean interface and ad-removal scope remain author claims, not evidence of eliminated in-app ads/all telemetry or compatibility with other models.

Author reports 115 packages backed up, 25 disabled and about one hour; RAM a little over 100MB to nearly 700MB, swap 367MB to 16MB, none independently measured.
Reuses CleanYourTV and an open-source launcher; ADB/UI-tree/configuration adaptation is not root or a firmware rebuild, and recovery is untested.

## Sources

- [Wujizhuzhu's full WorkBuddy/ADB Xiaomi Master 82 modification report, October 25, 2026](https://x.com/i/status/2114264402975445017)

[中文](../wujizhuzhu-xiaomi82-workbuddy-adb-cleanup.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
