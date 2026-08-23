# Reproducibility Status — Public-Safe Edition

## Reproducible from distributed files

- Section 5.2 is data-backed by the complete 1,128-row dyadic mandate–relational similarity file.
- Figure 5.1 and Figure 5.2 can be rebuilt from that dyadic file.
- Figure 5.3 retained mandate-overlap edges and node summaries can be regenerated using the top-decile mandate-similarity rule.
- Section 5.3 is data-backed by the q90 relational-network edge list and 48-node metrics file; the network tables can be reconstructed from the dyadic data.
- Section 5.4 includes full 48-IGO regulatory–delivery, functional-alignment, and functional-orientation exports.
- Regulatory strength and delivery capacity are recomputable from the public-safe `Matrix_Wide` sheets using the component categories documented in `functional_score_construction_audit.md`.
- All supplied R scripts, final figure files, plot-data exports, and selected table files are retained.

## Public-release boundary

The eight substantive normalised workbooks retain only `Matrix_Wide`. Evidence-rich `Traceability_Long` sheets containing verbatim descriptions, cleaned text, keyword maps, and KWIC evidence are excluded from public distribution. This prevents redistribution of source-derived text without altering the analytical matrices used in Chapter 5.

The supervisor-marked working draft and three internal literature/concept-note exports are also excluded. These files were not computational dependencies.

## Bounded limitation

The complete 48-case functional-alignment series is supplied as the canonical archived output used in the analysis and is cross-checked against the class-count and selected-score files. The archive does not contain a recovered final intermediate R object from which that series was originally rendered. This limitation affects end-to-end regeneration of that one score series, not its availability for verification or secondary analysis.

See `workbook_sanitisation_report.csv`, `analytical_invariance_check.csv`, and `VALIDATION_STATUS.md`.
