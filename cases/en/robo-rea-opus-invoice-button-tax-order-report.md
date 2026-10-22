# Invoice-button reconstruction: Robo reports tiered REA/Opus analysis and a tax-order bug missed by green tests

Category: Applications and clients · REA
Record date: 2026-10-21
Stage: Needs verification

At 23:21:00 Beijing time on October 21, 2026, Robo (@0xRoboAI) posted a report about reconstructing an invoicing feature with REA and Opus 5.5. This is a deferred candidate from the earlier 20:00-24:00 window, not a project newly published in the current window. The stated goal is not to copy a whole paid application but to understand the behavior of one invoice button in an unnamed, reportedly $468/year app and create a separate implementation from a specification.

The post describes REA mapping 9,316 functions, Opus reading 214, and then producing SPEC.md and 50 tests. The reported split is 180 functions at low effort for $1.08, 31 at high effort for $1.27, and three at maximum effort for $1.14. Robo claims $3.49 total and 145 minutes, with the first 12 minutes spent by the user defining the goal. These are source-reported costs and times, not measurements by this collection. No billing record, tool trace or cache log was obtained to substantiate further claims of free scanning or cached input at $0.20 rather than $4 per million tokens; no general savings ratio is inferred.

The useful limitation is a test counterexample: the post says the first rebuild passed all 50 tests but still had one wrong rule. Moving the discount before tax reportedly left all 30 normal examples passing, with only two of ten edge examples detecting the change. The text does not fully reconcile those groups with the total of 50, or supply invoice inputs, tax jurisdiction, the original application's correct tax order or failure logs. It therefore does not establish whether discounts should precede or follow tax. The author also claims a zero-percent score under stacked obfuscation without defining the sample or scoring method; this is not generalized to all protection or all REA analysis.

An additional fetch of the original post confirms authorship and date. A video is attached but was not verified by playback here, and the linked article and implementation were not obtained. The retrieved material provides no product name, original build, executable specification, source code or comparison tests. This remains an unverified report, not an independent reproduction or a guarantee of eliminating a subscription. It concerns reported button behavior, not original-source recovery, and establishes no permission to copy an entire application.

Originally posted 2026-10-21T23:21:00+08:00; deferred review from the earlier October 21 20:00 to October 22 00:00 window.
9,316/214 functions, $3.49, 145 minutes and test counts are author-reported without original logs; fetching the source again does not refresh the result date.

## Sources

- [Robo's report on REA/Opus invoice-button reconstruction and a tax-order test counterexample](https://x.com/i/status/2112927137288028314)

[中文](../robo-rea-opus-invoice-button-tax-order-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
