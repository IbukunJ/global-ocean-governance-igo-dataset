# Reproduce Figure 5.1 from dyadic similarity data
library(readr); library(dplyr); library(ggplot2)
d <- read_csv('02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv', show_col_types = FALSE) %>% mutate(delta_incongruence = mandate_similarity - relational_similarity)
lower <- quantile(d$delta_incongruence, 1/3, na.rm = TRUE); upper <- quantile(d$delta_incongruence, 2/3, na.rm = TRUE)
p <- ggplot(d, aes(delta_incongruence)) + geom_histogram(bins = 27, fill = '#D8B365', colour = 'white') + geom_vline(xintercept = c(mean(d$delta_incongruence), median(d$delta_incongruence), 0), linetype = c('dashed','dashed','dotted')) + labs(x='Delta incongruence', y='Number of dyads') + theme_minimal(base_size=12)
ggsave('04_figures/final/fig_5_1_delta_incongruence_distribution_rebuilt.png', p, width=8.5, height=5.5, dpi=300)
