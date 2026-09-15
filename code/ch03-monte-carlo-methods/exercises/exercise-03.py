"""
Chapter 3 - Monte Carlo Methods
Exercise 3

Notes: notes/ch03-monte-carlo-methods/exercises.md

Simulate from the pdf

    f(x) = x/2         for 0 <= x < 1
    f(x) = 1/2         for 1 <= x <= 2.5

using (a) the inverse-transform method and (b) acceptance-rejection with
proposal g(x) = (8/25)*x on [0, 2.5].

For (a): F(x) = x^2/4 for 0 <= x < 1, F(x) = 1/4 + (x-1)/2 for 1 <= x <= 2.5.
Inverse: for u <= 1/4, x = 2*sqrt(u); for u > 1/4, x = 2u + 1/2.

For (b): g(x) = (8/25)*x on [0, 2.5] has its own cdf G(x) = (4/25)*x^2, so it
is sampled via its own inverse-transform G^{-1}(u) = 2.5*sqrt(u), then
accepted/rejected against f.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 10000

# (a) Inverse-transform method
def f_inv(u):
    return np.where(u <= 0.25, 2*np.sqrt(u), 2*u + 0.5)

U = np.random.rand(n)
X_invtransform = f_inv(U)

# (b) Acceptance-rejection with proposal g(x) = (8/25)x on [0, 2.5]
def f_pdf(x):
    return np.where(x < 1, 0.5*x, 0.5)

def g_pdf(x):
    return (8/25)*x

def g_sample(size):
    u = np.random.rand(size)
    return 2.5*np.sqrt(u)  # inverse-transform for g

# find C = max f(x)/g(x) over (0, 2.5] so that C*g(x) >= f(x) everywhere
x_check = np.linspace(1e-6, 2.5, 100000)
C = np.max(f_pdf(x_check) / g_pdf(x_check))

accepted = []
while len(accepted) < n:
    batch = 2*(n - len(accepted))
    Y = g_sample(batch)
    U2 = np.random.rand(batch)
    keep = U2 <= f_pdf(Y) / (C*g_pdf(Y))
    accepted.extend(Y[keep].tolist())
X_acceptreject = np.array(accepted[:n])

plt.figure()
plt.hist(X_invtransform, bins=50, density=True, alpha=0.5, label='inverse-transform')
plt.hist(X_acceptreject, bins=50, density=True, alpha=0.5, label='acceptance-rejection')
xx = np.linspace(0, 2.5, 500)
plt.plot(xx, f_pdf(xx), 'k-', label='true pdf')
plt.legend()
plt.xlabel('x')
plt.ylabel('density')
plt.show()

print('C used for acceptance-rejection:', C)
