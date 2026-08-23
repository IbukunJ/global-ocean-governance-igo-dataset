# Recreate q90 relational network and centrality tables
library(readr); library(dplyr); library(igraph); library(tibble)
d <- read_csv('02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv', show_col_types = FALSE)
q90 <- quantile(d$relational_similarity, .90, na.rm=TRUE)
edges <- d %>% filter(relational_similarity >= q90)
vertices <- tibble(name = sort(unique(c(d$IGO_A, d$IGO_B))))
g <- graph_from_data_frame(edges %>% transmute(from=IGO_A, to=IGO_B, weight=relational_similarity), directed=FALSE, vertices=vertices)
E(g)$distance <- 1 - E(g)$weight
metrics <- tibble(organisation=V(g)$name, degree=degree(g), strength=strength(g, weights=E(g)$weight), betweenness=betweenness(g, weights=E(g)$distance, normalized=TRUE), eigenvector_centrality=eigen_centrality(g, weights=E(g)$weight)$vector)
metrics$eigenvector_centrality <- metrics$eigenvector_centrality / max(metrics$eigenvector_centrality, na.rm=TRUE)
write_csv(edges, '02_processed_outputs/section_5_3_relational_coordination/relational_network_edges_q90_rebuilt.csv')
write_csv(metrics, '02_processed_outputs/section_5_3_relational_coordination/relational_network_node_metrics_q90_rebuilt.csv')
