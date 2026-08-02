#!/usr/bin/env python3
"""Read-only structural and hash audit for one Frida Manager variant."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
RELEASE_STATES = {"candidate", "experimental", "stable", "blocked"}


def sha256_file(path: Path) -> str:
    """Return a lowercase SHA-256 digest without modifying the file."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON object and raise a useful error for another top-level type."""
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError("top-level JSON value must be an object")
    return value


def require_mapping(lock: Dict[str, Any], key: str, errors: List[str]) -> Dict[str, Any]:
    """Return a required child object or record an error."""
    value = lock.get(key)
    if not isinstance(value, dict):
        errors.append(f"artifact-lock.json: {key} must be an object")
        return {}
    return value


def verify_artifact(
    variant_dir: Path,
    section_name: str,
    section: Dict[str, Any],
    errors: List[str],
) -> None:
    """Verify a locked artifact filename, digest shape, file presence, and bytes."""
    filename = section.get("file")
    expected = section.get("sha256")
    if not isinstance(filename, str) or not filename or Path(filename).name != filename:
        errors.append(f"artifact-lock.json: {section_name}.file must be one filename")
        return
    if not isinstance(expected, str) or SHA256_PATTERN.fullmatch(expected.lower()) is None:
        errors.append(f"artifact-lock.json: {section_name}.sha256 must be 64 hex characters")
        return
    artifact = variant_dir / filename
    if not artifact.is_file():
        errors.append(f"missing {section_name} artifact: {artifact}")
        return
    actual = sha256_file(artifact)
    if actual != expected.lower():
        errors.append(
            f"{section_name} hash mismatch: expected {expected.lower()}, actual {actual}"
        )


def audit_variant(manager_root: Path, version: str) -> List[str]:
    """Audit one version directory and return deterministic error messages."""
    errors: List[str] = []
    variant_dir = manager_root / "magisk_module" / "bin" / version
    lock_path = variant_dir / "artifact-lock.json"
    if not lock_path.is_file():
        return [f"missing variant lock: {lock_path}"]
    try:
        lock = load_json(lock_path)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        return [f"cannot read {lock_path}: {error}"]

    if lock.get("fridaVersion") != version:
        errors.append(
            "artifact-lock.json: fridaVersion must match the requested version directory"
        )
    protocol = lock.get("protocolVersion")
    if not isinstance(protocol, int) or isinstance(protocol, bool) or protocol < 1:
        errors.append("artifact-lock.json: protocolVersion must be a positive integer")
    abi = lock.get("abi")
    if not isinstance(abi, str) or not abi.strip():
        errors.append("artifact-lock.json: abi must be a non-empty string")

    qualification = require_mapping(lock, "qualification", errors)
    release_status = qualification.get("releaseStatus")
    if release_status not in RELEASE_STATES:
        errors.append(
            "artifact-lock.json: qualification.releaseStatus must be candidate, "
            "experimental, stable, or blocked"
        )
    report = qualification.get("report")
    if not isinstance(report, str) or not report.strip():
        errors.append("artifact-lock.json: qualification.report must be recorded")
    elif release_status in {"experimental", "stable", "blocked"}:
        report_path = manager_root / report
        if not report_path.is_file():
            errors.append(f"qualification report does not exist: {report_path}")

    engine = require_mapping(lock, "engine", errors)
    server = require_mapping(lock, "server", errors)
    adapter = require_mapping(lock, "adapter", errors)
    for section_name, section in (
        ("engine", engine),
        ("server", server),
        ("adapter", adapter),
    ):
        verify_artifact(variant_dir, section_name, section, errors)

    source = server.get("source")
    if not isinstance(source, str) or not source.strip():
        errors.append("artifact-lock.json: server.source must record provenance")
    interface_version = adapter.get("interfaceVersion")
    if not isinstance(interface_version, int) or isinstance(interface_version, bool):
        errors.append("artifact-lock.json: adapter.interfaceVersion must be an integer")
    return errors


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        description="Audit a Frida Manager version lock and packaged artifact hashes."
    )
    parser.add_argument("manager_root", type=Path)
    parser.add_argument("--version", required=True)
    return parser


def main(arguments: Optional[Sequence[str]] = None) -> int:
    """Run the audit and return nonzero when any invariant fails."""
    args = build_parser().parse_args(arguments)
    errors = audit_variant(args.manager_root.resolve(), args.version)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Variant readiness failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Variant {args.version} passed structural and hash readiness checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
