"""
Chapter 3 - Monte Carlo Methods
Exercise 18

Notes: notes/ch03-monte-carlo-methods/exercises.md

Implement a cross-entropy (CE) method and a simulated annealing (SA)
algorithm to minimize a least-squares objective built from the Hougen
reaction-rate model (referenced from Section 5.5's nonlinear regression
example):

    rate(x1,x2,x3; theta) = (theta1*x2 - x3/theta5)
                             / (1 + theta2*x1 + theta3*x2 + theta4*x3)

Since the book's exact Hougen dataset is not available in this repository,
synthetic (x1,x2,x3,y) data is generated from the Hougen model with a known
true theta plus noise, and both algorithms attempt to recover theta by
minimizing the sum of squared residuals. This keeps the code fully
self-contained and runnable.
"""

import numpy as np

def hougen(x1, x2, x3, theta):
    t1, t2, t3, t4, t5 = theta
    return (t1*x2 - x3/t5) / (1 + t2*x1 + t3*x2 + t4*x3)

# synthetic data generation (stand-in for the real Hougen dataset)
np.random.seed(0)
true_theta = np.array([1.25, 0.06, 0.04, 0.10, 1.20])
n_obs = 20
x1 = np.random.uniform(1, 5, n_obs)
x2 = np.random.uniform(1, 5, n_obs)
x3 = np.random.uniform(1, 5, n_obs)
y_obs = hougen(x1, x2, x3, true_theta) + 0.01*np.random.randn(n_obs)

def objective(theta):
    if np.any(theta <= 0):
        return 1e10
    pred = hougen(x1, x2, x3, theta)
    return np.sum((y_obs - pred)**2)

# --- Simulated annealing ---
def simulated_annealing(obj, x0, n_iter=5000, T0=1.0, beta=0.999, step=0.05):
    x = x0.copy()
    Sx = obj(x)
    best_x, best_S = x.copy(), Sx
    T = T0
    for _ in range(n_iter):
        T *= beta
        y = x + step*np.random.randn(len(x))
        Sy = obj(y)
        if Sy < Sx or np.random.rand() < np.exp(-(Sy-Sx)/max(T, 1e-12)):
            x, Sx = y, Sy
            if Sx < best_S:
                best_x, best_S = x.copy(), Sx
    return best_x, best_S

x0 = np.array([1.0, 0.1, 0.1, 0.1, 1.0])
sa_theta, sa_val = simulated_annealing(objective, x0)
print('Simulated annealing result: theta =', sa_theta, ', objective =', sa_val)

# --- Cross-entropy method ---
def cross_entropy_minimize(obj, mu0, sigma0, N=200, rho=0.1, n_iter=100, eps=1e-6):
    mu, sigma = mu0.copy(), sigma0.copy()
    Nel = int(np.ceil(N*rho))
    for _ in range(n_iter):
        if np.max(sigma) < eps:
            break
        X = mu + sigma*np.random.randn(N, len(mu))
        X = np.abs(X)  # keep parameters positive
        vals = np.array([obj(x) for x in X])
        order = np.argsort(vals)
        elite = X[order[:Nel]]
        mu = elite.mean(axis=0)
        sigma = elite.std(axis=0)
    return mu, obj(mu)

mu0 = np.array([1.0, 0.1, 0.1, 0.1, 1.0])
sigma0 = np.array([0.5, 0.05, 0.05, 0.05, 0.5])
ce_theta, ce_val = cross_entropy_minimize(objective, mu0, sigma0)
print('Cross-entropy method result: theta =', ce_theta, ', objective =', ce_val)

print('True theta (used to generate synthetic data):', true_theta)
