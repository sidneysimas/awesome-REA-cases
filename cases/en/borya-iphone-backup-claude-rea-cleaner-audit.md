# Old iPhone backup audit: Borya says Claude restored photo identities and REA traced a cleaner's MobileSync access

Category: Applications and clients · REA
Record date: 2026-10-27
Stage: Needs verification

At 18:10:40 Beijing time on October 27, 2026, Borya | Official (@BoryaOfficial) says he asked Claude Code to check a Windows laptop for risks during an ordinary iPhone backup. It reportedly found three old phone backups in MobileSync\Backup, the oldest from 2020, totaling 152 GB and 196,530 randomly named files without extensions, none password-protected. He says iCloud Photos had always been off, so the backups preserved camera rolls from their respective dates plus iMessage and WhatsApp photos. These are his environment-specific statements, not facts generalized to all Windows backups.

He reports that Claude read the backup index to restore photo identities and compared old backups with the new one, finding 5,207 photos no longer on the phone. This means finding data still preserved in old backups, not demonstrating recovery of securely erased disk files. He also says Claude wrote a local OCR script returning only matching filenames, finding passport, bank-card screenshot, ID-photo and 12-word wallet-seed content. No sensitive values are disclosed, and this collection neither requests nor accesses them. His assurance that no photos left the laptop is not an independently verified end-to-end dataflow guarantee.

The security check lists five programs: two PC cleaners, a PDF converter, an old VPN and a game launcher. The author says REA opened all five, found the string MobileSync in one cleaner, and Process Monitor showed that cleaner entering the backup directory on each launch. This establishes only author-reported strings and access observations, not that photos were uploaded, seed words stolen or data continuously exfiltrated for two years. Original-post lookup confirms the full long post and attribution. He says a check prompt will be pinned later; this collection obtained neither that prompt, scripts, binary names, captures nor Process Monitor logs. Included as an unverified account of backup-index analysis and program auditing, without independent reproduction.

Candidate snapshot: 1 like, 197 views, 1 repost. The 5,207 photos, three backups, 152 GB and 196,530 files are author-provided figures.
Access to a backup directory is not proof of exfiltration. No identity-document, card or wallet secrets were read or disclosed here.

## Sources

- [Borya's Claude/REA backup-recovery and cleaner-access report, October 27, 2026](https://x.com/i/status/2115023366792839466)

[中文](../borya-iphone-backup-claude-rea-cleaner-audit.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
