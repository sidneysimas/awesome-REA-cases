# Air-fryer voice control: vartekxx's REA evidence and human-confirmation workflow

Category: Hardware and interoperability · REA
Record date: 2026-10-23
Stage: Needs verification

At 04:35:41 Beijing time on October 23, 2026, @vartekxx reports using REA to inspect an owned air fryer's software and control logic, having Opus 5.5 map commands, states and safety limits, building a small temperature/timer/start/stop connector, and connecting it to Claude voice mode. The author gives a spoken 190-degree-Celsius, 30-minute request as the result, claiming operation without buttons or the vendor app.

The complete companion prompt at 04:40:15 is not an implementation: brand, model, firmware, connection and target path remain placeholders. It requires read-only evidence collection, local-versus-cloud distinction and recorded observations, inferences and unknowns. It considers an official local API, standards such as Matter/HomeKit/MQTT, a local interface legitimately used by the vendor app, then manufacturer-supported automation. If safe control cannot be proven, it must stop rather than assume connectivity.

Connector requirements include default dry-run, an exact device allowlist, manufacturer temperature/time limits, immediate human approval, emergency stop and state readback after each action. Bypassing pairing, safety locks or thermal limits, flashing firmware and unattended physical testing are forbidden. The voice layer reads back device, temperature and duration; only explicit approval authorizes one start. The prompt ends by requesting a plan, not an immediate physical command.

No exact model, protocol trace, source, tests or state screenshots are supplied, so a functioning connector and voice control remain unconfirmed. The 190-degree example is not a safe setting for arbitrary devices. This records an unverified interoperability workflow with an author completion claim; prompt safety requirements do not establish enforced safeguards. This collection read the author's thread but operated no device or target code.

Author update: October 23, 2026, 04:40:15 Beijing time.
Device model, source and measured tests absent; 190 degrees Celsius/30 minutes is only an example and safety gates are prompt requirements.

## Sources

- [Original author report: REA/Opus air-fryer voice control](https://x.com/i/status/2113368716297511327)
- [Full author prompt: proven interfaces, state readback and per-action confirmation](https://x.com/i/status/2113369868028256299)

[中文](../air-fryer-rea-opus-confirmed-voice-workflow.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
