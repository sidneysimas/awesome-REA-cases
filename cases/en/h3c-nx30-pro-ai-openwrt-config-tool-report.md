# H3C NX30 Pro: an author reports AI-assisted inspection, Python tool adaptation and OpenWrt flashing

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-23
Stage: Needs verification

In a post at 11:38:34 Beijing time on October 23, 2026, the author describes replacing H3C NX30 Pro factory firmware V100R010 with OpenWrt for home-network use. They say they neither programmed nor opened the device, instead connecting cables, pressing buttons, typing commands and taking photos under an unnamed AI's guidance. This was not an independently discovered AI vulnerability: the author explicitly credits AI finding ArtiSheng's same-version record, derived from chariri's (@chariri) article, and reading two existing tools.

According to the report, AI ported an open-source Rust tool to Python and wrote a configuration-modification script, obtaining a root shell through the factory configuration-restore path. It also requested backups of ten flash partitions, preservation of factory BL2, and hash checks on boot and release firmware. After repeated temporary-TFTP timeouts, AI reportedly combined code inspection and photographed logs to attribute the problem to Windows Firewall handling of negotiated ports. The author reports a subsequent 9.1MB transfer in 1.2 seconds and seeing the OpenWrt 25.12.6 interface at 05:21. Times, versions, counts and transfer results are author claims, not measurements by this collection.

No original repository URL, ported script, complete logs, image-verification records or running tests were obtained. The post names neither the model nor REA. The claim that the tools had no backdoors recounts an AI review and cannot establish safety. This records AI-assisted understanding, adaptation and diagnosis of existing device tools, not universal unlocking, a new vulnerability or autonomous flashing. No target was downloaded or run; disabling all firewall protection is not recommended as routine practice.

Source: October 23, 2026, 11:38:34 Beijing time.
Ten partitions, 9.1MB/1.2 seconds, 05:21 and OpenWrt 25.12.6 are author reports; prior research credited to ArtiSheng and chariri.

## Sources

- [Author's NX30 Pro account: configuration-tool adaptation, transfer diagnosis and flashing result](https://x.com/i/status/2113475139216314799)

[中文](../h3c-nx30-pro-ai-openwrt-config-tool-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
