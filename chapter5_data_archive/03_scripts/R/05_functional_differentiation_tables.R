# Section 5.4: functional differentiation score exports
# Run from the root of chapter5_data_archive.

library(readr)
library(dplyr)

base <- '02_processed_outputs/section_5_4_functional_differentiation'

# Full exports generated for final deposit
reg_delivery <- read_csv(file.path(base, 'regulatory_delivery_scores_all_48_igos.csv'), show_col_types = FALSE)
functional_alignment <- read_csv(file.path(base, 'functional_alignment_scores_all_48_igos.csv'), show_col_types = FALSE)
functional_classes <- read_csv(file.path(base, 'functional_orientation_classes_all_48_igos.csv'), show_col_types = FALSE)
class_counts <- read_csv(file.path(base, 'functional_orientation_class_counts_all_48_igos.csv'), show_col_types = FALSE)

# Quick verification checks
stopifnot(nrow(reg_delivery) == 48)
stopifnot(nrow(functional_alignment) == 48)
stopifnot(nrow(functional_classes) == 48)
stopifnot(sum(class_counts$number_of_igos) == 48)

# Figure-specific data, using the corrected Chapter 5 figure order:
# Figure 5.10 = regulatory-delivery scatterplot
# Figure 5.11 = functional-orientation sunburst / hierarchy
# Figure 5.12 = ranked functional-alignment distribution
fig_5_10 <- read_csv(file.path(base, 'figure_5_10_regulatory_delivery_plot_data_all_48_igos.csv'), show_col_types = FALSE)
fig_5_11 <- read_csv(file.path(base, 'figure_5_11_functional_orientation_sunburst_data_all_48_igos.csv'), show_col_types = FALSE)
fig_5_12 <- read_csv(file.path(base, 'figure_5_12_functional_alignment_plot_data_all_48_igos.csv'), show_col_types = FALSE)

# Selected table outputs used in the Chapter 5 prose
table_5_10 <- read_csv(file.path(base, 'table_5_10_selected_regulatory_delivery_gap_results.csv'), show_col_types = FALSE)
table_5_11 <- read_csv(file.path(base, 'table_5_11_functional_orientation_classes.csv'), show_col_types = FALSE)
table_5_12 <- read_csv(file.path(base, 'table_5_12_selected_functional_alignment_scores.csv'), show_col_types = FALSE)

list(
  regulatory_delivery = reg_delivery,
  functional_alignment = functional_alignment,
  functional_classes = functional_classes,
  class_counts = class_counts,
  fig_5_10 = fig_5_10,
  fig_5_11_sunburst = fig_5_11,
  fig_5_12_ranked_alignment = fig_5_12,
  table_5_10 = table_5_10,
  table_5_11 = table_5_11,
  table_5_12 = table_5_12
)
