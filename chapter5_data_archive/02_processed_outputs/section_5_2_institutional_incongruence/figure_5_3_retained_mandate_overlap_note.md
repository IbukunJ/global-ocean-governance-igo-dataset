# Figure 5.3 retained mandate-overlap ties

This output supports Figure 5.3, *Strongest mandate-overlap ties among IGOs*.

- Source data: `dyadic_mandate_relational_similarity.csv`
- Retention rule: retain dyads with `mandate_similarity >= q90(mandate_similarity)`
- q90 mandate-similarity threshold: 0.734433892970
- Retained dyads: 113
- Figure outputs: `04_figures/final/fig_5_3_strongest_mandate_overlap_ties.png`, `.pdf`, `.svg`

The retained edge list should be read as a visualisation-ready extract of the strongest mandate-overlap ties. It does not represent relational coordination; relational coordination is assessed separately in Section 5.3 using the q90 relational-similarity network.
