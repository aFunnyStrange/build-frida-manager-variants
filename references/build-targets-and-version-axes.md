# Build Targets and Version Axes

## Keep product identities independent

Track at least four axes:

1. Manager product version and repository revision.
2. Frida runtime version and Android ABI.
3. Device Engine protocol and version-owned compatibility artifacts.
4. Common Hub, Agent, collaboration, and sync protocol/revision.

The root module combines them, but they do not become one version. A Hub built from one Manager revision is a
Manager release asset, not a Frida-version variant, unless repository evidence shows a Frida-specific Hub
contract. Public release names may include the Manager version; ordinary build outputs may use stable
platform names. Stage and rename deterministically in a release directory instead of manually changing files
in place.

## Build target contract

Inspect the maintained entrypoints before invoking them. In the verified repository example:

| Target | Required toolchains | Expected responsibility |
| --- | --- | --- |
| `engine <frida-version>` | Android SDK, locked NDK/CMake, matching Core devkit | Build only the Android ABI-specific native Engine |
| `sync` | Go | Test and build the Android collaboration/sync daemon; no Frida Core link |
| `remote` | Go | Test and build Android Agent/local Hub plus declared external Hub/ctl targets |
| `webui` | Node/npm | Run WebUI and Engine protocol fixtures, then generate the production bundle |
| `module <frida-version>` | all applicable toolchains | Assemble one selected runtime plus common services and WebUI |
| `all <frida-version>` | all applicable toolchains | Force a complete rebuild before assembly |

Resolve executable and SDK paths before changing working directory. `sdk.dir=...` is Android
`local.properties` syntax, not a shell command. On Windows set `ANDROID_SDK_ROOT` as an environment variable;
on POSIX export it. Android ABI is the target platform even when the host is Windows, macOS, or Linux.

## Three lock layers

- **Dependency acquisition lock**: upstream URL/archive, version, platform, hash, and source or devkit identity.
- **Runtime artifact lock**: final Engine, server, adapter, and every version-owned compatibility artifact as
  packaged, with protocol, ABI, qualification, provenance, and report.
- **Release manifest**: module, standalone server, common Hub/ctl, examples, notices, and final SHA-256 values.

Verify all three without treating one as a substitute for another. Registration is the normal producer of
the runtime lock. For Frida families that need a Java compatibility prelude, registration must build or accept
that prelude and lock it in the same transaction.

## Locked repackage semantics

A locked repackage is useful for Manager documentation, WebUI, or common-service changes. It must:

- leave every version-owned locked byte unchanged;
- verify those bytes before staging;
- rebuild only declared common/product artifacts;
- create a new module/release identity when common artifacts or packaging change;
- never claim to qualify native compatibility.

If an entrypoint named `--use-locked-engine` still rebuilds another artifact included in the runtime lock,
treat the name and behavior as a contract defect. Fix or narrow the entrypoint before using it for a release.

## Packaging policy

Normal release packaging accepts only `stable`. An isolated lab override may accept `unqualified` or
`experimental` and must label the result accordingly. `blocked` is quarantine state, not a stronger form of
experimental; ordinary module packaging and release staging must reject it.
