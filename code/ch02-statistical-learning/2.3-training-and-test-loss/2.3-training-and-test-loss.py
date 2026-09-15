"""
Chapter 2 - Statistical Learning
Section 2.3 - Training and Test Loss

Notes: notes/ch02-statistical-learning/2.3-training-and-test-loss.md

Example 2.1 - Polynomial Regression (training loss, model complexity, test loss).

This inlines the book's three chained scripts (polyregN.py, the fitted-curve
plot, and the test-loss plot) into a single standalone script.
"""

import numpy as np
from numpy.random import rand, randn
from numpy.linalg import norm, solve
import matplotlib.pyplot as plt


def generate_data(beta, sig, n):
    u = np.random.rand(n, 1)
    y = (u ** np.arange(0, 4)) @ beta + sig * np.random.randn(n, 1)
    return u, y


np.random.seed(12)
beta = np.array([[10, -140, 400, -250]]).T
n = 100
sig = 5
u, y = generate_data(beta, sig, n)
xx = np.arange(np.min(u), np.max(u) + 5e-3, 5e-3)
yy = np.polyval(np.flip(beta), xx)

plt.figure()
plt.plot(u, y, '.', markersize=8)
plt.plot(xx, yy, '--', linewidth=3)
plt.xlabel(r'$u$')
plt.ylabel(r'$h^*(u)$')
plt.legend(['data points', 'true'])
plt.show()

# --- fit polynomial models of order p = 1, ..., 18 and record training loss ---
max_p = 18
p_range = np.arange(1, max_p + 1, 1)
X = np.ones((n, 1))
betahat, trainloss = {}, {}

for p in p_range:
    if p > 1:
        X = np.hstack((X, u ** (p - 1)))
    betahat[p] = solve(X.T @ X, X.T @ y)
    trainloss[p] = (norm(y - X @ betahat[p]) ** 2 / n)
    print(f'p = {p:2d}   training loss = {trainloss[p]:.4f}')

p_selected = [2, 4, 16]
plt.figure()
plots = [plt.plot(u, y, 'k.', markersize=8)[0],
         plt.plot(xx, yy, 'k--', linewidth=3)[0]]
for i in p_selected:
    yy_fit = np.polyval(np.flip(betahat[i]), xx)
    plots.append(plt.plot(xx, yy_fit)[0])
plt.xlabel(r'$u$')
plt.ylabel(r'$h^{\mathcal{H}_p}_{\tau}(u)$')
plt.legend(plots, ('data points', 'true', '$p=2$, underfit',
                    '$p=4$, correct', '$p=16$, overfit'))
plt.show()

# --- generate test data and plot test loss against the number of parameters ---
u_test, y_test = generate_data(beta, sig, n)

MSE = []
X_test = np.ones((n, 1))
for p in p_range:
    if p > 1:
        X_test = np.hstack((X_test, u_test ** (p - 1)))
    y_hat = X_test @ betahat[p]
    MSE.append(np.sum((y_test - y_hat) ** 2 / n))
    print(f'p = {p:2d}   test loss = {MSE[-1]:.4f}')

plt.figure()
plt.plot(p_range, MSE, 'b', p_range, MSE, 'bo')
plt.xticks(ticks=p_range)
plt.xlabel('Number of parameters $p$')
plt.ylabel('Test loss')
plt.show()
