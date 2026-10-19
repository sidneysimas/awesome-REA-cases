# Instagram 448: Claude/REA investigation of Reels-ranking clues in APK strings

Category: Applications and clients · REA
Record date: 2026-10-19
Stage: Analysis test

At 18:02 Beijing time on October 19, @err_cod explains an Instagram Reels-ranking investigation: extract Android version 448.0.0.52.84 from a rooted phone, use Claude Code (Opus 4.8), REA MCP, ADB, strings and grep to extract about 787,000 text lines from 22 code files, then search ranking-related names individually. The motivation is understanding why the author's Reels do not spread.

Reading the same-minute author conversation identifies pwatch, pcomments, psendbutton, reels_skip_rate, MIXED_UNCONNECTED, CLIPS_AUDIO/AUTHOR/TOPIC_NOT_INTERESTED and incrementality score. The author interprets these as watch completion, comments, sends, client-side reranking, mixing unconnected accounts and not-interested feedback, then offers content advice. This entry records the author's interpretation of client strings, not a verified ordering of signal importance, actual activation for every user or server-side causal mechanism.

At 18:02:17 the author explicitly cautions that real names appearing in the app show related functionality in code, not exact signal weights. The supplied APK SHA256 is abbreviated and cannot identify an exact file for verification. No complete APK hash, inspectable extraction, call trace or live controlled experiment was obtained. This collection neither acquired the APK, executed the app nor independently reproduced the work. The candidate and supplementary conversation are dated October 19; supplements explain rather than replace the original candidate.

Candidate snapshot: 2 likes, 78 views and 0 reposts; engagement on other conversation posts is not attributed to this candidate.

## Sources

- [Candidate: err_cod specifies version, scale and Claude/REA tools](https://x.com/i/status/2112122149695848613)
- [Supplementary author-thread opening: Reels distribution question](https://x.com/i/status/2112122119643627844)
- [Supplement: pwatch, pcomments and psendbutton](https://x.com/i/status/2112122123686936985)
- [Supplement: client-ranking and skip-rate interpretation](https://x.com/i/status/2112122127608594581)
- [Author's supplementary caveat: names are not exact weights](https://x.com/i/status/2112122152589873174)

[中文](../instagram-448-ranking-rea-strings.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
