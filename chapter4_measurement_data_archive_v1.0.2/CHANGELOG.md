# Changelog

## v1.0.3 - 2026-08-02

- Produced a public-safe distribution edition of the Chapter 4 archive.
- Excluded 58 third-party institutional source documents.
- Replaced page and paragraph extraction outputs with metadata-only indexes retaining identifiers, counts, locators, and SHA-256 hashes.
- Replaced candidate, decision, and traceability source-text tables with public metadata indexes.
- Excluded source-dependent RAW/CLEAN narrative workbooks, KWIC-bearing traceability CSVs, and family workbooks.
- Added a public source register, rights statement, dual-licence note, public-release audit, and full file-level removal register.
- Updated archive documentation, chapter crosswalk, validation code, manifest, checksums, and citation metadata.
- No category activation, hybrid score, normalised score, descriptive statistic, baseline matrix value, or corrected master-matrix value was changed.

## v1.0.2 - 2026-07-29

- Added bounded descriptive summaries at attribute-family, category, and IGO levels for the revised Chapter 4 results section.
- Added the ranked 48-IGO descriptive profile plot and its regeneration script.
- Updated the chapter-to-data crosswalk, archive documentation, manifest, checksums, citation metadata, and validation script.
- No underlying category activations, hybrid scores, normalised matrices, or baseline Attribute Matrix records were changed.

## v1.0.1 - 2026-07-18

- Added `05_category_schema/documentation/ch03_attribute_category_identification_v1.0.docx` as a read-only Chapter 3-origin methodological provenance source.
- Clarified that the provenance document explains category development and mapping but is not an executable Chapter 4 output.
- Updated the root README, category-schema README, archive structure, exclusions note, chapter-to-data crosswalk, manifest, checksums, and citation metadata.
- No research data, category activations, scores, normalised matrices, or validation results were changed.

## v1.0 - 2026-07-18

- Created a Chapter 4-only archive from the working project bundle.
- Removed Chapter 3 and Chapter 5 materials, nested ZIP duplicates, temporary files, caches, operating-system metadata, and working chapter drafts.
- Standardised folder names and canonical data filenames.
- Renamed 58 source documents while preserving original filenames and hashes in the document manifest.
- Added README files, chapter-to-data crosswalk, validation status, manifest, checksums, citation metadata, and rights note.
- Corrected the Stage B R expression so RAW frequency is conditional on CLEAN presence.
- Corrected the Step 4 orphan-register assignment so a valid zero-row orphan table remains empty.
- Reconciled the 80-category analysis schema with the labels and tier values used in the verified scoring workbooks.
- Regenerated within-IGO and across-IGO matrices to align with Equations 4.2 and 4.3.
- Added corrected family workbooks, descriptive statistics, and a 48 x 174 master matrix.
