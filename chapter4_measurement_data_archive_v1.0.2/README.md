# Chapter 4 Measurement Data Archive  
## Global Ocean Economy Governance IGOs — Public-Safe Edition

## Overview

This archive contains the Chapter 4 data, code, documentation, and reproducibility materials used to construct comparative measures of the institutional design of **48 globally mandated intergovernmental organisations (IGOs)** involved in global ocean economy governance. It documents the measurement chain from study-population definition and documentary-corpus registration through evidence review, Attribute Matrix integration, category activation, hybrid scoring, dual normalisation, and analysis-ready outputs.

This is a **public-safe distribution edition**. It preserves the analytical architecture and canonical outputs while excluding third-party institutional documents and source-derived long-text fields that should not be redistributed without an individual rights assessment. The excluded material is replaced, where feasible, by stable identifiers, locators, counts, and SHA-256 hashes.

The data measure **documented institutional characteristics and governance capacity**. They do not directly measure implementation, organisational influence, legal compliance, ecological outcomes, socioeconomic performance, or distributive effects.

## Release identity

- **Public release version:** 1.0.3
- **Prepared:** 2026-08-02
- **Derived from complete examination archive:** v1.0.2
- **Internal folder name retained:** `chapter4_measurement_data_archive_v1.0.2`

The internal folder name is retained to preserve correspondence with methodological appendices and existing file references. Public-safety changes concern distribution and documentation only; they do not alter the analytical results.

## What is included

The public archive retains:

- the final **48-IGO study roster**;
- a **58-document provenance register** containing stable identifiers, filenames, document characteristics, and SHA-256 hashes;
- page- and paragraph-level **metadata indexes without extracted text**;
- metadata-only coding-review and traceability indexes for **3,636 candidates**, **3,676 decision-log records**, and **3,074 retained evidence records**;
- the researcher-generated baseline **Attribute Matrix**;
- the reconciled **80-category schema** and **48 × 80 activation matrix**;
- corrected hybrid, within-IGO, and across-IGO score matrices;
- family-level matrix-wide outputs;
- descriptive summaries and the corrected **48 × 174 master matrix**;
- Python and R code documenting the computational workflow;
- methodological documentation, data dictionaries, validation records, and integrity checks.

## What is not included

The public archive excludes:

- **57 PDF files and one DOC file** constituting the institutional source corpus;
- extracted page and paragraph text;
- candidate excerpts and other source-dependent evidence fields;
- Step 3 and scoring workbooks that embed verbatim or KWIC evidence;
- source-dependent RAW and CLEAN narrative workbooks;
- duplicated long-text traceability outputs.

See `PUBLIC_RELEASE_AUDIT.md` and `00_overview/removed_files_public_release.csv` for the complete rationale and file-level register.

## Read first

1. `PUBLIC_RELEASE_AUDIT.md` explains the public-distribution boundary.
2. `00_overview/chapter_to_data_crosswalk.csv` links Chapter 4 claims and outputs to canonical files.
3. `VALIDATION_STATUS.md` records verified counts, equation corrections, and public-safety checks.
4. `07_analysis_ready_outputs/ch04_analysis_ready_matrices.xlsx` is the most convenient consolidated analytical workbook.
5. `MANIFEST.csv` lists every distributed payload file and its status.
6. `CHECKSUMS_SHA256.csv` provides file-integrity hashes.
7. `RIGHTS_AND_REUSE.md` and `LICENSE.md` specify reuse conditions.

## Repository structure

```text
chapter4_measurement_data_archive_v1.0.2/
├── 00_overview/
├── 01_study_population/
├── 02_document_corpus/
├── 03_attribute_coding_clean_review/
├── 04_attribute_matrix_integration/
├── 05_category_schema/
├── 06_scoring_and_normalisation/
├── 07_analysis_ready_outputs/
├── 08_documentation/
├── PUBLIC_RELEASE_AUDIT.md
├── README.md
├── RIGHTS_AND_REUSE.md
├── LICENSE.md
├── CITATION.cff
├── CHANGELOG.md
├── VALIDATION_STATUS.md
├── VALIDATION_SUMMARY.csv
├── MANIFEST.csv
└── CHECKSUMS_SHA256.csv
```

## Measurement framework

The analysis covers nine governance attributes:

1. Year of Establishment  
2. Spatial Jurisdiction  
3. Subject Matter Jurisdiction  
4. Sources of Jurisdiction  
5. Defined Objectives  
6. Strategies  
7. Inter-Institutional Relationships  
8. Vertical Coordination  
9. Horizontal Coordination  

Eight non-temporal attribute families are operationalised through ten categories each, producing an **80-category analytical schema**. The archive provides CLEAN-confirmed category activation, hybrid scores, and dual normalisation within and across organisations.

## Canonical public files

### Study population

- `01_study_population/data/ch04_s1_igo_roster_48.csv`

### Documentary provenance and corpus indexes

- `02_document_corpus/data/processed/ch04_s2_public_source_register_58.csv`
- `02_document_corpus/data/processed/ch04_s2_document_manifest_58.csv`
- `02_document_corpus/data/processed/ch04_s2_document_extraction_summary_58.csv`
- `02_document_corpus/data/interim/ch04_s2_page_index_public_2435.csv.gz`
- `02_document_corpus/data/interim/ch04_s2_paragraph_index_public_5159.csv.gz`
- `02_document_corpus/data/interim/ch04_s2_extraction_log_130.csv`

The public source register reports the absence of preserved `source_url` and `access_date` values rather than reconstructing them. Institutional documents must be reacquired from their issuing organisations.

### Coding review and traceability

- `03_attribute_coding_clean_review/data/ch04_s3_candidate_review_index_public_3636.csv`
- `03_attribute_coding_clean_review/data/ch04_s3_decision_log_public_3676.csv`
- `03_attribute_coding_clean_review/data/ch04_s3_traceability_index_public_3074.csv`
- `03_attribute_coding_clean_review/outputs/tables/ch04_s3_summary_statistics.csv`
- `03_attribute_coding_clean_review/outputs/tables/ch04_s3_coverage_by_igo_attribute.csv`

The public indexes preserve decisions, identifiers, evidence tiers, locators, URLs where recorded, researcher rationales, and cryptographic hashes. They do not contain source excerpts.

### Baseline Attribute Matrix

- `04_attribute_matrix_integration/data/ch04_s4_baseline_attribute_matrix_wide_48x10.csv`
- `04_attribute_matrix_integration/data/ch04_s4_baseline_attribute_matrix_long_480.csv`
- `04_attribute_matrix_integration/outputs/ch04_s4_data_integration_bundle.xlsx`
- `04_attribute_matrix_integration/outputs/ch04_s4_integrity_checks.csv`

The baseline matrix contains researcher-generated institutional synthesis, not the source-document corpus.

### Category schema and activation

- `05_category_schema/data/ch04_s5_category_schema_80_reconciled.csv`
- `05_category_schema/data/ch04_s5_category_activation_matrix_48x80.csv`
- `05_category_schema/documentation/ch03_attribute_category_identification_v1.0.docx`

### Scoring and normalisation

- `06_scoring_and_normalisation/outputs/ch04_s6_hybrid_score_matrix_48x80.csv`
- `06_scoring_and_normalisation/outputs/ch04_s6_within_igo_matrix_48x80.csv`
- `06_scoring_and_normalisation/outputs/ch04_s6_across_igo_matrix_48x80.csv`
- `06_scoring_and_normalisation/outputs/ch04_s6_descriptive_statistics_corrected.csv`
- `06_scoring_and_normalisation/outputs/family_csvs/*_matrix_wide_corrected.csv`

Source-dependent RAW/CLEAN and KWIC-bearing files are not distributed. The retained code documents the scoring logic, while the supplied matrices are the canonical public analytical outputs.

### Analysis-ready products

- `07_analysis_ready_outputs/ch04_analysis_ready_matrices.xlsx`
- `07_analysis_ready_outputs/ch04_master_matrix_48x174_corrected.csv`
- `07_analysis_ready_outputs/descriptive_summary/ch04_family_summary.csv`
- `07_analysis_ready_outputs/descriptive_summary/ch04_category_prevalence.csv`
- `07_analysis_ready_outputs/descriptive_summary/ch04_igo_overall_profiles.csv`
- `07_analysis_ready_outputs/descriptive_summary/ch04_igo_overall_profile_plot.png`

## Reproducibility boundary

The archive supports two forms of reuse:

### Open analytical reproduction

Users can reproduce Chapter 4 descriptive analysis and conduct secondary analysis from the category activation, hybrid-score, normalised, and master matrices. These files contain the canonical public results.

### Restricted source-pipeline reconstruction

Rebuilding the documentary corpus, candidate retrieval, full evidence review, or RAW/CLEAN text-processing stages requires lawful reacquisition of the 58 institutional documents or authorised access to the complete restricted archive. The public metadata and hashes support reconstruction and verification but do not substitute for the source texts.

The supplied code is retained to document the pipeline. Some scripts therefore reference inputs deliberately absent from the public edition and should not be interpreted as immediately executable without local source reconstruction.

## Validation

Run the public-release validator from the archive root:

```bash
python 00_overview/validate_archive.py
```

The validator checks:

- expected case and record counts;
- matrix dimensions and missingness;
- absence of third-party PDF/DOC files;
- absence of extracted paragraph text and evidence-rich public fields;
- presence of public indexes and exclusion documentation;
- archive hygiene and checksum integrity.

## Integrity and versioning

`CHECKSUMS_SHA256.csv` records SHA-256 hashes for distributed files. Substantive changes to classifications or scores should be released as a new version rather than overwriting this archive. The GitHub repository may remain a living development environment, while the corresponding Zenodo record should preserve immutable versioned releases.

## Rights and citation

Researcher-generated data, matrices, figures, and documentation are licensed under **CC BY 4.0**. Original Python and R code is licensed under the **MIT License**. Institutional source documents are not included and remain governed by their issuing organisations.

See `CITATION.cff` for machine-readable citation metadata. Add the final Zenodo DOI to `CITATION.cff` and this README once reserved.
