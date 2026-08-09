# Build Frida Manager Variants

> Status: **draft-inactive**. Static validation is available; representative version onboarding and authorized
> live compatibility qualification are still required before activation.

This Skill acquires or builds, locks, packages, and qualifies an exact Frida version for Frida Manager. It
keeps `frida-server`, the frida-core Device Engine, the typed server adapter, root-module assets, and release
evidence consistent while separating build success from runtime compatibility.

It explicitly distinguishes downloading an official prebuilt server from compiling Frida from source.

The Skill includes qualification lessons extracted only from the retrieved task “熟悉并调整 Frida UI
管理器”, including candidate hash churn, installed-file comparison, Android/root-manager matrix differences,
boot readiness, blocked-version handling, native build entrypoints, and GitHub Release asset integrity.

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
- `references/`: artifact contract, compatibility matrix, and release evidence.
- `references/verified-history-qualification-lessons.md`: retrieved variant failures and promotion gates.
- `scripts/check_variant_readiness.py`: read-only lock/hash/structure checker for a Manager variant.
