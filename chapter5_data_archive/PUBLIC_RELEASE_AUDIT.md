# Public-Release Audit

## Release identity

- **Source archive:** `chapter5_data_archive_v6_final.zip`
- **Source archive SHA-256:** `5f9c21249ace02c9fb8b9f59a4f624829ab97f0ecc25f5b37b4ea086af6acce9`
- **Public release:** `chapter5_data_archive_public_v1.0.0.zip`
- **Internal root folder retained:** `chapter5_data_archive/`
- **Release date:** 2 August 2026
- **Resource type:** Dataset and reproducibility archive

## Purpose

This audit records every material transformation made to create a public-safe Chapter 5 archive. The objective was to preserve the analytical data, code, figures, and methodological provenance while excluding supervisory records, internal working notes, and evidence-rich source text that should remain in restricted research storage.

## 1. Supervisory working material

The following file was removed:

```text
00_documentation/archive_notes/chapter5_marked_or_working_draft_reference.docx
```

Inspection of its OOXML package identified:

- 36 Word comments;
- 3 insertion elements;
- 3 deletion elements; and
- the named comment author recorded in the source package.

The document was not a computational dependency. Its removal does not alter any dataset, script, table, figure, or analytical result.

## 2. Internal literature and concept notes

Three internal text exports were removed:

```text
00_documentation/archive_notes/literature_and_concept_notes_1.txt
00_documentation/archive_notes/literature_and_concept_notes_2.txt
00_documentation/archive_notes/literature_and_concept_notes_3.txt
```

These were nonessential working records containing extensive source-derived quotations and tentative literature synthesis. Two were byte-identical duplicates. They were excluded conservatively because they are not required to reproduce the Chapter 5 analysis and were not prepared as publication-ready research data.

A public notice remains at:

```text
00_documentation/archive_notes/README_PUBLIC_SAFE.md
```

## 3. Evidence-rich normalised workbooks

Eight substantive normalised workbooks contained an evidence-rich `Traceability_Long` sheet and an analysis-ready `Matrix_Wide` sheet. The traceability sheets included verbatim institutional descriptions, cleaned text, term frequencies, trigger mappings, KWIC snippets, and scoring provenance.

For public distribution:

- all eight `Traceability_Long` sheets were removed;
- the original workbook filenames were retained;
- each public workbook contains only `Matrix_Wide`;
- each retained matrix contains 48 IGO rows plus a header and 22 columns; and
- all 8 × 49 × 22 matrix cells were compared with the source workbooks and found identical.

The transformation withholds **3,840 evidence rows** while preserving every analytical matrix value used downstream.

The following workbook did not contain an evidence-rich traceability sheet and remains byte-identical:

```text
01_raw_inputs/normalised_attribute_workbooks/year_of_establishment_categories_density.xlsx
```

See `05_quality_assurance/workbook_sanitisation_report.csv`.

## 4. Citation and licensing

`CITATION.cff` was revised from thesis-supplement wording to publication-neutral dataset metadata. It now identifies the resource as a dataset and requests citation using the version-specific DOI once available.

`LICENSE_NOTICE.md` was replaced with final mixed-licence terms:

- CC BY 4.0 for researcher-generated data, tables, figures, and documentation;
- MIT License for original R code; and
- no relicensing of third-party rights.

Supporting licence files are included.

## 5. Publication-neutral provenance wording

The `score_source` field in:

```text
02_processed_outputs/section_5_4_functional_differentiation/functional_alignment_scores_all_48_igos.csv
```

was revised to remove reliance on the excluded working draft. All analytical fields remain identical. The corresponding narrative sentence in `functional_score_construction_audit.md` was updated consistently.

## 6. Analytical invariance

The public-safety transformation did not alter the Chapter 5 results:

- 8 public score matrices are cell-identical to the source `Matrix_Wide` sheets;
- the 48-case functional-alignment file is analytically identical apart from its provenance-note field; and
- 51 additional input, output, script, and figure files are byte-identical to the complete source archive.

All 60 analytical invariance checks pass. See `05_quality_assurance/analytical_invariance_check.csv`.

## 7. Metadata review

All remaining DOCX and XLSX files were reviewed programmatically:

- 4 retained DOCX files contain no comments or tracked-change elements;
- 9 retained XLSX files contain no comments, threaded comments, or external-link packages;
- none of the public XLSX files contains a `Traceability_Long` sheet; and
- no retained package contains the supervisor names searched during the release audit.

See `05_quality_assurance/docx_and_workbook_metadata_review.csv`.

## 8. Reproducibility boundary

The public archive supports verification and secondary analysis from the supplied matrices, dyadic files, network data, functional-differentiation outputs, R scripts, and figures. It does not support source-level audit of verbatim institutional evidence. That layer remains in the complete restricted archive and in the restricted Chapter 4 measurement archive.

## 9. File integrity

The public release contains regenerated manifests and SHA-256 checksums. Run:

```bash
python 05_quality_assurance/validate_public_archive.py
```

The archive-level SHA-256 hash is supplied separately so it can be checked without creating a self-referential archive.
