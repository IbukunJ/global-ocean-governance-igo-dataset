# Chapter 5 data archive: setup packages
# Run from the archive root. This script checks for packages used by the Chapter 5
# computational workflow and installs missing packages from the active R repository.
required <- c(
  'readxl','readr','dplyr','tidyr','stringr','janitor','purrr','tibble',
  'ggplot2','ggrepel','scales','igraph','tidygraph','ggraph','circlize'
)
missing <- required[!vapply(required, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing) > 0) install.packages(missing)
