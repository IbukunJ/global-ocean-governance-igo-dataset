# run_all.R
# ------------------------------------------------------------------------------
# Convenience wrapper to regenerate the Chapter 4 analysis artefacts.
# ------------------------------------------------------------------------------

source('code/pipeline/00_project_options.R')
source('code/pipeline/01_build_historical_context.R')

# Stage A (RAW-only; first normalisation)
source('code/pipeline/02_build_stageA_raw_only_tables.R')

# Stage B (FULL; CLEAN-integrated normalisation)
source('code/pipeline/03_build_stageB_full_normalised_tables.R')

# Master analysis matrix + figures + dictionaries
source('code/pipeline/04_build_master_matrix.R')
source('code/pipeline/05_make_figures.R')
source('code/pipeline/06_make_dictionaries_and_codebook.R')

# Optional: render narrative reports/notebooks (kept for convenience)
if (file.exists('pipeline/04_render_reports.R')) {
  source('code/pipeline/04_render_reports.R')
}
