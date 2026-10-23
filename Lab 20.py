import numpy as np
from scipy.stats import ttest_ind

A = np.array([0.20, 0.22, 0.19, 0.25, 0.21, 0.23])
B = np.array([0.28, 0.30, 0.27, 0.29, 0.31, 0.26])

t_stat, p_value = ttest_ind(A, B)

print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")