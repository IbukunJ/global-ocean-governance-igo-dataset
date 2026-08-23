# Naming convention

Canonical files follow `ch04_s<stage>_<content>_<dimension-or-count>.<ext>`. Lower-case letters, numerals, and underscores are used where practical.

Public-safe replacements add `_public_` or `_index_public_` to distinguish metadata-only files from restricted evidence-rich originals. Stable `doc_id`, `igo_id`, `record_id`, and `trace_key` values are preserved wherever available. Source-document filenames remain recorded in manifests and hashes even though the files themselves are not distributed.

Executable scripts retain their original names where renaming would reduce methodological traceability. The internal top-level folder name remains `chapter4_measurement_data_archive_v1.0.2` to preserve correspondence with existing appendices; the public release version is stated in the root README, changelog, and citation metadata.
