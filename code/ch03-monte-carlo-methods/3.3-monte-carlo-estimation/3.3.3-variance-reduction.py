"""
Chapter 3 - Monte Carlo Methods
Section 3.3.3 - Variance Reduction (under 3.3 Monte Carlo Estimation)

Notes: notes/ch03-monte-carlo-methods/3.3-monte-carlo-estimation.md

TODO: transcribe the runnable code example(s) for this section here.
"""

import numpy as np
from numpy import pi, exp, sqrt, sin, cos, log
import matplotlib.pyplot as plt
from numpy.random import rand

# --- Part A: control variables (Example 3.13), building on Example 3.10's setup ---
c = (2*pi)**(3/2)
H_mcint = lambda x: c*np.sqrt(np.abs(np.sum(x, axis=1)))
N = 10**6
z = 1.96
x = np.random.randn(N, 3)
y = H_mcint(x)
mY = np.mean(y)
sY = np.std(y)
RE = sY/mY/np.sqrt(N)
print('CMC estimate = {:3.3f}, CI = ({:3.3f},{:3.3f})'.format(
      mY, mY*(1-z*RE), mY*(1+z*RE)))

Yc = np.sum(x**2, axis=1)  # control variable data
yc = 3  # true expectation of control variable
C = np.cov(y, Yc)  # sample covariance matrix
cor = C[0][1] / np.sqrt(C[0][0]*C[1][1])
alpha = C[0][1] / C[1][1]

est = np.mean(y - alpha*(Yc-yc))
RECV = np.sqrt((1-cor**2)*C[0][0]/N) / est  # relative error

print('CV Estimate = {:3.3f}, CI = ({:3.3f},{:3.3f}), Corr = {:3.3f}'.format(
      est, est*(1-z*RECV), est*(1+z*RECV), cor))

# --- Part B: importance sampling (Example 3.14) ---
b = 1000
H_is = lambda x1, x2: (2*b)**2 * exp(-sqrt(x1**2+x2**2)/4)*(sin(2*sqrt(
        x1**2+x2**2))+1)*(x1**2 + x2**2 < b**2)
f_is = 1/((2*b)**2)
N_is = 10**6
X1 = -b + 2*b*rand(N_is, 1)
X2 = -b + 2*b*rand(N_is, 1)
Z = H_is(X1, X2)
estCMC = np.mean(Z).item()
RECMC = np.std(Z)/estCMC/sqrt(N_is).item()
print('CMC (uniform) CI = ({:3.3f},{:3.3f}), RE = {: 3.3f}'.format(
    estCMC*(1-1.96*RECMC), estCMC*(1+1.96*RECMC), RECMC))

lam = 0.1
g_is = lambda x1, x2: lam*exp(-sqrt(x1**2 + x2**2)*lam)/sqrt(x1**2 + x2
    **2)/(2*pi)
U = rand(N_is, 1)
V = rand(N_is, 1)
R = -log(U)/lam
X1_is = R*cos(2*pi*V)
X2_is = R*sin(2*pi*V)
Z_is = H_is(X1_is, X2_is)*f_is/g_is(X1_is, X2_is)
estIS = np.mean(Z_is).item()
REIS = np.std(Z_is)/estIS/sqrt(N_is).item()
print('Importance sampling CI = ({:3.3f},{:3.3f}), RE = {: 3.3f}'.format(
    estIS*(1-1.96*REIS), estIS*(1+1.96*REIS), REIS))
