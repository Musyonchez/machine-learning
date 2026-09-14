---
appendix: C
section: "C.7"
title: "Multivariate Normal Distribution"
pdf_pages: "452-457"
---

## C.7 Multivariate Normal Distribution

The normal (or Gaussian) distribution — especially its multidimensional version — plays a central role in data science and machine learning. Recall from Table C.1 that a random variable $X$ is said to have a *normal* distribution with parameters $\mu$ and $\sigma^2$ if its pdf is given by

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}, \quad x \in \mathbb{R}. \tag{C.25}$$

We write $X \sim \mathcal{N}(\mu, \sigma^2)$. The parameters $\mu$ and $\sigma^2$ are the expectation and variance of the distribution, respectively. If $\mu = 0$ and $\sigma = 1$ then

$$f(x) = \frac{1}{\sqrt{2\pi}}\mathrm{e}^{-x^2/2},$$

and the distribution is known as the *standard normal* distribution. The cdf of the standard normal distribution is often denoted by $\Phi$ and its pdf by $\varphi$. In Figure C.5 the pdf of the $\mathcal{N}(\mu,\sigma^2)$ distribution for various $\mu$ and $\sigma^2$ is plotted.

> **Figure C.5:** The pdf of the $\mathcal{N}(\mu,\sigma^2)$ distribution for various $\mu$ and $\sigma^2$ — three bell curves plotted over $x \in [-4,6]$: $\mathcal{N}(0,1/4)$ (narrow, tall peak at 0), $\mathcal{N}(0,1)$ (medium spread, peak at 0), and $\mathcal{N}(2,1)$ (medium spread, peak at 2), illustrating how $\mu$ shifts and $\sigma^2$ scales the curve.

We next consider some important properties of the normal distribution.

> **Theorem C.5: Standardization**
>
> Let $X \sim \mathcal{N}(\mu,\sigma^2)$ and define $Z = (X-\mu)/\sigma$. Then $Z$ has a standard normal distribution.

*Proof:* The cdf of $Z$ is given by

$$\mathbb{P}[Z \leqslant z] = \mathbb{P}[(X-\mu)/\sigma \leqslant z] = \mathbb{P}[X \leqslant \mu + \sigma z] = \int_{-\infty}^{\mu+\sigma z} \frac{1}{\sigma\sqrt{2\pi}}\mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}\,\mathrm{d}x = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}}\mathrm{e}^{-y^2/2}\,\mathrm{d}y = \Phi(z),$$

where we make a change of variable $y = (x-\mu)/\sigma$ in the fourth equation. Hence, $Z \sim \mathcal{N}(0,1)$. $\square$

The rescaling procedure in Theorem C.5 is called *standardization*. It follows from Theorem C.5 that any $X \sim \mathcal{N}(\mu,\sigma^2)$ can be written as

$$X = \mu + \sigma Z, \quad \text{where } Z \sim \mathcal{N}(0,1).$$

In other words, any normal random variable can be viewed as an *affine transformation* — that is, a linear transformation plus a constant — of a standard normal random variable.

We now generalize this to $n$ dimensions. Let $Z_1, \ldots, Z_n$ be independent and standard normal random variables. The joint pdf of $\boldsymbol{Z} = [Z_1, \ldots, Z_n]^\top$ is given by

$$f_Z(\boldsymbol{z}) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi}}\mathrm{e}^{-\frac{1}{2}z_i^2} = (2\pi)^{-\frac{n}{2}}\mathrm{e}^{-\frac{1}{2}\boldsymbol{z}^\top\boldsymbol{z}}, \quad \boldsymbol{z}\in\mathbb{R}^n. \tag{C.26}$$

We write $\boldsymbol{Z} \sim \mathcal{N}(\boldsymbol{0}, \mathbf{I})$, where $\mathbf{I}$ is the identity matrix. Consider the affine transformation

$$\boldsymbol{X} = \boldsymbol{\mu} + \mathbf{B}\boldsymbol{Z} \tag{C.27}$$

for some $m \times n$ matrix $\mathbf{B}$ and $m$-dimensional vector $\boldsymbol{\mu}$. Note that, by (C.20) and (C.21) (p.432), $\boldsymbol{X}$ has expectation vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma} = \mathbf{B}\mathbf{B}^\top$. We say that $\boldsymbol{X}$ has a *multivariate normal* or *multivariate Gaussian* distribution with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$. We write $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$.

The following theorem states that any affine combination of independent multivariate normal random variables is again multivariate normal.

> **Theorem C.6: Affine Transformation of Normal Random Vectors**
>
> Let $\boldsymbol{X}_1, \boldsymbol{X}_2, \ldots, \boldsymbol{X}_r$ be independent $m_i$-dimensional normal random vectors, with $\boldsymbol{X}_i \sim \mathcal{N}(\boldsymbol{\mu}_i, \boldsymbol{\Sigma}_i)$, $i = 1, \ldots, r$. Then, for any $n \times 1$ vector $\boldsymbol{a}$ and $n \times m_i$ matrices $\mathbf{B}_1, \ldots, \mathbf{B}_r$,
>
> $$\boldsymbol{a} + \sum_{i=1}^{r}\mathbf{B}_i\boldsymbol{X}_i \sim \mathcal{N}\Big(\boldsymbol{a} + \sum_{i=1}^{r}\mathbf{B}_i\boldsymbol{\mu}_i,\ \sum_{i=1}^{r}\mathbf{B}_i\boldsymbol{\Sigma}_i\mathbf{B}_i^\top\Big). \tag{C.28}$$

*Proof:* Denote the $n$-dimensional random vector in the left-hand side of (C.28) by $\boldsymbol{Y}$. By definition, each $\boldsymbol{X}_i$ can be written as $\boldsymbol{\mu}_i + \mathbf{A}_i\boldsymbol{Z}_i$, where the $\{\boldsymbol{Z}_i\}$ are independent (because the $\{\boldsymbol{X}_i\}$ are independent), so that

$$\boldsymbol{Y} = \boldsymbol{a} + \sum_{i=1}^{r}\mathbf{B}_i(\boldsymbol{\mu}_i + \mathbf{A}_i\boldsymbol{Z}_i) = \boldsymbol{a} + \sum_{i=1}^{r}\mathbf{B}_i\boldsymbol{\mu}_i + \sum_{i=1}^{r}\mathbf{B}_i\mathbf{A}_i\boldsymbol{Z}_i,$$

which is an affine combination of independent standard normal random vectors. Hence, $\boldsymbol{Y}$ is multivariate normal. Its expectation vector and covariance matrix can be found easily from Theorem C.3 (p.432). $\square$

The next theorem shows that the distribution of a subvector of a multivariate normal random vector is again normal.

> **Theorem C.7: Marginal Distributions of Normal Random Vectors**
>
> Let $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ be an $n$-dimensional normal random vector. Decompose $\boldsymbol{X}$, $\boldsymbol{\mu}$, and $\boldsymbol{\Sigma}$ as
>
> $$\boldsymbol{X} = \begin{bmatrix}\boldsymbol{X}_p \\ \boldsymbol{X}_q\end{bmatrix}, \quad \boldsymbol{\mu} = \begin{bmatrix}\boldsymbol{\mu}_p \\ \boldsymbol{\mu}_q\end{bmatrix}, \quad \boldsymbol{\Sigma} = \begin{bmatrix}\boldsymbol{\Sigma}_p & \boldsymbol{\Sigma}_r \\ \boldsymbol{\Sigma}_r^\top & \boldsymbol{\Sigma}_q\end{bmatrix}, \tag{C.29}$$
>
> where $\boldsymbol{\Sigma}_p$ is the upper left $p \times p$ corner of $\boldsymbol{\Sigma}$ and $\boldsymbol{\Sigma}_q$ is the lower right $q \times q$ corner of $\boldsymbol{\Sigma}$. Then, $\boldsymbol{X}_p \sim \mathcal{N}(\boldsymbol{\mu}_p, \boldsymbol{\Sigma}_p)$.

*Proof:* We give a proof assuming that $\boldsymbol{\Sigma}$ is positive definite. Let $\mathbf{B}\mathbf{B}^\top$ be the (lower) Cholesky decomposition of $\boldsymbol{\Sigma}$ (see p.373). We can write

$$\begin{bmatrix}\boldsymbol{X}_p \\ \boldsymbol{X}_q\end{bmatrix} = \begin{bmatrix}\boldsymbol{\mu}_p \\ \boldsymbol{\mu}_q\end{bmatrix} + \underbrace{\begin{bmatrix}\mathbf{B}_p & \mathbf{O} \\ \mathbf{C}_r & \mathbf{C}_q\end{bmatrix}}_{\mathbf{B}} \begin{bmatrix}\boldsymbol{Z}_p \\ \boldsymbol{Z}_q\end{bmatrix}, \tag{C.30}$$

where $\boldsymbol{Z}_p$ and $\boldsymbol{Z}_q$ are independent $p$- and $q$-dimensional standard normal random vectors. In particular, $\boldsymbol{X}_p = \boldsymbol{\mu}_p + \mathbf{B}_p\boldsymbol{Z}_p$, which means that $\boldsymbol{X}_p \sim \mathcal{N}(\boldsymbol{\mu}_p, \boldsymbol{\Sigma}_p)$, since $\mathbf{B}_p\mathbf{B}_p^\top = \boldsymbol{\Sigma}_p$. $\square$

By relabeling the elements of $\boldsymbol{X}$ we see that Theorem C.7 implies that *any* subvector of $\boldsymbol{X}$ has a multivariate normal distribution. For example, $\boldsymbol{X}_q \sim \mathcal{N}(\boldsymbol{\mu}_q, \boldsymbol{\Sigma}_q)$.

The following theorem shows that not only the marginal distributions of a normal random vector are normal, but also its *conditional distributions*.

> **Theorem C.8: Conditional Distributions of Normal Random Vectors**
>
> Let $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ be an $n$-dimensional normal random vector with $\det(\boldsymbol{\Sigma}) > 0$. If $\boldsymbol{X}$ is decomposed as in (C.29), then
>
> $$\big(\boldsymbol{X}_q \mid \boldsymbol{X}_p = \boldsymbol{x}_p\big) \sim \mathcal{N}\big(\boldsymbol{\mu}_q + \boldsymbol{\Sigma}_r^\top\boldsymbol{\Sigma}_p^{-1}(\boldsymbol{x}_p - \boldsymbol{\mu}_p),\ \boldsymbol{\Sigma}_q - \boldsymbol{\Sigma}_r^\top\boldsymbol{\Sigma}_p^{-1}\boldsymbol{\Sigma}_r\big). \tag{C.31}$$
>
> As a consequence, $\boldsymbol{X}_p$ and $\boldsymbol{X}_q$ are *independent* if and only if they are *uncorrelated*; that is, if $\boldsymbol{\Sigma}_r = \mathbf{O}$ (zero matrix).

*Proof:* From (C.30) we see that $\boldsymbol{X}_p = \boldsymbol{\mu}_p + \mathbf{B}_p\boldsymbol{Z}_p$ and $\boldsymbol{X}_q = \boldsymbol{\mu}_q + \mathbf{C}_r\boldsymbol{Z}_p + \mathbf{C}_q\boldsymbol{Z}_q$. Consequently,

$$(\boldsymbol{X}_q \mid \boldsymbol{X}_p = \boldsymbol{x}_p) = \boldsymbol{\mu}_q + \mathbf{C}_r\mathbf{B}_p^{-1}(\boldsymbol{x}_p - \boldsymbol{\mu}_p) + \mathbf{C}_q\boldsymbol{Z}_q,$$

where $\boldsymbol{Z}_q$ is a $q$-dimensional multivariate standard normal random vector. It follows that $\boldsymbol{X}_q$ conditional on $\boldsymbol{X}_p = \boldsymbol{x}_p$ has a $\mathcal{N}(\boldsymbol{\mu}_q + \mathbf{C}_r\mathbf{B}_p^{-1}(\boldsymbol{x}_p-\boldsymbol{\mu}_p), \mathbf{C}_q\mathbf{C}_q^\top)$ distribution. The proof of (C.31) is completed by observing that $\boldsymbol{\Sigma}_r^\top\boldsymbol{\Sigma}_p^{-1} = \mathbf{C}_r\mathbf{B}_p^\top(\mathbf{B}_p^\top)^{-1}\mathbf{B}_p^{-1} = \mathbf{C}_r\mathbf{B}_p^{-1}$, and

$$\boldsymbol{\Sigma}_q - \boldsymbol{\Sigma}_r^\top\boldsymbol{\Sigma}_p^{-1}\boldsymbol{\Sigma}_r = \mathbf{C}_r\mathbf{C}_r^\top + \mathbf{C}_q\mathbf{C}_q^\top - \mathbf{C}_r\mathbf{B}_p^{-1}\underbrace{\boldsymbol{\Sigma}_r}_{\mathbf{B}_p\mathbf{C}_r^\top} = \mathbf{C}_q\mathbf{C}_q^\top.$$

If $\boldsymbol{X}_p$ and $\boldsymbol{X}_q$ are independent, then they are obviously uncorrelated, as $\boldsymbol{\Sigma}_r = \mathbb{E}[(\boldsymbol{X}_p-\boldsymbol{\mu}_p)(\boldsymbol{X}_q-\boldsymbol{\mu}_q)^\top] = \mathbb{E}(\boldsymbol{X}_p-\boldsymbol{\mu}_p)\,\mathbb{E}(\boldsymbol{X}_q-\boldsymbol{\mu}_q)^\top = \mathbf{O}$. Conversely, if $\boldsymbol{\Sigma}_r = \mathbf{O}$, then by (C.31) the conditional distribution of $\boldsymbol{X}_q$ given $\boldsymbol{X}_p$ is the same as the unconditional distribution of $\boldsymbol{X}_q$; that is, $\mathcal{N}(\boldsymbol{\mu}_q, \boldsymbol{\Sigma}_q)$. In other words, $\boldsymbol{X}_q$ is independent of $\boldsymbol{X}_p$. $\square$

The next few results are about the relationships between the normal, chi-squared, Student, and F distributions, defined in Table C.1. Recall that the chi-squared family of distributions, denoted by $\chi_n^2$, are simply $\mathsf{Gamma}(n/2, 1/2)$ distributions, where the parameter $n \in \{1,2,3,\ldots\}$ is called the *degrees of freedom*.

> **Theorem C.9: Relationship Between Normal and $\chi^2$ Distributions**
>
> If $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is an $n$-dimensional normal random vector with $\det(\boldsymbol{\Sigma}) > 0$, then
>
> $$(\boldsymbol{X}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\boldsymbol{X}-\boldsymbol{\mu}) \sim \chi_n^2. \tag{C.32}$$

*Proof:* Let $\mathbf{B}\mathbf{B}^\top$ be the Cholesky decomposition of $\boldsymbol{\Sigma}$, where $\mathbf{B}$ is invertible. Since $\boldsymbol{X}$ can be written as $\boldsymbol{\mu} + \mathbf{B}\boldsymbol{Z}$, where $\boldsymbol{Z} = [Z_1,\ldots,Z_n]^\top$ is a vector of independent standard normal random variables, we have

$$(\boldsymbol{X}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\boldsymbol{X}-\boldsymbol{\mu}) = (\boldsymbol{X}-\boldsymbol{\mu})^\top(\mathbf{B}\mathbf{B}^\top)^{-1}(\boldsymbol{X}-\boldsymbol{\mu}) = \boldsymbol{Z}^\top\boldsymbol{Z} = \sum_{i=1}^{n}Z_i^2.$$

Using the independence of $Z_1,\ldots,Z_n$, the moment generating function of $Y = \sum_{i=1}^n Z_i^2$ is given by

$$\mathbb{E}\mathrm{e}^{sY} = \mathbb{E}\mathrm{e}^{s(Z_1^2+\cdots+Z_n^2)} = \mathbb{E}[\mathrm{e}^{sZ_1^2}\cdots\mathrm{e}^{sZ_n^2}] = \big(\mathbb{E}\mathrm{e}^{sZ^2}\big)^n,$$

where $Z \sim \mathcal{N}(0,1)$. The moment generating function of $Z^2$ is

$$\mathbb{E}\mathrm{e}^{sZ^2} = \int_{-\infty}^{\infty}\mathrm{e}^{sz^2}\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-z^2/2}\mathrm{d}z = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\mathrm{e}^{-\frac{1}{2}(1-2s)z^2}\mathrm{d}z = \frac{1}{\sqrt{1-2s}},$$

so that $\mathbb{E}\mathrm{e}^{sY} = \big(\tfrac{1}{2}/(\tfrac{1}{2}-s)\big)^{n/2}$, $s < \tfrac{1}{2}$, which is the moment generating function of the $\mathsf{Gamma}(n/2, 1/2)$ distribution; that is, the $\chi_n^2$ distribution — see Example C.1. The result now follows from the uniqueness of the moment generating function. $\square$

A consequence of Theorem C.9 is that if $\boldsymbol{X} = [X_1,\ldots,X_n]^\top$ is $n$-dimensional standard normal, then the squared length $\|\boldsymbol{X}\|^2 = X_1^2+\cdots+X_n^2$ has a $\chi_n^2$ distribution. If instead $X_i \sim \mathcal{N}(\mu_i, 1), i = 1,\ldots$, then $\|\boldsymbol{X}\|^2$ is said to have a *noncentral $\chi_n^2$ distribution*. This distribution depends on the $\{\mu_i\}$ only through the norm $\|\boldsymbol{\mu}\|$. We write $\|\boldsymbol{X}\|^2 \sim \chi_n^2(\theta)$, where $\theta = \|\boldsymbol{\mu}\|$ is the *noncentrality parameter*.

Such distributions frequently occur when considering *projections* of multivariate normal random variables, as summarized in the following theorem.

> **Theorem C.10: Relationship Between Normal and Noncentral $\chi^2$ Distributions**
>
> Let $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{I}_n)$ be an $n$-dimensional normal random vector and let $\mathcal{V}_k \subset \mathcal{V}_m$ be linear subspaces of dimensions $k$ and $m$, respectively, with $k < m \leqslant n$. Let $\boldsymbol{X}_k$ and $\boldsymbol{X}_m$ be orthogonal projections of $\boldsymbol{X}$ onto $\mathcal{V}_k$ and $\mathcal{V}_m$, and let $\boldsymbol{\mu}_k$ and $\boldsymbol{\mu}_m$ be the corresponding projections of $\boldsymbol{\mu}$. Then, the following holds.
>
> 1. The random vectors $\boldsymbol{X}_k$, $\boldsymbol{X}_m - \boldsymbol{X}_k$, and $\boldsymbol{X} - \boldsymbol{X}_m$ are independent.
> 2. $\|\boldsymbol{X}_k\|^2 \sim \chi_k^2(\|\boldsymbol{\mu}_k\|)$, $\|\boldsymbol{X}_m - \boldsymbol{X}_k\|^2 \sim \chi_{m-k}^2(\|\boldsymbol{\mu}_m - \boldsymbol{\mu}_k\|)$, and $\|\boldsymbol{X} - \boldsymbol{X}_m\|^2 \sim \chi_{n-m}^2(\|\boldsymbol{\mu} - \boldsymbol{\mu}_m\|)$.

*Proof:* Let $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_n$ be an orthonormal basis of $\mathbb{R}^n$ such that $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_k$ spans $\mathcal{V}_k$ and $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_m$ spans $\mathcal{V}_m$. By (A.8) (p.362) we can write the orthogonal projection matrices onto $\mathcal{V}_j$, as $\mathbf{P}_j = \sum_{i=1}^{j}\boldsymbol{v}_i\boldsymbol{v}_i^\top$, $j = k,m,n$, where $\mathcal{V}_n$ is defined as $\mathbb{R}^n$. Note that $\mathbf{P}_n$ is simply the identity matrix. Let $\mathbf{V} := [\boldsymbol{v}_1,\ldots,\boldsymbol{v}_n]$ and define $\boldsymbol{Z} := [Z_1,\ldots,Z_n]^\top = \mathbf{V}^\top\boldsymbol{X}$. Recall from Section A.2 (p.361) that any orthogonal transformation such as $\boldsymbol{z} = \mathbf{V}^\top\boldsymbol{x}$ is *length preserving*; that is, $\|\boldsymbol{z}\| = \|\boldsymbol{x}\|$.

To prove the first statement of the theorem, note that $\mathbf{V}^\top\boldsymbol{X}_j = \mathbf{V}^\top\mathbf{P}_j\boldsymbol{X} = [Z_1,\ldots,Z_j,0,\ldots,0]^\top$, $j = k,m$. It follows that $\mathbf{V}^\top(\boldsymbol{X}_m-\boldsymbol{X}_k) = [0,\ldots,0,Z_{k+1},\ldots,Z_m,0,\ldots,0]^\top$ and $\mathbf{V}^\top(\boldsymbol{X}-\boldsymbol{X}_m) = [0,\ldots,0,Z_{m+1},\ldots,Z_n]^\top$. Moreover, being a linear transformation of a normal random vector, $\boldsymbol{Z}$ is also normal, with covariance matrix $\mathbf{V}^\top\mathbf{V} = \mathbf{I}_n$. In particular, the $\{Z_i\}$ are *independent*. This shows that $\boldsymbol{X}_k$, $\boldsymbol{X}_m-\boldsymbol{X}_k$ and $\boldsymbol{X}-\boldsymbol{X}_m$ are independent as well.

Next, observe that $\|\boldsymbol{X}_k\| = \|\mathbf{V}^\top\boldsymbol{X}_k\| = \|\boldsymbol{Z}_k\|$, where $\boldsymbol{Z}_k := [Z_1,\ldots,Z_k]^\top$. The latter vector has independent components with variances 1, and its squared norm has therefore (by definition) a $\chi_k^2(\theta)$ distribution. The noncentrality parameter is $\theta = \|\mathbb{E}\boldsymbol{Z}_k\| = \|\mathbb{E}\boldsymbol{X}_k\| = \|\boldsymbol{\mu}_k\|$, again by the length-preserving property of orthogonal transformations. This shows that $\|\boldsymbol{X}_k\|^2 \sim \chi_k^2(\|\boldsymbol{\mu}_k\|)$. The distributions of $\|\boldsymbol{X}_m-\boldsymbol{X}_k\|^2$ and $\|\boldsymbol{X}-\boldsymbol{X}_m\|^2$ follow by analogy. $\square$

Theorem C.10 is frequently used in the statistical analysis of *normal linear models*; see Section 5.4 (p.182). In typical situations $\boldsymbol{\mu}$ lies in the subspace $\mathcal{V}_m$ or even $\mathcal{V}_k$ — in which case $\|\boldsymbol{X}_m-\boldsymbol{X}_k\|^2 \sim \chi_{m-k}^2$ and $\|\boldsymbol{X}-\boldsymbol{X}_m\|^2 \sim \chi_{n-m}^2$, independently. The (scaled) quotient then turns out to have an F distribution — a consequence of the following theorem.

> **Theorem C.11: Relationship Between $\chi^2$ and F Distributions**
>
> Let $U \sim \chi_m^2$ and $V \sim \chi_n^2$ be independent. Then,
>
> $$\frac{U/m}{V/n} \sim \mathsf{F}(m,n).$$

*Proof:* For notational simplicity, let $c = m/2$ and $d = n/2$. The pdf of $W = U/V$ is given by $f_W(w) = \int_0^\infty f_U(wv)\, v\, f_V(v)\, \mathrm{d}v$. Substituting the pdfs of the corresponding Gamma distributions, we have

$$f_W(w) = \int_0^\infty \frac{(wv)^{c-1}\mathrm{e}^{-wv/2}}{\Gamma(c)2^c}\, v\, \frac{v^{d-1}\mathrm{e}^{-v/2}}{\Gamma(d)2^d}\, \mathrm{d}v = \frac{w^{c-1}}{\Gamma(c)\Gamma(d)2^{c+d}}\int_0^\infty v^{c+d-1}\mathrm{e}^{-(1+w)v/2}\, \mathrm{d}v = \frac{\Gamma(c+d)}{\Gamma(c)\Gamma(d)}\frac{w^{c-1}}{(1+w)^{c+d}},$$

where the last equality follows from the fact that the integrand is equal to $\Gamma(\alpha)\lambda^{-\alpha}$ times the density of the $\mathsf{Gamma}(\alpha,\lambda)$ distribution with $\alpha = c+d$ and $\lambda = (1+w)/2$. The density of $Z = \frac{n}{m}\frac{U}{V}$ is given by

$$f_Z(z) = f_W(zm/n)\, m/n.$$

The proof is completed by comparing the resulting expression with the pdf of the F distribution given in Table C.1 (p.425). $\square$

**Corollary C.1 (Relationship Between Normal, $\chi^2$, and $t$ Distributions).** Let $Z \sim \mathcal{N}(0,1)$ and $V \sim \chi_n^2$ be independent. Then,

$$\frac{Z}{\sqrt{V/n}} \sim \mathsf{t}_n.$$

*Proof:* Let $T = Z/\sqrt{V/n}$. Because $Z^2 \sim \chi_1^2$, we have by Theorem C.11 that $T^2 \sim \mathsf{F}(1,n)$. The result follows now from the symmetry around 0 of the pdf of $T$ and the fact that the square of a $\mathsf{t}_n$ random variable has an $\mathsf{F}(1,n)$ distribution. $\square$
