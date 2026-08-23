#!/usr/bin/env python3
"""Regenerate the Chapter 4 descriptive overview outputs and ranked profile plot.

The IGO-level summary is an unweighted descriptive mean across the 80 across-IGO
category scores. It is not an effectiveness index or external benchmark.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
profiles = pd.read_csv(HERE / "ch04_igo_overall_profiles.csv")
profiles = profiles.sort_values("mean_across", ascending=True)

fig, ax = plt.subplots(figsize=(8.2, 11.5))
y = range(len(profiles))
ax.scatter(profiles["mean_across"], y, s=24)
ax.axvline(profiles["mean_across"].mean(), linestyle="--", linewidth=1,
           label=f"Population mean = {profiles['mean_across'].mean():.2f}")
ax.set_yticks(list(y))
ax.set_yticklabels(profiles["institution"], fontsize=6.8)
ax.set_xlabel("Mean across-IGO category-profile score")
ax.set_ylabel("")
ax.set_title("Descriptive category-profile means across 48 organisations")
ax.grid(axis="x", linewidth=0.4, alpha=0.5)
ax.legend(loc="lower right", fontsize=8, frameon=False)
fig.tight_layout()
fig.savefig(HERE / "ch04_igo_overall_profile_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print("Wrote", HERE / "ch04_igo_overall_profile_plot.png")
