# Telegram trading bot: cypher pepe reports Claude Code finding clipboard exfiltration by static inspection

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-23
Stage: Needs verification

At 00:57:12 Beijing time on October 23, 2026, cypher pepe (@cypher_frog) describes inspecting an unnamed sniper bot shared in a private Telegram chat. Such bots monitor pending transactions for rapid purchases. He says it came with GitHub source, an English README, a demonstration video and 200 stars, but provides no repository or sample identity. He explicitly says he did not run it. Instead he asked Claude Code to decompile it, enumerate network calls and system-resource access, and identify behavior outside its advertised purpose, reportedly receiving a report in 70 seconds.

The alleged findings are startup checks for standard MetaMask, Phantom, Rabby and keystore paths followed by a POST reporting those paths; clipboard reads and transmission every 30 minutes; and branches disabling suspicious functions in a virtual machine or sandbox. He also claims the same IP hosted another bot. Looking back over four bots in a month, he describes one as clean, one as having possibly legitimate analytics, and two as exfiltrating clipboard contents and scanning the filesystem; the latter two allegedly did not match their published source. Timing, counts, network location, trading functionality and build mismatches are all claims in the post, not findings by this collection.

An additional fetch recovered the full ending and prompt for network destinations and frequency, wallet paths, clipboard behavior, environment detection and source comparison. This completes the same candidate rather than adding another. No binary hash, repository, decompiler report, packet capture, build comparison or execution log was obtained. Since the author says he did not run it, normal trading and non-sandbox behavior cannot be treated as dynamically verified. Environment checks alone also do not establish that arbitrary software is malicious. This remains an unverified static-analysis report, not a confirmed malware-family attribution or a guarantee that a 70-second review proves software safe. This collection downloaded no sample and accessed no wallet or alleged exfiltration endpoint.

Originally posted 2026-10-23T00:57:12+08:00. The 70 seconds, 30-minute interval, 200 stars and four-sample counts are author statements, not independently checked.

## Sources

- [cypher pepe's full report and prompt for Claude Code inspection of an unnamed trading bot](https://x.com/i/status/2113313734831526252)

[中文](../cypher-pepe-claude-sniper-bot-static-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
