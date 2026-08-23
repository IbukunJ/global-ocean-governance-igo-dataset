# Global Ocean Economy Governance IGO Attribute Dataset and Reproducibility Archive

## Overview

This repository contains the data, documentation, coding frameworks, scripts, validation records, and analysis outputs supporting a comparative empirical assessment of intergovernmental organisations (IGOs) involved in global ocean economy governance. It is maintained as a publication-neutral research resource for the analysis of institutional design, jurisdictional scope, authority, strategy, inter-institutional relationships, coordination architecture, organisational ecology, and governance complexity.

The repository preserves the full methodological lineage from literature screening and manual seed-theme development through NLP-assisted theme discovery, governance-attribute taxonomy construction, document review, evidence-linked coding, matrix integration, hybrid scoring, dual normalisation, and exploratory analysis of fragmentation, relational coordination, and functional differentiation.

## Scope and interpretation

The study population comprises 48 globally mandated IGOs with documented relevance to the governance of the global ocean economy. The data describe institutional characteristics recorded in authoritative documents and validated coding records. They provide comparative measures of documented governance capacity and institutional configuration; they do not directly measure implementation, organisational influence, state compliance, ecological outcomes, socioeconomic performance, or distributive effects.

## Governance attributes

The analytical framework contains nine attributes:

| Code | Governance attribute | Analytical focus |
|---|---|---|
| `YE` | Year of Establishment | Founding period, institutional age, cohort, and density context |
| `SJ` | Spatial Jurisdiction | Maritime and geographic scope |
| `SMJ` | Subject Matter Jurisdiction | Thematic and sectoral mandate breadth |
| `SoJ` | Sources of Jurisdiction | Legal, delegated, normative, and strategic bases of authority |
| `DO` | Defined Objectives | Stated institutional purposes and priorities |
| `STR` | Strategies | Instruments and pathways used to pursue mandates |
| `IIR` | Inter-Institutional Relationships | Documented relationships with organisations and actor groups |
| `VC` | Vertical Coordination | Linkages across global, regional, national, and subnational levels |
| `HC` | Horizontal Coordination | Coordination across institutions, sectors, and peer networks |

## Repository structure

Internal folder names are preserved because they are used in methodological appendices, scripts, manifests, and chapter-to-data crosswalks.

```text
.
├── README.md
├── CITATION.cff
├── LICENSE.md
├── RIGHTS_AND_REUSE.md
├── .gitignore
├── Chapter3_Data_Archive_v1/
├── chapter4_measurement_data_archive_v1.0.2/
└── chapter5_data_archive/
```

### `Chapter3_Data_Archive_v1/`

This archive documents development and validation of the governance-attribute taxonomy. It contains:

- Stage 1 literature evidence and manual seed-theme provenance;
- Stage 2 NLP-assisted theme discovery, synonym expansion, stop-list development, candidate queues, decision templates, scripts, and diagnostics;
- Stage 3 reduction ledgers and crosswalks tracing 80 first-order themes through concepts, constructs, five categories, and nine final attributes;
- validation tables, figures, run metadata, requirements, manifests, and checksums.

The Stage 1 screening funnel must be read with the reconciliation note in the archive. The final public release should present one internally consistent sequence of identification, screening, exclusion, and retention counts.

### `chapter4_measurement_data_archive_v1.0.2/`

This archive documents construction of evidence-linked institutional measures for 48 IGOs. It contains:

- the 48-organisation study roster;
- documentary provenance and extraction metadata;
- candidate review, decision, and traceability records;
- the baseline Attribute Matrix;
- the reconciled 80-category schema and activation matrix;
- hybrid scores and corrected within-IGO and across-IGO normalised matrices;
- a corrected 48 × 174 master matrix;
- descriptive summaries, scripts, validation reports, manifests, and checksums.

The verified measurement archive records 58 source documents, 2,435 extracted pages, 5,159 paragraph-level evidence units, 3,636 reviewed candidate passages, 3,074 retained evidence records, and 1,862 CLEAN-confirmed IGO-category activations. The public repository does not relicense third-party source documents or unrestricted full-text extractions; consult the document manifest and rights statement for provenance and access conditions.

### `chapter5_data_archive/`

This archive contains the processed datasets, R scripts, figures, data dictionary, and quality-assurance records used to examine three connected features of the governance system:

1. institutional incongruence between mandate similarity and relational similarity;
2. relational-network structure, centrality, nexus nodes, and institutional silos; and
3. functional differentiation, including regulatory–delivery alignment and technical-rule/guardrail orientation.

The public archive excludes marked thesis drafts, supervisor comments, tracked changes, and other working materials that are not necessary for reproduction.

## Data lineage

```text
Literature identification and screening
        ↓
Manual seed-theme provenance
        ↓
NLP-assisted governance-theme discovery
        ↓
Theme normalisation and reduction
        ↓
Category and attribute derivation
        ↓
IGO study-population and document-corpus construction
        ↓
Indicator-linked evidence retrieval and CLEAN review
        ↓
Attribute Matrix integration and validation
        ↓
Category activation, hybrid scoring, and dual normalisation
        ↓
Dyadic, network, and functional-differentiation analysis
```

## Getting started

1. Read this root README and `RIGHTS_AND_REUSE.md`.
2. Open each component archive's README and manifest before using its files.
3. For the measurement dataset, begin with the Chapter 4 chapter-to-data crosswalk and validation status.
4. For analysis-ready use, consult the corrected Chapter 4 master matrix and consolidated workbooks.
5. For Chapter 5 reproduction, run the documented R entry point from the Chapter 5 archive root.
6. Verify downloaded ZIP files against `SHA256SUMS.txt` in the corresponding GitHub or Zenodo release.

## Reproducibility

The repository includes Python and R scripts, package requirements, run metadata, configuration files, intermediate products, decision records, manifests, and checksums. Human-reviewed CLEAN decisions are treated as fixed research inputs; scripts reproduce the computational transformations built on those decisions.

Reproduction should be undertaken from a tagged release because the default branch may contain later documentation or workflow improvements. The first integrated public release is `v1.0.0`.

## Known limitations

- The data are document-based and should not be interpreted as direct measures of implementation or outcomes.
- Documentary visibility may vary across organisations and institutional functions.
- Human review and adjudication remain integral to the coding architecture despite computational retrieval and transformation.
- Some original source files may require separate retrieval from issuing organisations because third-party rights prevent open redistribution.
- The Chapter 4 release documents corrections to archived scoring and normalisation code; users should rely on the canonical corrected matrices identified in its validation report.
- Exact reproduction depends on the software environments and source-document versions recorded in the component archives.

## Citation

Cite the version-specific Zenodo DOI for the files used in an analysis. See `CITATION.cff` for machine-readable citation metadata. When relevant, also cite the associated thesis, methods paper, or empirical publication linked from the Zenodo record.

## Licence and rights

Researcher-generated data, documentation, tables, and figures are licensed under Creative Commons Attribution 4.0 International. Original Python and R code is licensed under the MIT License. Third-party documents and text remain governed by their original rights and are not relicensed by this repository. See `LICENSE.md` and `RIGHTS_AND_REUSE.md` for the operative scope.

## Creator

**Ibukun Adewumi**  
Australian National Centre for Ocean Resources and Security (ANCORS)  
University of Wollongong

Add the verified ORCID, repository contact email, GitHub URL, and Zenodo DOI before public release.
