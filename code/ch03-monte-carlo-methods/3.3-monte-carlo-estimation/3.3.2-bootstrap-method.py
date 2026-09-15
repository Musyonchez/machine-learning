"""
Chapter 3 - Monte Carlo Methods
Section 3.3.2 - Bootstrap Method (under 3.3 Monte Carlo Estimation)

Notes: notes/ch03-monte-carlo-methods/3.3-monte-carlo-estimation.md

TODO: transcribe the runnable code example(s) for this section here.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    from numba import jit
except ImportError:
    def jit(*args, **kwargs):
        def decorator(func):
            return func
        return decorator

# --- Example 3.12: bootstrapping the ratio estimator (renewal reward process) ---
np.random.seed(123)
n = 1000
P = np.array([[0, 0.2, 0.5, 0.3],
              [0.5, 0, 0.5, 0],
              [0.3, 0.7, 0, 0],
              [0.1, 0, 0, 0.9]])
r = np.array([4, 3, 10, 1])
Corg = np.array(np.zeros((n, 1)))
Rorg = np.array(np.zeros((n, 1)))
rho = 0.9

@jit()  # for speed-up if numba is available
def generate_cyclereward(n):
    for i in range(n):
        t = 1
        xreg = 1  # regenerative state (out of 1,2,3,4)
        reward = r[0]
        x = np.amin(np.argwhere(np.cumsum(P[xreg-1, :]) > np.random.rand())) + 1
        while x != xreg:
            t += 1
            reward += rho**(t-1) * r[x-1]
            x = np.amin(np.where(np.cumsum(P[x-1, :]) > np.random.rand())) + 1
        Corg[i] = t
        Rorg[i] = reward
    return Corg, Rorg

Corg, Rorg = generate_cyclereward(n)

Aorg = np.mean(Rorg) / np.mean(Corg)
print('Long-run average reward estimate: {:.3f}'.format(Aorg))

K = 5000
A = np.array(np.zeros((K, 1)))
for i in range(K):
    ind = np.ceil(n * np.random.rand(1, n)).astype(int)[0] - 1
    C = Corg[ind]
    R = Rorg[ind]
    A[i] = np.mean(R) / np.mean(C)

plt.xlabel('long-run average reward')
plt.ylabel('density')
sns.kdeplot(A.flatten(), fill=True)
plt.show()
