---
appendix: C
section: "C.2"
title: "Random Variables and Probability Distributions"
pdf_pages: "440-443"
---

## C.2 Random Variables and Probability Distributions

It is often convenient to describe a random experiment via "random variables", representing numerical measurements of the experiment. Random variables are usually denoted by capital letters from the last part of the alphabet. From a mathematical point of view, a *random variable* $X$ is a function from $\Omega$ to $\mathbb{R}$ such that sets of the form $\{a < X \leqslant b\} := \{\omega \in \Omega : a < X(\omega) \leqslant b\}$ are events (and so can be assigned a probability).

All probabilities involving a random variable $X$ can be computed, in principle, from its *cumulative distribution function* (cdf), defined by

$$F(x) = \mathbb{P}[X \leqslant x], \quad x \in \mathbb{R}.$$

For example $\mathbb{P}[a < X \leqslant b] = \mathbb{P}[X \leqslant b] - \mathbb{P}[X \leqslant a] = F(b) - F(a)$. Figure C.2 shows a generic cdf. Note that any cdf is right-continuous, increasing, and lies between 0 and 1.

> **Figure C.2:** A generic cumulative distribution function (cdf) $F(x)$: a right-continuous, non-decreasing step-like/curved function rising from 0 to 1 as $x$ increases from $-\infty$ to $\infty$, with jumps at points of positive probability mass.

A cdf $F_d$ is called *discrete* if there exist numbers $x_1, x_2, \ldots$ and probabilities $0 < f(x_i) \leqslant 1$ summing up to 1, such that for all $x$

$$F_d(x) = \sum_{x_i \leqslant x} f(x_i). \tag{C.3}$$

Such a cdf is piecewise constant and has jumps of sizes $f(x_1), f(x_2), \ldots$ at points $x_1, x_2, \ldots$, respectively. The function $f(x)$ is called a *probability mass function* or *discrete probability density function* (pdf). It is often easier to use the pdf rather than the cdf, since probabilities can simply be calculated from it via summation:

$$\mathbb{P}[X \in B] = \sum_{x \in B} f(x),$$

as illustrated in Figure C.3.

> **Figure C.3:** Discrete probability density function (pdf) $f(x)$ shown as a bar chart over discrete values of $x$; the darker bars correspond to a subset $B$ of the $x$-values, and the sum of their heights equals the probability $\mathbb{P}[X \in B]$.

A cdf $F_c$ is called *continuous*[^1], if there exists a positive function $f$ such that for all $x$

$$F_c(x) = \int_{-\infty}^{x} f(u)\, \mathrm{d}u. \tag{C.4}$$

Note that such an $F_c$ is differentiable (and hence continuous) with derivative $f$. The function $f$ is called the *probability density function (continuous pdf)*. By the fundamental theorem of integration, we have

$$\mathbb{P}[a < X \leqslant b] = F(b) - F(a) = \int_a^b f(x)\, \mathrm{d}x.$$

Thus, calculating probabilities reduces to integration, as illustrated in Figure C.4.

> **Figure C.4:** Continuous probability density function (pdf) $f(x)$: a smooth bell-like curve, with the shaded area between $a$ and $b$ (with a marked point $x$) corresponding to the probability $\mathbb{P}[X \in B]$, where $B = (a,b)$.

**Remark C.2 (Probability Density and Probability Mass).** It is important to note that we deliberately use the *same* name, "pdf", and symbol, $f$, in both the discrete and continuous case, rather than distinguish between a probability mass function (pmf) and probability density function (pdf). From a theoretical point of view the pdf plays exactly the same role in the discrete and continuous cases. We use the notation $X \sim \mathsf{Dist}$, $X \sim f$, and $X \sim F$ to indicate that $X$ has distribution $\mathsf{Dist}$, pdf $f$, and cdf $F$. $\blacksquare$

Tables C.1 and C.2 list a number of important continuous and discrete distributions. Note that in Table C.1, $\Gamma$ is the gamma function: $\Gamma(\alpha) = \int_0^\infty \mathrm{e}^{-x} x^{\alpha - 1}\, \mathrm{d}x, \quad \alpha > 0$.

### Table C.1: Commonly used continuous distributions

| Name | Notation | $f(x)$ | $x \in$ | Parameters |
|---|---|---|---|---|
| Uniform | $\mathcal{U}[\alpha,\beta]$ | $\dfrac{1}{\beta - \alpha}$ | $[\alpha,\beta]$ | $\alpha < \beta$ |
| Normal | $\mathcal{N}(\mu,\sigma^2)$ | $\dfrac{1}{\sigma\sqrt{2\pi}} \mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$ | $\mathbb{R}$ | $\sigma > 0,\ \mu \in \mathbb{R}$ |
| Gamma | $\mathsf{Gamma}(\alpha,\lambda)$ | $\dfrac{\lambda^\alpha x^{\alpha-1} \mathrm{e}^{-\lambda x}}{\Gamma(\alpha)}$ | $\mathbb{R}_+$ | $\alpha, \lambda > 0$ |
| Inverse Gamma | $\mathsf{InvGamma}(\alpha,\lambda)$ | $\dfrac{\lambda^\alpha x^{-\alpha-1} \mathrm{e}^{-\lambda x^{-1}}}{\Gamma(\alpha)}$ | $\mathbb{R}_+$ | $\alpha, \lambda > 0$ |
| Exponential | $\mathsf{Exp}(\lambda)$ | $\lambda \mathrm{e}^{-\lambda x}$ | $\mathbb{R}_+$ | $\lambda > 0$ |
| Beta | $\mathsf{Beta}(\alpha,\beta)$ | $\dfrac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha-1}(1-x)^{\beta-1}$ | $[0,1]$ | $\alpha,\beta > 0$ |
| Weibull | $\mathsf{Weib}(\alpha,\lambda)$ | $\alpha\lambda (\lambda x)^{\alpha-1} \mathrm{e}^{-(\lambda x)^\alpha}$ | $\mathbb{R}_+$ | $\alpha,\lambda > 0$ |
| Pareto | $\mathsf{Pareto}(\alpha,\lambda)$ | $\alpha\lambda (1+\lambda x)^{-(\alpha+1)}$ | $\mathbb{R}_+$ | $\alpha,\lambda > 0$ |
| Student | $\mathsf{t}_\nu$ | $\dfrac{\Gamma(\frac{\nu+1}{2})}{\sqrt{\nu\pi}\,\Gamma(\frac{\nu}{2})} \left(1 + \dfrac{x^2}{\nu}\right)^{-(\nu+1)/2}$ | $\mathbb{R}$ | $\nu > 0$ |
| F | $\mathsf{F}(m,n)$ | $\dfrac{\Gamma(\frac{m+n}{2})\,(m/n)^{m/2} x^{(m-2)/2}}{\Gamma(\frac{m}{2})\Gamma(\frac{n}{2})\,[1+(m/n)x]^{(m+n)/2}}$ | $\mathbb{R}_+$ | $m,n \in \mathbb{N}_+$ |

The $\mathsf{Gamma}(n/2, 1/2)$ distribution is called the *chi-squared distribution* with $n$ degrees of freedom, denoted $\chi_n^2$. The $\mathsf{t}_1$ distribution is also called the *Cauchy* distribution.

### Table C.2: Commonly used discrete distributions

| Name | Notation | $f(x)$ | $x \in$ | Parameters |
|---|---|---|---|---|
| Bernoulli | $\mathsf{Ber}(p)$ | $p^x(1-p)^{1-x}$ | $\{0,1\}$ | $0 \leqslant p \leqslant 1$ |
| Binomial | $\mathsf{Bin}(n,p)$ | $\dbinom{n}{x} p^x (1-p)^{n-x}$ | $\{0,1,\ldots,n\}$ | $0 \leqslant p \leqslant 1,\ n \in \mathbb{N}$ |
| Discrete uniform | $\mathcal{U}\{1,\ldots,n\}$ | $\dfrac{1}{n}$ | $\{1,\ldots,n\}$ | $n \in \{1,2,\ldots\}$ |
| Geometric | $\mathsf{Geom}(p)$ | $p(1-p)^{x-1}$ | $\{1,2,\ldots\}$ | $0 \leqslant p \leqslant 1$ |
| Poisson | $\mathsf{Poi}(\lambda)$ | $\mathrm{e}^{-\lambda} \dfrac{\lambda^x}{x!}$ | $\mathbb{N}$ | $\lambda > 0$ |

[^1]: In advanced probability, we would say "*absolutely continuous with respect to the Lebesgue measure*".
