# Section 5.4 Functional Score Export Audit

This folder now contains full 48-IGO score exports for Figures 5.10-5.12.

## Figure 5.10: regulatory strength vs delivery capacity

`regulatory_delivery_scores_all_48_igos.csv` and `figure_5_10_regulatory_delivery_plot_data_all_48_igos.csv` were computed from the normalised Attribute Matrix workbooks in `01_raw_inputs/normalised_attribute_workbooks/`.

### Regulatory strength

Regulatory strength is the row-wise mean of four across-IGO Source of Jurisdiction categories:

1. `Binding Secondary Law_AcrossIGO`
2. `Compliance & Oversight_AcrossIGO`
3. `Delegated or Derived Powers_AcrossIGO`
4. `Foundational Treaties & Charters_AcrossIGO`

This reproduces the selected values used in the Chapter 5 text, including IOC = 4.583, ITU = 3.958, UNOOSA = 3.750, ILO = 3.750, IAEA = 2.500, UN DOALOS = 2.917, and UNDRR = 0.000 before rounding.

### Delivery capacity

Delivery capacity is the row-wise mean of seven across-IGO coordination and delivery-pathway categories:

1. `Multi-level Planning Structures_AcrossIGO`
2. `Policy Alignment with National Plans_AcrossIGO`
3. `Reporting & Compliance Mechanisms_AcrossIGO`
4. `Technical Assistance to States_AcrossIGO`
5. `Inter-agency Technical Cooperation_AcrossIGO`
6. `Shared Monitoring Frameworks_AcrossIGO`
7. `Thematic Working Groups_AcrossIGO`

This reproduces the selected values used in the Chapter 5 text, including IOC = 1.286, ITU = 0.238, UNOOSA = 0.714, ILO = 0.714, IAEA = 2.476, UN DOALOS = 2.952, and UNDRR = 1.619 before rounding.

## Figures 5.11-5.12: functional alignment and orientation classes

`functional_alignment_scores_all_48_igos.csv`, `figure_5_11_functional_alignment_plot_data_all_48_igos.csv`, and `figure_5_12_functional_orientation_sunburst_data_all_48_igos.csv` provide the full 48-case functional-orientation data. The scores are the archived full ranked values used in the Chapter 5 functional-alignment analysis and were cross-checked against the associated class-count and selected-score outputs. The class counts are:

- Technical-rule dominant: 28 IGOs
- Balanced: 12 IGOs
- Guardrail dominant: 8 IGOs

## Notes

- `figure_label` preserves the label visible in the figure. `igo_acronym` harmonises labels to the archive naming convention.
- `CCS` in the embedded figure is harmonised as `UNFCCC`, corresponding to the Climate Change Secretariat.
- These exports replace the earlier selected-only Section 5.4 files and remove the previous missing-data note.
