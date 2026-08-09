# Verified Historical Task: Variant and Qualification Lessons

## Evidence scope

This reference uses only the retrieved task **“熟悉并调整 Frida UI 管理器”**. The other task in the same
working directory was excluded. The recorded matrix included Frida 17.10.1 on two authorized arm64 Android
environments using different Android generations and root managers. An older Frida 16.5.6 path remained
blocked after serious runtime instability. These are historical facts, not current upstream compatibility
guarantees.

## Candidate identity lessons

1. Treat every native or generated change as a new candidate. In the task, Engine logging, Spawn recovery,
   Java-Bridge handling, and adapter/package changes repeatedly changed the Engine or module hash. Each new
   hash required a new lock and could not inherit the older binary's device qualification.
2. Downgrade a changed but untested stable variant to `experimental` until the exact final bytes pass the
   declared live matrix. Build, protocol fixtures, and a prior version's device success prove only `candidate`.
3. Compare three byte sets separately: source/build outputs, final packaged assets, and files installed on each
   device. The task caught a device-bundled Hub that differed from the current module tree even though other
   core files matched.
4. Keep old candidate hashes as historical evidence, never as co-current releases. A report must identify the
   exact Engine, server, adapter, module ZIP, Hub, and Manager revision it tested.

## Compatibility matrix lessons

- One Frida version passed on both an Android 16/SukiSU-class environment and an Android 13/KernelSU
  Next-class environment, but the failure modes differed. Do not extrapolate “newer Android passed, therefore
  older Android passes”; run the matrix.
- Boot timing is part of compatibility. The first server start after boot required a once-per-boot readiness
  gate in one environment, while later same-boot restarts were fast.
- Process enumeration and paused Spawn behavior varied by Android environment. Qualification must cover PID
  Attach, Name Attach, normal Spawn, paused Spawn/Resume, target exit, and recovery independently.
- A version that compiled and performed limited operations still remained blocked after target and system
  instability. Never retry a blocked live path without a new hypothesis, isolation plan, exact authorization,
  rollback, and stopping conditions.
- A new compatibility prelude can make traditional raw Java scripts work, but its Frida bundle framing and
  version-locked bytes become part of the variant contract and live regression matrix.

## Build-system lessons

- Use repository-resolved absolute toolchain paths before changing working directories; otherwise a valid
  bundled toolchain can appear missing.
- Provide native Windows `.bat` and POSIX `.sh` entrypoints when the product promises those platforms. Test
  the entrypoints themselves, not merely their underlying commands.
- Windows delayed expansion can consume `!` inside validation expressions. Prefer batch-safe expressions and
  add a real Windows packaging test.
- `frida-compile` output is a framed bundle, not always plain concatenable JavaScript. Disable source maps when
  required, parse the declared executable section strictly, and include the resulting prelude hash in the
  artifact lock.
- If a root manager protects the mounted module tree, install the rebuilt ZIP through the supported module
  installer and reboot instead of claiming a hot-swapped file was validated.

## Qualification ladder learned from the task

### Candidate

- exact official prebuilt or locked source provenance;
- matching server/core/adapter/ABI/protocol identity;
- deterministic build and package output;
- final packaged hashes verified;
- static and protocol fixtures pass.

### Experimental

- candidate gates pass;
- some bounded host or device tests pass;
- exact final bytes have not completed every declared device/root-manager/app/lifecycle row.

### Stable

- exact installed files match the final package;
- normal and paused Spawn, PID and Name Attach, script load/RPC/Reload, Detach/Kill, restart recovery, custom
  port restoration, boot persistence, and cleanup pass on every declared row;
- documentation and the qualification report name the exact hashes and unsupported dimensions.

### Blocked

- a reproducible safety, system stability, startup, protocol, or runtime failure prevents promotion;
- the variant stays excluded from ordinary builds/releases even if compilation succeeds.

## Release lessons

- Verify ordinary build paths separately from release publication.
- Before release, compare installed validated module files with the release staging tree, then hash the final
  module ZIP, standalone server, every Hub binary, example archive, and checksum manifest.
- Keep public examples tracked and secrets/private evidence ignored. Inspect the generated archive, not only
  source control status.
- A GitHub Release's automatic source archive follows its tag target. If a tag is deliberately moved, verify
  whether the existing Release must be recreated and re-upload every asset with fresh checksums.
- Publish only after the final asset set is stable; post-build documentation or generated-file changes can
  invalidate previously recorded hashes.
