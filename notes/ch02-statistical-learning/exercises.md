---
chapter: 2
section: "exercises"
title: "Exercises"
pdf_pages: "77-84"
---

1. Suppose that the loss function is the piecewise linear function
$$
\text{Loss}(y,\widehat{y}) = \alpha\,(\widehat{y}-y)_+ + \beta\,(y-\widehat{y})_+, \quad \alpha,\beta > 0,
$$
where $c_+$ is equal to $c$ if $c > 0$, and zero otherwise. Show that the minimizer of the risk $\ell(g) = \mathbb{E}\,\text{Loss}(Y, g(\boldsymbol{X}))$ satisfies
$$
\mathbb{P}[Y < g^*(\boldsymbol{x}) \mid \boldsymbol{X} = \boldsymbol{x}] = \frac{\beta}{\alpha+\beta}.
$$
In other words, $g^*(\boldsymbol{x})$ is the $\beta/(\alpha+\beta)$ quantile of $Y$, conditional on $\boldsymbol{X} = \boldsymbol{x}$.

2. Show that, for the squared-error loss, the approximation error $\ell(g^{\mathcal{G}}) - \ell(g^*)$ in (2.16), is equal to $\mathbb{E}(g^{\mathcal{G}}(\boldsymbol{X}) - g^*(\boldsymbol{X}))^2$. [Hint: expand $\ell(g^{\mathcal{G}}) = \mathbb{E}(Y - g^*(\boldsymbol{X}) + g^*(\boldsymbol{X}) - g^{\mathcal{G}}(\boldsymbol{X}))^2$.]

3. Suppose $\mathcal{G}$ is the class of *linear* functions. A linear function evaluated at a feature $\boldsymbol{x}$ can be described as $g(\boldsymbol{x}) = \boldsymbol{\beta}^\top \boldsymbol{x}$ for some parameter vector $\boldsymbol{\beta}$ of appropriate dimension. Denote $g^{\mathcal{G}}(\boldsymbol{x}) = \boldsymbol{x}^\top \boldsymbol{\beta}^{\mathcal{G}}$ and $g^{\mathcal{G}}_{\mathcal{T}}(\boldsymbol{x}) = \boldsymbol{x}^\top \widehat{\boldsymbol{\beta}}$. Show that
$$
\mathbb{E}\left(g^{\mathcal{G}}_{\mathcal{T}}(\boldsymbol{X}) - g^*(\boldsymbol{X})\right)^2 = \mathbb{E}\left(\boldsymbol{X}^\top \widehat{\boldsymbol{\beta}} - \boldsymbol{X}^\top \boldsymbol{\beta}^{\mathcal{G}}\right)^2 + \mathbb{E}\left(\boldsymbol{X}^\top \boldsymbol{\beta}^{\mathcal{G}} - g^*(\boldsymbol{X})\right)^2.
$$
Hence, deduce that the statistical error in (2.16) is $\ell(g^{\mathcal{G}}_{\mathcal{T}}) - \ell(g^{\mathcal{G}}) = \mathbb{E}(g^{\mathcal{G}}_{\mathcal{T}}(\boldsymbol{X}) - g^{\mathcal{G}}(\boldsymbol{X}))^2$.

4. Show that formula (2.24) holds for the 0–1 loss with 0–1 response.

5. Let $\boldsymbol{X}$ be an $n$-dimensional normal random vector with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$, where the determinant of $\boldsymbol{\Sigma}$ is non-zero. Show that $\boldsymbol{X}$ has joint probability density
$$
f_{\boldsymbol{X}}(\boldsymbol{x}) = \frac{1}{\sqrt{(2\pi)^n\,|\boldsymbol{\Sigma}|}}\, \mathrm{e}^{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu})}, \quad \boldsymbol{x} \in \mathbb{R}^n.
$$

6. *(See page 360.)* Let $\widehat{\boldsymbol{\beta}} = \mathbf{A}^+\boldsymbol{y}$. Using the defining properties of the pseudo-inverse, show that for any $\boldsymbol{\beta} \in \mathbb{R}^p$,
$$
\|\mathbf{A}\widehat{\boldsymbol{\beta}} - \boldsymbol{y}\| \leqslant \|\mathbf{A}\boldsymbol{\beta} - \boldsymbol{y}\|.
$$

7. Suppose that in the polynomial regression Example 2.1 we select the linear class of functions $\mathcal{G}_p$ with $p \geqslant 4$. Then, $g^* \in \mathcal{G}_p$ and the approximation error is zero, because $g^{\mathcal{G}_p}(\boldsymbol{x}) = g^*(\boldsymbol{x}) = \boldsymbol{x}^\top \boldsymbol{\beta}$, where $\boldsymbol{\beta} = [10, -140, 400, -250, 0, \ldots, 0]^\top \in \mathbb{R}^p$. Use the tower property to show that the learner $g_{\mathcal{T}}(\boldsymbol{x}) = \boldsymbol{x}^\top \widehat{\boldsymbol{\beta}}$ with $\widehat{\boldsymbol{\beta}} = \mathbf{X}^+\boldsymbol{y}$, assuming $\text{rank}(\mathbf{X}) \geqslant 4$, is *unbiased*: *(see page 431, "UNBIASED")*
$$
\mathbb{E}\, g_{\mathcal{T}}(\boldsymbol{x}) = g^*(\boldsymbol{x}).
$$

8. (Exercise 7 continued.) Observe that the learner $g_{\mathcal{T}}$ can be written as a linear combination of the response variable: $g_{\mathcal{T}}(\boldsymbol{x}) = \boldsymbol{x}^\top \mathbf{X}^+ \boldsymbol{Y}$. Prove that for any learner of the form $\boldsymbol{x}^\top \mathbf{A}\boldsymbol{y}$, where $\mathbf{A} \in \mathbb{R}^{p\times n}$ is some matrix and that satisfies $\mathbb{E}_{\mathbf{X}}[\boldsymbol{x}^\top \mathbf{A}\boldsymbol{Y}] = g^*(\boldsymbol{x})$, we have
$$
\mathbb{V}\text{ar}_{\mathbf{X}}[\boldsymbol{x}^\top \mathbf{X}^+ \boldsymbol{Y}] \leqslant \mathbb{V}\text{ar}_{\mathbf{X}}[\boldsymbol{x}^\top \mathbf{A}\boldsymbol{Y}],
$$
where the equality is achieved for $\mathbf{A} = \mathbf{X}^+$. This is called the *Gauss–Markov inequality*. Hence, using the Gauss–Markov inequality deduce that for the unconditional variance:
$$
\mathbb{V}\text{ar}\, g_{\mathcal{T}}(\boldsymbol{x}) \leqslant \mathbb{V}\text{ar}[\boldsymbol{x}^\top \mathbf{A}\boldsymbol{Y}].
$$
Deduce that $\mathbf{A} = \mathbf{X}^+$ also minimizes the expected generalization risk.

9. Consider again the polynomial regression Example 2.1. Use the fact that $\mathbb{E}_{\mathbf{X}}\,\widehat{\boldsymbol{\beta}} = \mathbf{X}^+ \boldsymbol{h}^*(\boldsymbol{u})$, where $\boldsymbol{h}^*(\boldsymbol{u}) = \mathbb{E}[Y \mid \boldsymbol{U}=\boldsymbol{u}] = [h^*(u_1),\ldots,h^*(u_n)]^\top$, to show that the expected in-sample risk is:
$$
\mathbb{E}_{\mathbf{X}}\, \ell_{\text{in}}(g_{\mathcal{T}}) = \ell^* + \frac{\|\boldsymbol{h}^*(\boldsymbol{u})\|^2 - \|\mathbf{X}\mathbf{X}^+ \boldsymbol{h}^*(\boldsymbol{u})\|^2}{n} + \frac{\ell^* p}{n}.
$$
*(see page 430)* Also, use Theorem C.2 to show that the expected statistical error is:
$$
\mathbb{E}_{\mathbf{X}}\, (\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta})^\top \mathbf{H}_p (\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \ell^*\,\text{tr}(\mathbf{X}^+ (\mathbf{X}^+)^\top \mathbf{H}_p) + (\mathbf{X}^+ \boldsymbol{h}^*(\boldsymbol{u}) - \boldsymbol{\beta})^\top \mathbf{H}_p (\mathbf{X}^+ \boldsymbol{h}^*(\boldsymbol{u}) - \boldsymbol{\beta}).
$$

10. Consider the setting of the polynomial regression in Example 2.2. Use Theorem C.19 *(see page 449)* to prove that
$$
\sqrt{n}\left(\widehat{\boldsymbol{\beta}}_n - \boldsymbol{\beta}_p\right) \overset{\mathrm{d}}{\longrightarrow} \mathcal{N}\!\left(\mathbf{0},\, \ell^* \mathbf{H}_p^{-1} + \mathbf{H}_p^{-1} \mathbf{M}_p \mathbf{H}_p^{-1}\right), \tag{2.53}
$$
where $\mathbf{M}_p := \mathbb{E}[\boldsymbol{X}\boldsymbol{X}^\top (g^*(\boldsymbol{X}) - g^{\mathcal{G}_p}(\boldsymbol{X}))^2]$ is the matrix with $(i,j)$-th entry:
$$
\int_0^1 u^{i+j-2}\left(h^{\mathcal{H}_p}(u) - h^*(u)\right)^2 \mathrm{d}u,
$$
and $\mathbf{H}_p^{-1}$ is the $p \times p$ *inverse Hilbert matrix* with $(i,j)$-th entry: *(see "INVERSE HILBERT MATRIX")*
$$
(-1)^{i+j}(i+j-1)\binom{p+i-1}{p-j}\binom{p+j-1}{p-i}\binom{i+j-2}{i-1}^2.
$$
Observe that $\mathbf{M}_p = \mathbf{0}$ for $p \geqslant 4$, so that the matrix $\mathbf{M}_p$ term is due to choosing a restrictive class $\mathcal{G}_p$ that does not contain the true prediction function.

11. In Example 2.2 we saw that the statistical error can be expressed (see (2.20)) as
$$
\int_0^1 \left([1,\ldots,u^{p-1}](\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta}_p)\right)^2 \mathrm{d}u = (\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta}_p)^\top \mathbf{H}_p (\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta}_p).
$$
By Exercise 10 the random vector $\boldsymbol{Z}_n := \sqrt{n}(\widehat{\boldsymbol{\beta}}_n - \boldsymbol{\beta}_p)$ has asymptotically a multivariate normal distribution with mean vector $\mathbf{0}$ and covariance matrix $\mathbf{V} := \ell^* \mathbf{H}_p^{-1} + \mathbf{H}_p^{-1}\mathbf{M}_p \mathbf{H}_p^{-1}$. Use Theorem C.2 to show that the *expected* statistical error is asymptotically
$$
\mathbb{E}(\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta}_p)^\top \mathbf{H}_p (\widehat{\boldsymbol{\beta}} - \boldsymbol{\beta}_p) \simeq \frac{\ell^* p}{n} + \frac{\text{tr}(\mathbf{M}_p \mathbf{H}_p^{-1})}{n}, \quad n \to \infty. \tag{2.54}
$$
Plot this large-sample approximation of the expected statistical error and compare it with the outcome of the statistical error.

We note a subtle technical detail: In general, convergence in distribution does not imply convergence in $L_p$-norm (see Example C.6), and so here we have implicitly assumed that *(see page 442)*
$$
\|\boldsymbol{Z}_n\| \xrightarrow{\mathrm{d}} \text{Dist.} \;\Rightarrow\; \|\boldsymbol{Z}_n\| \xrightarrow{L_2} \text{constant} := \lim_{n\uparrow\infty} \mathbb{E}\|\boldsymbol{Z}_n\|.
$$

12. Consider again Example 2.2. The result in (2.53) suggests that $\mathbb{E}\widehat{\boldsymbol{\beta}} \to \boldsymbol{\beta}_p$ as $n \to \infty$, where $\boldsymbol{\beta}_p$ is the solution in the class $\mathcal{G}_p$ given in (2.18). Thus, the large-sample approximation of the pointwise bias of the learner $g^{\mathcal{G}_p}_{\mathcal{T}}(\boldsymbol{x}) = \boldsymbol{x}^\top \widehat{\boldsymbol{\beta}}$ at $\boldsymbol{x} = [1,\ldots,u^{p-1}]^\top$ is
$$
\mathbb{E}\, g^{\mathcal{G}_p}_{\mathcal{T}}(\boldsymbol{x}) - g^*(\boldsymbol{x}) \simeq [1,\ldots,u^{p-1}]\boldsymbol{\beta}_p - [1,u,u^2,u^3]\boldsymbol{\beta}^*, \quad n \to \infty.
$$
Use Python to reproduce Figure 2.17, which shows the (large-sample) pointwise squared bias of the learner for $p \in \{1,2,3\}$. Note how the bias is larger near the endpoints $u=0$ and $u=1$. Explain why the areas under the curves correspond to the approximation errors.

> **Figure 2.17.** The large-sample pointwise squared bias of the learner for $p = 1, 2, 3$. The bias is zero for $p \geqslant 4$. (Plot of pointwise squared bias vs. $u \in [0,1]$, showing curves for $p=1$ (dotted), $p=2$ (dashed), $p=3$ (solid), each with two humps reaching up to about 250, 40, and 120 respectively, all going to zero at $u=0, 0.5, 1$.)

13. For our running Example 2.2 we can use (2.53) to derive a large-sample approximation of the pointwise variance of the learner $g_{\mathcal{T}}(\boldsymbol{x}) = \boldsymbol{x}^\top \boldsymbol{\beta}_n$. In particular, show that for large $n$
$$
\mathbb{V}\text{ar}\, g_{\mathcal{T}}(\boldsymbol{x}) \simeq \frac{\ell^*\, \boldsymbol{x}^\top \mathbf{H}_p^{-1} \boldsymbol{x}}{n} + \frac{\boldsymbol{x}^\top \mathbf{H}_p^{-1} \mathbf{M}_p \mathbf{H}_p^{-1} \boldsymbol{x}}{n}, \quad n \to \infty. \tag{2.55}
$$
Figure 2.18 shows this (large-sample) variance of the learner for different values of the predictor $u$ and model index $p$. Observe that the variance ultimately increases in $p$ and that it is smaller at $u = 1/2$ than closer to the endpoints $u=0$ or $u=1$. Since the bias is also larger near the endpoints, we deduce that the pointwise mean squared error (2.21) is larger near the endpoints of the interval $[0,1]$ than near its middle. In other words, the error is much smaller in the center of the data cloud than near its periphery.

> **Figure 2.18.** The pointwise variance of the learner for various pairs of $p$ and $u$. (3-D bar/stem plot of variance of learner against $u \in \{0.05, \ldots, 0.95\}$ and $p \in \{1,3,5,7,9\}$, showing variance generally increasing with $p$ and higher near the endpoints of $u$.)

14. Let $h: x \mapsto \mathbb{R}$ be a convex function and let $X$ be a random variable. Use the subgradient definition of convexity to prove *Jensen's inequality*: *(see page 403)*
$$
\mathbb{E}\,h(X) \geqslant h(\mathbb{E}X). \tag{2.56}
$$

15. Using Jensen's inequality, show that the Kullback–Leibler divergence between probability densities $f$ and $g$ is always positive; that is,
$$
\mathbb{E}\ln \frac{f(X)}{g(X)} \geqslant 0,
$$
where $X \sim f$.

16. The purpose of this exercise is to prove the following *Vapnik–Chernovenkis bound*: for any *finite* class $\mathcal{G}$ (containing only a finite number $|\mathcal{G}|$ of possible functions) and a general *bounded* loss function, $l \leqslant \text{Loss} \leqslant u$, the expected statistical error is bounded from above according to:
$$
\mathbb{E}\,\ell(g^{\mathcal{G}}_{\mathcal{T}_n}) - \ell(g^{\mathcal{G}}) \leqslant \frac{(u-l)\sqrt{2\ln(2|\mathcal{G}|)}}{\sqrt{n}}. \tag{2.57}
$$
Note how this bound conveniently does not depend on the distribution of the training set $\mathcal{T}_n$ (which is typically unknown), but only on the complexity (i.e., cardinality) of the class $\mathcal{G}$. We can break up the proof of (2.57) into the following four parts:

    (a) For a general function class $\mathcal{G}$, training set $\mathcal{T}$, risk function $\ell$, and training loss $\ell_{\mathcal{T}}$, we have, by definition, $\ell(g^{\mathcal{G}}_{\mathcal{T}}) \leqslant \ell(g)$ and $\ell_{\mathcal{T}}(g^{\mathcal{G}}_{\mathcal{T}}) \leqslant \ell_{\mathcal{T}}(g)$ for all $g \in \mathcal{G}$. Show that
    $$
    \ell(g^{\mathcal{G}}_{\mathcal{T}}) - \ell(g^{\mathcal{G}}) \leqslant \sup_{g \in \mathcal{G}} |\ell_{\mathcal{T}}(g) - \ell(g)| + \ell_{\mathcal{T}}(g^{\mathcal{G}}) - \ell(g^{\mathcal{G}}),
    $$
    where we used the notation $\sup$ (supremum) for the least upper bound. Since $\mathbb{E}\ell_{\mathcal{T}}(g) = \mathbb{E}\ell(g)$, we obtain, after taking expectations on both sides of the inequality above:
    $$
    \mathbb{E}\,\ell(g^{\mathcal{G}}_{\mathcal{T}}) - \ell(g^{\mathcal{G}}) \leqslant \mathbb{E}\sup_{g\in\mathcal{G}} |\ell_{\mathcal{T}}(g) - \ell(g)|.
    $$

    (b) If $X$ is a zero-mean random variable taking values in the interval $[l,u]$, then the following *Hoeffding's inequality* states that the moment generating function satisfies
    $$
    \mathbb{E}\,\mathrm{e}^{tX} \leqslant \exp\!\left(\frac{t^2(u-l)^2}{8}\right), \quad t \in \mathbb{R}. \tag{2.58}
    $$
    Prove this result by using the fact that the line segment joining points $(l, \exp(tl))$ and $(u, \exp(tu))$ bounds the convex function $x \mapsto \exp(tx)$ for $x \in [l,u]$; that is:
    $$
    \mathrm{e}^{tx} \leqslant \mathrm{e}^{tl}\,\frac{u-x}{u-l} + \mathrm{e}^{tu}\,\frac{x-l}{u-l}, \quad x \in [l,u].
    $$

    (c) Let $Z_1,\ldots,Z_n$ be (possibly dependent and non-identically distributed) zero-mean random variables with moment generating functions that satisfy $\mathbb{E}\exp(tZ_k) \leqslant \exp(t^2\eta^2/2)$ for all $k$ and some parameter $\eta$. Use Jensen's inequality (2.56) to prove that for any $t > 0$, *(see page 427)*
    $$
    \mathbb{E}\max_k Z_k = \frac{1}{t}\,\mathbb{E}\ln\max_k \mathrm{e}^{tZ_k} \leqslant \frac{1}{t}\ln n + \frac{t\eta^2}{2}.
    $$
    From this derive that
    $$
    \mathbb{E}\max_k Z_k \leqslant \eta\sqrt{2\ln n}.
    $$
    Finally, show that this last inequality implies that
    $$
    \mathbb{E}\max_k |Z_k| \leqslant \eta\sqrt{2\ln(2n)}. \tag{2.59}
    $$

    (d) Returning to the objective of this exercise, denote the elements of $\mathcal{G}$ by $g_1,\ldots,g_{|\mathcal{G}|}$, and let $Z_k = \ell_{\mathcal{T}_n}(g_k) - \ell(g_k)$. By part (a) it is sufficient to bound $\mathbb{E}\max_k |Z_k|$. Show that the $\{Z_k\}$ satisfy the conditions of (c) with $\eta = (u-l)/\sqrt{n}$. For this you will need to apply part (b) to the random variable $\text{Loss}(g(\boldsymbol{X}), Y) - \ell(g)$, where $(\boldsymbol{X}, Y)$ is a generic data point. Now complete the proof of (2.57).

17. Consider the problem in Exercise 16a above. Show that
$$
|\ell_{\mathcal{T}}(g^{\mathcal{G}}_{\mathcal{T}}) - \ell(g^{\mathcal{G}})| \leqslant 2\sup_{g\in\mathcal{G}} |\ell_{\mathcal{T}}(g) - \ell(g)| + \ell_{\mathcal{T}}(g^{\mathcal{G}}) - \ell(g^{\mathcal{G}}).
$$
From this, conclude:
$$
\mathbb{E}\,|\ell_{\mathcal{T}}(g^{\mathcal{G}}_{\mathcal{T}}) - \ell(g^{\mathcal{G}})| \leqslant 2\mathbb{E}\sup_{g\in\mathcal{G}} |\ell_{\mathcal{T}}(g) - \ell(g)|.
$$
The last bound allows us to assess how close the training loss $\ell_{\mathcal{T}}(g^{\mathcal{G}}_{\mathcal{T}})$ is to the optimal risk $\ell(g^{\mathcal{G}})$ within class $\mathcal{G}$.

18. Show that for the normal linear model $\boldsymbol{Y} \sim \mathcal{N}(\mathbf{X}\boldsymbol{\beta}, \sigma^2 \mathbf{I}_n)$, the maximum likelihood estimator of $\sigma^2$ is identical to the method of moments estimator (2.37).

19. Let $X \sim \text{Gamma}(\alpha, \lambda)$. Show that the pdf of $Z = 1/X$ is equal to
$$
\frac{\lambda^\alpha (z)^{-\alpha-1} \mathrm{e}^{-\lambda(z)^{-1}}}{\Gamma(\alpha)}, \quad z > 0.
$$

20. Consider the sequence $w_0, w_1, \ldots$, where $w_0 = g(\boldsymbol{\theta})$ is a non-degenerate initial guess and $w_t(\boldsymbol{\theta}) \propto w_{t-1}(\boldsymbol{\theta})\, g(\tau \mid \boldsymbol{\theta})$, $t \geqslant 1$. We assume that $g(\tau \mid \boldsymbol{\theta})$ is not the constant function (with respect to $\boldsymbol{\theta}$) and that the maximum likelihood value
$$
g(\tau \mid \widehat{\boldsymbol{\theta}}) = \max_{\boldsymbol{\theta}} g(\tau \mid \boldsymbol{\theta}) < \infty
$$
exists (is bounded). Let
$$
l_t := \int g(\tau \mid \boldsymbol{\theta})\, w_t(\boldsymbol{\theta})\, \mathrm{d}\boldsymbol{\theta}.
$$
Show that $\{l_t\}$ is a strictly increasing and bounded sequence. Hence, conclude that its limit is $g(\tau \mid \widehat{\boldsymbol{\theta}})$.

21. Consider the Bayesian model for $\tau = \{x_1,\ldots,x_n\}$ with likelihood $g(\tau\mid\mu)$ such that $(X_1,\ldots,X_n\mid\mu) \overset{\text{iid}}{\sim} \mathcal{N}(\mu, 1)$ and prior pdf $g(\mu)$ such that $\mu \sim \mathcal{N}(\nu, 1)$ for some hyperparameter $\nu$. Define a sequence of densities $w_t(\mu)$, $t \geqslant 2$ via $w_t(\mu) \propto w_{t-1}(\mu)\,g(\tau\mid\mu)$, starting with $w_1(\mu) = g(\mu)$. Let $a_t$ and $b_t$ denote the mean and precision${}^4$ of $\mu$ under the posterior $g_t(\mu\mid\tau) \propto g(\tau\mid\mu)w_t(\mu)$. Show that $g_t(\mu\mid\tau)$ is a normal density with precision $b_t = b_{t-1} + n$, $b_0 = 1$ and mean $a_t = (1-\gamma_t)a_{t-1} + \gamma_t \overline{x}_n$, $a_0 = \nu$, where $\gamma_t := n/(b_{t-1}+n)$. Hence, deduce that $g_t(\mu\mid\tau)$ converges to a degenerate density with a point-mass at $\overline{x}_n$.

    > ${}^4$ The precision is the reciprocal of the variance.

22. Consider again Example 2.8, where we have a normal model with improper prior $g(\boldsymbol{\theta}) = g(\mu,\sigma^2) \propto 1/\sigma^2$. Show that the prior predictive pdf is an improper density $g(x) \propto 1$, but that the posterior predictive density is
$$
g(x\mid\tau) \propto \left(1 + \frac{(x-\overline{x}_n)^2}{(n+1)S_n^2}\right)^{-n/2}.
$$
Deduce that $\dfrac{X - \overline{x}_n}{S_n \sqrt{(n+1)/(n-1)}} \sim \mathsf{t}_{n-1}$.

23. Assuming that $X_1,\ldots,X_n \overset{\text{iid}}{\sim} f$, show that (2.48) holds and that $\ell_n^* = -n\,\mathbb{E}\ln f(\boldsymbol{X})$.

24. Suppose that $\tau = \{x_1,\ldots,x_n\}$ are observations of iid continuous and strictly positive random variables, and that there are two possible models for their pdf. The first model $p=1$ is
$$
g(x\mid\theta, p=1) = \theta \exp(-\theta x)
$$
and the second $p=2$ is
$$
g(x\mid\theta, p=2) = \left(\frac{2\theta}{\pi}\right)^{1/2} \exp\!\left(-\frac{\theta x^2}{2}\right).
$$
For both models, assume that the prior for $\theta$ is a gamma density
$$
g(\theta) = \frac{b^t}{\Gamma(t)}\,\theta^{t-1}\exp(-b\theta),
$$
with the same hyperparameters $b$ and $t$. Find a formula for the Bayes factor, $g(\tau\mid p=1)/g(\tau\mid p=2)$, for comparing these models.

25. Suppose that we have a total of $m$ possible models with prior probabilities $g(p)$, $p=1,\ldots,m$. Show that the posterior probability of model $g(p\mid\tau)$ can be expressed in terms of all the $p(p-1)$ Bayes factors:
$$
g(p=i\mid\tau) = \left(1 + \sum_{j\neq i} \frac{g(p=j)}{g(p=i)} B_{j\mid i}\right)^{-1}.
$$

26. Given the data $\tau = \{x_1,\ldots,x_n\}$, suppose that we use the likelihood $(X\mid\boldsymbol{\theta}) \sim \mathcal{N}(\mu,\sigma^2)$ with parameter $\boldsymbol{\theta} = (\mu,\sigma^2)^\top$ and wish to compare the following two nested models.

    (a) Model $p=1$, where $\sigma^2 = \sigma_0^2$ is known and this is incorporated via the prior
    $$
    g(\boldsymbol{\theta}\mid p=1) = g(\mu\mid\sigma^2, p=1)\,g(\sigma^2\mid p=1) = \frac{1}{\sqrt{2\pi}\sigma}\,\mathrm{e}^{-\frac{(\mu-x_0)^2}{2\sigma^2}} \times \delta(\sigma^2 - \sigma_0^2).
    $$

    (b) Model $p=2$, where both mean and variance are unknown with prior
    $$
    g(\boldsymbol{\theta}\mid p=2) = g(\mu\mid\sigma^2)\,g(\sigma^2) = \frac{1}{\sqrt{2\pi}\sigma}\,\mathrm{e}^{-\frac{(\mu-x_0)^2}{2\sigma^2}} \times \frac{b^t (\sigma^2)^{-t-1} \mathrm{e}^{-b/\sigma^2}}{\Gamma(t)}.
    $$

    Show that the prior $g(\boldsymbol{\theta}\mid p=1)$ can be viewed as the limit of the prior $g(\boldsymbol{\theta}\mid p=2)$ when $t\to\infty$ and $b = t\sigma_0^2$. Hence, conclude that
    $$
    g(\tau\mid p=1) = \lim_{\substack{t\to\infty \\ b=t\sigma_0^2}} g(\tau\mid p=2)
    $$
    and use this result to calculate $B_{1\mid 2}$. Check that the formula for $B_{1\mid 2}$ agrees with the Savage–Dickey density ratio:
    $$
    \frac{g(\tau\mid p=1)}{g(\tau\mid p=2)} = \frac{g(\sigma^2=\sigma_0^2\mid\tau)}{g(\sigma^2=\sigma_0^2)},
    $$
    where $g(\sigma^2\mid\tau)$ and $g(\sigma^2)$ are the posterior and prior, respectively, under model $p=2$.
