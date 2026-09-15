"""
Chapter 2 - Statistical Learning
Exercise 12

Notes: notes/ch02-statistical-learning/exercises.md

Reproduce Figure 2.17: the large-sample pointwise squared bias of the
learner for p in {1, 2, 3} in the polynomial regression running example
(Example 2.1 / 2.2). The bias is zero for p >= 4.
"""

import numpy as np
import matplotlib.pyplot as plt

# true model h*(u) = beta_star[0] + beta_star[1]*u + beta_star[2]*u^2 + beta_star[3]*u^3
beta_star = np.array([10, -140, 400, -250])

# large-sample least-squares coefficients within each restricted class H_p,
# from equation (2.18) in the book
beta_p = {
    1: np.array([65 / 6]),
    2: np.array([-20 / 3, 35]),
    3: np.array([-5 / 2, 10, 25]),
}

u = np.linspace(0, 1, 500)
h_star = beta_star[0] + beta_star[1] * u + beta_star[2] * u ** 2 + beta_star[3] * u ** 3

styles = {1: ':', 2: '--', 3: '-'}

plt.figure()
for p in [1, 2, 3]:
    coeffs = beta_p[p]
    h_p = sum(coeffs[i] * u ** i for i in range(len(coeffs)))
    bias_sq = (h_p - h_star) ** 2
    print(f'p = {p}: max pointwise squared bias = {np.max(bias_sq):.4f}')
    plt.plot(u, bias_sq, styles[p], label=f'$p={p}$')

plt.xlabel('u')
plt.ylabel('pointwise squared bias')
plt.legend()
plt.show()
