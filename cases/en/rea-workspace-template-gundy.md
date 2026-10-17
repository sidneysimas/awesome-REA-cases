# REA Workspace Template: separate originals, analysis copies and evidence

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: Related project

At 23:05 Beijing time on October 17, 2026, Gundy (@Gundy886) publishes REA Workspace Template to address confusing observations with guesses, accidental changes to originals and lost cross-session progress. Each target gets a workspace separating target originals, work copies, notes evidence and prompts. Claims are tagged CONFIRMED/GUESS with source lines, function addresses or capture locations. Import creates a SHA-256 baseline; modifications happen on copies, with renaming and handoff logs. Workflows cover source, APKs, native binaries, JS/Electron, HAR and unknown formats; the post caps the first pass at 30 functions.

Reading the dobest1024/rea-workspace-template README and its October 17, 2026 VALIDATION record confirms project-level MCP configurations for Claude Code and Codex. The scaffold copies rather than executes samples; the HAR script produces a structure-only analysis copy. The project reports 12 standard-library tests, a healthy REA 6.4.0 handshake, synthetic-JS static analysis and sanitized inspection of one synthetic POST HAR record. It has not validated real APK/native targets, complete anonymization of business HARs, API-client integration or restarted Claude/Codex UI connections.

The repository explicitly says 0444 permissions and client rules are not an unbypassable sandbox, the hash baseline is not tamper-proof storage, and anonymization still requires human review of hosts, paths and field names. Template checks do not demonstrate successful reversing of real software or strong isolation. Public repository and documentation reading confirms inspectable implementation and boundaries; the latest commit fc15b9a4ba2a8b40510d19a2dd80209f665711c5 is dated 22:43 that day. This collection did not execute the template, install REA or run its tests.

Candidate published October 17, 2026, 23:05; repository commit at 22:43 Beijing time; validation document dated October 17, 2026.
The 12 tests, MCP handshake and synthetic JS/HAR checks are internal project records, not rerun here.
No promise of real-target success, complete anonymization or unbypassable isolation; real APK/native analysis and client UI integration remain unverified.

## Sources

- [Candidate: Gundy's workspace template and conventions](https://x.com/i/status/2111473593305682203)
- [Public template: project configuration and protection boundaries](https://github.com/dobest1024/rea-workspace-template)
- [Project acceptance record: synthetic samples and unverified items](https://github.com/dobest1024/rea-workspace-template/blob/fc15b9a4ba2a8b40510d19a2dd80209f665711c5/docs/VALIDATION.md)

[中文](../rea-workspace-template-gundy.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
