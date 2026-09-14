---
appendix: C
section: "C.14"
title: "Hypothesis Testing"
pdf_pages: "476-480"
---

## C.14 Hypothesis Testing

Suppose the model for the data $\mathcal{T}$ is described by a family of probability distributions that depend on a parameter $\theta\in\Theta$. The aim of *hypothesis testing* is to decide, on the basis of the observed data $\tau$, which of two competing hypotheses holds true; these being the *null hypothesis*, $H_0: \theta\in\Theta_0$, and the *alternative hypothesis*, $H_1: \theta\in\Theta_1$.

In classical statistics the null hypothesis and alternative hypothesis do not play equivalent roles. $H_0$ contains the "status quo" statement and is only rejected if the observed data are very unlikely to have happened under $H_0$.

The decision whether to accept or reject $H_0$ is dependent on the outcome of a *test statistic* $\boldsymbol{T} = \boldsymbol{T}(\mathcal{T})$. For simplicity, we discuss only the one-dimensional case $\boldsymbol{T}\equiv T$. Two (related) types of decision rules are generally used:

1. **Decision rule 1**: *Reject $H_0$ if $T$ falls in the critical region.*

   Here the *critical region* is any appropriately chosen region in $\mathbb{R}$. In practice a critical region is one of the following:

   - *left one-sided*: $(-\infty, c]$,
   - *right one-sided*: $[c,\infty)$,
   - *two-sided*: $(-\infty,c_1]\cup[c_2,\infty)$.

   For example, for a right one-sided test, $H_0$ is rejected if the outcome of the test statistic is too large. The endpoints $c$, $c_1$, and $c_2$ of the critical regions are called *critical values*.

2. **Decision rule 2**: *Reject $H_0$ if the* P-value *is smaller than some significance level $\alpha$.*

   The *P-value* is the probability that, under $H_0$, the (random) test statistic takes a value as extreme as or more extreme than the one observed. In particular, if $t$ is the observed outcome of the test statistic $T$, then

   - *left one-sided test*: $P := \mathbb{P}_{H_0}[T\leqslant t]$,
   - *right one-sided*: $P := \mathbb{P}_{H_0}[T\geqslant t]$,
   - *two-sided*: $P := \min\{2\,\mathbb{P}_{H_0}[T\leqslant t],\ 2\,\mathbb{P}_{H_0}[T\geqslant t]\}$.

   The smaller the P-value, the greater the strength of the evidence against $H_0$ provided by the data. As a rule of thumb:

   $$
   \begin{aligned}
   P < 0.10 &\quad \text{suggestive evidence,} \\
   P < 0.05 &\quad \text{reasonable evidence,} \\
   P < 0.01 &\quad \text{strong evidence.}
   \end{aligned}
   $$

Whether the first or the second decision rule is used, one can make two types of errors, as depicted in Table C.4.

**Table C.4: Type I and II errors in hypothesis testing.**

| Decision | True statement: $H_0$ is true | True statement: $H_1$ is true |
|---|---|---|
| Accept $H_0$ | Correct | Type II Error |
| Reject $H_0$ | Type I Error | Correct |

The choice of the test statistic and the corresponding critical region involves a multiobjective optimization criterion, whereby both the probabilities of a type I and type II error should, ideally, be chosen as small as possible. Unfortunately, these probabilities compete with each other. For example, if the critical region is made larger (smaller), the probability of a type II error is reduced (increased), but at the same time the probability of a type I error is increased (reduced).

Since the type I error is considered more serious, Neyman and Pearson [93] suggested the following approach: choose the critical region such that the probability of a type II error is as small as possible, while keeping the probability of a type I error below a predetermined small *significance level $\alpha$*.

**Remark C.3 (Equivalence of Decision Rules).** Note that decision rule 1 and 2 are equivalent in the following sense:

$$\text{Reject } H_0 \text{ if } T \text{ falls in the critical region, at significance level } \alpha.$$
$$\Leftrightarrow$$
$$\text{Reject } H_0 \text{ if the P-value is} \leqslant \text{significance level } \alpha.$$

In other words, the P-value of the test is the smallest level of significance that would lead to the rejection of $H_0$. $\blacksquare$

> In general, a statistical test involves the following steps:
>
> 1. Formulate an appropriate statistical model for the data.
> 2. Give the null ($H_0$) and alternative ($H_1$) hypotheses in terms of the parameters of the model.
> 3. Determine the test statistic (a function of the data only).
> 4. Determine the (approximate) distribution of the test statistic under $H_0$.
> 5. Calculate the outcome of the test statistic.
> 6. Calculate the P-value *or* the critical region, given a preselected significance level $\alpha$.
> 7. Accept or reject $H_0$.

The actual choice of an appropriate test statistic is akin to selecting a good estimator for the unknown parameter $\theta$. The test statistic should summarize the information about $\theta$ and make it possible to distinguish between the alternative hypotheses.

**Example C.15 (Hypothesis Testing).** We are given outcomes $x_1,\ldots,x_m$ and $y_1,\ldots,y_n$ of two simulation studies obtained via independent runs, with $m=100$ and $n=50$. The sample means and standard deviations are $\overline{x} = 1.3$, $s_X = 0.1$ and $\overline{y} = 1.5$, $s_Y = 0.3$. Thus, the $\{x_i\}$ are outcomes of iid random variables $\{X_i\}$, the $\{y_i\}$ are outcomes of iid random variables $\{Y_i\}$, and the $\{X_i\}$ and $\{Y_i\}$ are independent. We wish to assess whether the expectations $\mu_X = \mathbb{E}X_i$ and $\mu_Y = \mathbb{E}Y_i$ are the same or not. Going through the 7 steps above, we have:

1. The model is already specified above.
2. $H_0: \mu_X - \mu_Y = 0$ versus $H_1: \mu_X - \mu_Y \neq 0$.
3. For similar reasons as in Example C.14, take

$$T = \frac{\overline{X}-\overline{Y}}{\sqrt{S_X^2/m + S_Y^2/n}}.$$

4. By the central limit theorem, the statistic $T$ has, under $H_0$, approximately a standard normal distribution (assuming the variances are finite).
5. The outcome of $T$ is $t = (\overline{x}-\overline{y})/\sqrt{s_X^2/m + s_Y^2/n} \approx -4.59$.
6. As this is a two-sided test, the P-value is $2\,\mathbb{P}_{H_0}[T\leqslant -4.59] \approx 4\cdot 10^{-6}$.
7. Because the P-value is extremely small, there is overwhelming evidence that the two expectations are not the same. $\blacksquare$

### Further Reading

Accessible treatises on probability and stochastic processes include [27, 26, 39, 54, 101]. Kallenberg's book [61] provides a complete graduate-level overview of the foundations of modern probability. Details on the convergence of probability measures and limit theorems can be found in [11]. For an accessible introduction to mathematical statistics with simple applications see, for example, [69, 74, 124]. For a more detailed overview of statistical inference, see [10, 25]. A standard reference for classical (frequentist) statistical inference is [78].
