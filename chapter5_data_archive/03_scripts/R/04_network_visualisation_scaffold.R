# Simple scaffold for network visualisation from archived node/edge outputs
library(readr); library(dplyr); library(igraph); library(ggraph); library(ggplot2)
edges <- read_csv('02_processed_outputs/section_5_3_relational_coordination/relational_network_edges_q90.csv', show_col_types=FALSE) %>% transmute(from=IGO_A, to=IGO_B, weight=relational_similarity)
nodes <- read_csv('02_processed_outputs/section_5_3_relational_coordination/relational_network_node_metrics_q90.csv', show_col_types=FALSE) %>% rename(name=organisation)
g <- graph_from_data_frame(edges, directed=FALSE, vertices=nodes)
p <- ggraph(g, layout='fr') + geom_edge_link(aes(width=weight), colour='grey75', alpha=.5) + geom_node_point(aes(size=eigenvector_centrality, colour=relational_position)) + geom_node_text(aes(label=name), repel=TRUE, size=3) + theme_void()
ggsave('04_figures/final/fig_5_7_network_rebuilt_scaffold.png', p, width=11, height=8, dpi=300)
