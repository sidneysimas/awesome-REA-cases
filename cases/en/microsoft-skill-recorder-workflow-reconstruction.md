# Microsoft Skill Recorder: reconstruct reusable agent skills from recordings and activity events

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-25
Stage: Related project

At 12:25:54 Beijing time on October 25, 2026, TechVerser (@realfxw) introduced Microsoft Skill Recorder as a way to turn one recording of a person doing a task into repeatable agent skills. It reconstructs application workflows rather than decompiling application binaries and is included as a related project in broader AI-assisted behavior reconstruction.

Supplementary reading on October 26 examined the public microsoft/skill-recorder README, pinned to September 21 commit b05d59036182e897e1a60e90651e775cf5f97e8d. The project describes locally capturing the screen, window switches, browser paths, clipboard previews, an optional recorded terminal and spoken narration, then using GitHub Copilot CLI to reconstruct intent and ordered steps for user review and editing. These become SKILL.md or a scheduled/triggered Automation. Native CLI/API tools are preferred over replaying fixed click coordinates. Generalizing one form submission into batch processing is a project design goal, not an experiment performed here.

The privacy boundary matters: recording, storage, frame extraction and optional Whisper transcription are local, but Analyze sends the event timeline, extracted images, narration text and bounded terminal-output excerpts to GitHub's cloud. Sensitive-information checks and skill previews are not security guarantees. The README calls macOS the primary target and describes Windows 11 x64/ARM64 support. No app was installed, no screen was recorded and no generated skill was executed here. Cross-platform behavior, generalization accuracy and redaction effectiveness were not independently tested, and the post's platform-compatibility claims are not upgraded to verified integrations.

Related behavior-reconstruction tool, not a binary-decompilation case; not installed or run.
Local recording is not offline analysis: Analyze uploads data, and previews/scanning do not guarantee safety.

## Sources

- [TechVerser's Skill Recorder introduction, October 25, 2026](https://x.com/i/status/2114211826493714625)
- [Supplementary Microsoft project README pinned to a September 21 commit](https://github.com/microsoft/skill-recorder/blob/b05d59036182e897e1a60e90651e775cf5f97e8d/README.md)

[中文](../microsoft-skill-recorder-workflow-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
