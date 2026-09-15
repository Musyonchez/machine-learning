"""
Chapter 3 - Monte Carlo Methods
Exercise 16

Notes: notes/ch03-monte-carlo-methods/exercises.md

Estimate mu = integral from -2 to 2 of exp(-x^2/2) dx via two importance
sampling approaches:
  (1) H(x) = 4*exp(-x^2/2), f = Uniform[-2,2] pdf
  (2) H(x) = sqrt(2*pi)*indicator(-2<=x<=2), f = Normal(0,1) pdf
(a) estimate mu with N=1000 for both approaches
(b) relative error with N=100
(c) 95% confidence interval with N=100
(d) find N such that the relative width of the 95% CI is below 0.01
"""

import numpy as np
from scipy import stats

def estimate(H_func, sampler, N):
    X = sampler(N)
    Y = H_func(X)
    mY = np.mean(Y)
    sY = np.std(Y, ddof=1)
    RE = sY / mY / np.sqrt(N)
    return mY, RE

# Approach 1: uniform on [-2,2]
H1 = lambda x: 4*np.exp(-x**2/2)
sampler1 = lambda N: np.random.uniform(-2, 2, N)

# Approach 2: standard normal
H2 = lambda x: np.sqrt(2*np.pi) * ((x >= -2) & (x <= 2)).astype(float)
sampler2 = lambda N: np.random.randn(N)

true_mu = np.sqrt(2*np.pi) * (stats.norm.cdf(2) - stats.norm.cdf(-2))
print('True mu (via scipy):', true_mu)

# (a) N=1000 estimates
for name, H, sampler in [('uniform', H1, sampler1), ('normal', H2, sampler2)]:
    mY, _ = estimate(H, sampler, 1000)
    print(f'(a) {name}: estimate = {mY:.4f}')

# (b) N=100 relative errors
for name, H, sampler in [('uniform', H1, sampler1), ('normal', H2, sampler2)]:
    mY, RE = estimate(H, sampler, 100)
    print(f'(b) {name}: relative error = {RE:.4f}')

# (c) 95% CI with N=100
z = 1.96
for name, H, sampler in [('uniform', H1, sampler1), ('normal', H2, sampler2)]:
    mY, RE = estimate(H, sampler, 100)
    ci = (mY*(1-z*RE), mY*(1+z*RE))
    print(f'(c) {name}: 95% CI = ({ci[0]:.4f}, {ci[1]:.4f})')

# (d) find N such that relative CI width < 0.01, i.e. 2*z*RE < 0.01
for name, H, sampler in [('uniform', H1, sampler1), ('normal', H2, sampler2)]:
    _, RE_100 = estimate(H, sampler, 100)
    # RE scales as 1/sqrt(N), so RE_100 * sqrt(100/N) < 0.01/(2*z)
    N_needed = int(np.ceil(100 * (RE_100 / (0.01/(2*z)))**2))
    mY_final, RE_final = estimate(H, sampler, N_needed)
    print(f'(d) {name}: N needed = {N_needed}, estimate = {mY_final:.4f}, '
          f'true = {true_mu:.4f}')
