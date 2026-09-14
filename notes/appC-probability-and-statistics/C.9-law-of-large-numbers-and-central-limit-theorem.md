---
appendix: C
section: "C.9"
title: "Law of Large Numbers and Central Limit Theorem"
pdf_pages: "463-469"
---

## C.9 Law of Large Numbers and Central Limit Theorem

Two main results in probability are the *law of large numbers* and *the central limit theorem*. Both are limit theorems involving sums of independent random variables. In particular, consider a sequence $X_1, X_2, \ldots$ of iid random variables with finite expectation $\mu$ and finite variance $\sigma^2$. For each $n$ define $\overline{X}_n := (X_1+\cdots+X_n)/n$. What can we say about the (random) sequence of averages $\overline{X}_1, \overline{X}_2, \overline{X}_3, \ldots$? By (C.12) and (C.14) (p.429) we have $\mathbb{E}\overline{X}_n = \mu$ and $\mathbb{V}\mathrm{ar}\,\overline{X}_n = \sigma^2/n$. Hence, as $n$ increases, the variance of the (random) average $\overline{X}_n$ goes to 0. This means that by Definition C.8, the average $\overline{X}_n$ converges to $\mu$ in $L^2$-norm as $n\to\infty$, that is, $\overline{X}_n \xrightarrow{\ L^2\ } \mu$.

In fact, to obtain *convergence in probability* the variance need not be finite — it is sufficient to assume that $\mu = \mathbb{E}X < \infty$.

> **Theorem C.15: Weak Law of Large Numbers**
>
> If $X_1, \ldots, X_n$ are iid with finite expectation $\mu$, then for all $\varepsilon > 0$
>
> $$\lim_{n\to\infty}\mathbb{P}\big[|\overline{X}_n - \mu| > \varepsilon\big] = 0.$$
>
> In other words, $\overline{X}_n \xrightarrow{\ \mathbb{P}\ } \mu$.

The theorem has a natural generalization for random vectors. Namely, if $\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} < \infty$ (see p.355), then $\mathbb{P}\big[\|\overline{\boldsymbol{X}}_n - \boldsymbol{\mu}\| > \varepsilon\big] \to 0$, where $\|\cdot\|$ is the Euclidean norm. We give a proof in the scalar case.

*Proof:* Let $Z_k := X_k - \mu$ for all $k$, so that $\mathbb{E}Z = 0$. We thus need to show that $\overline{Z}_n \xrightarrow{\ \mathbb{P}\ } 0$. We use the properties of the characteristic function of $Z$ denoted as $\psi_Z$ (see p.441). Due to the iid assumption, we have

$$\psi_{\overline{Z}_n}(t) = \mathbb{E}\,\mathrm{e}^{\mathrm{i}t\overline{Z}_n} = \mathbb{E}\prod_{i=1}^{n}\mathrm{e}^{\mathrm{i}tZ_i/n} = \prod_{i=1}^{n}\mathbb{E}\,\mathrm{e}^{\mathrm{i}tZ_i/n} = \prod_{i=1}^{n}\psi_Z(t/n) = [\psi_Z(t/n)]^n. \tag{C.37}$$

An application of Taylor's Theorem B.1 in the neighborhood of $t=0$ yields

$$\psi_Z(t/n) = \psi_Z(0) + o(t/n).$$

Since $\psi_Z(0)=1$, we have:

$$\psi_{\overline{Z}_n}(t) = [\psi_Z(t/n)]^n = [1+o(1/n)]^n \longrightarrow 1, \quad n\to\infty.$$

The characteristic function of a random variable that always equals zero is 1. Therefore, Theorem C.12 implies that $\overline{Z}_n \xrightarrow{\ d\ } 0$. However, according to Example C.6, convergence in distribution to a constant implies convergence in probability. Hence, $\overline{Z}_n \xrightarrow{\ \mathbb{P}\ } 0$. $\square$

There is also a stronger version of this theorem, as follows.

> **Theorem C.16: Strong Law of Large Numbers**
>
> If $X_1, \ldots, X_n$ are iid with expectation $\mu$ and $\mathbb{E}X^2 < \infty$, then for all $\varepsilon > 0$
>
> $$\lim_{n\to\infty}\mathbb{P}\Big[\sup_{k\geqslant n}|\overline{X}_k - \mu| > \varepsilon\Big] = 0.$$
>
> In other words, $\overline{X}_n \xrightarrow{\text{a.s.}} \mu$.

*Proof:* First, note that any random variable $X$ can be written as the difference of two nonnegative random variables: $X = X_+ - X_-$, where $X_+ := \max\{X,0\}$ and $X_- := -\min\{X,0\}$. Thus, without loss of generality, we assume that the random variables in the theorem above are nonnegative.

Second, from the sequence $\{\overline{X}_1, \overline{X}_2, \overline{X}_3, \ldots\}$ we can pick up the subsequence $\{\overline{X}_1, \overline{X}_4, \overline{X}_9, \overline{X}_{16}, \ldots\} =: \{\overline{X}_{j^2}\}$. Then, from Chebyshev's inequality (C.36) and the iid condition, we have

$$\sum_{j=1}^{\infty}\mathbb{P}\big[|\overline{X}_{j^2}-\mu|>\varepsilon\big] \leqslant \frac{\mathbb{V}\mathrm{ar}\,X}{\varepsilon^2}\sum_{j=1}^{\infty}\frac{1}{j^2} < \infty.$$

Therefore, by definition $\overline{X}_{n^2} \xrightarrow{\text{cpl.}} \mu$ and from Theorem C.13 we conclude that $\overline{X}_{n^2}\xrightarrow{\text{a.s.}}\mu$.

Third, for any arbitrary $n$, we can find a $k$, say $k = \lfloor\sqrt{n}\rfloor$, so that $k^2 \leqslant n \leqslant (k+1)^2$. For such a $k$ and nonnegative $X_1, X_2, \ldots$, it holds that

$$\frac{k^2}{(k+1)^2}\overline{X}_{k^2} \leqslant \overline{X}_n \leqslant \overline{X}_{(k+1)^2}\frac{(k+1)^2}{k^2}.$$

Since $\overline{X}_{k^2}$ and $\overline{X}_{(k+1)^2}$ converge almost surely to $\mu$ as $k$ (and hence $n$) goes to infinity, we conclude that $\overline{X}_n \xrightarrow{\text{a.s.}} \mu$. $\square$

Note that the condition $\mathbb{E}X^2 < \infty$ in Theorem C.16 can be weakened to $\mathbb{E}|X| < \infty$ and the iid condition on the variables $X_1, \ldots, X_n$ can be relaxed to mere pairwise independence. The corresponding proof, however, is significantly more difficult.

The *Central Limit Theorem* describes the approximate distribution of $\overline{X}_n$, and it applies to both continuous and discrete random variables. Loosely, it states that

> *the average of a large number of iid random variables approximately has a normal distribution.*

Specifically, the random variable $\overline{X}_n$ has a distribution that is approximately normal, with expectation $\mu$ and variance $\sigma^2/n$.

> **Theorem C.17: Central Limit Theorem**
>
> If $X_1, \ldots, X_n$ are iid with finite expectation $\mu$ and finite variance $\sigma^2$, then for all $x\in\mathbb{R}$,
>
> $$\lim_{n\to\infty}\mathbb{P}\left[\frac{\overline{X}_n-\mu}{\sigma/\sqrt{n}}\leqslant x\right] = \Phi(x),$$
>
> where $\Phi$ is the cdf of the standard normal distribution.

*Proof:* Let $Z_k := (X_k-\mu)/\sigma$ for all $k$, so that $\mathbb{E}Z=0$ and $\mathbb{E}Z^2=1$. We thus need to show that $\sqrt{n}\,\overline{Z}_n \xrightarrow{\ d\ } \mathcal{N}(0,1)$. We again use the properties of the characteristic function. Let $\psi_Z$ be the characteristic function of an iid copy of $Z$, then due to the iid assumption a similar calculation to the one in (C.37) yields

$$\psi_{\sqrt{n}\overline{Z}_n}(t) = \mathbb{E}\,\mathrm{e}^{\mathrm{i}t\sqrt{n}\overline{Z}_n} = [\psi_Z(t/\sqrt{n})]^n.$$

An application of Taylor's Theorem B.1 in the neighborhood of $t=0$ yields

$$\psi_Z(t/\sqrt{n}) = 1 + \frac{t}{\sqrt{n}}\psi_Z'(0) + \frac{t^2}{2n}\psi_Z''(0) + o(t^2/n).$$

Since $\psi_Z'(0) = \mathbb{E}\frac{\mathrm{d}}{\mathrm{d}t}\mathrm{e}^{\mathrm{i}tZ}\Big|_{t=0} = \mathrm{i}\,\mathbb{E}Z = 0$ and $\psi_Z''(0) = \mathrm{i}^2\,\mathbb{E}Z^2 = -1$, we have:

$$\psi_{\sqrt{n}\overline{Z}_n}(t) = [\psi_Z(t/\sqrt{n})]^n = \left[1-\frac{t^2}{2n}+o(1/n)\right]^n \longrightarrow \mathrm{e}^{-t^2/2}, \quad n\to\infty.$$

From Example C.4, we recognize $\mathrm{e}^{-t^2/2}$ as the characteristic function of the standard normal distribution. Thus, from Theorem C.12 we conclude that $\sqrt{n}\,\overline{Z}_n \xrightarrow{\ d\ } \mathcal{N}(0,1)$. $\square$

> **Figure C.6:** Illustration of the central limit theorem for (left) the uniform distribution and (right) the exponential distribution. The left panel shows the pdfs of $\overline{X}_1, 2\overline{X}_2, \ldots, 4\overline{X}_4$ for the case where the $\{X_i\}$ have a $\mathcal{U}[0,1]$ distribution — curves for $n=1,2,3,4$ progressively narrowing and forming a bell shape peaked near 1. The right panel shows the same for the $\mathsf{Exp}(1)$ distribution — curves for $n=1,2,3,4$ starting from a decaying exponential shape ($n=1$) and converging toward a symmetric bell shape as $n$ increases. In both cases we clearly see convergence to a bell-shaped curve, characteristic of the normal distribution.

The multivariate version of the central limit theorem is the basis for many asymptotic (in the size of the training set) results in machine learning and data science.

> **Theorem C.18: Multivariate Central Limit Theorem**
>
> Let $\boldsymbol{X}_1, \ldots, \boldsymbol{X}_n$ be iid random vectors with expectation vector $\boldsymbol{\mu}$ and finite covariance matrix $\boldsymbol{\Sigma}$. Define $\overline{\boldsymbol{X}}_n := (\boldsymbol{X}_1+\cdots+\boldsymbol{X}_n)/n$. Then,
>
> $$\sqrt{n}\,(\overline{\boldsymbol{X}}_n - \boldsymbol{\mu}) \xrightarrow{\ d\ } \mathcal{N}(\boldsymbol{0}, \boldsymbol{\Sigma}) \quad \text{as } n\to\infty.$$

One application is as follows. Suppose that a parameter of interest, $\boldsymbol{\theta}^*$, is the unique solution of the system of equations $\mathbb{E}\,\boldsymbol{\psi}(\boldsymbol{X}\mid\boldsymbol{\theta}^*) = \boldsymbol{0}$, where $\boldsymbol{\psi}$ is a vector-valued (or multi-valued) function and the distribution of $\boldsymbol{X}$ does not depend on $\boldsymbol{\theta}$. An *M-estimator* of $\boldsymbol{\theta}^*$, denoted $\widehat{\boldsymbol{\theta}}_n$, is the solution to the system of equations that results from approximating the expectation with respect to $\boldsymbol{X}$ using an average of $n$ iid copies of $\boldsymbol{X}$:

$$\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}) := \frac{1}{n}\sum_{i=1}^{n}\boldsymbol{\psi}(\boldsymbol{X}_i\mid\boldsymbol{\theta}).$$

Thus, $\overline{\boldsymbol{\psi}}_n(\widehat{\boldsymbol{\theta}}_n) = \boldsymbol{0}$.

> **Theorem C.19: M-estimator**
>
> The M-estimator is asymptotically normal as $n\to\infty$:
>
> $$\sqrt{n}\,(\widehat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}^*) \xrightarrow{\ d\ } \mathcal{N}(\boldsymbol{0}, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-\top}), \tag{C.38}$$
>
> where $\mathbf{A} := -\mathbb{E}\dfrac{\partial\boldsymbol{\psi}}{\partial\boldsymbol{\theta}}(\boldsymbol{X}\mid\boldsymbol{\theta}^*)$ and $\mathbf{B} := \mathbb{E}\big[\boldsymbol{\psi}(\boldsymbol{X}\mid\boldsymbol{\theta}^*)\boldsymbol{\psi}(\boldsymbol{X}\mid\boldsymbol{\theta}^*)^\top\big]$ is the covariance matrix (see p.398) of $\boldsymbol{\psi}(\boldsymbol{X}\mid\boldsymbol{\theta}^*)$.

*Proof:* We give a proof under the simplifying assumption[^3] that $\widehat{\boldsymbol{\theta}}_n$ is a unique root, that is, for any $\theta$ and $\varepsilon$, there exists a $\delta>0$ such that $\|\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}\|>\varepsilon$ implies that $\|\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta})\|>\delta$.

First, we argue that $\widehat{\boldsymbol{\theta}}_n \xrightarrow{\ \mathbb{P}\ } \boldsymbol{\theta}^*$; that is, $\mathbb{P}[\|\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*\|>\varepsilon]\to0$. From the multivariate extension of Theorem C.15, we have that

$$\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*) \xrightarrow{\ \mathbb{P}\ } \mathbb{E}\,\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*) = \mathbb{E}\,\boldsymbol{\psi}(\boldsymbol{X}\mid\boldsymbol{\theta}^*) = \boldsymbol{0}.$$

Therefore, using the uniqueness of $\widehat{\boldsymbol{\theta}}_n$, we can show that $\widehat{\boldsymbol{\theta}}_n \xrightarrow{\ \mathbb{P}\ } \boldsymbol{\theta}^*$ via the bound:

$$\mathbb{P}\big[\|\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*\|>\varepsilon\big] \leqslant \mathbb{P}\big[\|\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*)\|>\delta\big] = \mathbb{P}\big[\|\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*)-\mathbb{E}\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*)\|>\delta\big] \to 0, \quad n\to\infty.$$

Second, we take a Taylor expansion of each component of the vector $\overline{\boldsymbol{\psi}}_n(\widehat{\boldsymbol{\theta}}_n)$ around $\boldsymbol{\theta}^*$ to obtain:

$$\overline{\boldsymbol{\psi}}_n(\widehat{\boldsymbol{\theta}}_n) = \overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*) + \mathbf{J}_n(\boldsymbol{\theta}')(\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*),$$

where $\mathbf{J}_n(\boldsymbol{\theta})$ is the Jacobian of $\overline{\boldsymbol{\psi}}_n$ at $\boldsymbol{\theta}$, and $\boldsymbol{\theta}'$ lies on the line segment joining $\widehat{\boldsymbol{\theta}}_n$ and $\boldsymbol{\theta}^*$. Rearrange the last equation and multiply both sides by $\sqrt{n}\,\mathbf{A}^{-1}$ to obtain:

$$-\mathbf{A}^{-1}\mathbf{J}_n(\boldsymbol{\theta}')\sqrt{n}\,(\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*) = \mathbf{A}^{-1}\sqrt{n}\,\overline{\boldsymbol{\psi}}_n(\boldsymbol{\theta}^*).$$

By the central limit theorem, $\sqrt{n}\,\overline{\boldsymbol{\psi}}(\boldsymbol{\theta}^*)$ converges in distribution to $\mathcal{N}(\boldsymbol{0}, \mathbf{B})$. Therefore,

$$-\mathbf{A}^{-1}\mathbf{J}_n(\boldsymbol{\theta}')\sqrt{n}\,(\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*) \xrightarrow{\ d\ } \mathcal{N}(\boldsymbol{0}, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-\top}).$$

Theorem C.15 (the weak law of large numbers) applied to the iid random matrices $\{\frac{\partial}{\partial\boldsymbol{\theta}}\boldsymbol{\psi}(\boldsymbol{X}_i\mid\boldsymbol{\theta})\}$ shows that

$$\mathbf{J}_n(\boldsymbol{\theta}) \xrightarrow{\ \mathbb{P}\ } \mathbb{E}\frac{\partial}{\partial\boldsymbol{\theta}}\boldsymbol{\psi}(\boldsymbol{X}\mid\boldsymbol{\theta}).$$

Moreover, since $\widehat{\boldsymbol{\theta}}_n \xrightarrow{\ \mathbb{P}\ } \boldsymbol{\theta}^*$ and $\mathbf{J}_n$ is continuous in $\boldsymbol{\theta}$, we have that $\mathbf{J}_n(\boldsymbol{\theta}') \xrightarrow{\ \mathbb{P}\ } -\mathbf{A}$. Therefore, by Slutsky's theorem (p.444), $-\mathbf{A}^{-1}\mathbf{J}_n(\boldsymbol{\theta}')\sqrt{n}\,(\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*) - \sqrt{n}\,(\widehat{\boldsymbol{\theta}}_n-\boldsymbol{\theta}^*) \xrightarrow{\ \mathbb{P}\ } \boldsymbol{0}$. $\square$

[^3]: The result holds under far less stringent assumptions.

Finally, we mention *Laplace's approximation*, which shows how integrals or expectations behave under the normal distribution with a vanishingly small variance.

> **Theorem C.20: Laplace's Approximation**
>
> Suppose that $\boldsymbol{\theta}_n \to \boldsymbol{\theta}^*$, where $\boldsymbol{\theta}^*$ lies in the interior of the open set $\Theta \subseteq \mathbb{R}^p$ and that $\boldsymbol{\Sigma}_n$ is a $p\times p$ covariance matrix such that $\boldsymbol{\Sigma}_n \to \boldsymbol{\Sigma}^*$. Let $g : \Theta \mapsto \mathbb{R}$ be a continuous function with $g(\boldsymbol{\theta}^*)\neq0$. Then, as $n\to\infty$,
>
> $$n^{p/2}\int_{\Theta} g(\boldsymbol{\theta})\,\mathrm{e}^{-\frac{n}{2}(\boldsymbol{\theta}-\boldsymbol{\theta}_n)^\top\boldsymbol{\Sigma}_n^{-1}(\boldsymbol{\theta}-\boldsymbol{\theta}_n)}\,\mathrm{d}\boldsymbol{\theta} \to g(\boldsymbol{\theta}^*)\sqrt{|2\pi\boldsymbol{\Sigma}^*|}. \tag{C.39}$$

*Proof (Sketch for a bounded domain $\Theta$):* The left-hand side of (C.39) can be written as the expectation with respect to the $\mathcal{N}(\boldsymbol{\theta}_n, \boldsymbol{\Sigma}_n/n)$ distribution:

$$\sqrt{|2\pi\boldsymbol{\Sigma}_n|}\int_{\Theta} g(\boldsymbol{\theta})\frac{\exp\left(-\frac{n}{2}(\boldsymbol{\theta}-\boldsymbol{\theta}_n)^\top\boldsymbol{\Sigma}_n^{-1}(\boldsymbol{\theta}-\boldsymbol{\theta}_n)\right)}{|2\pi\boldsymbol{\Sigma}_n/n|^{1/2}}\mathrm{d}\boldsymbol{\theta} = \sqrt{|2\pi\boldsymbol{\Sigma}_n|}\,\mathbb{E}[g(\boldsymbol{X}_n)\mathbb{1}\{\boldsymbol{X}_n\in\Theta\}],$$

where $\boldsymbol{X}_n \sim \mathcal{N}(\boldsymbol{\theta}_n, \boldsymbol{\Sigma}_n/n)$. Let $\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},\mathbf{I})$. Then, $\boldsymbol{\theta}_n + \boldsymbol{\Sigma}_n^{1/2}\boldsymbol{Z}/\sqrt{n}$ has the same distribution as $\boldsymbol{X}_n$ and $\big(\boldsymbol{\theta}_n+\boldsymbol{\Sigma}_n^{1/2}\boldsymbol{Z}/\sqrt{n}\big) \to \boldsymbol{\theta}^*$ as $n\to\infty$. By continuity of $g(\boldsymbol{\theta})\mathbb{1}\{\boldsymbol{\theta}\in\Theta\}$ in the interior of $\Theta$, as $n\to\infty$:[^4]

$$\mathbb{E}[g(\boldsymbol{X}_n)\mathbb{1}\{\boldsymbol{X}_n\in\Theta\}] = \mathbb{E}\left[g\left(\boldsymbol{\theta}_n+\frac{\boldsymbol{\Sigma}_n^{1/2}\boldsymbol{Z}}{\sqrt{n}}\right)\mathbb{1}\left\{\left(\boldsymbol{\theta}_n+\frac{\boldsymbol{\Sigma}_n^{1/2}\boldsymbol{Z}}{\sqrt{n}}\right)\in\Theta\right\}\right] \longrightarrow g(\boldsymbol{\theta}^*)\mathbb{1}\{\boldsymbol{\theta}^*\in\Theta\}.$$

Since $\boldsymbol{\theta}^*$ lies in the interior of $\Theta$, we have $\mathbb{1}\{\boldsymbol{\theta}^*\in\Theta\}=1$, completing the proof. $\square$

[^4]: We can exchange the limit and expectation, as $g(\boldsymbol{\theta})\mathbb{1}\{\boldsymbol{\theta}\in\Theta\} \leqslant \max_{\theta\in\Theta}g(\boldsymbol{\theta})$ and $\int_\Theta \max_{\theta\in\Theta}g(\boldsymbol{\theta})\,\mathrm{d}\boldsymbol{\theta} = |\Theta|\max_{\theta\in\Theta}g(\boldsymbol{\theta}) < \infty$.

As an application of Theorem C.20 we can show the following.

> **Theorem C.21: Approximation of Integrals**
>
> Suppose that $r : \boldsymbol{\theta} \mapsto \mathbb{R}$ is twice continuously differentiable with a unique global minimum at $\boldsymbol{\theta}^*$ and $g : \boldsymbol{\theta} \mapsto \mathbb{R}$ is continuous with $g(\boldsymbol{\theta}^*) > 0$. Then, as $n\to\infty$,
>
> $$\ln\int_{\mathbb{R}^p} g(\boldsymbol{\theta})\,\mathrm{e}^{-n\,r(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} \simeq -n\,r(\boldsymbol{\theta}^*) - \frac{p}{2}\ln n. \tag{C.40}$$
>
> More generally, if $r_n$ has a unique global minimum $\boldsymbol{\theta}_n$ and $r_n \to r \Rightarrow \boldsymbol{\theta}_n \to \boldsymbol{\theta}^*$, then
>
> $$\ln\int_{\mathbb{R}^p} g(\boldsymbol{\theta})\,\mathrm{e}^{-n\,r_n(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} \simeq -n\,r_n(\boldsymbol{\theta}^*) - \frac{p}{2}\ln n.$$

*Proof (Sketch, of (C.40); see p.400):* Let $\mathbf{H}(\boldsymbol{\theta})$ be the Hessian matrix of $r$ at $\boldsymbol{\theta}$. By Taylor's theorem we can write

$$r(\boldsymbol{\theta}) - r(\boldsymbol{\theta}^*) = (\boldsymbol{\theta}-\boldsymbol{\theta}^*)^\top\underbrace{\frac{\partial r(\boldsymbol{\theta}^*)}{\partial\boldsymbol{\theta}}}_{=\boldsymbol{0}} + \frac{1}{2}(\boldsymbol{\theta}-\boldsymbol{\theta}^*)^\top\mathbf{H}(\overline{\boldsymbol{\theta}})(\boldsymbol{\theta}-\boldsymbol{\theta}^*),$$

where $\overline{\boldsymbol{\theta}}$ is a point that lies on the line segment joining $\boldsymbol{\theta}^*$ and $\boldsymbol{\theta}$. Since $\boldsymbol{\theta}^*$ is a unique global minimum, there must be a small enough neighborhood of $\boldsymbol{\theta}^*$, say $\Theta$, such that $r$ is a strictly (also known as strongly) convex function on $\Theta$ (see p.403). In other words, $\mathbf{H}(\boldsymbol{\theta})$ is a positive definite matrix for all $\boldsymbol{\theta}\in\Theta$ and there exists a smallest positive eigenvalue $\lambda_1 > 0$ such that $\boldsymbol{x}^\top\mathbf{H}(\boldsymbol{\theta})\boldsymbol{x} \geqslant \lambda_1\|\boldsymbol{x}\|^2$ for all $\boldsymbol{x}$. In addition, since the maximum eigenvalue of $\mathbf{H}(\boldsymbol{\theta})$ is a continuous function of $\boldsymbol{\theta}\in\Theta$ and $\Theta$ is bounded, there must exist a constant $\lambda_2 > \lambda_1$ such that $\boldsymbol{x}^\top\mathbf{H}(\boldsymbol{\theta})\boldsymbol{x} \leqslant \lambda_2\|\boldsymbol{x}\|^2$ for all $\boldsymbol{x}$. In other words, denoting $r^* := r(\boldsymbol{\theta}^*)$, we have the bounds:

$$-\frac{\lambda_2}{2}\|\boldsymbol{\theta}-\boldsymbol{\theta}^*\|^2 \leqslant -(r(\boldsymbol{\theta})-r^*) \leqslant -\frac{\lambda_1}{2}\|\boldsymbol{\theta}-\boldsymbol{\theta}^*\|^2, \quad \boldsymbol{\theta}\in\Theta.$$

Therefore,

$$\mathrm{e}^{-nr^*}\int_\Theta g(\boldsymbol{\theta})\,\mathrm{e}^{-\frac{n\lambda_2}{2}\|\boldsymbol{\theta}-\boldsymbol{\theta}^*\|^2}\,\mathrm{d}\boldsymbol{\theta} \leqslant \int_\Theta g(\boldsymbol{\theta})\,\mathrm{e}^{-nr(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} \leqslant \mathrm{e}^{-nr^*}\int_\Theta g(\boldsymbol{\theta})\,\mathrm{e}^{-\frac{n\lambda_1}{2}\|\boldsymbol{\theta}-\boldsymbol{\theta}^*\|^2}\,\mathrm{d}\boldsymbol{\theta}.$$

An application of Theorem C.20 yields $\int_\Theta g(\boldsymbol{\theta})\,\mathrm{e}^{-nr(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} = O(\mathrm{e}^{-nr^*}/n^{p/2})$ and, more importantly,

$$\ln\int_\Theta g(\boldsymbol{\theta})\,\mathrm{e}^{-nr(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} \simeq -nr^* - \frac{p}{2}\ln n.$$

Thus, the proof will be complete once we show that $\int_{\overline{\Theta}} g(\boldsymbol{\theta})\,\mathrm{e}^{-nr(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta}$, with $\overline{\Theta} := \mathbb{R}^p\setminus\Theta$, is asymptotically negligible compared to $\int_\Theta g(\boldsymbol{\theta})\,\mathrm{e}^{-nr(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta}$. Since $\boldsymbol{\theta}^*$ is a global minimum that lies outside any neighborhood of $\overline{\Theta}$, there must exist a constant $c > 0$ such that $r(\boldsymbol{\theta})-r^* > c$ for all $\boldsymbol{\theta}\in\overline{\Theta}$. Therefore,

$$\begin{aligned}
\int_{\overline{\Theta}} g(\boldsymbol{\theta})\,\mathrm{e}^{-nr(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} &= \mathrm{e}^{-(n-1)r^*}\int_{\overline{\Theta}} g(\boldsymbol{\theta})\,\mathrm{e}^{-r(\boldsymbol{\theta})}\,\mathrm{e}^{-(n-1)(r(\boldsymbol{\theta})-r^*)}\,\mathrm{d}\boldsymbol{\theta} \\
&\leqslant \mathrm{e}^{-(n-1)r^*}\int_{\overline{\Theta}} g(\boldsymbol{\theta})\,\mathrm{e}^{-r(\boldsymbol{\theta})}\,\mathrm{e}^{-(n-1)c}\,\mathrm{d}\boldsymbol{\theta} \\
&\leqslant \mathrm{e}^{-(n-1)(r^*+c)}\int_{\mathbb{R}^p} g(\boldsymbol{\theta})\,\mathrm{e}^{-r(\boldsymbol{\theta})}\,\mathrm{d}\boldsymbol{\theta} = O(\mathrm{e}^{-n(r^*+c)}).
\end{aligned}$$

The last expression is of order $o(\mathrm{e}^{-nr^*}/n^{p/2})$, concluding the proof. $\square$
