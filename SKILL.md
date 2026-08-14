---
name: build-frida-manager-variants
description: DRAFT/INACTIVE. Acquire or build, lock, integrate, package, and qualify an exact Frida version for an authorized Frida Manager across frida-server, frida-core Device Engine, version adapter, root-module assets, and release evidence. Use when the user asks for an xx-version Frida server compatible with Frida Manager, a new ABI/version variant, compatibility diagnosis, or promotion from experimental to stable. Distinguish official prebuilt acquisition from source compilation and never infer runtime compatibility from build success.
---

# Build Frida Manager Variants

## Status and authorization

This Skill is a draft. Use it only for Skill development and validation until explicitly activated. Building
and statically inspecting artifacts does not authorize injection. Live qualification is limited to explicitly
named user-owned devices and owned/source-available test apps. Refuse third-party or system-process injection,
access-control bypass, credential extraction, stealth, or persistence.

## Fix the variant identity

Before downloading or building, record the independent version axes:

- exact Frida version and release source;
- Android ABI and intended Android/device/root-manager matrix;
- Manager product version/revision and Engine protocol version;
- common-service protocol/revision for Hub, Agent, collaboration, and sync artifacts;
- server acquisition mode: official prebuilt or source build;
- matching frida-core devkit/source and Engine build mode;
- server-adapter family/interface version;
- requested output: local candidate, installable module, or release asset.

Ask when any identity field changes the artifact set. Do not describe unpacking an official `frida-server`
release as compilation. If source compilation is requested, lock source commits, submodules, toolchains,
patches, and reproducible commands separately.

Use current official Frida release/source information when selecting a version or URL. Treat repository locks
as verified repository evidence, not proof that upstream is still current.

Do not encode the Frida version into Hub release identity unless the Hub protocol actually changes. Read
[build-targets-and-version-axes.md](references/build-targets-and-version-axes.md) before choosing a build
target, toolchain, lock, output name, or release-staging name.

For failures involving version promotion, Android/root-manager differences, boot readiness, generated
artifacts, installed-file hashes, or release packaging, read
[verified-history-qualification-lessons.md](references/verified-history-qualification-lessons.md). Its facts
come from two retrieved tasks and must be requalified for new versions and environments.

## Select the workflow

1. **Official-prebuilt route**: acquire the exact server and devkit from official release assets, verify hashes,
   build the matching Engine, select or implement a typed adapter, and package a candidate.
2. **Source-build route**: first justify why the prebuilt route is insufficient, then lock and build all source
   inputs. Never mix an untracked server build with a release devkit merely because versions look similar.
3. **Existing variant diagnosis**: verify the lock and bytes first, reproduce the failing layer, and classify it
   as acquisition, build, packaging, startup, protocol, or runtime compatibility failure.

Follow [artifact-contract.md](references/artifact-contract.md). Run the read-only checker before packaging:

```powershell
python scripts/check_variant_readiness.py <frida-manager-root> --version <x.y.z>
```

## Build and integrate

Keep Frida-version-specific CLI behavior in a typed server adapter. Do not expose free-form command fragments
through UI, shell, sync, or remote inputs. Build the Engine against the exact locked core interface and retain
compiler/linker identity. Register the variant through the Manager's maintained generator when one exists;
do not hand-edit generated locks or package trees. The generator must include every version-owned compatibility
artifact. If registration omits one, fix the generator before using the candidate rather than completing the
lock manually.

Treat dependency acquisition locks, packaged runtime artifact locks, and release manifests as different
contracts. A locked-artifact repackage must verify and reuse every version-owned byte. It must not rebuild a
compatibility prelude or another locked artifact under a flag that claims to reuse locked artifacts.

Every variant lock must bind the Frida version, ABI, Manager protocol, Engine bytes, server bytes and source,
adapter bytes/interface, qualification state, and report reference. Hash both inputs and final packaged files.
For a qualified state, require the referenced report to contain the exact locked artifact digests, not merely
the same version label or Android matrix.

Any change to Engine source, compatibility prelude, adapter, server bytes, packaging, or generated WebUI
creates a new candidate identity. Do not carry a previous binary's `stable` label across the hash change.

## Qualify by gates

Use [qualification-matrix.md](references/qualification-matrix.md). Keep these outcomes distinct:

- `candidate`: identity, hashes, structure, and builds pass;
- `experimental`: bounded protocol tests pass but the supported live matrix is incomplete;
- `stable`: the declared device/app/root-manager matrix passes the full live regression and restart recovery;
- `blocked`: a reproducible safety, startup, protocol, or runtime failure prevents promotion and ordinary
  packaging.

Build success, `--version`, an open port, and one successful spawn or attach never imply `stable`. An
experimental override may package `unqualified` or `experimental` candidates only in an isolated lab path;
it must not make `blocked` variants packageable. A blocked older version must not be retried on the same live
path without a new hypothesis, isolation, and explicit authorization.

Keep ordinary validation separate from release publication. Publishing a GitHub Release, pushing a tag, or
uploading assets is an external mutation and requires the user's explicit request. Follow
[release-and-reporting.md](references/release-and-reporting.md).

## Finish safely

After live tests, detach sessions, stop owned target processes and Manager runtime, restore the default port and
configuration, and verify no stale server remains. Report candidate hashes, qualification class, exact tested
matrix, untested dimensions, failures, cleanup, and whether any external release action was performed. After
publication, verify the public release state, asset inventory, and provider-reported digests instead of relying
on the completed upload form.
