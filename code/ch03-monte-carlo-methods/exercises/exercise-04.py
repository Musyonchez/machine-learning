"""
Chapter 3 - Monte Carlo Methods
Exercise 4

Notes: notes/ch03-monte-carlo-methods/exercises.md

Construct simulation algorithms, via inverse-transform, for:
(a) Weib(alpha, lambda), cdf F(x) = 1 - exp(-(lambda*x)^alpha)
    => F^{-1}(u) = (-ln(1-u))^(1/alpha) / lambda
(b) Pareto(alpha, lambda), pdf f(x) = alpha*lambda*(1+lambda*x)^(-(alpha+1))
    cdf F(x) = 1 - (1+lambda*x)^(-alpha)
    => F^{-1}(u) = ((1-u)^(-1/alpha) - 1) / lambda
"""

import numpy as np
import matplotlib.pyplot as plt

n = 10000

# (a) Weibull(alpha, lambda) via inverse-transform
def sim_weibull(alpha, lam, size):
    U = np.random.rand(size)
    return (-np.log(1-U))**(1/alpha) / lam

# (b) Pareto(alpha, lambda) via inverse-transform
def sim_pareto(alpha, lam, size):
    U = np.random.rand(size)
    return ((1-U)**(-1/alpha) - 1) / lam

alpha_w, lam_w = 2.0, 1.5
X_weib = sim_weibull(alpha_w, lam_w, n)

alpha_p, lam_p = 3.0, 1.0
X_par = sim_pareto(alpha_p, lam_p, n)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(X_weib, bins=50, density=True)
axes[0].set_title(f'Weibull(alpha={alpha_w}, lambda={lam_w})')
axes[1].hist(X_par, bins=50, density=True)
axes[1].set_title(f'Pareto(alpha={alpha_p}, lambda={lam_p})')
plt.tight_layout()
plt.show()
