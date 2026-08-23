# Figure 5.3: retained mandate-overlap edge list and chord visualisation
# Run from the root of chapter5_data_archive.

library(readr)
library(dplyr)

source_file <- '02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv'
out_dir <- '02_processed_outputs/section_5_2_institutional_incongruence'
fig_dir <- '04_figures/final'

dyads <- read_csv(source_file, show_col_types = FALSE)

q90_mandate <- quantile(dyads$mandate_similarity, 0.90, na.rm = TRUE)

retained_edges <- dyads %>%
  filter(mandate_similarity >= q90_mandate) %>%
  arrange(desc(mandate_similarity), IGO_A, IGO_B) %>%
  mutate(
    edge_rank_by_mandate_similarity = row_number(),
    q90_mandate_threshold = as.numeric(q90_mandate),
    retention_rule = 'mandate_similarity >= q90(mandate_similarity)',
    edge_weight_for_chord = mandate_similarity
  ) %>%
  select(
    edge_rank_by_mandate_similarity,
    IGO_A, IGO_B,
    mandate_similarity, relational_similarity, delta_incongruence,
    positive_incongruence, high_incongruence,
    q90_mandate_threshold, retention_rule, edge_weight_for_chord
  )

write_csv(retained_edges, file.path(out_dir, 'figure_5_3_retained_mandate_overlap_edges.csv'))

node_summary <- retained_edges %>%
  select(IGO_A, IGO_B, mandate_similarity) %>%
  tidyr::pivot_longer(c(IGO_A, IGO_B), names_to = 'endpoint', values_to = 'organisation') %>%
  group_by(organisation) %>%
  summarise(
    retained_overlap_degree = n(),
    retained_overlap_strength = sum(mandate_similarity, na.rm = TRUE),
    max_retained_mandate_similarity = max(mandate_similarity, na.rm = TRUE),
    .groups = 'drop'
  ) %>%
  arrange(desc(retained_overlap_degree), desc(retained_overlap_strength), organisation)

write_csv(node_summary, file.path(out_dir, 'figure_5_3_retained_mandate_overlap_node_summary.csv'))

# Optional chord rendering. This requires the circlize package.
# If circlize is not installed, the script still writes the retained edge and node-summary CSVs.
if (requireNamespace('circlize', quietly = TRUE)) {
  chord_mat <- retained_edges %>%
    select(IGO_A, IGO_B, edge_weight_for_chord)

  png(file.path(fig_dir, 'fig_5_3_strongest_mandate_overlap_ties_rebuilt.png'),
      width = 2400, height = 2400, res = 300)
  circlize::circos.clear()
  circlize::chordDiagram(
    x = chord_mat,
    transparency = 0.45,
    annotationTrack = c('grid'),
    preAllocateTracks = 1
  )
  circlize::circos.trackPlotRegion(
    track.index = 1,
    panel.fun = function(x, y) {
      sector_name <- circlize::get.cell.meta.data('sector.index')
      xlim <- circlize::get.cell.meta.data('xlim')
      ylim <- circlize::get.cell.meta.data('ylim')
      circlize::circos.text(mean(xlim), ylim[1], sector_name,
                            facing = 'clockwise', niceFacing = TRUE,
                            adj = c(0, 0.5), cex = 0.45)
    },
    bg.border = NA
  )
  circlize::circos.clear()
  dev.off()
}
