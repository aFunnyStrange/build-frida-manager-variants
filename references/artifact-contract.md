# Frida Manager Variant Artifact Contract

## Required identity

Bind each candidate to:

- exact Frida version and Android ABI;
- official release URL and downloaded archive hash, or exact source revision/submodules/toolchain/patch set;
- matching frida-core devkit/source lock;
- Manager product version/revision, Engine protocol, and common-service protocol/revision;
- Device Engine filename and SHA-256;
- frida-server filename, provenance, and SHA-256;
- adapter filename, interface version, family, and SHA-256;
- qualification state and report path;
- every version-owned compatibility artifact, including generated Java-Bridge preludes when applicable.

Do not store credentials, browser cookies, private device identifiers, or proprietary app data in public locks.
Keep exact authorized scope and sensitive live evidence in an ignored local directory.

## Consistency rules

- Directory version, lock version, server/core version, and reported runtime version must agree.
- ABI must agree across the release asset, devkit, Engine, server, device, and package destination.
- Packaged hashes must be recomputed after copying; source hashes alone are insufficient.
- Adapter selection follows observed CLI behavior, not only the major version number.
- A qualification report must name the exact candidate hashes it evaluated.
- Dependency locks, runtime artifact locks, and release manifests must remain separate and cross-referenced.
- `stable` is attached to exact bytes; `blocked` bytes are excluded from ordinary packaging even when an
  experimental override exists.
