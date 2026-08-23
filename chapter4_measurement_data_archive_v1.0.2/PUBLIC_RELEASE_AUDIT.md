# Public-release audit

**Release:** 1.0.3  
**Prepared:** 2026-08-02  
**Internal top-level folder retained:** `chapter4_measurement_data_archive_v1.0.2`

## Release principle

This edition separates open analytical reproducibility from restricted corpus redistribution. Researcher-generated variables, classifications, scores, code, documentation, and synthesis remain available. Third-party source documents and source-derived long-text fields are withheld and replaced, where feasible, by stable identifiers, locators, counts, and SHA-256 hashes.

## Exclusion summary

A total of **96 files** from the complete examination archive were excluded or replaced for public distribution:

- **58** — Third-party source document excluded from public distribution; reacquire from issuing organisation.
- **16** — Text-bearing RAW/CLEAN workbook excluded from public distribution; category matrices and scores retained.
- **8** — Traceability table embeds verbatim attribute text and KWIC evidence; matrix-wide output retained.
- **8** — Workbook embeds verbatim text and KWIC evidence; corresponding matrix-wide CSV retained.
- **1** — Evidence-rich table replaced by metadata-only public index: ch04_s3_candidate_review_index_public_3636.csv.
- **1** — Evidence-rich table replaced by metadata-only public index: ch04_s3_decision_log_public_3676.csv.
- **1** — Evidence-rich table replaced by metadata-only public index: ch04_s3_traceability_index_public_3074.csv.
- **1** — Full paragraph text extraction replaced by metadata-only public index.
- **1** — Original page-extraction table replaced by metadata-only public index.
- **1** — Workbook embeds source excerpts and duplicated long-form evidence; public CSV indexes replace it.

## Analytical invariance

No study-population record, category definition, category activation, hybrid score, within-IGO score, across-IGO score, descriptive statistic, or corrected master-matrix value was changed during preparation of this public-safe edition. SHA-256 comparison confirms that 28 retained canonical data and output files are byte-identical to the complete archive; see `00_overview/analytical_invariance_check.csv`.

## Remaining documentary limitation

The original 58-row document manifest contains blank `source_url` and `access_date` fields for sources whose retrieval metadata were not preserved. These values have not been inferred. The public source register identifies this limitation and provides document identifiers, filenames, issuing organisations, and SHA-256 hashes to support lawful reacquisition.

## Reproducibility boundary

The public archive supports reproduction and secondary analysis from the final matrices and documents the source-dependent pipeline. Reconstructing the documentary corpus, evidence retrieval, and full RAW/CLEAN text processing requires locally reacquired source materials or authorised access to the restricted archive.

## Detailed register

See `00_overview/removed_files_public_release.csv` for the complete file-level exclusion register.
