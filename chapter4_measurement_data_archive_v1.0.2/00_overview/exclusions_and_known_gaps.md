# Exclusions and known gaps — public-safe edition

## Deliberate public-release exclusions

This edition excludes:

- the 58 third-party institutional source documents (57 PDFs and one DOC file);
- page- and paragraph-level extracted text;
- candidate excerpts and other evidence-rich Step 3 fields;
- the Step 3 consolidated workbook embedding those fields;
- source-dependent RAW/CLEAN narrative workbooks;
- KWIC-bearing scoring traceability CSVs and family workbooks;
- nested ZIP duplicates, working chapter drafts, `.DS_Store`, `__MACOSX`, temporary Office files, caches, and Git metadata.

Metadata-only indexes and SHA-256 hashes replace the excluded source-text layers where feasible. The full file-level register is `removed_files_public_release.csv`.

## Source-retrieval metadata gap

The supplied complete archive did not preserve a `source_url` or `access_date` for every one of the 58 source documents. These fields remain blank in the public register rather than being inferred. Users should locate documents through the issuing organisation using document identifiers, filenames, titles or notes, and SHA-256 hashes.

## Methodological provenance exception

One Chapter 3-origin document is retained as a deliberate provenance exception: `05_category_schema/documentation/ch03_attribute_category_identification_v1.0.docx`. It is researcher-generated and documents the conceptual development, consolidation, and mapping of the categories used in Chapter 4. It is not an executable Chapter 4 output; the authoritative schema remains `05_category_schema/data/ch04_s5_category_schema_80_reconciled.csv`.

## Reproducibility limit

The public archive supports analysis from canonical matrices and documents the source-dependent pipeline. A complete rerun from institutional text requires lawful reacquisition of the source documents or authorised access to the restricted archive. The accessible final records also do not provide verified counts for targeted manual re-checks and resulting corrections; these values are not inferred.
