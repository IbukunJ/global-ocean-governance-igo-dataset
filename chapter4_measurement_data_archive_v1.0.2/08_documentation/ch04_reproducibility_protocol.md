# Chapter 4 reproducibility protocol

## Recommended order

1. Verify the 48-case roster in `01_study_population/`.
2. Verify document identities and checksums in the Stage 2 manifest. Re-run extraction only where source-document access and PyMuPDF compatibility permit.
3. Treat the Stage 3 candidate queue and CLEAN decisions as audited human-coded inputs. Run `validate_step3_outputs.py` to confirm screening totals and traceability-row consistency.
4. Rebuild the baseline matrix with `step4_integrate.py` and confirm all integrity checks pass.
5. Run the Stage 6 R pipeline from `06_scoring_and_normalisation/` with `Rscript run_all.R`. Compare regenerated outputs with the supplied canonical matrices and reconciliation report.
6. Use `07_analysis_ready_outputs/ch04_analysis_ready_matrices.xlsx` for examiner navigation and `ch04_master_matrix_48x174_corrected.csv` for programmatic analysis.

## Fixed human decisions

The CLEAN decisions are not regenerated automatically. They are the human-adjudicated measurement inputs. Reproducibility therefore means preserving and reusing those decisions transparently, not replacing them with an automated classifier.

## Expected counts

The expected counts are 48 cases, 58 documents, 2,435 pages, 5,159 paragraphs, 3,636 candidates, 3,074 retained evidence records, 480 integrated matrix cells including Scale, 3,840 category observations, and 1,862 confirmed category activations.
