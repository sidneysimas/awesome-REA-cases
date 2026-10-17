# Amazon Prime tvOS: investigating IPA Universal Links to open shows from a personal app

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-17
Stage: Needs verification

At 19:51 Beijing time on October 17, 2026, Xiao (@im_xiaoxiao) reports analyzing Amazon Prime's tvOS IPA with 'RAE+ghidra', finding its supported Universal Link format and enabling a personal app to jump directly to an animated show's playback page. Reverse engineering serves cross-app deep-link discovery, not video decryption, subscription bypass or a complete Prime-client rebuild. The post says RAE rather than REA and does not further establish the tool's identity, so the spelling is not silently corrected or treated as a confirmed REA test. Codex is explicitly mentioned in the working environment.

The author also reports that either RAE or Ghidra consumed 10G of disk per minute until the computer filled up and Codex could no longer execute, requiring manual disk-usage investigation. Attribution, the unit convention behind 10G and the growth mechanism are unverified; this is not generalized into a Ghidra or REA defect. No link format, IPA version, code, demonstration or jump-validation record is published in the post. Success remains author-reported, without implying compatibility with every show or tvOS version. Supplementary original-post reading confirms the author and full wording; no IPA was executed or independently reproduced here.

Source published: October 17, 2026, 19:51 Beijing time; the tool is written RAE, not silently changed to REA.
Successful navigation and 10G-per-minute disk growth are author reports without public implementation or test records.

## Sources

- [Xiao's Prime tvOS deep-link investigation and disk-failure account](https://x.com/i/status/2111424789827228006)

[中文](../prime-tvos-universal-link-ghidra-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
