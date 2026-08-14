# Qualification Matrix

## Static and build gates

Verify lock schema, exact hashes, executable formats/ABI, Engine link inputs, adapter API, module layout, WebUI
version selection, install scripts, uninstall cleanup, and reproducible package output. Treat a successful build
as `candidate` only.

## Protocol gate

Exercise server start/stop/status/version, Engine readiness, endpoint failure, request validation, generation,
idempotency, single-flight conflicts, timeouts, target exit, detach, and Engine/server restart recovery. Cover
both PID and name semantics even if only one is exposed in a particular UI.

## Authorized live gate

For every declared device/root-manager row, use only named owned test apps and verify:

- module install/update and clean boot startup;
- server lifecycle and loopback-only endpoint;
- UI-driven spawn paused/normal where supported;
- UI-driven Attach by PID and/or name as declared;
- safe raw/compiled agent load, bounded RPC, reload, detach, and target-exit recovery;
- service restart and device reboot persistence;
- uninstall/rollback and restoration of default configuration.

Record exact passes, failures, and untested cells. Two devices do not establish universal Android
compatibility. Never turn a blocked runtime into stable based on a different version's results.

Stratify the matrix by Android version/ROM, ABI and zygote model, root manager, Frida version, and exact
candidate hashes. Do not require `zygote_secondary` on an arm64-only system. Separate runtime failures from
test-script readiness: wait for the owned test library/application state needed by a Java/JNI probe, and rerun
the corrected probe on the stable baseline before attributing failure to the new Frida variant.

Public reports may summarize Android version, ABI, root-manager family, operations, and sanitized failures.
Keep device serials, private package names, source paths, and raw logs in ignored authorization/evidence files.
