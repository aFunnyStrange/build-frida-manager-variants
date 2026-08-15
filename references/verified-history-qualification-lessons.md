# Verified Historical Tasks: Variant and Qualification Lessons

## Evidence scope

This reference uses both retrieved tasks in the `frida_manager` working directory: **熟悉并调整 Frida UI
管理器** and **查找 frida_manager 构建文档**. The first recorded Manager development, releases, and an
authorized compatibility matrix; the second clarified build targets, toolchains, output names, and the inputs
needed to add a version. The matrix later included Frida 17.10.1 and 17.17.0 across authorized arm64 Android
13, 14, and 16 environments, while 16.7.19 and 16.5.6 remained excluded after different runtime failures.
These are historical facts for exact candidates, not current upstream compatibility guarantees. A later read
of the completed first task, the local repository, and GitHub's public API confirmed that Manager v2.0.2 was
first published from `e54e3a3`, then explicitly replaced at final source commit `3c37c2f`. The final Release
still contained two stable Frida 17 runtime modules, two matching standalone servers, five Hub binaries, an
examples archive, and `SHA256SUMS` as exactly 11 public assets.

## Candidate identity lessons

1. Treat every native or generated change as a new candidate. Engine, Java-Bridge compatibility, adapter,
   common service, WebUI, and package changes repeatedly changed artifact or module hashes. Exact native bytes
   could not inherit the older binary's device qualification.
2. Downgrade a changed but untested stable variant to `experimental` until the exact final bytes pass the
   declared live matrix. Build, protocol fixtures, and a prior version's device success prove only `candidate`.
3. Compare three byte sets separately: source/build outputs, final packaged assets, and files installed on each
   device. The history caught a device-bundled Hub that differed from the current module tree even though other
   core files matched.
4. Keep old candidate hashes as historical evidence, never as co-current releases. A report must identify the
   exact Engine, server, adapter, compatibility prelude, module ZIP, common services, and Manager revision.
5. Keep Manager product identity separate from Frida runtime identity. Hub/ctl and other common services were
   built from the Manager protocol and release, while Engine/server/compatibility bytes were Frida-version
   owned. Packaging them together did not make the Hub a Frida-version-specific artifact.
6. The history exposed three contracts: official Core archive dependency locks, final packaged runtime locks,
   and release SHA-256 manifests. None substitutes for another.

## Compatibility matrix lessons

- Do not extrapolate between Android generations or root managers. Run every declared row and retain exact
  candidate hashes.
- Boot timing is part of compatibility. The first server start after boot required a once-per-boot readiness
  gate in one environment, while later same-boot restarts were fast.
- Process enumeration, Attach, and paused Spawn behavior varied. Qualify exact-PID Attach, Name Attach, normal
  Spawn, paused Spawn/Resume, target exit, and recovery independently.
- Arm64-only Android may legitimately run only the primary zygote. A readiness gate that required both zygote
  processes falsely blocked a compatible device; readiness must follow the actual ABI/zygote model.
- A Java/JNI demo initially failed because it called the native method through the wrong object and ran before
  the target library initialized. Correct the owned probe and regress it on the stable baseline before
  assigning the failure to a Frida candidate.
- Frida 16.x did not produce one family result. 16.7.19 passed bounded Android 13/14 stages but failed Android
  16 Attach; 16.5.6 disturbed process creation in another environment. A blocked live path requires a new
  hypothesis, isolation plan, exact authorization, rollback, and stopping conditions before any retry.
- A compatibility prelude can make traditional raw Java scripts work, but its framed bundle and exact bytes
  become part of the variant contract and live regression matrix.

## Build-system lessons

- Resolve repository and toolchain paths before changing working directories. `sdk.dir=...` belongs in
  `local.properties`; Windows shells need an environment variable such as `ANDROID_SDK_ROOT`.
- Provide and test native Windows `.bat` and POSIX `.sh` entrypoints when those hosts are promised. Windows
  delayed expansion can consume `!` inside validation expressions.
- `engine` built the version-specific native Engine; `sync`, `remote`, and `webui` built common components;
  `module` assembled them, and `all` forced a complete rebuild. The official server was a runtime/packaging
  input, not an Engine compile-time input.
- Target platform meant Android ABI, not host operating system. The remote target matrix separately built Hub
  and ctl binaries for desktop/server platforms.
- `frida-compile` output is framed, not always plain concatenable JavaScript. Disable source maps when required,
  parse the declared executable section strictly, and lock the resulting prelude bytes.
- The maintained registration entrypoint historically omitted the Frida 17 Java compatibility artifact.
  Manual hash edits made an immediate build pass but were not durable; the generator must own every
  version-specific artifact.
- A flag named `--use-locked-engine` still rebuilt the Java compatibility artifact. Rebuilding any locked
  version-owned byte contradicts an ordinary locked repackage and can cause unexplained hash churn.
- One experimental override admitted `blocked` as well as incomplete variants. `blocked` is quarantine state,
  not an opt-in package flavor; the variant stays excluded from ordinary builds/releases.
- If a root manager protects the mounted module tree, install the rebuilt ZIP through its supported installer
  and reboot instead of claiming a hot-swapped file was validated.

## Release and reporting lessons

- Ordinary build outputs and product-versioned Release asset names differed. Stage copies and rename them
  deterministically, then recompute hashes.
- Scan source, generated WebUI, ZIPs, examples, and staged assets. Keep exact device serials, private package
  names, workstation paths, credentials, and raw authorization evidence in ignored local files.
- Verify ignored examples intended for release are actually tracked.
- When moving a tag changes GitHub's automatic source archive, recreate or update the Release and verify every
  asset; the automatic source archive follows its tag target.
- A prepared tag or filled browser form is not a published Release. Verify tag target, uploaded assets,
  download links, hashes, and Latest state before reporting completion.
- The v2.0.2 browser bulk upload failed even though file access had already been enabled. Uploading assets
  individually, waiting for each progress state, counting 11 attached names before Publish, and querying the
  public release after navigation produced reliable completion evidence.
- A text-only privacy scan missed absolute workstation paths embedded in native Engine symbol metadata.
  Reproducible compiler prefix maps removed them, but also changed both Engine hashes. Apply and scan these
  flags before live qualification so the final released bytes, lock, and report remain one candidate.
- GitHub's public API exposed SHA-256 digests for every uploaded asset. Those digests matched the local manifest
  entries; the API digest for `SHA256SUMS` separately proved the manifest file itself.
- The published 17.10.1 lock referenced a public validation summary, but that summary did not contain the final
  artifact digests. The 17.17.0 stable lock omitted `qualification.report`. Treat both as evidence-chain gaps:
  successful release publication and runtime qualification do not replace cryptographic report binding.
- The final five-device matrix covered each device's standalone and local-RPC path, the complete collaboration
  flow on maintained baseline rows, five explicit external-Hub routes, one automatic group route, a second
  reboot/restore pass, and installed-file hash checks. This proves only that exact sanitized matrix.
- A client request set exactly to the 30-second server ceiling crossed a scheduling/clock boundary; a 25-second
  client budget passed while the server ceiling remained unchanged. Five-branch presence needed a separate
  60-second convergence window. Operation deadlines, online TTL, and discovery convergence are independent.
- The final same-version replacement exposed several release-tool failures: PowerShell 5 binary upload through
  `Invoke-WebRequest` raised an internal null-reference error, console output was buffered, and GitHub asset
  renaming returned 404 after temporary uploads. The resumable script reused verified uploads and ultimately
  uploaded exact final names, then verified all 11 assets and absence of temporary names through the API.
- A fixed token-shaped value in a demo test survived earlier filename-oriented checks. Public scans must inspect
  release-bound examples and test data for credential-shaped literals, even when they are believed to be fake.

## Qualification ladder learned from the tasks

### Candidate

- exact official prebuilt or locked source provenance;
- matching server/core/adapter/ABI/protocol and compatibility identity;
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
- documentation and sanitized qualification reports name exact hashes and unsupported dimensions.

### Blocked

- a reproducible safety, startup, protocol, or runtime failure prevents promotion;
- the failure and cleanup evidence remain recorded;
- ordinary package and release paths reject the candidate even when experimental builds are enabled.
