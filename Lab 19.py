import numpy as np
from scipy import stats

drug = np.array([10, 12, 11, 15, 14, 13, 12, 16, 14, 15])
placebo = np.array([5, 7, 6, 8, 7, 6, 5, 9, 8, 7])

drug_ci = stats.t.interval(
    0.95,
    len(drug) - 1,
    loc=np.mean(drug),
    scale=stats.sem(drug)
)

placebo_ci = stats.t.interval(
    0.95,
    len(placebo) - 1,
    loc=np.mean(placebo),
    scale=stats.sem(placebo)
)

print("Drug 95% CI:", drug_ci)
print("Placebo 95% CI:", placebo_ci)