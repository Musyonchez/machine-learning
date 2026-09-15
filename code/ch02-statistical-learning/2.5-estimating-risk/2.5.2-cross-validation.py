"""
Chapter 2 - Statistical Learning
Section 2.5.2 - Cross-Validation (under 2.5 Estimating Risk)

Notes: notes/ch02-statistical-learning/2.5-estimating-risk.md

Example 2.4 - K-fold Cross-Validation.

This inlines the polynomial-regression setup from Example 2.1
(polyregN.py: data generation and fitting models of order p = 1, ..., 18)
as a prerequisite, then adds the K-fold cross-validation code (polyregCV.py).
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

# --- fit polynomial models of order p = 1, ..., 18 ---
max_p = 18
p_range = np.arange(1, max_p + 1, 1)
X = np.ones((n, 1))
betahat, trainloss = {}, {}

for p in p_range:
    if p > 1:
        X = np.hstack((X, u ** (p - 1)))
    betahat[p] = solve(X.T @ X, X.T @ y)
    trainloss[p] = (norm(y - X @ betahat[p]) ** 2 / n)

# --- K-fold cross-validation (polyregCV.py) ---
K_vals = [5, 10, 100]  # number of folds
cv = np.zeros((len(K_vals), max_p))  # cv loss
X = np.ones((n, 1))

for p in p_range:
    if p > 1:
        X = np.hstack((X, u ** (p - 1)))
    j = 0
    for K in K_vals:
        loss = []
        for k in range(1, K + 1):
            # integer indices of test samples
            test_ind = ((n / K) * (k - 1) + np.arange(1, n / K + 1) - 1).astype('int')
            train_ind = np.setdiff1d(np.arange(n), test_ind)

            X_train, y_train = X[train_ind, :], y[train_ind, :]
            X_test, y_test = X[test_ind, :], y[test_ind]

            betahat_cv = solve(X_train.T @ X_train, X_train.T @ y_train)
            loss.append(norm(y_test - X_test @ betahat_cv) ** 2)

        cv[j, p - 1] = sum(loss) / n
        print(f'p = {p:2d}   K = {K:3d}   CV loss = {cv[j, p - 1]:.4f}')
        j += 1

# basic plotting
plt.figure()
plt.plot(p_range, cv[0, :], 'k-.')
plt.plot(p_range, cv[1, :], 'r')
plt.plot(p_range, cv[2, :], 'b--')
plt.xlabel('Number of parameters $p$')
plt.ylabel('K-fold CV loss')
plt.legend(['K=5', 'K=10', 'K=100'])
plt.show()
