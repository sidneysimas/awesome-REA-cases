# REA plus Jev: an idea for sending high-risk findings back for more evidence

Category: Applications and clients · REA
Record date: 2026-10-22
Stage: Needs verification

At 01:25 Beijing time on October 22, 2026, Jey (@0xJeyx) proposes sending every REA finding about a closed application, together with evidence and limitations, to Jev for a probability of being wrong. A score above 0.5 sends the finding back to REA for more evidence; the rest proceeds into the rebuild. This is a concrete idea for reducing implementation errors through additional investigation, not a completed experiment on a named application.

The post claims that on 98 real agent traces, including 61 known failures, Jev caught 54 failures at the default 0.50 threshold with 71% precision. It also claims calibrated scores, interpreting 0.8 as roughly eight out of ten equally scored traces failing, and a price of $0.019 per 100 checks. No dataset, failure annotations, calibration curve, public code or REA-specific test is provided. These self-reported metrics are not correctness rates for reverse-engineering findings or proof that a score below 0.5 makes a finding safe to use. A 71% precision means flagged items still contain false alarms, not that all unflagged items are reliable.

This entry records the proposed risk-scoring and re-investigation loop only. Jev was not called or paid for, and calibration was not retested here. It cannot replace checking addresses, raw bytes and behavioral evidence for individual findings.

October 22, 2026 candidate snapshot: 24 likes, 333 views, 2 reposts; source update: 2026-10-22T01:25:21+08:00. Engagement does not validate the scorer.

## Sources

- [Jey's REA-to-Jev scoring and re-investigation proposal, with self-reported metrics](https://x.com/i/status/2112958430033990012)

[中文](../jev-rea-finding-risk-loop-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
