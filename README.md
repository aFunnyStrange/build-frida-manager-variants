# Build Frida Manager Variants

> Status: **draft-inactive**. The v2.0.2 repository, authorized matrix, and completed public release now provide
> representative evidence. Exact report-to-digest binding, an independent forward use, and explicit activation
> approval remain.

This Skill acquires or builds, locks, packages, and qualifies an exact Frida runtime for Frida Manager. It
keeps `frida-server`, the frida-core Device Engine, typed server adapter, version-owned compatibility assets,
root-module package, and release evidence consistent while separating build success from runtime
compatibility. It distinguishes official prebuilt acquisition from source compilation.

The workflow combines verified lessons from both retrieved `frida_manager` tasks. It covers
product-versus-runtime version axes, build targets and toolchains, three lock layers, candidate hash churn,
Android/root-manager matrices, blocked-version quarantine, and GitHub Release asset integrity.
The completed and later explicitly replaced v2.0.2 review also adds five-device clustered qualification,
deadline-versus-convergence rules, native binary path-redaction, resumable same-version replacement safeguards,
and post-publication provider-digest checks.

## Install for Codex

Do not install this draft until it is activated. After activation, link the complete
`build-frida-manager-variants/` source directory into the user Skill directory. The linked directory must
directly contain `SKILL.md`; do not install by copying editable sources.

Windows PowerShell:

```powershell
$skillsRoot = Join-Path $HOME ".agents\skills"
$source = (Resolve-Path "<repository-root>\build-frida-manager-variants").Path
$link = Join-Path $skillsRoot "build-frida-manager-variants"
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
if (Test-Path -LiteralPath $link) { throw "Destination already exists: $link" }
New-Item -ItemType Junction -Path $link -Target $source | Out-Null
```

macOS:

```bash
skills_root="$HOME/.agents/skills"
source_dir="$(cd "<repository-root>/build-frida-manager-variants" && pwd)"
link_path="$skills_root/build-frida-manager-variants"
mkdir -p "$skills_root"
if [ -e "$link_path" ] || [ -L "$link_path" ]; then echo "Destination already exists: $link_path" >&2; exit 1; fi
ln -s "$source_dir" "$link_path"
```

After activation, invoke it as `$build-frida-manager-variants`. For cross-agent reuse, CC Switch v3.13 or
newer can scan/import the local Skill from `~/.agents/skills` and sync compatible targets. Review each target
agent's format, tools, and permissions after import.

## Files

- `SKILL.md`: identity, acquisition/build, packaging, qualification, and release gates.
- `references/build-targets-and-version-axes.md`: identities, toolchains, targets, locks, and locked repackage
  semantics.
- `references/`: artifact, matrix, release, and verified-history evidence.
- `scripts/check_variant_readiness.py`: read-only lock/hash/structure checker for a Manager variant.
