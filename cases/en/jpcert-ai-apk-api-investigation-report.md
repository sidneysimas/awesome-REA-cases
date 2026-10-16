# JPCERT/CC: tracing APK analysis and API probing on attack servers

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-16
Stage: Analysis test

An October 16 post by @satorukatsuno01 discusses a series of unauthorized-access incidents and points to JPCERT/CC's October 15 investigation. This review read that official original: investigators report confirming AI use for known-vulnerability scans and API attacks, finding traces of APK analysis followed by investigation of associated APIs for vulnerabilities such as SSRF, and finding APKs and Blutter/jadx-related files on another server. The target activity is identifying attackable service interfaces through Android/Flutter clients. The official result is infrastructure and analysis evidence, not proof of complete app decompilation. The report does not disclose the AI model, exact stages of use or REA, so co-located tools do not establish an autonomous AI attack chain. The candidate separately quotes another company's observation of 326 IP addresses and over 1,200 requests in about 40 minutes, while explicitly noting it is neither direct AI evidence nor tied to this incident. Those numbers are not merged into JPCERT's findings. This collection read public reports and neither accessed target services nor reproduced attacks. The October 15 original is retrospective supporting evidence, not a newly published report in the current window.

Candidate published: 2026-10-16 18:56 Beijing time; official report dated 2026-10-15.
AI use is reported by investigators; model and automation of individual steps undisclosed, REA unconfirmed.

## Sources

- [October 16: @satorukatsuno01's investigation commentary](https://x.com/i/status/2111048734926836191)
- [October 15 official JPCERT/CC investigation (retrospective supporting evidence)](https://blogs.jpcert.or.jp/ja/2026/10/web_api_attacks.html)

[中文](../jpcert-ai-apk-api-investigation-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
