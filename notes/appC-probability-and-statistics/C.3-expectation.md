---
appendix: C
section: "C.3"
title: "Expectation"
pdf_pages: "444-445"
---

## C.3 Expectation

It is often useful to consider different kinds of numerical characteristics of a random variable. One such quantity is the expectation, which measures the "average" value of the distribution.

The *expectation* (or expected value or mean) of a random variable $X$ with pdf $f$, denoted by $\mathbb{E}X$ or $\mathbb{E}[X]$ (and sometimes $\mu$), is defined by

$$\mathbb{E}X = \begin{cases} \sum_x x f(x) & \text{discrete case,} \\ \int_{-\infty}^{\infty} x f(x)\, \mathrm{d}x & \text{continuous case.} \end{cases}$$

If $X$ is a random variable, then a function of $X$, such as $X^2$ or $\sin(X)$, is again a random variable. Moreover, the expected value of a function of $X$ is simply a weighted average of the possible values that this function can take. That is, for any real function $h$

$$\mathbb{E}h(X) = \begin{cases} \sum_x h(x) f(x) & \text{discrete case,} \\ \int_{-\infty}^{\infty} h(x) f(x)\, \mathrm{d}x & \text{continuous case,} \end{cases}$$

provided that the sum or integral are well-defined.

The *variance* of a random variable $X$, denoted by $\mathbb{V}\mathrm{ar}\, X$ (and sometimes $\sigma^2$), is defined by

$$\mathbb{V}\mathrm{ar}\, X = \mathbb{E}(X - \mathbb{E}[X])^2 = \mathbb{E}X^2 - (\mathbb{E}X)^2.$$

The square root of the variance is called the *standard deviation*. Table C.3 lists the expectations and variances for some well-known distributions. Both variance and standard deviation measure the spread or dispersion of the distribution. Note, however, that the standard deviation measures the dispersion in the same units as the random variable, unlike the variance, which uses squared units.

### Table C.3: Expectations and variances for some well-known distributions

| Dist. | $\mathbb{E}X$ | $\mathbb{V}\mathrm{ar}\,X$ | Dist. | $\mathbb{E}X$ | $\mathbb{V}\mathrm{ar}\,X$ |
|---|---|---|---|---|---|
| $\mathsf{Bin}(n,p)$ | $np$ | $np(1-p)$ | $\mathsf{Gamma}(\alpha,\lambda)$ | $\dfrac{\alpha}{\lambda}$ | $\dfrac{\alpha}{\lambda^2}$ |
| $\mathsf{Geom}(p)$ | $\dfrac{1}{p}$ | $\dfrac{1-p}{p^2}$ | $\mathcal{N}(\mu,\sigma^2)$ | $\mu$ | $\sigma^2$ |
| $\mathsf{Poi}(\lambda)$ | $\lambda$ | $\lambda$ | $\mathsf{Beta}(\alpha,\beta)$ | $\dfrac{\alpha}{\alpha+\beta}$ | $\dfrac{\alpha\beta}{(\alpha+\beta)^2(1+\alpha+\beta)}$ |
| $\mathcal{U}[\alpha,\beta]$ | $\dfrac{\alpha+\beta}{2}$ | $\dfrac{(\beta-\alpha)^2}{12}$ | $\mathsf{Weib}(\alpha,\lambda)$ | $\dfrac{\Gamma(1/\alpha)}{\alpha\lambda}$ | $\dfrac{2\Gamma(2/\alpha)}{\alpha\lambda} - \left(\dfrac{\Gamma(1/\alpha)}{\alpha\lambda}\right)^2$ |
| $\mathsf{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ | $\mathsf{F}(m,n)$ | $\dfrac{n}{n-2}\ (n>2)$ | $\dfrac{2n^2(m+n-2)}{m(n-2)^2(n-4)}\ (n>4)$ |
| $\mathsf{t}_\nu$ | $0\ (\nu>1)$ | $\dfrac{\nu}{\nu-2}\ (\nu>2)$ | | | |

It is sometimes useful to consider the *moment generating function* of a random variable $X$. This is the function $M$ defined by

$$M(s) = \mathbb{E}\, \mathrm{e}^{sX}, \quad s \in \mathbb{R}. \tag{C.5}$$

The moment generating functions of two random variables coincide if and only if the random variables have the same distribution; see also Theorem C.12.

**Example C.1 (Moment Generation Function of the $\mathsf{Gamma}(\alpha, \lambda)$ Distribution).** Let $X \sim \mathsf{Gamma}(\alpha, \lambda)$. For $s < \lambda$, the moment generating function of $X$ at $s$ is given by

$$M(s) = \mathbb{E}\mathrm{e}^{sX} = \int_0^\infty \mathrm{e}^{sx} \frac{\mathrm{e}^{-\lambda x} \lambda^\alpha x^{\alpha - 1}}{\Gamma(\alpha)}\, \mathrm{d}x = \left(\frac{\lambda}{\lambda - s}\right)^\alpha \int_0^\infty \underbrace{\frac{\mathrm{e}^{-(\lambda-s)x}(\lambda - s)^\alpha x^{\alpha-1}}{\Gamma(\alpha)}}_{\text{pdf of } \mathsf{Gamma}(\alpha, \lambda - s)}\, \mathrm{d}x = \left(\frac{\lambda}{\lambda - s}\right)^\alpha.$$

For $s \geqslant \lambda$, $M(s) = \infty$. Interestingly, the moment generating function has a much simpler formula than the pdf. $\blacksquare$
