# Brother's scan button: Claude and REA connect Scan to PC to NAS and object storage

Category: Hardware and interoperability · REA
Record date: 2026-10-18

At 18:39 Beijing time on October 18, @aurimasniekis reports reverse-engineering Brother's Scan to PC button application for his parents' printer, sending scans to SMB, FTP, S3 or a local directory without leaving a personal computer running Brother's software. He attributes the work to Claude and REA, says roughly one hour solved the problem, and did not pursue deeper printer-firmware research. A host or NAS running the Go service is still required: this is not serverless uploading directly from the printer.

Supplementary reading of the same-day author thread and public README identifies protocol research into NETserver and BRPhoenixConnection from macOS Push Scan Tool 2.3.1 and libLxBsScanCoreApi from Linux brscan5, the latter explicitly analyzed with REA and Ghidra. Scan command handling builds on prior brother-scand work and also references sane-airscan. The service registers as a selectable PC through HTTPS/SNMP, receives button events on UDP 54925, and retrieves panel settings and scan data through TCP 54921. The author reports honoring PDF, multi-page TIFF, JPEG and color/gray/black-and-white choices, with a web interface for scan history, downloads and custom scans.

The README explicitly reports testing only a Brother MFC-L2800DW on firmware 1.32; other models are expected compatibility, not tested coverage. It lists amd64, arm64 and armv7 images and an approximately 13MB image, all project documentation rather than builds run by this collection. OCR text formats fall back to PDF without text recognition; PDF/A, secure and signed PDF choices are saved as ordinary PDF. Public documentation and the implementation repository were located, but no target, image, integration tests or physical scans were run here. Success for every destination, resolution and model is not established, and software interoperability must not be described as a firmware compromise.

October 18 candidate snapshot: main post 0 likes, 18 views; not independent scan validation. Only project-reported testing on MFC-L2800DW firmware 1.32; approximately one hour and 13MB are author/project figures.
GitHub API dates repository creation to October 17 at 19:47 UTC, October 18 at 03:47 Beijing time; repository documentation is supplementary verification, not another candidate.

## Sources

- [Aurimas Niekis's Claude/REA scan-button report](https://x.com/i/status/2111769060631609593)
- [Same thread: roughly one hour, three image architectures and tested model](https://x.com/i/status/2111769069020176520)
- [Same-day supplement: registration, UDP events and protocol sources](https://x.com/i/status/2111769064590970940)
- [Same-day supplement: panel formats and web interface](https://x.com/i/status/2111769066360766602)
- [Public Go project and README: compatibility, protocols and prior work](https://github.com/aurimasniekis/go-brother-scan-to-network-server)

[中文](../brother-scan-button-claude-rea-server.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
