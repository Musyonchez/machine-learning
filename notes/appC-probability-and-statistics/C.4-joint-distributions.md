---
appendix: C
section: "C.4"
title: "Joint Distributions"
pdf_pages: "445-446"
---

## C.4 Joint Distributions

Distributions for random vectors and stochastic processes can be specified in much the same way as for random variables. In particular, the distribution of a random vector $\boldsymbol{X} = [X_1, \ldots, X_n]^\top$ is completely determined by specifying the *joint cdf* $F$, defined by

$$F(x_1, \ldots, x_n) = \mathbb{P}[X_1 \leqslant x_1, \ldots, X_n \leqslant x_n], \quad x_i \in \mathbb{R},\ i = 1, \ldots, n.$$

Similarly, the distribution of a *stochastic process*, that is, a collection of random variables $\{X_t, t \in \mathcal{T}\}$, for some index set $\mathcal{T}$, is completely determined by its finite-dimensional distributions; specifically, the distributions of the random vectors $[X_{t_1}, \ldots, X_{t_n}]^\top$ for every choice of $n$ and $t_1, \ldots, t_n$.

By analogy to the one-dimensional case, a random vector $\boldsymbol{X} = [X_1, \ldots, X_n]^\top$ taking values in $\mathbb{R}^n$ is said to have a pdf $f$ if, in the continuous case,

$$\mathbb{P}[\boldsymbol{X} \in B] = \int_B f(\boldsymbol{x})\, \mathrm{d}\boldsymbol{x}, \tag{C.6}$$

for all $n$-dimensional rectangles $B$. Replace the integral with a sum for the discrete case. The pdf is also called the *joint pdf* of $X_1, \ldots, X_n$. The pdfs of the individual components — called *marginal pdfs* — can be recovered from the joint pdf by "integrating out the other variables". For example, for a continuous random vector $[X, Y]^\top$ with pdf $f$, the pdf $f_X$ of $X$ is given by

$$f_X(x) = \int f(x, y)\, \mathrm{d}y.$$
