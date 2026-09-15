"""
Chapter 3 - Monte Carlo Methods
Section 3.4.4 - Noisy Optimization (under 3.4 Monte Carlo for Optimization)

Notes: notes/ch03-monte-carlo-methods/3.4-monte-carlo-for-optimization.md

Example 3.18: choosing an importance-sampling parameter via stochastic
approximation (stochapprox.py) followed by the stochastic counterpart method
(stochcounterpart.py, which the book builds by importing from stochapprox.py).

Example 3.19: cross-entropy method for a noisy discrete "black box"
optimization problem (Snoisy.py + CEnoisy.py).

Both examples are inlined into this single standalone file, each in its own
clearly marked part.
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# --- Part A: stochastic approximation (Example 3.18) ---
b = 100  # choose b large enough, but not too large
delta = 0.01
H = lambda x1, x2: (2*b)**2*np.exp(-np.sqrt(x1**2 + x2**2)/4)*(np.
    sin(2*np.sqrt(x1**2+x2**2)+1))*(x1**2+x2**2 < b**2)
f = 1/(2*b)**2
g = lambda x1, x2, lam: lam*np.exp(-np.sqrt(x1**2+x2**2)*lam)/np.\
    sqrt(x1**2+x2**2)/(2*pi)
beta = 10**-7  # step size very small, as the gradient is large
lam = 0.25
lams = np.array([lam])
N = 10**4
for i in range(200):
    x1 = -b + 2*b*np.random.rand(N, 1)
    x2 = -b + 2*b*np.random.rand(N, 1)
    lamL = lam - delta/2
    lamR = lam + delta/2
    estL = np.mean(H(x1, x2)**2*f/g(x1, x2, lamL))
    estR = np.mean(H(x1, x2)**2*f/g(x1, x2, lamR))  # use SAME x1,x2
    gr = (estR-estL)/delta  # gradient
    lam = lam - gr*beta  # gradient descent
    lams = np.hstack((lams, lam))
    beta = beta*0.99

print('Stochastic approximation estimate of lambda*: {:.4f}'.format(lam))
plt.figure()
lamsize = range(0, (lams.size))
plt.plot(lamsize, lams)
plt.xlabel('iteration')
plt.ylabel(r'$\lambda_t$')
plt.show()

# --- continuing: stochastic counterpart method (Example 3.18 cont.) ---
lams_grid = np.linspace(0.01, 0.31, 1000)
res = []
res = np.array(res)
for i in range(lams_grid.size):
    lam_g = lams_grid[i]
    np.random.seed(1)
    g_fixed = lambda x1, x2: lam_g*np.exp(-np.sqrt(x1**2+x2**2)*lam_g)/np.sqrt(
        x1**2+x2**2)/(2*pi)
    X = -b+2*b*np.random.rand(N, 1)
    Y = -b+2*b*np.random.rand(N, 1)
    Z = H(X, Y)**2*f/g_fixed(X, Y)
    estCMC = np.mean(Z)
    res = np.hstack((res, estCMC))

print('Stochastic counterpart best lambda: {:.4f}'.format(lams_grid[np.argmin(res)]))
plt.figure()
plt.plot(lams_grid, res)
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$\hat{S}(\lambda)$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.show()


# --- Part B: CE method for noisy optimization (Example 3.19) ---
def Snoisy(X):  # takes a matrix
    n_bits = X.shape[1]
    N_rows = X.shape[0]
    xorg = np.hstack((np.ones((1, n_bits//2)), np.zeros((1, n_bits//2))))
    theta = 0.4  # probability to flip the input
    s = np.zeros(N_rows)
    for i in range(0, N_rows):
        flip = (np.random.uniform(size=(n_bits)) < theta).astype(int)
        ind = flip > 0
        X[i][ind] = 1 - X[i][ind]
        s[i] = (X[i] != xorg).sum()
    return s


n = 100
rho = 0.1
N_ce = 1000
Nel = int(N_ce*rho)
eps = 0.01
p = 0.5*np.ones(n)
i = 0
pstart = p
ps = np.zeros((1000, n))
ps[0] = pstart
while np.max(np.minimum(p, 1-p)) > eps:
    i += 1
    X = (np.random.uniform(size=(N_ce, n)) < p).astype(int)
    X_tmp = np.array(X, copy=True)
    SX = Snoisy(X_tmp)
    ids = np.argsort(SX, axis=0)
    Elite = X[ids[0:Nel], :]
    p = np.mean(Elite, axis=0)
    ps[i] = p

print('Estimated hidden binary vector (rounded):')
print(np.round(p))
