---
chapter: 3
section: "Exercises"
title: "Exercises"
pdf_pages: "132-138"
---

# Exercises

1. We can modify the Box–Muller method in Example 3.1 to draw $X$ and $Y$ uniformly on the unit disc, $\{(x,y) \in \mathbb{R}^2 : x^2+y^2 \le 1\}$, in the following way: Independently draw a radius $R$ and an angle $\Theta \sim \mathcal{U}(0,2\pi)$, and return $X = R\cos(\Theta)$, $Y = R\sin(\Theta)$. The question is how to draw $R$.

   (a) Show that the cdf of $R$ is given by $F_R(r) = r^2$ for $0 \le r \le 1$ (with $F_R(r)=0$ and $F_R(r)=1$ for $r<0$ and $r>1$, respectively).

   (b) Explain how to simulate $R$ using the inverse-transform method.

   (c) Simulate 100 independent draws of $[X,Y]^\top$ according to the method described above.

2. A simple acceptance–rejection method to simulate a vector $\boldsymbol{X}$ in the unit $d$-ball $\{\boldsymbol{x} \in \mathbb{R}^d : \|\boldsymbol{x}\| \le 1\}$ is to first generate $\boldsymbol{X}$ uniformly in the hyper cube $[-1,1]^d$ and then to accept the point only if $\|\boldsymbol{X}\| \le 1$. Determine an analytic expression for the probability of acceptance as a function of $d$ and plot this for $d = 1, \ldots, 50$.

3. Let the random variable $X$ have pdf

$$
f(x) = \begin{cases} \frac{1}{2}x, & 0 \le x < 1, \\ \frac{1}{2}, & 1 \le x \le \frac{5}{2}. \end{cases}
$$

   Simulate a random variable from $f(x)$, using

   (a) the inverse-transform method;

   (b) the acceptance–rejection method, using the proposal density

   $$
   g(x) = \frac{8}{25}x, \quad 0 \le x \le \frac{5}{2}.
   $$

4. Construct simulation algorithms for the following distributions:

   (a) The $\mathrm{Weib}(\alpha,\lambda)$ distribution, with cdf $F(x) = 1 - \mathrm{e}^{-(\lambda x)^\alpha}$, $x \ge 0$, where $\lambda > 0$ and $\alpha > 0$.

   (b) The $\mathrm{Pareto}(\alpha,\lambda)$ distribution, with pdf $f(x) = \alpha\lambda(1+\lambda x)^{-(\alpha+1)}$, $x \ge 0$, where $\lambda > 0$ and $\alpha > 0$.

5. We wish to sample from the pdf

$$
f(x) = x\,\mathrm{e}^{-x}, \quad x \ge 0,
$$

   using acceptance–rejection with the proposal pdf $g(x) = \mathrm{e}^{-x/2}/2$, $x \ge 0$.

   (a) Find the smallest $C$ for which $Cg(x) \ge f(x)$ for all $x$.

   (b) What is the efficiency of this acceptance–rejection method?

6. Let $[X,Y]^\top$ be uniformly distributed on the triangle with corners $(0,0), (1,2)$, and $(-1,1)$. Give the distribution of $[U,V]^\top$ defined by the linear transformation

$$
\begin{bmatrix} U \\ V \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} X \\ Y \end{bmatrix}.
$$

7. Explain how to generate a random variable from the *extreme value distribution*, which has cdf

$$
F(x) = 1 - \mathrm{e}^{-\exp\left(\frac{x-\mu}{\sigma}\right)}, \quad -\infty < x < \infty, \quad (\sigma > 0),
$$

   via the inverse-transform method.

8. Write a program that generates and displays 100 random vectors that are uniformly distributed within the ellipse

$$
5x^2 + 21xy + 25y^2 = 9.
$$

   [Hint: Consider generating uniformly distributed samples within the circle of radius 3 and use the fact that linear transformations preserve uniformity to transform the circle to the given ellipse.]

9. Suppose that $X_i \sim \mathrm{Exp}(\lambda_i)$, independently, for all $i = 1, \ldots, n$. Let $\boldsymbol{\Pi} = [\Pi_1,\ldots,\Pi_n]^\top$ be the random permutation induced by the ordering $X_{\Pi_1} < X_{\Pi_2} < \cdots < X_{\Pi_n}$, and define $Z_1 := X_{\Pi_1}$ and $Z_j := X_{\Pi_j} - X_{\Pi_{j-1}}$ for $j = 2, \ldots, n$.

   (a) Determine an $n \times n$ matrix $\boldsymbol{A}$ such that $\boldsymbol{Z} = \boldsymbol{A}\boldsymbol{X}$ and show that $\det(\boldsymbol{A}) = 1$.

   (b) Denote the joint pdf of $\boldsymbol{X}$ and $\boldsymbol{\Pi}$ as

   $$
   f_{\boldsymbol{X},\boldsymbol{\Pi}}(\boldsymbol{x},\boldsymbol{\pi}) = \prod_{i=1}^n \lambda_{\pi_i} \exp(-\lambda_{\pi_i} x_{\pi_i}) \times \mathbb{1}\{x_{\pi_1} < \cdots < x_{\pi_n}\}, \quad \boldsymbol{x} \ge \boldsymbol{0}, \ \boldsymbol{\pi} \in \mathcal{P}_n,
   $$

   where $\mathcal{P}_n$ is the set of all $n!$ permutations of $\{1,\ldots,n\}$. Use the multivariate transformation formula (C.22) to show that

   $$
   f_{\boldsymbol{Z},\boldsymbol{\Pi}}(\boldsymbol{z},\boldsymbol{\pi}) = \exp\left(-\sum_{i=1}^n z_i \sum_{k \ge i} \lambda_{\pi_k}\right)\prod_{i=1}^n \lambda_i, \quad \boldsymbol{z} \ge \boldsymbol{0}, \ \boldsymbol{\pi} \in \mathcal{P}_n.
   $$

   Hence, conclude that the probability mass function of the random permutation $\boldsymbol{\Pi}$ is:

   $$
   \mathbb{P}[\boldsymbol{\Pi} = \boldsymbol{\pi}] = \prod_{i=1}^n \frac{\lambda_{\pi_i}}{\sum_{k \ge i}\lambda_{\pi_k}}, \quad \boldsymbol{\pi} \in \mathcal{P}_n.
   $$

   (c) Write pseudo-code to simulate a *uniform* random permutation $\boldsymbol{\Pi} \in \mathcal{P}_n$; that is, such that $\mathbb{P}[\boldsymbol{\Pi}=\boldsymbol{\pi}] = \frac{1}{n!}$, and explain how this uniform random permutation can be used to reshuffle a training set $\tau_n$.

10. Consider the Markov chain with transition graph given in Figure 3.17, starting in state 1.

> **Figure 3.17:** The transition graph for the Markov chain $\{X_t, t=0,1,2,\ldots\}$ — six states (1 through 6, with state 1 marked "Start") connected by directed edges with transition probabilities: $1\to2$: 0.2, $2\to1$: 0.5, $2\to3$: 0.5, $3\to1$: 0.3, $3\to4$: 0.7, $1\to4$: 0.3, $4\to6$: 1, $4\to5$: (implied via other edges), $6\to3$: 0.1, $6\to5$: 0.2, $5\to6$: 0.9, $5\to1$: 0.5, $5\to4$: 0.8 (exact full edge list as depicted in the diagram).

    (a) Construct a computer program to simulate the Markov chain, and show a realization for $N = 100$ steps.

    (b) Compute the limiting probabilities that the Markov chain is in state $1,2,\ldots,6$, by solving the global balance equations (C.42).

    (c) Verify that the exact limiting probabilities correspond to the average fraction of times that the Markov process visits states $1,2,\ldots,6$, for a large number of steps $N$.

11. As a generalization of Example C.9, consider a random walk on an arbitrary undirected connected graph with a finite vertex set $\mathcal{V}$. For any vertex $v \in \mathcal{V}$, let $d(v)$ be the number of neighbors of $v$ — called the *degree* of $v$. The random walk can jump to each one of the neighbors with probability $1/d(v)$ and can be described by a Markov chain. Show that, if the chain is *aperiodic*, the limiting probability that the chain is in state $v$ is equal to $d(v)/\sum_{v' \in \mathcal{V}} d(v')$.

12. Let $U, V \sim_{\text{iid}} \mathcal{U}(0,1)$. The reason why in Example 3.7 the sample mean and sample median behave very differently is that $\mathbb{E}[U/V] = \infty$, while the median of $U/V$ is finite. Show this, and compute the median. [Hint: start by determining the cdf of $Z = U/V$ by writing it as an expectation of an indicator function.]

13. Consider the problem of generating samples from $Y \sim \mathrm{Gamma}(2,10)$.

    (a) Direct simulation: Let $U_1, U_2 \sim_{\text{iid}} \mathcal{U}(0,1)$. Show that $-\ln(U_1)/10 - \ln(U_2)/10 \sim \mathrm{Gamma}(2,10)$. [Hint: derive the distribution of $-\ln(U_1)/10$ and use Example C.1.]

    (b) Simulation via MCMC: Implement an independence sampler to simulate from the $\mathrm{Gamma}(2,10)$ target pdf

    $$
    f(x) = 100\,x\,\mathrm{e}^{-10x}, \quad x \ge 0,
    $$

    using proposal transition density $q(y\mid x) = g(y)$, where $g(y)$ is the pdf of an $\mathrm{Exp}(5)$ random variable. Generate $N = 500$ samples, and compare the true cdf with the empirical cdf of the data.

14. Let $\boldsymbol{X} = [X,Y]^\top$ be a random column vector with a bivariate normal distribution with expectation vector $\boldsymbol{\mu} = [1,2]^\top$ and covariance matrix

$$
\boldsymbol{\Sigma} = \begin{bmatrix} 1 & a \\ a & 4 \end{bmatrix}.
$$

    (a) What are the conditional distributions of $(Y\mid X=x)$ and $(X\mid Y=y)$? [Hint: use Theorem C.8.]

    (b) Implement a Gibbs sampler to draw $10^3$ samples from the bivariate distribution $\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma})$ for $a = 0, 1$, and $1.75$, and plot the resulting samples.

15. Here the objective is to sample from the 2-dimensional pdf

$$
f(x,y) = c\,\mathrm{e}^{-(xy+x+y)}, \quad x \ge 0, \quad y \ge 0,
$$

    for some normalization constant $c$, using a Gibbs sampler. Let $(X,Y) \sim f$.

    (a) Find the conditional pdf of $X$ given $Y=y$, and the conditional pdf of $Y$ given $X=x$.

    (b) Write working Python code that implements the Gibbs sampler and outputs 1000 points that are approximately distributed according to $f$.

    (c) Describe how the normalization constant $c$ could be estimated via Monte Carlo simulation, using random variables $X_1,\ldots,X_N,Y_1,\ldots,Y_N \overset{\text{iid}}{\sim} \mathrm{Exp}(1)$.

16. We wish to estimate $\mu = \int_{-2}^{2} \mathrm{e}^{-x^2/2}\, dx = \int H(x) f(x)\, dx$ via Monte Carlo simulation using two different approaches: (1) defining $H(x) = 4\mathrm{e}^{-x^2/2}$ and $f$ the pdf of the $\mathcal{U}[-2,2]$ distribution and (2) defining $H(x) = \sqrt{2\pi}\,\mathbb{1}\{-2 \le x \le 2\}$ and $f$ the pdf of the $\mathcal{N}(0,1)$ distribution.

    (a) For both cases estimate $\mu$ via the estimator $\widehat{\mu}$

    $$
    \widehat{\mu} = N^{-1}\sum_{i=1}^N H(X_i). \tag{3.34}
    $$

    Use a sample size of $N = 1000$.

    (b) For both cases estimate the relative error $\kappa$ of $\widehat{\mu}$ using $N = 100$.

    (c) Give a 95% confidence interval for $\mu$ for both cases using $N = 100$.

    (d) From part (b), assess how large $N$ should be such that the relative width of the confidence interval is less than 0.01, and carry out the simulation with this $N$. Compare the result with the true value of $\mu$.

17. Consider estimation of the tail probability $\mu = \mathbb{P}[X \ge \gamma]$ of some random variable $X$, where $\gamma$ is large. The crude Monte Carlo estimator of $\mu$ is

$$
\widehat{\mu} = \frac{1}{N}\sum_{i=1}^N Z_i, \tag{3.35}
$$

    where $X_1,\ldots,X_N$ are iid copies of $X$ and $Z_i = \mathbb{1}\{X_i \ge \gamma\}$, $i = 1,\ldots,N$.

    (a) Show that $\widehat{\mu}$ is unbiased; that is, $\mathbb{E}\widehat{\mu} = \mu$.

    (b) Express the relative error of $\widehat{\mu}$, i.e.,

    $$
    \mathrm{RE} = \frac{\sqrt{\mathbb{V}\mathrm{ar}\,\widehat{\mu}}}{\mathbb{E}\widehat{\mu}},
    $$

    in terms of $N$ and $\mu$.

    (c) Explain how to estimate the relative error of $\widehat{\mu}$ from outcomes $x_1,\ldots,x_N$ of $X_1,\ldots,X_N$, and how to construct a 95% confidence interval for $\mu$.

    (d) An unbiased estimator $Z$ of $\mu$ is said to be *logarithmically efficient* if

    $$
    \lim_{\gamma\to\infty} \frac{\ln \mathbb{E}Z^2}{\ln \mu^2} = 1. \tag{3.36}
    $$

    Show that the CMC estimator (3.35) with $N=1$ is not logarithmically efficient.

18. One of the test cases in [70] involves the minimization of the *Hougen* function. Implement a cross-entropy and a simulated annealing algorithm to carry out this optimization task.

19. In the *binary knapsack problem*, the goal is to solve the optimization problem:

$$
\max_{\boldsymbol{x}\in\{0,1\}^n} \boldsymbol{p}^\top \boldsymbol{x},
$$

    subject to the constraints

    $$
    \boldsymbol{A}\boldsymbol{x} \le \boldsymbol{c},
    $$

    where $\boldsymbol{p}$ and $\boldsymbol{w}$ are $n \times 1$ vectors of non-negative numbers, $\boldsymbol{A} = (a_{ij})$ is an $m \times n$ matrix, and $\boldsymbol{c}$ is an $m \times 1$ vector. The interpretation is that $x_j = 1$ or $0$ depending on whether item $j$ with value $p_j$ is packed into the knapsack or not, $j = 1,\ldots,n$; The variable $a_{ij}$ represents the $i$-th attribute (e.g., volume, weight) of the $j$-th item. Associated with each attribute is a maximal capacity, e.g., $c_1$ could be the maximum volume of the knapsack, $c_2$ the maximum weight, etc.

    Write a CE program to solve the `Sento1.dat` knapsack problem at http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/mknap2.txt, as described in [16].

20. Let $(C_1,R_1),(C_2,R_2),\ldots$ be a renewal reward process, with $\mathbb{E}R_1 < \infty$ and $\mathbb{E}C_1 < \infty$. Let $A_t = \sum_{i=1}^{N_t} R_i/t$ be the average reward at time $t = 1,2,\ldots$, where $N_t = \max\{n : T_n \le t\}$ and we have defined $T_n = \sum_{i=1}^n C_i$ as the time of the $n$-th renewal.

    (a) Show that $T_n/n \overset{\text{a.s.}}{\longrightarrow} \mathbb{E}C_1$ as $n \to \infty$.

    (b) Show that $N_t \overset{\text{a.s.}}{\longrightarrow} \infty$ as $t \to \infty$.

    (c) Show that $N_t/t \overset{\text{a.s.}}{\longrightarrow} 1/\mathbb{E}C_1$ as $t \to \infty$. [Hint: Use the fact that $T_{N_t} \le t \le T_{N_t+1}$ for all $t = 1,2,\ldots$.]

    (d) Show that

    $$
    A_t \overset{\text{a.s.}}{\longrightarrow} \frac{\mathbb{E}R_1}{\mathbb{E}C_1} \quad \text{as} \quad t \to \infty.
    $$

21. Prove Theorem 3.3.

22. Prove that if $H(\boldsymbol{x}) \ge 0$ the importance sampling pdf $g^*$ in (3.22) gives the zero-variance importance sampling estimator $\widehat{\mu} = \mu$.

23. Let $X$ and $Y$ be random variables (not necessarily independent) and suppose we wish to estimate the expected difference $\mu = \mathbb{E}[X-Y] = \mathbb{E}X - \mathbb{E}Y$.

    (a) Show that if $X$ and $Y$ are *positively correlated*, the variance of $X-Y$ is smaller than if $X$ and $Y$ are *independent*.

    (b) Suppose now that $X$ and $Y$ have cdfs $F$ and $G$, respectively, and are simulated via the inverse-transform method: $X = F^{-1}(U)$, $Y = G^{-1}(V)$, with $U, V \sim \mathcal{U}(0,1)$, not necessarily independent. Intuitively, one might expect that if $U$ and $V$ are positively correlated, the variance of $X-Y$ would be smaller than if $U$ and $V$ are independent. Show that this is not always the case by providing a counter-example.

    (c) Continuing (b), assume now that $F$ and $G$ are continuous. Show that the variance of $X-Y$ by taking *common random numbers* $U=V$ is no larger than when $U$ and $V$ are independent. [Hint: Use the following lemma of Hoeffding [41]: If $(X,Y)$ have joint cdf $H$ with marginal cdfs of $X$ and $Y$ being $F$ and $G$, respectively, then

    $$
    \mathbb{C}\mathrm{ov}(X,Y) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} (H(x,y) - F(x)G(y))\, dx\, dy,
    $$

    provided $\mathbb{C}\mathrm{ov}(X,Y)$ exists.]
