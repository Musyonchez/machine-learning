"""
Chapter 3 - Monte Carlo Methods
Exercise 19

Notes: notes/ch03-monte-carlo-methods/exercises.md

Write a cross-entropy (CE) program for a binary knapsack problem.

NOTE: the original exercise references downloading the real problem
instance from an external file, Sento1.dat. To keep this file self-contained
and runnable without any external download, a small synthetic knapsack
instance (random values p, constraint matrix A, capacities c) is generated
instead. Swap in the real p, A, c arrays (loaded from the downloaded file)
to solve the actual Sento1 instance.
"""

import numpy as np

np.random.seed(0)
n = 20  # number of items
m = 3   # number of constraints (attributes)
p = np.random.uniform(1, 100, n)          # item values
A = np.random.uniform(1, 20, (m, n))      # constraint coefficients
c = A.sum(axis=1) * 0.5                   # capacities (roughly half of total)

def objective(x):
    # maximize p @ x subject to A @ x <= c; return NEGATIVE value with a
    # penalty for infeasibility so a minimization CE routine can be used
    violation = np.maximum(A @ x - c, 0).sum()
    return -(p @ x) + 1e4*violation

def cross_entropy_knapsack(obj, n_items, N=500, rho=0.1, n_iter=200, eps=1e-3):
    prob = 0.5*np.ones(n_items)
    Nel = int(np.ceil(N*rho))
    for _ in range(n_iter):
        if np.max(np.minimum(prob, 1-prob)) < eps:
            break
        X = (np.random.rand(N, n_items) < prob).astype(float)
        vals = np.array([obj(x) for x in X])
        order = np.argsort(vals)
        elite = X[order[:Nel]]
        prob = elite.mean(axis=0)
    return prob

best_prob = cross_entropy_knapsack(objective, n)
best_x = (best_prob > 0.5).astype(float)
print('Estimated best solution (rounded probabilities):', best_x)
print('Value:', p @ best_x, ' | Feasible:', np.all(A @ best_x <= c))
