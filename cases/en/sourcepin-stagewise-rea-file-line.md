# sourcepin: studying stagewise with REA to map page elements before calling a model

Category: Applications and clients · REA
Record date: 2026-10-21
Stage: In progress

At 06:19 Beijing time on October 21, 2026, Aayush Swami (Aayushswamidev) announces sourcepin after studying stagewise with REA. Users select an element on their local development site and describe a change; the tool finds its source location before asking AI to read and edit that file. The author reports 86 ms for a snapshot plus exact mapping.

Supplementary inspection of sourcepin commit 6c72ecef (05:27 Beijing time, October 21) found its v0.1 README and research notes. The target was open-source stagewise at 43c6b252, not recovery without source. The author read source directly and used REA 6.7.0 for static module/IPC graphs and feature traces. The whole-repository graph had 1,397 resource limitations and remained incomplete; focused traces also had partial coverage. Mapping uses React 19 development fiber._debugStack and Next.js error-overlay calls, then checks the opening tag on the line. Unsupported setups fall back to static JSX matching or text candidates, distinguishing exact, likely and unknown rather than claiming universal exactness.

The README reports correct mapping for 29 elements in a purpose-built small app, on macOS/Chrome with Next.js and React 19 development webpack. Turbopack is untested; Vue and Svelte are unsupported. The inspected public bench JSON contains five requests with and without mapping, using the same gpt-oss-120b through OpenRouter. All ten rows are correct, totaling 10 versus 15 tool calls and 15 versus 21 model steps. Documentation rounds average whole-turn time to 13.4 seconds in both conditions, so fewer steps do not establish end-to-end acceleration. A separate single stagewise run used a different test page, and Electron screenshots differed from headless Chrome; this is not a large controlled benchmark.

Public AGPL-3.0 code and evidence are inspectable. The author says it was written from scratch without copying stagewise code. This collection did not install or rerun it and has not independently validated the 86 ms, mapping accuracy, safety isolation or code provenance.

## Sources

- [Aayush Swami announces stagewise research and sourcepin](https://x.com/i/status/2112670162105376938)
- [sourcepin README at 6c72ecef: mapping, measurements and limits](https://github.com/aayushswami123/sourcepin/blob/6c72ecef36e7f7a713e8f7d2b49ff2c9a6e09908/README.md)
- [Static study notes: partial REA graph and source traces](https://github.com/aayushswami123/sourcepin/blob/6c72ecef36e7f7a713e8f7d2b49ff2c9a6e09908/docs/rea/01-source-map.md)
- [Project's raw five-request mapping-on/off comparison JSON](https://github.com/aayushswami123/sourcepin/blob/6c72ecef36e7f7a713e8f7d2b49ff2c9a6e09908/docs/rea/evidence/bench-openrouter-gpt-oss-120b.json)

[中文](../sourcepin-stagewise-rea-file-line.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
