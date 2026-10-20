# Android API Extraction Skill: trace UI call flows to HTTP endpoints

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-20
Stage: Related project

At 05:10 Beijing time on October 20, @mobileossfinds introduces Android Reverse Engineering & API Extraction, a Claude Code skill tracing Activities/Fragments through ViewModels and repositories to HTTP calls. Retrieving the original post's image alt text identifies SimoneAvogadro/android-reverse-engineering-skill, distinct from the already-listed newliver666/apk-reverse.

The public master-branch README describes jadx and optional Fernflower/Vineflower analysis of APK, XAPK, JAR and AAR files, requiring Java JDK 17+. It organizes package fingerprinting, Manifest inspection, Retrofit/OkHttp API extraction and Kotlin metadata-based name recovery. It also documents Ktor, Apollo GraphQL and Koin patterns and experimental Windows PowerShell support. The purpose is documenting interfaces and call paths during authorized analysis, not a demonstrated recreation of a commercial app's backend.

GitHub metadata reports the latest push at 16:15 Beijing time on October 12, older supplementary project context rather than a new release in this window. The README's claim of approximately 100% recovery for certain Kotlin classes in a typical app lacks an inspectable sample for this review; it is not generalized to recovery of all R8 obfuscation. This collection installed no skill, downloaded no APK, extracted no credentials and ran no project scripts, confirming documentation and identity only.

## Sources

- [Niko's call-flow skill introduction and repository screenshot](https://x.com/i/status/2112290204320981036)
- [Project README: workflow and experimental platform support](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md)

[中文](../android-api-extraction-claude-skill.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
