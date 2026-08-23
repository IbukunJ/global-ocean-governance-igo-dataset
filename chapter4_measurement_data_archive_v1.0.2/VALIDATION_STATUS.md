# Validation status — public-safe edition

## Overall result

The public-safe Chapter 4 archive passed **54 of 54** programmed structural, analytical, and distribution checks. No failed checks remain.

## Verified analytical values

- 48 organisations in the study roster.
- 58 registered institutional source documents represented through metadata and hashes.
- 2,435 metadata-only page records.
- 5,159 metadata-only paragraph records.
- 130 logged extraction exceptions.
- 3,636 candidate-review records represented through a public index.
- 3,676 decision-log records represented through a public index.
- 3,074 retained evidence records represented through a public traceability index.
- 48 baseline matrix rows and 480 long-form IGO × attribute cells.
- Zero blank substantive fields and zero orphan evidence records in the integrated matrix.
- 80 category definitions and 1,862 CLEAN-confirmed category activations.
- Complete 48 × 80 hybrid, within-IGO, and across-IGO matrices.
- Complete corrected 48 × 174 master matrix.
- Eight family summaries, 80 category summaries, and 48 organisation profiles.

## Public-safety verification

The release contains:

- no PDF or legacy DOC source files;
- no extracted page or paragraph text;
- no candidate excerpts, source-title evidence strings, full matrix narratives duplicated inside Step 3 audit indexes, or full evidence excerpts;
- no source-dependent RAW/CLEAN narrative workbooks, except the researcher-generated Year of Establishment context file;
- no KWIC-bearing family workbooks or scoring traceability-long CSVs; and
- a 96-row file-level register documenting every exclusion or replacement.

The public corpus and coding indexes retain identifiers, structural locators, record counts, source URLs where originally recorded, and SHA-256 hashes to support provenance without redistributing source content.

## Source-retrieval metadata limitation

All 58 `source_url` and `access_date` fields are blank in the supplied document manifest. The public archive reports this gap explicitly and does not infer replacement values. Lawful source reconstruction therefore requires searches through issuing organisations using document identifiers, filenames, notes, and hashes.

## Analytical invariance

The public-safety transformation did not change the study roster, baseline Attribute Matrix, category schema, category activations, hybrid scores, within-IGO scores, across-IGO scores, descriptive outputs, or corrected master matrix. `00_overview/analytical_invariance_check.csv` confirms that 28 retained canonical data and output files are byte-identical to their counterparts in the complete archive.

## Code and execution boundary

The archive preserves Python and R code to document the complete methodological chain. Scripts that reconstruct the documentary corpus or regenerate text-dependent scoring inputs require locally reacquired sources or authorised access to the restricted archive. The canonical public matrices are ready for descriptive reproduction and secondary analysis.

## Detailed checks

See `VALIDATION_SUMMARY.csv`. Run `python 00_overview/validate_archive.py` from the archive root to repeat the public-release checks and verify file checksums.
