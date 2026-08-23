# Chapter 5 Data and Reproducibility Archive  
## Fragmentation, Coordination and Functional Differentiation in Global Ocean Economy Governance — Public-Safe Edition

**Version:** 1.0.0  
**Release date:** 2 August 2026  
**Unit of analysis:** 48 globally mandated intergovernmental organisations (IGOs)

This archive contains the data, analytical outputs, R scripts, figures, methodological references, and quality-assurance records supporting the comparative analysis of institutional fragmentation, relational coordination, and functional differentiation in global ocean economy governance. It is designed as a publication-neutral research-data resource for transparent verification, secondary analysis, and reuse.

The archive measures documented institutional characteristics and relational patterns. It does **not** directly measure organisational influence, implementation quality, legal compliance, ecological outcomes, socioeconomic performance, or distributive effects.

## Public-release status

This is the public-safe edition of the Chapter 5 archive. It preserves the original internal root folder and the established analytical filenames, while excluding material that should remain in restricted research storage.

The public-safety transformation:

- removes the supervisor-marked working draft containing 36 comments and six tracked-change elements;
- excludes three nonessential internal literature/concept-note exports containing extensive source-derived quotations and tentative synthesis;
- removes the evidence-rich `Traceability_Long` sheets from eight normalised attribute workbooks while retaining the original workbook filenames and all `Matrix_Wide` values unchanged;
- retains the Year of Establishment workbook unchanged;
- replaces provisional licensing with final mixed-licence terms;
- replaces thesis-specific citation wording with publication-neutral dataset metadata; and
- regenerates manifests, checksums, and validation records.

See `PUBLIC_RELEASE_AUDIT.md` for the full decision trail.

## Analytical scope

### Institutional incongruence

The Section 5.2 data contain all **1,128 unordered IGO dyads** among the 48 organisations. They compare mandate similarity with relational similarity and derive the measure:

```text
delta_incongruence = mandate_similarity - relational_similarity
```

Positive values indicate that organisations are more similar in mandate space than in documented relational space. The archive also contains the retained top-decile mandate-overlap edge set used for Figure 5.3.

Canonical files:

- `02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv`
- `02_processed_outputs/section_5_2_institutional_incongruence/highest_incongruence_dyads.csv`
- `02_processed_outputs/section_5_2_institutional_incongruence/figure_5_3_retained_mandate_overlap_edges.csv`
- `02_processed_outputs/section_5_2_institutional_incongruence/figure_5_3_retained_mandate_overlap_node_summary.csv`

### Relational coordination

The Section 5.3 data represent the top-decile relational-similarity network. The public archive contains **113 retained edges** and node-level metrics for all **48 organisations**, including degree, strength, normalised betweenness, eigenvector centrality, community membership, and interpretive relational position.

Canonical files:

- `02_processed_outputs/section_5_3_relational_coordination/relational_network_edges_q90.csv`
- `02_processed_outputs/section_5_3_relational_coordination/relational_network_node_metrics_q90.csv`
- `02_processed_outputs/section_5_3_relational_coordination/table_5_7_network_level_descriptive_statistics.csv`
- `02_processed_outputs/section_5_3_relational_coordination/table_5_8_selected_centrality_results.csv`

### Functional differentiation

The Section 5.4 data contain complete 48-organisation exports for regulatory strength, delivery capacity, the regulatory–delivery gap, functional alignment, and functional-orientation classes. Figure-specific plot data and selected tabular outputs are included.

Canonical files:

- `02_processed_outputs/section_5_4_functional_differentiation/regulatory_delivery_scores_all_48_igos.csv`
- `02_processed_outputs/section_5_4_functional_differentiation/functional_alignment_scores_all_48_igos.csv`
- `02_processed_outputs/section_5_4_functional_differentiation/functional_orientation_classes_all_48_igos.csv`
- `02_processed_outputs/section_5_4_functional_differentiation/functional_orientation_class_counts_all_48_igos.csv`
- `02_processed_outputs/section_5_4_functional_differentiation/functional_score_construction_audit.md`

The regulatory-strength and delivery-capacity components can be recomputed from the public-safe normalised matrices. The full functional-alignment series is supplied as the canonical archived 48-case output and is cross-checked against the class-count and selected-score files.

## Archive structure

```text
chapter5_data_archive/
├── README.md
├── CITATION.cff
├── LICENSE_NOTICE.md
├── LICENSE_DATA_CC_BY_4.0.md
├── LICENSE_CODE_MIT.txt
├── PUBLIC_RELEASE_AUDIT.md
├── RELEASE_NOTES_v1.0.0.md
├── DATA_DICTIONARY.md
├── MANIFEST.csv
├── MANIFEST.json
├── MANIFEST_PUBLIC_v1.0.0_filelist.txt
│
├── 00_documentation/
│   ├── archive_notes/
│   │   └── README_PUBLIC_SAFE.md
│   └── methodological_reference/
│
├── 01_raw_inputs/
│   └── normalised_attribute_workbooks/
│       ├── README_PUBLIC_SAFE.md
│       ├── eight public-safe Matrix_Wide workbooks
│       └── year_of_establishment_categories_density.xlsx
│
├── 02_processed_outputs/
│   ├── section_5_2_institutional_incongruence/
│   ├── section_5_3_relational_coordination/
│   └── section_5_4_functional_differentiation/
│
├── 03_scripts/
│   └── R/
│
├── 04_figures/
│   ├── design_drafts/
│   └── final/
│
└── 05_quality_assurance/
    ├── checksums_sha256.txt
    ├── reproducibility_status.md
    ├── workbook_sanitisation_report.csv
    ├── removed_or_replaced_files_public_release.csv
    ├── analytical_invariance_check.csv
    ├── docx_and_workbook_metadata_review.csv
    ├── validate_public_archive.py
    └── VALIDATION_STATUS.md
```

## Public-safe normalised inputs

The following eight workbooks retain their original filenames but now contain only the 48-case `Matrix_Wide` sheet:

- `defined_objectives_full_normalised.xlsx`
- `horizontal_coordination_full_normalised.xlsx`
- `interinstitutional_relationships_full_normalised.xlsx`
- `sources_of_jurisdiction_full_normalised.xlsx`
- `spatial_jurisdiction_full_normalised.xlsx`
- `strategies_full_normalised.xlsx`
- `subject_matter_jurisdiction_full_normalised.xlsx`
- `vertical_coordination_full_normalised.xlsx`

Each retained matrix has 49 rows including the header and 22 columns. Cell-by-cell checks confirm that the public `Matrix_Wide` values are identical to the complete restricted workbooks. The removed `Traceability_Long` sheets contained verbatim descriptions, cleaned text, keyword frequencies, trigger maps, and KWIC evidence. Those evidence-rich records remain part of the restricted research archive and are not redistributed.

## Reproduction

Run the R workflow from the archive root:

```r
source("03_scripts/R/run_all_chapter5.R")
```

or from a shell:

```bash
Rscript 03_scripts/R/run_all_chapter5.R
```

The setup script checks the required R packages. Figure 5.3 chord rendering is optional and requires `circlize`; the edge and node-summary CSVs are generated even when that package is unavailable.

The scripts generate rebuilt files alongside the canonical archived outputs rather than overwriting the supplied reference files.

## Reproducibility boundary

The public archive supports:

1. verification of all supplied Chapter 5 analytical tables and figures;
2. reproduction of the dyadic incongruence calculations and retained mandate-overlap data;
3. reconstruction of the top-decile relational network and node metrics;
4. recomputation of regulatory-strength and delivery-capacity components from the public score matrices; and
5. secondary analysis of the complete 48-organisation and 1,128-dyad datasets.

The public archive does not reproduce the underlying source-document evidence or the evidence-rich text-to-score traceability layer. Lawful source-level reconstruction requires the restricted measurement archive or reacquisition of the underlying institutional documents.

## Quality assurance

Run:

```bash
python 05_quality_assurance/validate_public_archive.py
```

The validator checks:

- required files and record counts;
- absence of the supervisor-marked document and internal working-note exports;
- absence of comments and tracked changes in remaining DOCX files;
- absence of `Traceability_Long` sheets, spreadsheet comments, and external links in the public-safe workbooks;
- 48-case and 1,128-dyad dimensions;
- matrix-value invariance;
- publication-neutral citation and final licence wording;
- archive hygiene; and
- SHA-256 checksum integrity.

## Rights and reuse

Researcher-generated data, tables, figures, and documentation are licensed under **CC BY 4.0**. Original R code is licensed under the **MIT License**. Third-party rights are not transferred by this archive. See `LICENSE_NOTICE.md` for the exact scope.

## Citation

Use `CITATION.cff` and the version-specific Zenodo DOI once assigned. Until a DOI is added, cite:

> Adewumi, I. (2026). *Chapter 5 Data and Reproducibility Archive: Fragmentation, Coordination and Functional Differentiation in Global Ocean Economy Governance* (Version 1.0.0) [Data set].

## Versioning

Substantive changes to data, classifications, or analytical outputs should be released as a new version. The GitHub repository may remain a living development environment, while Zenodo should preserve immutable, versioned release archives.
