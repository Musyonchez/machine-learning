"""
Chapter 3 - Monte Carlo Methods
Exercise 14

Notes: notes/ch03-monte-carlo-methods/exercises.md

Part (b): Gibbs sampler for a bivariate normal with mean [1, 2] and
covariance [[1, a], [a, 4]], for a in {0, 1, 1.75}. Draw 1000 samples for
each a and plot them.

Conditional distributions (Theorem C.8):
    (Y | X=x) ~ N(2 + a*(x-1), 4 - a^2)
    (X | Y=y) ~ N(1 + (a/4)*(y-2), 1 - a^2/4)
"""

import numpy as np
import matplotlib.pyplot as plt

def gibbs_bvn(a, n_samples=1000):
    mu1, mu2 = 1, 2
    x, y = mu1, mu2
    samples = np.zeros((n_samples, 2))
    for t in range(n_samples):
        # (X | Y=y) ~ N(mu1 + (a/4)*(y-mu2), 1 - a^2/4)
        x = mu1 + (a/4)*(y-mu2) + np.sqrt(max(1 - a**2/4, 1e-12))*np.random.randn()
        # (Y | X=x) ~ N(mu2 + a*(x-mu1), 4 - a^2)
        y = mu2 + a*(x-mu1) + np.sqrt(max(4 - a**2, 1e-12))*np.random.randn()
        samples[t] = [x, y]
    return samples

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, a in zip(axes, [0, 1, 1.75]):
    s = gibbs_bvn(a)
    ax.scatter(s[:, 0], s[:, 1], s=5, alpha=0.5)
    ax.set_title(f'a = {a}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
plt.tight_layout()
plt.show()
