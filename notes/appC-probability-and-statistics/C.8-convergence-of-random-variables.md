---
appendix: C
section: "C.8"
title: "Convergence of Random Variables"
pdf_pages: "457-463"
---

## C.8 Convergence of Random Variables

Recall that a random variable $X$ is a function from $\Omega$ to $\mathbb{R}$. If we have a sequence of random variables $X_1, X_2, \ldots$ (for instance, $X_n(\omega) = X(\omega) + \frac{1}{n}$ for each $\omega \in \Omega$), then one can consider the pointwise convergence:

$$\lim_{n\to\infty} X_n(\omega) = X(\omega), \quad \text{for all } \omega \in \Omega,$$

in which case we say that $X_1, X_2, \ldots$ *converges surely* to $X$. A more interesting type of convergence uses the probability measure $\mathbb{P}$ associated with $X$.

> **Definition C.1: Convergence in Probability**
>
> The sequence of random variables $X_1, X_2, \ldots$ *converges in probability* to a random variable $X$ if, for all $\varepsilon > 0$,
>
> $$\lim_{n\to\infty}\mathbb{P}[|X_n - X| > \varepsilon] = 0.$$
>
> We denote the *convergence in probability* as $X_n \xrightarrow{\ \mathbb{P}\ } X$.

Convergence in probability refers only to the distribution of $X_n$. Instead, if the sequence $X_1, X_2, \ldots$ is defined on a common probability space, then we can consider the following mode of convergence that uses the joint distribution of the sequence of random variables.

> **Definition C.2: Almost Sure Convergence**
>
> The sequence of random variables $X_1, X_2, \ldots$ *converges almost surely* to a random variable $X$ if for every $\varepsilon > 0$
>
> $$\lim_{n\to\infty}\mathbb{P}\Big[\sup_{k\geqslant n}|X_k - X| > \varepsilon\Big] = 0.$$
>
> We denote the *almost sure convergence* as $X_n \xrightarrow{\ \text{a.s.}\ } X$.

Note that in accordance with these definitions $X_n \xrightarrow{\text{a.s.}} 0$ is equivalent to $\sup_{k\geqslant n}|X_k| \xrightarrow{\ \mathbb{P}\ } 0$.

**Example C.3 (Convergence in Probability Versus Almost Sure Convergence).** Since the event $\{|X_n - X| > \varepsilon\}$ is contained in $\{\sup_{k\geqslant n}|X_k - X| > \varepsilon\}$, we can conclude that almost sure convergence implies convergence in probability. However, the converse is not true in general. For instance, consider the iid sequence $X_1, X_2, \ldots$ with marginal distribution

$$\mathbb{P}[X_n = 1] = 1 - \mathbb{P}[X_n = 0] = 1/n.$$

Clearly, $X_n \xrightarrow{\ \mathbb{P}\ } 0$. However, for $\varepsilon < 1$ and any $n = 1, 2, \ldots$ we have,

$$\begin{aligned}
\mathbb{P}\Big[\sup_{k\geqslant n}|X_k| \leqslant \varepsilon\Big] &= \mathbb{P}[X_n \leqslant \varepsilon, X_{n+1} \leqslant \varepsilon, \ldots] \\
&= \mathbb{P}[X_n \leqslant \varepsilon] \times \mathbb{P}[X_{n+1} \leqslant \varepsilon] \times \cdots \quad \text{(using independence)} \\
&= \lim_{m\to\infty}\prod_{k=n}^{m}\mathbb{P}[X_k \leqslant \varepsilon] = \lim_{m\to\infty}\prod_{k=n}^{m}\left(1 - \frac{1}{k}\right) \\
&= \lim_{m\to\infty}\frac{n-1}{n}\times\frac{n}{n+1}\times\cdots\times\frac{m-1}{m} = 0.
\end{aligned}$$

It follows that $\mathbb{P}[\sup_{k\geqslant n}|X_k - 0| > \varepsilon] = 1$ for any $0 < \varepsilon < 1$ and all $n \geqslant 1$. In other words, it is *not* true that $X_n \xrightarrow{\text{a.s.}} 0$. $\blacksquare$

Another important type of convergence is useful when we are interested in estimating expectations or multidimensional integrals via Monte Carlo methodology (see p.67).

> **Definition C.3: Convergence in Distribution**
>
> The sequence of random variables $X_1, X_2, \ldots$ is said to *converge in distribution* to a random variable $X$ with distribution function $F_X(x) = \mathbb{P}[X \leqslant x]$ provided that:
>
> $$\lim_{n\to\infty}\mathbb{P}[X_n \leqslant x] = F_X(x) \text{ for all } x \text{ such that } \lim_{a\to x}F_X(a) = F_X(x). \tag{C.33}$$
>
> We denote the *convergence in distribution* as either $X_n \xrightarrow{\ d\ } X$, or $X_n \xrightarrow{\ d\ } F_X$.

The generalization to random vectors replaces (C.33) with

$$\lim_{n\to\infty}\mathbb{P}[\boldsymbol{X}_n \in A] = \mathbb{P}[\boldsymbol{X}\in A] \text{ for all } A \subset \mathbb{R}^n \text{ such that } \mathbb{P}[\boldsymbol{X}\in\partial A] = 0, \tag{C.34}$$

where $\partial A$ denotes the boundary of the set $A$.

A useful tool for demonstrating convergence in distribution is the *characteristic function* $\psi_X$ of a random vector $\boldsymbol{X}$, defined as the expectation:

$$\psi_X(\boldsymbol{t}) := \mathbb{E}\,\mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{X}}, \quad \boldsymbol{t}\in\mathbb{R}^n. \tag{C.35}$$

The moment generating function in (C.5) (p.427) is a special case of the characteristic function evaluated at $t = -\mathrm{i}s$. Note that while the moment generating function of a random variable may not exist, its characteristic function always exists. The characteristic function of a random vector $\boldsymbol{X}\sim f$ is closely related to the Fourier transform of its pdf $f$ (see p.390).

**Example C.4 (Characteristic Function of a Multivariate Gaussian Random Vector).** The density of the multivariate standard normal distribution is given in (C.26) and thus the characteristic function of $\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},\mathbf{I}_n)$ is

$$\begin{aligned}
\psi_Z(\boldsymbol{t}) &= \mathbb{E}\,\mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{Z}} = (2\pi)^{-n/2}\int_{\mathbb{R}^n}\mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{z} - \frac{1}{2}\|\boldsymbol{z}\|^2}\,\mathrm{d}\boldsymbol{z} \\
&= \mathrm{e}^{-\|\boldsymbol{t}\|^2/2}(2\pi)^{-n/2}\int_{\mathbb{R}^n}\mathrm{e}^{-\frac{1}{2}\|\boldsymbol{z}-\mathrm{i}\boldsymbol{t}^\top\|^2}\,\mathrm{d}\boldsymbol{z} = \mathrm{e}^{-\|\boldsymbol{t}\|^2/2}, \quad \boldsymbol{t}\in\mathbb{R}^n.
\end{aligned}$$

Hence, the characteristic function of the random vector $\boldsymbol{X} = \boldsymbol{\mu} + \mathbf{B}\boldsymbol{Z}$ in (C.27) with multivariate normal distribution $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is given by (see p.435)

$$\begin{aligned}
\psi_X(\boldsymbol{t}) &= \mathbb{E}\,\mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{X}} = \mathbb{E}\,\mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top(\boldsymbol{\mu}+\mathbf{B}\boldsymbol{Z})} \\
&= \mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{\mu}}\,\mathbb{E}\,\mathrm{e}^{\mathrm{i}(\mathbf{B}^\top\boldsymbol{t})^\top\boldsymbol{Z}} = \mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{\mu}}\,\psi_Z(\mathbf{B}^\top\boldsymbol{t}) \\
&= \mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{\mu} - \|\mathbf{B}^\top\boldsymbol{t}\|^2/2} = \mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{\mu} - \boldsymbol{t}^\top\boldsymbol{\Sigma}\boldsymbol{t}/2}.
\end{aligned}$$
$\blacksquare$

The importance of the characteristic function is mainly derived from the following result, for which a proof can be found, for example, in [11].

> **Theorem C.12: Characteristic Function**
>
> Suppose that $\psi_{X_1}(\boldsymbol{t}), \psi_{X_2}(\boldsymbol{t}), \ldots$ are the characteristic functions of the sequence of random vectors $\boldsymbol{X}_1, \boldsymbol{X}_2, \ldots$ and $\psi_X(\boldsymbol{t})$ is the characteristic function of $\boldsymbol{X}$. Then, the following three statements are equivalent:
>
> 1. $\lim_{n\to\infty}\psi_{X_n}(\boldsymbol{t}) = \psi_X(\boldsymbol{t})$ for all $\boldsymbol{t}\in\mathbb{R}^n$.
> 2. $\boldsymbol{X}_n \xrightarrow{\ d\ } \boldsymbol{X}$.
> 3. $\lim_{n\to\infty}\mathbb{E}h(\boldsymbol{X}_n) = \mathbb{E}h(\boldsymbol{X})$ for all bounded continuous functions $h : \mathbb{R}^d \mapsto \mathbb{R}$.

**Example C.5 (Convergence in Distribution).** Define the random variables $Y_1, Y_2, \ldots$ as

$$Y_n := \sum_{k=1}^{n} X_k\left(\frac{1}{2}\right)^k, \quad n = 1, 2, \ldots,$$

where $X_1, X_2, \ldots \overset{\text{iid}}{\sim} \mathsf{Ber}(1/2)$. We now show that $Y_n \xrightarrow{\ d\ } \mathcal{U}(0,1)$. First, note that

$$\mathbb{E}\exp(\mathrm{i}tY_n) = \prod_{k=1}^{n}\mathbb{E}\exp(\mathrm{i}tX_k/2^k) = 2^{-n}\prod_{k=1}^{n}(1+\exp(\mathrm{i}t/2^k)).$$

Second, from the collapsing product, $(1-\exp(\mathrm{i}t/2^n))\prod_{k=1}^{n}(1+\exp(\mathrm{i}t/2^k)) = 1-\exp(\mathrm{i}t)$, we have

$$\mathbb{E}\exp(\mathrm{i}tY_n) = (1-\exp(\mathrm{i}t))\frac{1/2^n}{1-\exp(\mathrm{i}t/2^n)}.$$

It follows that $\lim_{n\to\infty}\mathbb{E}\exp(\mathrm{i}tY_n) = (\exp(\mathrm{i}t)-1)/(\mathrm{i}t)$, which we recognize as the characteristic function of the $\mathcal{U}(0,1)$ distribution. $\blacksquare$

Yet another mode of convergence is the following.

> **Definition C.4: Convergence in $L^p$-norm**
>
> The sequence of random variables $X_1, X_2, \ldots$ *converges in $L^p$-norm* to a random variable $X$ if
>
> $$\lim_{n\to\infty}\mathbb{E}|X_n - X|^p = 0, \quad p\geqslant 1.$$
>
> We denote the *convergence in $L^p$-norm* as $X_n \xrightarrow{\ L^p\ } X$.

The case for $p=2$ corresponds to convergence in mean squared error. The following example illustrates that convergence in $L^p$-norm is qualitatively different from convergence in distribution.

**Example C.6 (Comparison of Modes of Convergence).** Define $X_n := 1-X$, where $X$ has a uniform distribution on the interval $(0,1)$. Clearly, $X_n \xrightarrow{\ d\ } \mathcal{U}(0,1)$. However, $\mathbb{E}|X_n - X| \longrightarrow \mathbb{E}|1-2X| = 1/2$ and so the sequence does not converge in $L^1$-norm. In addition, $\mathbb{P}[|X_n-X|>\varepsilon] \longrightarrow 1-\varepsilon \neq 0$ and so $X_n$ does not converge in probability as well.

Thus, in general $X_n \xrightarrow{\ d\ } X$ implies neither $X_n \xrightarrow{\ \mathbb{P}\ } X$, nor $X_n \xrightarrow{\ L^1\ } X$.

We mention, however, that if $X_n \xrightarrow{\ d\ } c$ for some constant $c$, then $X_n \xrightarrow{\ \mathbb{P}\ } c$ as well. To see this, note that $X_n \xrightarrow{\ d\ } c$ stands for

$$\lim_{n\to\infty}\mathbb{P}[X_n\leqslant x] = \begin{cases}1, & x>c \\ 0, & x<c\end{cases}.$$

In other words, we can write:

$$\mathbb{P}[|X_n-c|>\varepsilon] \leqslant 1-\mathbb{P}[X_n\leqslant c+\varepsilon] + \mathbb{P}[X_n\leqslant c-\varepsilon] \longrightarrow 1-1+0 = 0, \quad n\to\infty,$$

which shows that $X_n \xrightarrow{\ \mathbb{P}\ } c$ by definition. $\blacksquare$

> **Definition C.5: Complete Convergence**
>
> The sequence of random variables $X_1, X_2, \ldots$ is said to *converge completely* to $X$ if for all $\varepsilon > 0$
>
> $$\sum_n \mathbb{P}[|X_n-X|>\varepsilon] < \infty.$$
>
> We denote the *complete convergence* as $X_n \xrightarrow{\ \text{cpl.}\ } X$.

**Example C.7 (Complete and Almost Sure Convergence).** We show that complete convergence implies almost sure convergence. We can bound the criterion for almost sure convergence as follows:

$$\begin{aligned}
\mathbb{P}\Big[\sup_{k\geqslant n}|X_k-X|>\varepsilon\Big] &= \mathbb{P}[\cup_{k\geqslant n}\{|X_k-X|>\varepsilon\}] \\
&\leqslant \sum_{k\geqslant n}\mathbb{P}[|X_k-X|>\varepsilon] \quad \text{by union bound in (C.1)} \\
&\leqslant \underbrace{\sum_{k=1}^{\infty}\mathbb{P}[|X_k-X|>\varepsilon]}_{=c<\infty \text{ from } X_n\xrightarrow{\text{cpl.}}X} - \sum_{k=1}^{n-1}\mathbb{P}[|X_k-X|>\varepsilon] \\
&\leqslant c - \sum_{k=1}^{n-1}\mathbb{P}[|X_k-X|>\varepsilon] \longrightarrow c-c=0, \quad n\to\infty.
\end{aligned}$$

Hence, by definition $X_n \xrightarrow{\text{a.s.}} X$. $\blacksquare$

The next theorem shows how the different types of convergence are related to each other. For example, in the diagram below, the notation $\overset{p\geqslant q}{\Rightarrow}$ means that $L^p$-norm convergence implies $L^q$-norm convergence under the assumption that $p \geqslant q \geqslant 1$.

> **Theorem C.13: Modes of Convergence**
>
> The most general relationships among the various modes of convergence for numerical random variables are shown on the following hierarchical diagram:
>
> $$\boxed{X_n \xrightarrow{\text{cpl.}} X} \Rightarrow \boxed{X_n \xrightarrow{\text{a.s.}} X} \Downarrow$$
> $$\boxed{X_n \xrightarrow{\ \mathbb{P}\ } X} \Rightarrow \boxed{X_n \xrightarrow{\ d\ } X}$$
> $$\Uparrow$$
> $$\boxed{X_n \xrightarrow{\ L^p\ } X} \overset{p\geqslant q}{\Rightarrow} \boxed{X_n \xrightarrow{\ L^q\ } X}$$
>
> (Reading: complete convergence $\Rightarrow$ almost sure convergence $\Rightarrow$ convergence in probability $\Rightarrow$ convergence in distribution; and $L^p$-norm convergence $\Rightarrow$ convergence in probability, with $L^p \Rightarrow L^q$ for $p \geqslant q \geqslant 1$.)

*Proof:* **1.** First, we show that $X_n \xrightarrow{\ \mathbb{P}\ } X \Rightarrow X_n \xrightarrow{\ d\ } X$ using the inequality $\mathbb{P}[A\cap B]\leqslant\mathbb{P}[A]$ for any event $B$. To this end, consider the distribution function $F_{X_n}$ of $X_n$:

$$\begin{aligned}
F_{X_n}(x) &= \mathbb{P}[X_n\leqslant x] = \mathbb{P}[X_n\leqslant x, |X_n-X|>\varepsilon] + \mathbb{P}[X_n\leqslant x, |X_n-X|\leqslant\varepsilon] \\
&\leqslant \mathbb{P}[|X_n-X|>\varepsilon] + \mathbb{P}[X_n\leqslant x, X\leqslant X_n+\varepsilon] \\
&\leqslant \mathbb{P}[|X_n-X|>\varepsilon] + \mathbb{P}[X\leqslant x+\varepsilon].
\end{aligned}$$

Now, in the arguments above we can switch the roles of $X_n$ and $X$ (there is a symmetry) to deduce the analogous result: $F_X(x)\leqslant\mathbb{P}[|X-X_n|>\varepsilon]+\mathbb{P}[X_n\leqslant x+\varepsilon]$. Therefore, making the switch $x\to x-\varepsilon$ gives $F_X(x-\varepsilon)\leqslant\mathbb{P}[|X-X_n|>\varepsilon]+F_{X_n}(x)$. Putting it all together gives:

$$F_X(x-\varepsilon) - \mathbb{P}[|X-X_n|>\varepsilon] \leqslant F_{X_n}(x) \leqslant \mathbb{P}[|X_n-X|>\varepsilon] + F_X(x+\varepsilon).$$

Taking $n\to\infty$ on both sides yields for any $\varepsilon>0$:

$$F_X(x-\varepsilon) \leqslant \lim_{n\to\infty}F_{X_n}(x) \leqslant F_X(x+\varepsilon).$$

Since $F_X$ is continuous at $x$ by assumption we can take $\varepsilon\downarrow0$ to conclude that $\lim_{n\to\infty}F_{X_n}(x)=F_X(x)$.

**2.** Second, we show that $X_n \xrightarrow{\ L^p\ } X \Rightarrow X_n \xrightarrow{\ L^q\ } X$ for $p\geqslant q\geqslant1$. Since the function $f(x)=x^{q/p}$ is concave for $q/p\leqslant1$, Jensen's inequality (see p.63) yields:

$$(\mathbb{E}|X|^p)^{q/p} = f(\mathbb{E}|X|^p) \geqslant \mathbb{E}f(|X|^p) = \mathbb{E}|X|^q.$$

In other words, $(\mathbb{E}|X_n-X|^q)^{1/q} \leqslant (\mathbb{E}|X_n-X|^p)^{1/p} \longrightarrow 0$, proving the statement of the theorem.

**3.** Third, we show that $X_n \xrightarrow{\ L^1\ } X \Rightarrow X_n \xrightarrow{\ \mathbb{P}\ } X$. First note that for any random variable $Y$, we can write: $\mathbb{E}|Y| \geqslant \mathbb{E}[|Y|\mathbb{1}_{\{|Y|>\varepsilon\}}] \geqslant \mathbb{E}[\varepsilon\,\mathbb{1}_{\{|Y|>\varepsilon\}}] = \varepsilon\,\mathbb{P}[|Y|>\varepsilon]$. Therefore, we obtain *Chebyshev's inequality*:

$$\mathbb{P}[|Y|>\varepsilon] \leqslant \frac{\mathbb{E}|Y|}{\varepsilon}. \tag{C.36}$$

Using Chebyshev's inequality and $X_n \xrightarrow{\ L^1\ } X$, we can write

$$\mathbb{P}[|X_n-X|>\varepsilon] \leqslant \frac{\mathbb{E}|X_n-X|}{\varepsilon} \longrightarrow 0, \quad n\to\infty.$$

Hence, by definition $X_n \xrightarrow{\ \mathbb{P}\ } X$.

**4.** Finally, $X_n \xrightarrow{\text{cpl.}} X \Rightarrow X_n \xrightarrow{\text{a.s.}} X \Rightarrow X_n \xrightarrow{\ \mathbb{P}\ } X$ is proved in Examples C.7 and C.3. $\square$

Finally, we will make use of the following theorem.

> **Theorem C.14: Slutsky**
>
> Let $g(\boldsymbol{x}, \boldsymbol{y})$ be a continuous scalar function of vectors $\boldsymbol{x}$ and $\boldsymbol{y}$. Suppose that $X_n \xrightarrow{\ d\ } X$ and $Y_n \xrightarrow{\ \mathbb{P}\ } c$ for some finite constant $c$. Then,
>
> $$g(X_n, Y_n) \xrightarrow{\ d\ } g(X, c).$$

*Proof:* We prove the theorem for scalar $X$ and $Y$. The proof for random vectors is analogous. First, we show that $\boldsymbol{Z}_n := \begin{bmatrix}X_n\\Y_n\end{bmatrix} \xrightarrow{\ d\ } \begin{bmatrix}X\\c\end{bmatrix} =: \boldsymbol{Z}$ using, for example, Theorem C.12 (p.441). In other words, we wish to show that the characteristic function of the joint distribution of $X_n$ and $Y_n$ converges pointwise as $n\to\infty$:

$$\psi_{X_n,Y_n}(\boldsymbol{t}) = \mathbb{E}\,\mathrm{e}^{\mathrm{i}(t_1X_n+t_2Y_n)} \longrightarrow \mathrm{e}^{\mathrm{i}t_2c}\,\mathbb{E}\,\mathrm{e}^{\mathrm{i}t_1X} = \psi_{X,c}(\boldsymbol{t}), \quad \forall\boldsymbol{t}\in\mathbb{R}^2.$$

To show the limit above, consider

$$\begin{aligned}
|\psi_{X_n,Y_n}(\boldsymbol{t}) - \psi_{X,c}(\boldsymbol{t})| &\leqslant |\psi_{X_n,c}(\boldsymbol{t})-\psi_{X,c}(\boldsymbol{t})| + |\psi_{X_n,Y_n}(\boldsymbol{t})-\psi_{X_n,c}(\boldsymbol{t})| \\
&= |\mathrm{e}^{\mathrm{i}t_2c}\,\mathbb{E}(\mathrm{e}^{\mathrm{i}t_1X_n}-\mathrm{e}^{\mathrm{i}t_1X})| + |\mathbb{E}\,\mathrm{e}^{\mathrm{i}(t_1X_n+t_2c)}(\mathrm{e}^{\mathrm{i}t_2(Y_n-c)}-1)| \\
&\leqslant |\mathrm{e}^{\mathrm{i}t_2c}|\times|\mathbb{E}(\mathrm{e}^{\mathrm{i}t_1X_n}-\mathrm{e}^{\mathrm{i}t_1X})| + \mathbb{E}|\mathrm{e}^{\mathrm{i}(t_1X_n+t_2c)}|\times|\mathrm{e}^{\mathrm{i}t_2(Y_n-c)}-1| \\
&\leqslant |\psi_{X_n}(t_1)-\psi_X(t_1)| + \mathbb{E}|\mathrm{e}^{\mathrm{i}t_2(Y_n-c)}-1|.
\end{aligned}$$

Since $X_n \xrightarrow{\ d\ } X$, Theorem C.12 implies that $\psi_{X_n}(t_1) \longrightarrow \psi_X(t_1)$, and the first term $|\psi_{X_n}(t_1)-\psi_X(t_1)|$ goes to zero. For the second term we use the fact that

$$|\mathrm{e}^{\mathrm{i}x}-1| = \left|\int_0^x \mathrm{i}\,\mathrm{e}^{\mathrm{i}\theta}\,\mathrm{d}\theta\right| \leqslant \left|\int_0^x |\mathrm{i}\,\mathrm{e}^{\mathrm{i}\theta}|\,\mathrm{d}\theta\right| = |x|, \quad x\in\mathbb{R}$$

to obtain the bound:

$$\begin{aligned}
\mathbb{E}|\mathrm{e}^{\mathrm{i}t_2(Y_n-c)}-1| &= \mathbb{E}|\mathrm{e}^{\mathrm{i}t_2(Y_n-c)}-1|\mathbb{1}_{\{|Y_n-c|>\varepsilon\}} + \mathbb{E}|\mathrm{e}^{\mathrm{i}t_2(Y_n-c)}-1|\mathbb{1}_{\{|Y_n-c|\leqslant\varepsilon\}} \\
&\leqslant 2\,\mathbb{E}\,\mathbb{1}_{\{|Y_n-c|>\varepsilon\}} + \mathbb{E}|t_2(Y_n-c)|\mathbb{1}_{\{|Y_n-c|\leqslant\varepsilon\}} \\
&\leqslant 2\,\mathbb{P}[|Y_n-c|>\varepsilon] + |t_2|\varepsilon \longrightarrow |t_2|\varepsilon, \quad n\to\infty.
\end{aligned}$$

Since $\varepsilon$ is arbitrary, we can let $\varepsilon\downarrow0$ to conclude that $\lim_{n\to\infty}|\psi_{X_n,Y_n}(\boldsymbol{t})-\psi_{X,c}(\boldsymbol{t})|=0$. In other words, $\boldsymbol{Z}_n \xrightarrow{\ d\ } \boldsymbol{Z}$, and by the continuity of $g$, we have $g(\boldsymbol{Z}_n)\xrightarrow{\ d\ }g(\boldsymbol{Z})$ or $g(X_n,Y_n)\xrightarrow{\ d\ }g(X,c)$. $\square$

**Example C.8 (Necessity of Slutsky's Condition).** The condition that $Y_n$ converges in probability to a constant cannot be relaxed. For example, suppose that $g(x,y) = x+y$, $X_n \xrightarrow{\ d\ } X \sim \mathcal{N}(0,1)$ and $Y_n \xrightarrow{\ d\ } Y \sim \mathcal{N}(0,1)$. Then, our intuition tempts us to *incorrectly* conclude that $X_n+Y_n \xrightarrow{\ d\ } \mathcal{N}(0,2)$. This intuition is false, because we can have $Y_n = -X_n$ for all $n$ so that $X_n+Y_n=0$, while both $X$ and $Y$ have the same marginal distribution (in this case standard normal). $\blacksquare$
