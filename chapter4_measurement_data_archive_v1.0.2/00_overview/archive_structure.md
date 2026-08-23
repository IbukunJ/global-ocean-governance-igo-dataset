# Archive structure — public-safe edition

- `00_overview/`: archive map, chapter-to-data crosswalk, exclusions, public-release removal register, naming rules, and validation code.
- `01_study_population/`: final 48-IGO roster.
- `02_document_corpus/`: documentary provenance, metadata-only page/paragraph indexes, extraction diagnostics, environment files, and reconstruction code. Third-party source documents and extracted text are not distributed.
- `03_attribute_coding_clean_review/`: retrieval configuration, metadata-only candidate/decision/traceability indexes, coding diagnostics, and code. Source excerpts are withheld.
- `04_attribute_matrix_integration/`: researcher-generated baseline Attribute Matrix, long-form matrix, integrity checks, and integration code.
- `05_category_schema/`: reconciled 80-category schema, activation matrix, and a read-only Chapter 3-origin methodological provenance document explaining category development and mapping.
- `06_scoring_and_normalisation/`: scoring/normalisation code, category configurations, safe matrix-wide outputs, corrected matrices, and statistics. RAW/CLEAN narrative inputs and KWIC-bearing traceability files are not distributed.
- `07_analysis_ready_outputs/`: consolidated analytical workbook, corrected 48 × 174 master matrix, descriptive summaries, and profile plot.
- `08_documentation/`: methodological appendix, source codebook, dictionaries, and reproducibility protocol.

Root-level `PUBLIC_RELEASE_AUDIT.md`, `RIGHTS_AND_REUSE.md`, and `LICENSE.md` define the public-distribution boundary. `MANIFEST.csv` and `CHECKSUMS_SHA256.csv` support file-level provenance and integrity.
