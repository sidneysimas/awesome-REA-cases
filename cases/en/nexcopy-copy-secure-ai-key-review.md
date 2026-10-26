# Nexcopy Copy Secure: AI traces viewers, configuration and 3DES content keying

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-25
Stage: Analysis test

The October 25 candidate at 07:18:48 Beijing time lists Nexcopy alongside other protection products. Xusheng Li's earlier official article, dated October 22 at 16:00 UTC, was read as supplementary evidence. This separate entry covers Nexcopy Copy Secure provisioned with Drive Wizard 1.0.81, with Windows and macOS viewers on the drive. Li says the Mac viewer retains Objective-C method names that help AI follow its design. The goal is checking whether copy protection and passwords actually constrain file encryption.

The original describes three-key Triple-DES CBC content encryption. A fixed value in the app opens an encrypted configuration that supplies a 24-byte content key and 8-byte IV. The password is only a separate UI string comparison; device identifiers are software checks, not content-key inputs. He presents the layouts of a 324-byte configuration and 140-byte test-file container, reporting that AI decrypted and restored his original file. Unpacking, cryptography tracing and finding the key-management failure reportedly took about ten minutes and five prompts.

The viewers also enumerate processes, intercept screenshot keys and use clipboard APIs, but these do not prevent inspection of client-side keying. These are researcher analysis and tests, not execution checks by this collection. They establish neither the same issue in every Nexcopy version or drive nor AI breaking the 3DES algorithm. No tool samples or third-party files were accessed, and configuration keys are not reproduced. The model and REA are unspecified. The candidate's shorthand about baked-in keys does not replace the actual two-stage key chain.

Drive Wizard 1.0.81, roughly ten minutes and five prompts follow the original report; no independent testing or all-product validation.

## Sources

- [Window candidate: Nexcopy protection-flaw account, October 25, 2026](https://x.com/i/status/2114134544836407379)
- [Earlier original: Xusheng Li's Nexcopy key chain and tests, October 22, 2026 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#nexcopy)

[中文](../nexcopy-copy-secure-ai-key-review.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
