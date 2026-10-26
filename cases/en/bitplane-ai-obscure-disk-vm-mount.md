# Old disk images: bitplane's reported guest-VM mounting tool and preserved rebuild toolchain

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-24
Stage: Needs verification

At 17:05:27 Beijing time on October 24, 2026, davidsong (@bitplane) lists an AI-assisted guest-VM mounting tool to help historians access obscure disk images from systems that no longer run. He reports building MacOS, RISC OS, TempleOS and seven other systems on Linux and running them in QEMU, including Darwin without Mac SDKs, alongside a cross-platform 9p server and Rust mkfs tools for test data.

The supplementary mountin README, last changed September 25, 2026 before this window, uses guest kernels and filesystem drivers, exposing read/write access over 9p, with rootless Podman builds and claimed source/output/container archives. It provides a format matrix for Linux, NetBSD, AROS, PureDarwin and others with project-reported end-to-end tests. However, it explicitly labels itself unstable, pre-alpha and experimental: guest selection, detection and launch layers remain under construction. Known NTFS, UFS and SysV paths fail or can crash a guest, and backups are required. This is not a promise of safe automatic access to arbitrary images.

Specific AI roles are not supplied. This collection downloaded no images, mounted nothing, rebuilt no systems and checked no archive completeness. MacOS and SDK-free claims remain attributed to the author; existing operating systems, filesystem drivers and QEMU are not AI achievements. The report remains unverified.

Explicitly experimental, with backup warnings and known driver failures or guest crashes. Format coverage and archives are project reports; neither execution nor archive completeness was verified.

## Sources

- [bitplane on old disk images and guest-VM tools, October 24, 2026](https://x.com/i/status/2113919789886218477)
- [Supplementary mountin README, last changed September 25, 2026](https://github.com/bitplane/mountin/blob/11aa2dba490ac0a234c763388dd7c30e8aa83d36/README.md)

[中文](../bitplane-ai-obscure-disk-vm-mount.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
