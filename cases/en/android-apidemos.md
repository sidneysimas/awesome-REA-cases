# Android ApiDemos: tracing Java methods from an APK

Category: Applications and clients · REA
Record date: 2026-10-12

ApiDemos is a sample app Appium uses to demonstrate and test Android features. A contributor used its real release APK to validate REA with headless JADX: reading the package and manifest, locating classes, inspecting members, extracting Java/smali for selected methods and tracing callers. ContextCompat.startActivities overload selection was checked separately. The aim is to let agents accurately locate specific implementations in installation packages. The original APK was not executed; this is a static-analysis example rather than an app replica.

## Sources

- [Original PR and validation](https://github.com/morluto/rea/pull/738)

[中文](../android-apidemos.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
