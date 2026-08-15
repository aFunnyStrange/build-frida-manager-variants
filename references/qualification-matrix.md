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

## Runtime timing and convergence gates

Treat runtime operation deadlines and distributed-state convergence as different clocks. Keep client RPC
deadlines below the protocol/server ceiling so transport delay, scheduling, rounding, and clock skew do not
turn an otherwise valid request into a boundary failure. A 30-second server maximum, for example, needs a
smaller client budget rather than an exactly equal value.

Presence convergence, registration, and discovery may have a longer bounded window than one RPC without
changing the RPC timeout or online TTL. Record these budgets independently. Do not add an automatic retry for
an isolated connection close unless recurrence and logs classify it as transient; one clean rerun is evidence
for the run, not a new general retry policy.

After consecutive Kill and Spawn cases, wait for the old exact PID to disappear before opening the next
session. On PowerShell hosts, do not use the read-only `$PID` automatic variable for a target PID.

For a declared multi-device release matrix, exercise each authorized device independently and also verify the
common external-Hub path: dynamic registration/presence, explicit client routing, automatic group routing,
full collaboration flow on the maintained baseline rows, and final restoration of installed hashes, stopped
services, targets, and default port. Public evidence remains sanitized as described above.
