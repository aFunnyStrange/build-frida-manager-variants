# Release and Reporting

Keep validation builds available on ordinary commits if useful, but make publication tag- or manually gated.
Before any release mutation, verify clean Git state, version/tag agreement, changelog, licenses/notices for
redistributed Frida assets, artifact hashes, qualification report, install/update/rollback notes, and that no
ignored authorization evidence entered the archive.

Release assets should include the installable module, SHA-256 manifest, concise compatibility matrix, known
blocked variants, and provenance for bundled server/core artifacts. A local candidate may be complete without
a GitHub Release. Tagging, pushing, and release upload require separate user authorization and post-upload
verification.
