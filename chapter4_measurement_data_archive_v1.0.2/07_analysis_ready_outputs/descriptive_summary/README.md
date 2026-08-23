# Descriptive overview outputs

This folder contains the bounded descriptive summaries added in response to supervisory requests for an overall account of what the Chapter 4 measurement outputs show across attribute families, categories, and organisations.

## Files

- `ch04_family_summary.csv`: activation counts/rates and corrected within-IGO/across-IGO means and standard deviations for the eight substantive attribute families.
- `ch04_category_prevalence.csv`: category-level activation counts, percentages, and descriptive score summaries.
- `ch04_igo_overall_profiles.csv`: organisation-level descriptive profile summaries.
- `ch04_igo_overall_profile_plot.png`: ranked visualisation of the 48 organisation-level mean across-IGO profile scores.
- `build_ch04_descriptive_overview.py`: script used to regenerate the ranked plot.

## Interpretation boundary

The organisation-level `mean_across` value is the unweighted mean of the 80 across-IGO category scores for descriptive overview only. It summarises the breadth and intensity of documented category activation under the Chapter 4 coding and normalisation rules. It is not an effectiveness index, performance ranking, or external benchmark.

The underlying canonical matrices remain in `06_scoring_and_normalisation/outputs/` and `07_analysis_ready_outputs/`.
