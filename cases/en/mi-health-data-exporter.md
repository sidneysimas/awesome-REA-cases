# Mi Health: timestamp repair and a cloud-data exporter

Category: Hardware and interoperability · REA use unconfirmed
Record date: 2026-10-15
Stage: In progress

The author first obtained a Xiaomi Sports Health SQLite database from a personal phone backup and exported it to AI, which suggested abnormal nighttime heart rates. Checking time, timeIn0Tz and zoneOffsetInSec revealed that the old export processed time zones twice, creating a 16-hour offset. The author then studied miothealth cloud authentication, RC4-Drop1024 and signing and published a pure-Python standard-library sync/CSV exporter to avoid repeated USB backups. Reading LilZeeCN/mi-health-exporter's README on October 15 confirmed eight CSV categories, merge-writing and timestamp design. However, daily summaries are limited to 100 entries per category without pagination, first password login was not validated with a real account for this release, and offline tests use synthetic data. The project includes neither the article's charts nor its AI skill and cannot guarantee full history. AI data analysis is explicit context, but AI protocol reverse engineering and REA use are unconfirmed. The article's medical conclusions excluding heart disease or inferring hearing damage from band data are not adopted.

No personal health database or credentials read; public-documentation inspection is not cloud-login validation.
Project documentation says session credentials are stored locally in plaintext files with mode 0600 where POSIX permissions are supported; users must protect both data and sessions.

## Sources

- [Author's research article](https://x.com/i/status/2110624271282139204)
- [Public implementation and limitations](https://github.com/LilZeeCN/mi-health-exporter)

[中文](../mi-health-data-exporter.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
