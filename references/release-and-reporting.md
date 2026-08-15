# Release and Reporting

Keep validation builds available on ordinary commits if useful, but make publication tag- or manually gated.
Before any release mutation, verify clean Git state, version/tag agreement, changelog, licenses/notices for
redistributed Frida assets, artifact hashes, qualification report, install/update/rollback notes, and that no
ignored authorization evidence entered the archive.

Scan binaries as well as text and archives for workstation paths and private identifiers. Native Release
builds may retain absolute source paths in debug, macro, or symbol metadata. Apply reproducible
`file/debug/macro-prefix-map` equivalents before live qualification; changing those flags rebuilds the native
candidate and therefore invalidates qualification attached to the previous bytes.

Release assets should include the installable module, SHA-256 manifest, concise compatibility matrix, known
blocked variants, and provenance for bundled server/core artifacts. A local candidate may be complete without
a GitHub Release. Tagging, pushing, and release upload require separate user authorization and post-upload
verification.

Keep ordinary build names distinct from release-staging names. Stage copies under the Manager product version,
verify hashes after staging, and never imply that a common Hub binary belongs to one Frida runtime version.
Do not report an in-progress release request as published; verify the tag target, assets, download links, and
Latest state after the external mutation completes.

Browser upload completion is not evidence that every asset reached the release. If a bulk upload fails, retry
one asset at a time, wait for each upload to leave its progress state, and count the attached names before
publishing. After publication, reopen the public page or use the provider's read-only API to verify draft and
prerelease flags, tag/target, Latest state, exact asset names/count, sizes, and provider-reported SHA-256
digests against the local release manifest. Verify the manifest asset's own provider digest separately because
a SHA-256 manifest normally does not include itself.

## Same-version replacement exception

Default to immutable published versions and tags. Reusing a public tag and replacing assets is an exceptional,
non-atomic external mutation: require an explicit user request, a visible replacement-build notice, and a
record of the old tag target, asset IDs, names, sizes, and digests. If the user did not explicitly choose this
path, publish a new patch version instead.

Build every runtime variant and common asset from the same final source revision before cutover. Scan release
examples and tests for token-shaped literals as well as known credential filenames; a fake fixed token in a
demo can still teach unsafe use or be mistaken for a real secret. Keep provider credentials process-only and
never print or persist them in release scripts or journals.

Treat replacement as a resumable transaction:

1. Snapshot the current public release and local manifest.
2. Upload staged assets under temporary names when the provider supports it, and validate uploaded state and
   byte size before touching public names.
3. Persist only non-secret progress in an ignored local journal so a retry reuses already verified uploads.
4. Do not assume GitHub Release assets can be renamed: verify that API operation before relying on it. If an
   atomic name swap is unavailable, prefer a new version. For an explicitly authorized exact-name cutover,
   disclose the temporary availability window and keep a direct re-upload recovery path.
5. Update the release body and tag deliberately. Moving the tag also changes provider-generated source
   archives, so verify the peeled tag commit against the final source revision.
6. Query the public API again and require the exact final name set/count, sizes, provider digests, no temporary
   names, correct draft/prerelease/Latest state, and the replacement notice.

Make upload scripts idempotent: reuse an existing asset only when its state and expected size/digest match,
skip already completed final names, and fail closed on ambiguous duplicates. Windows PowerShell 5
`Invoke-WebRequest -InFile` can fail on binary uploads; use a verified binary-capable client such as
`Invoke-RestMethod -InFile` or `curl.exe`, then confirm provider state rather than trusting buffered console
output.
