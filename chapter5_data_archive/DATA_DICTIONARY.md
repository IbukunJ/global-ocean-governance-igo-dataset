# Data Dictionary

## Public-safe normalised attribute workbooks

The eight substantive `*_full_normalised.xlsx` files contain only the `Matrix_Wide` analytical sheet in this public edition. Each matrix contains 48 IGO rows plus a header and 22 columns: institution name, ordinal score, ten within-IGO category scores, and ten across-IGO category scores. The evidence-rich `Traceability_Long` sheets are not distributed. `year_of_establishment_categories_density.xlsx` contains the organisation label, cleaned establishment year, founding-era category, five-year founding density, and cumulative institutional stock.

## dyadic_mandate_relational_similarity.csv
- `IGO_A`, `IGO_B`: unordered IGO dyad members.
- `mandate_similarity`: dyadic similarity in mandate space.
- `relational_similarity`: dyadic similarity in relational space.
- `delta_incongruence`: mandate similarity minus relational similarity.
- `positive_incongruence`: TRUE when delta incongruence is positive.
- `high_incongruence`: TRUE when the dyad meets high-mandate and low-relational filters.

## figure_5_3_retained_mandate_overlap_edges.csv
- `edge_rank_by_mandate_similarity`: rank after sorting retained edges from highest to lowest mandate similarity.
- `IGO_A`, `IGO_B`: unordered IGO dyad members.
- `mandate_similarity`: dyadic similarity in mandate space.
- `relational_similarity`: dyadic similarity in relational space, retained for comparison.
- `delta_incongruence`: mandate similarity minus relational similarity.
- `positive_incongruence`: TRUE when delta incongruence is positive.
- `high_incongruence`: TRUE when the dyad also meets the high-mandate/low-relational filter used in Table 5.6.
- `q90_mandate_threshold`: top-decile mandate-similarity threshold used to retain Figure 5.3 chord edges.
- `retention_rule`: text description of the retention rule.
- `edge_weight_for_chord`: edge weight used for the Figure 5.3 chord visualisation.

## figure_5_3_retained_mandate_overlap_node_summary.csv
- `organisation`: IGO acronym or short name.
- `retained_overlap_degree`: number of retained top-decile mandate-overlap ties attached to the organisation.
- `retained_overlap_strength`: weighted sum of retained mandate-similarity ties.
- `max_retained_mandate_similarity`: highest retained mandate-similarity value involving the organisation.

## relational_network_node_metrics_q90.csv
- `organisation`: IGO acronym or short name.
- `degree`: retained ties in the q90 relational network.
- `strength`: weighted sum of retained ties.
- `betweenness`: normalised betweenness centrality using distance = 1 - similarity.
- `eigenvector_centrality`: weighted eigenvector centrality, normalised to the highest observed value.
- `community`: detected community identifier.
- `relational_position`: interpretive role used in Chapter 5.

## relational_network_edges_q90.csv
- `IGO_A`, `IGO_B`: retained edge members.
- `relational_similarity`: retained edge weight.

## regulatory_delivery_scores_all_48_igos.csv
- `rank_by_gap_desc`: rank after sorting by regulatory-delivery gap from highest to lowest.
- `canonical_institution`: full Attribute Matrix institution label.
- `igo_acronym`: harmonised short label used in figures/tables.
- `Binding Secondary Law_AcrossIGO`, `Compliance & Oversight_AcrossIGO`, `Delegated or Derived Powers_AcrossIGO`, `Foundational Treaties & Charters_AcrossIGO`: component categories used to calculate regulatory strength.
- `regulatory_strength`: row-wise mean of the four regulatory component categories.
- `Multi-level Planning Structures_AcrossIGO`, `Policy Alignment with National Plans_AcrossIGO`, `Reporting & Compliance Mechanisms_AcrossIGO`, `Technical Assistance to States_AcrossIGO`, `Inter-agency Technical Cooperation_AcrossIGO`, `Shared Monitoring Frameworks_AcrossIGO`, `Thematic Working Groups_AcrossIGO`: component categories used to calculate delivery capacity.
- `delivery_capacity`: row-wise mean of the seven delivery component categories.
- `regulatory_delivery_gap`: regulatory strength minus delivery capacity.
- `regulatory_delivery_profile`: descriptive class based on gap direction and near-alignment threshold.

## functional_alignment_scores_all_48_igos.csv
- `rank_descending`: rank from most technical-rule dominant to most guardrail dominant.
- `figure_label`: label visible in the ranked functional-orientation figure.
- `igo_acronym`: harmonised archive label.
- `functional_alignment_score`: technical-rule emphasis minus guardrail emphasis.
- `functional_orientation`: Technical-rule dominant, Balanced, or Guardrail dominant.
- `canonical_institution`: full Attribute Matrix label where available.
- `plot_side`: plotting side relative to zero.
- `score_source`: provenance note for the full 48-case score series.

## functional_orientation_class_counts_all_48_igos.csv
- `functional_orientation`: class label.
- `number_of_igos`: count of IGOs in that class.
- `members`: semicolon-separated list of IGO acronyms in that class.

## figure_5_12_functional_orientation_sunburst_data_all_48_igos.csv
- `id`: hierarchy node identifier.
- `parent`: parent node for sunburst/tree visualisation.
- `label`: display label.
- `value`: count/value used by hierarchy visualisation.
- `functional_alignment_score`: IGO-level functional alignment score where applicable.
- `functional_orientation`: class label where applicable.


## Script: 02b_figure_5_3_mandate_overlap_chord_edges.R
- Rebuilds `figure_5_3_retained_mandate_overlap_edges.csv` from `dyadic_mandate_relational_similarity.csv`.
- Applies the retention rule `mandate_similarity >= q90(mandate_similarity)`.
- Writes `figure_5_3_retained_mandate_overlap_node_summary.csv`.
- Optionally renders a rebuilt chord diagram if the R package `circlize` is installed.

## Appendix: appendix_5a_chapter5_computational_methods_tools_packages_code.docx
- Expanded stand-alone documentation of Chapter 5 methods, tools, packages, output provenance, quality-assurance logic, and archived R code listings.
