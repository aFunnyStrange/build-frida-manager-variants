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
