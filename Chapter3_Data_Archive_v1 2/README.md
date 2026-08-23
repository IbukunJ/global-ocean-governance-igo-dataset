# Chapter 3 Data Archive (reconciled release v1.1.0)

This archive contains the cleaned, navigable, and auditable data products supporting the development
and validation of the governance attribute taxonomy in Chapter 3. It preserves the original Chapter 3
folder names used in the methodological appendices while adding a reconciled Stage 1 literature
screening audit trail.

## Controlling Stage 1 literature count

The literature-screening funnel used in this release is:

**100 records identified → 90 publications assessed at full text → 79 publications included in the qualitative synthesis.**

The 90-publication count is recoverable from the surviving workbook as the unique union of:

- 89 records in `1 - Literature`; and
- one included publication that appears only in `Screened Literature`.

Eleven assessed publications were not retained in the final 79-publication corpus. The identities of
the ten records removed between initial identification and full-text assessment were not preserved in
the surviving files, so the archive reports this as an aggregate limitation rather than reconstructing
unsupported record-level information.

For the complete audit, consult:

- `00_readme_and_manifest/CHAPTER3_COUNT_RECONCILIATION.md`
- `01_stage1_literature_evidence/Stage1_Literature_Evidence_ReadFirst.xlsx`
- `01_stage1_literature_evidence/Stage1_Literature_Count_Reconciliation.csv`
- `01_stage1_literature_evidence/Stage1_FullText_Assessed_Reconciled_90.csv`
- `01_stage1_literature_evidence/Stage1_Excluded_FullText_Records_11.csv`

## Folder structure

- `00_readme_and_manifest/` — archive manifest, structure guide, count reconciliation, release notes, and checksums.
- `01_stage1_literature_evidence/` — literature evidence dataset, screening reconciliation, final 79-publication corpus, and seed-theme provenance.
- `02_stage2_governance_theme_dataset/` — Stage 2 governance theme dataset, synonym validation outputs, stop-list, candidate queues, code, and environment.
- `03_stage3_reduction_and_taxonomy/` — Stage 3 reduction ledger, normalisation and reduction results, construct/category diagnostics, category-to-attribute crosswalks, code, and environment.
- `04_chapter_figures/` — figures generated for the Chapter 3 methodological and diagnostic workflow.

## Analytical sequence

The archive should be read in the following order:

1. **Stage 1:** literature identification, screening, evidence capture, and provisional seed-theme development.
2. **Stage 2:** Python-assisted paragraph retrieval, theme discovery, synonym expansion, stop-list refinement, and human validation.
3. **Stage 3:** reduction from 80 first-order themes to 56 normalised concepts, 31 salient concepts, 22 governance constructs, five categories, and nine operational attributes.
4. **Figures and diagnostics:** visual documentation of the Stage 2 and Stage 3 workflows and reduction decisions.

## Nine governance attributes

The final taxonomy comprises:

1. Year of Establishment (YE)
2. Spatial Jurisdiction (SJ)
3. Subject Matter Jurisdiction (SMJ)
4. Source of Jurisdiction (SoJ)
5. Defined Objectives (DO)
6. Strategies (STR)
7. Inter-Institutional Relationships (IIR)
8. Vertical Coordination (VC)
9. Horizontal Coordination (HC)

## Naming convention

Existing folder and bundle names are retained because they are referenced in the methodological
appendices. Newly added reconciliation files use the prefix `Stage1_` and explicit content descriptors.

## What is excluded

This cleaned archive excludes Chapter 4 and Chapter 5 analysis modules, Part II IGO document-corpus
bundles, raw copyrighted PDFs, macOS metadata (`__MACOSX`, `.DS_Store`), temporary Excel lock
files, and working thesis drafts.

## How to verify the archive

1. Begin with `00_readme_and_manifest/ch3_data_archive_manifest.csv`.
2. Verify file integrity using `00_readme_and_manifest/SHA256SUMS.txt`.
3. Read the Stage 1 reconciliation note before citing the literature counts.
4. Consult the workbook and CSV files for record-level provenance.
5. Follow Stage 2 and Stage 3 code, configuration files, logs, and tables for computational reproducibility.

## Citation

> Adewumi, I. (2026). *Global ocean economy governance IGO data archive I: Literature screening, theme discovery, and governance attribute derivation* (Version 1.0.0) [Data set], Zenodo, doi: 10.5281/zenodo.22058522.>
