# Electric-kettle interoperability: a read-only-first REA/Opus prompt with on-site confirmation

Category: Hardware and interoperability · REA
Record date: 2026-10-24
Stage: Needs verification

At 04:49:28-29 Beijing time on October 24, 2026, vartekx (@vartekxx) first claims control of a kettle from bed using Opus 5.5 and REA, then publishes a complete interoperability prompt. The concrete design is to inspect only an owned or authorized device's official application, firmware or user-supplied artifacts; establish the model, versions, manual and authorization; wait for human plan approval; and perform read-only analysis to identify local or cloud interfaces, pairing and message formats before deciding whether to implement status, temperature, target-temperature, start and stop functions. No filled-in device identity or actual protocol finding is supplied.

The prompt prefers official APIs or supported standards such as Matter, HomeKit and MQTT, then authorized local interfaces used by the official application. Findings must cite files, symbols, logs, traces or screenshots and distinguish facts, observations, inferences, unknowns and next tests. A minimal read-only request must be compared with physical state; if no safe interface is established, stop rather than invent a workaround. The connector should default to dry run, allowlist the exact device, derive temperature/duration limits from the manual, fail safely on disconnection, avoid automatic heating retries, keep local audit logs and include unit and integration tests. Stopping must require no additional confirmation.

Crucially, the prompt forbids firmware flashing, credential extraction, pairing bypasses and bypasses of temperature control, boil-dry protection, automatic shutoff or other safeguards. The owner must be physically present before starting and explicitly confirm adequate water and a closed lid for each action; ambiguity, expired approval or missing state verification cancels it. Eighty degrees Celsius is a voice-request example, not a tested device temperature. The control-from-bed introduction does not override these on-site requirements or establish safe real-world heating. No code, device responses, test results or independent reproduction are supplied. All safeguards are design requirements, not passed checks. This is an interoperability workflow idea; this collection connected to and started no device.

Sources: October 24, 2026, 04:49:28 and 04:49:29 Beijing time; 80 degrees Celsius is an example only, with no exact model or test results.

## Sources

- [vartekx's introductory kettle-control report, October 24, 2026](https://x.com/i/status/2113734573645324633)
- [The author's full prompt: read-only investigation, on-site approval and fail-safe stopping, October 24, 2026](https://x.com/i/status/2113734577693020353)

[中文](../kettle-rea-evidence-first-control-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
