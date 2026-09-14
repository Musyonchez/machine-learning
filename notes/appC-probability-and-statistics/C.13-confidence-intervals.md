---
appendix: C
section: "C.13"
title: "Confidence Intervals"
pdf_pages: "475-476"
---

## C.13 Confidence Intervals

An essential part in any estimation procedure is to provide an assessment of the *accuracy* of the estimate. Indeed, without information on its accuracy the estimate itself would be meaningless. Confidence intervals (also called *interval estimates*) provide a precise way of describing the uncertainty in the estimate.

Let $X_1,\ldots,X_n$ be random variables with a joint distribution depending on a parameter $\theta\in\Theta$. Let $T_1 < T_2$ be statistics; that is, $T_i = T_i(X_1,\ldots,X_n)$, $i=1,2$ are functions of the data, but not of $\theta$.

1. The random interval $(T_1,T_2)$ is called a *stochastic confidence interval* for $\theta$ with confidence $1-\alpha$ if

$$\mathbb{P}_\theta[T_1 < \theta < T_2] \geqslant 1-\alpha \quad \text{for all } \theta\in\Theta. \tag{C.51}$$

2. If $t_1$ and $t_2$ are the observed values of $T_1$ and $T_2$, then the interval $(t_1,t_2)$ is called the *(numerical) confidence interval* for $\theta$ with confidence $1-\alpha$ for every $\theta\in\Theta$.

3. If the right-hand side of (C.51) is merely a heuristic estimate or approximation of the true probability, then the resulting interval is called an *approximate confidence interval*.

4. The probability $\mathbb{P}_\theta[T_1 < \theta < T_2]$ is called the *coverage probability*. For a $1-\alpha$ confidence interval, it must be at least $1-\alpha$.

For multidimensional parameters $\boldsymbol{\theta}\in\mathbb{R}^d$ the stochastic confidence interval is replaced with a stochastic *confidence region* $C\subset\mathbb{R}^d$ such that $\mathbb{P}_{\boldsymbol{\theta}}[\boldsymbol{\theta}\in C] \geqslant 1-\alpha$ for all $\boldsymbol{\theta}$.

**Example C.14 (Approximate Confidence Interval for the Mean).** Let $X_1, X_2, \ldots, X_n$ be an iid sample from a distribution with mean $\mu$ and variance $\sigma^2 < \infty$ (both assumed to be unknown). By the central limit theorem and the law of large numbers,

$$T = \frac{\overline{X}-\mu}{S/\sqrt{n}} \overset{\text{approx.}}{\sim} \mathcal{N}(0,1),$$

for large $n$, where $S$ is the sample standard deviation. Rearranging the approximate equality $\mathbb{P}[|T|\leqslant z_{1-\alpha/2}] \approx 1-\alpha$, where $z_{1-\alpha/2}$ is the $1-\alpha/2$ quantile of the standard normal distribution, yields

$$\mathbb{P}\left[\overline{X} - z_{1-\alpha/2}\frac{S}{\sqrt{n}} \leqslant \mu \leqslant \overline{X} + z_{1-\alpha/2}\frac{S}{\sqrt{n}}\right] \approx 1-\alpha,$$

so that

$$\left(\overline{X} - z_{1-\alpha/2}\frac{S}{\sqrt{n}},\ \overline{X} + z_{1-\alpha/2}\frac{S}{\sqrt{n}}\right), \text{ abbreviated as } \overline{X} \pm z_{1-\alpha/2}\frac{S}{\sqrt{n}}, \tag{C.52}$$

is an approximate stochastic $(1-\alpha)$ confidence interval for $\mu$. $\blacksquare$

Since (C.52) is an asymptotic result only, care should be taken when applying it to cases where the sample size is small or moderate and the sampling distribution is heavily skewed.
