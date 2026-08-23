# Reproduce Figure 5.2 from dyadic similarity data
library(readr); library(dplyr); library(ggplot2); library(ggrepel)
d <- read_csv('02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv', show_col_types = FALSE) %>% mutate(delta_incongruence = mandate_similarity - relational_similarity, label = paste(IGO_A, IGO_B, sep='-'))
q90 <- quantile(d$mandate_similarity, .90); q10 <- quantile(d$relational_similarity, .10)
d <- d %>% mutate(dyad_type = case_when(mandate_similarity >= q90 & relational_similarity <= q10 ~ 'High-incongruence dyads', delta_incongruence > 0 ~ 'Positive incongruence', TRUE ~ 'Relationally bridged / near-aligned'))
labels <- d %>% filter(delta_incongruence > 0) %>% arrange(desc(delta_incongruence)) %>% slice_head(n=14)
p <- ggplot(d, aes(mandate_similarity, relational_similarity, colour=dyad_type)) + geom_abline(slope=1, intercept=0, linetype='dashed') + geom_vline(xintercept=q90, linetype='dotted') + geom_hline(yintercept=q10, linetype='dotted') + geom_point(alpha=.65) + geom_text_repel(data=labels, aes(label=label), size=3, max.overlaps=Inf) + coord_equal(xlim=c(0,1), ylim=c(0,1)) + labs(x='Mandate similarity', y='Relational similarity') + theme_minimal(base_size=12)
ggsave('04_figures/final/fig_5_2_mandate_relational_similarity_space_rebuilt.png', p, width=8.5, height=7, dpi=300)
