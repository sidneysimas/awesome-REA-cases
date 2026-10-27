# Civic Android head unit: Indra relays Crunchy-Nut1's Claude Code service audit and 18-package cleanup

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-26
Stage: Needs verification

At 23:32:45 Beijing time on October 26, 2026, Indra (@IndraVahan) relayed r/claudecode user u/Crunchy-Nut1 connecting Claude Code to a Chinese Android head unit in his Honda Civic. The post says an assistant kept listening for a wake word and ran a hidden WebView consuming about 30% CPU even without speech; the Bluetooth calling device had a preinstalled call recorder, a vendor root backdoor, a startup script installing APKs from a hidden directory before deleting them, a remote firmware updater, Baidu location services and a background vendor log collector. It also alleges that an eight-core Android 15 listing was actually four-core Android 9 with an October 2021 security patch. All are secondhand reports. Installed components do not establish actual recording or exfiltration, and hardware-advertising deception is not independently established.

The retelling attributes to Claude Code disabling the assistant and other apps, backing up and removing 18 packages, closing the alleged root backdoor and hidden APK installation mechanism, disabling cloud updates, configuring AdGuard Private DNS, upgrading WebView from 66 to 138, building a Civic launcher and icons, recalibrating reversing-camera guidelines, installing open-source apps with SHA-256 verification and restricting network access. Counts, revisions and CPU usage remain secondhand, not guarantees of complete or safe remediation. Hash verification also does not establish trust in a software author.

Supplementary X reading confirmed the reporting account and full text. The Reddit user's public-post endpoint returned 403; the original account, head-unit model, package names, startup script, logs, code and road testing were not obtained. This candidate concerns the head unit, not reverse engineering the Civic's vehicle-control systems. REA is not mentioned. Included as an unverified investigation/modification report without running code, operating a vehicle or claiming the device is backdoor-free, tracking-free or fully secure.

Candidate snapshot: 10 likes, 467 views, 1 repost. Substantially higher engagement at supplementary lookup does not replace it.
Secondhand report; Reddit's public endpoint returned 403. Original logs, code, model and vehicle tests were not obtained. Removing 18 packages and upgrading versions are not a complete security audit.

## Sources

- [Indra relays Crunchy-Nut1's Civic head-unit investigation and Claude cleanup, October 26, 2026](https://x.com/i/status/2114742034183733424)

[中文](../crunchy-nut1-civic-claude-head-unit-audit-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
