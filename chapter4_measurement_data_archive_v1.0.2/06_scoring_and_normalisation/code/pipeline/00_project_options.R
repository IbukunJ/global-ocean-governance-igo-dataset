# 00_project_options.R
# ------------------------------------------------------------------------------
# Project options and directory scaffolding.
# Run this script first (from the repository root).
# ------------------------------------------------------------------------------

# Reproducibility
set.seed(123)

dir.create("outputs", showWarnings = FALSE)
dir.create(file.path("outputs","reports"), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path("outputs","tables"), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path("outputs","figures"), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path("outputs","data"), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path("outputs","logs"), recursive = TRUE, showWarnings = FALSE)

# Lightweight sanity checks (inputs)
stopifnot(file.exists("config/category_schema.csv"))
stopifnot(file.exists("data/raw/ch04_s6_raw_year_of_establishment.csv"))
stopifnot(file.exists("data/raw/ch04_s6_raw_year_of_establishment_with_context.xlsx") || TRUE)
