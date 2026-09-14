---
appendix: C
section: "C.12"
title: "Estimation"
pdf_pages: "472-475"
---

## C.12 Estimation

Suppose the model $g(\cdot\mid\boldsymbol{\theta})$ for the data $\mathcal{T}$ is completely specified up to an unknown parameter vector $\boldsymbol{\theta}$. The aim is to estimate $\boldsymbol{\theta}$ on the basis of the observed data $\tau$ only (an alternative goal could be to estimate $\boldsymbol{\eta} = \boldsymbol{\psi}(\boldsymbol{\theta})$ for some vector-valued function $\boldsymbol{\psi}$). Specifically, the goal is to find an *estimator* $\boldsymbol{T} = \boldsymbol{T}(\mathcal{T})$ that is close to the unknown $\boldsymbol{\theta}$. The corresponding outcome $\boldsymbol{t} = \boldsymbol{T}(\tau)$ is the *estimate* of $\boldsymbol{\theta}$. The *bias* of an estimator $\boldsymbol{T}$ of $\boldsymbol{\theta}$ is defined as $\mathbb{E}\boldsymbol{T} - \boldsymbol{\theta}$. An estimator $\boldsymbol{T}$ of $\boldsymbol{\theta}$ is said to be *unbiased* if $\mathbb{E}_{\boldsymbol{\theta}}\boldsymbol{T} = \boldsymbol{\theta}$. We often write $\widehat{\boldsymbol{\theta}}$ for both an estimator and estimate of $\boldsymbol{\theta}$. The *mean squared error* (MSE) of a real-valued estimator $T$ is defined as

$$\mathrm{MSE} = \mathbb{E}_\theta(T-\theta)^2.$$

An estimator $T_1$ is said to be more *efficient* than an estimator $T_2$ if the MSE of $T_1$ is smaller than the MSE of $T_2$. The MSE can be written as the sum

$$\mathrm{MSE} = (\mathbb{E}_\theta T - \theta)^2 + \mathbb{V}\mathrm{ar}_\theta T.$$

The first term measures the unbiasedness and the second is the variance of the estimator. In particular, for an unbiased estimator the MSE of an estimator is simply equal to its variance.

For simulation purposes it is often important to include the running time of the estimator in efficiency comparisons. One way to compare two unbiased estimators $T_1$ and $T_2$ is to compare their *relative time variance products*,

$$\frac{r_i\,\mathbb{V}\mathrm{ar}\,T_i}{(\mathbb{E}\,T_i)^2}, \quad i = 1,2, \tag{C.44}$$

where $r_1$ and $r_2$ are the times required to calculate the estimators $T_1$ and $T_2$, respectively. In this scheme, $T_1$ is considered more efficient than $T_2$ if its relative time variance product is smaller. We discuss next two systematic approaches for constructing sound estimators.

### C.12.1 Method of Moments

Suppose $x_1,\ldots,x_n$ are outcomes from an iid sample $X_1,\ldots,X_n \sim_{\text{iid}} g(x\mid\boldsymbol{\theta})$, where $\boldsymbol{\theta} = [\theta_1,\ldots,\theta_k]^\top$ is unknown. The moments of the sampling distribution can be easily estimated. Namely, if $X\sim g(x\mid\boldsymbol{\theta})$, then the $r$-th moment of $X$, that is $\mu_r(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}X^r$ (assuming it exists), can be estimated through the *sample $r$-th moment*: $\frac{1}{n}\sum_{i=1}^{n}x_i^r$. The *method of moments* involves choosing the estimate $\widehat{\boldsymbol{\theta}}$ of $\boldsymbol{\theta}$ such that each of the first $k$ sample and true moments are matched:

$$\frac{1}{n}\sum_{i=1}^{n} x_i^r = \mu_r(\widehat{\boldsymbol{\theta}}), \quad r = 1,2,\ldots,k.$$

In general, this set of equations is nonlinear and so its solution often has to be found numerically.

**Example C.11 (Sample Mean and Sample Variance).** Suppose the data is given by $\mathcal{T} = \{X_1,\ldots,X_n\}$, where the $\{X_i\}$ form an iid sample from a general distribution with mean $\mu$ and variance $\sigma^2 < \infty$. Matching the first two moments gives the set of equations

$$\frac{1}{n}\sum_{i=1}^{n} x_i = \mu,$$

$$\frac{1}{n}\sum_{i=1}^{n} x_i^2 = \mu^2 + \sigma^2.$$

The method of moments estimates for $\mu$ and $\sigma^2$ are therefore the *sample mean*

$$\widehat{\mu} = \overline{x} = \frac{1}{n}\sum_{i=1}^{n} x_i, \tag{C.45}$$

and

$$\widehat{\sigma^2} = \frac{1}{n}\sum_{i=1}^{n} x_i^2 - (\overline{x})^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i-\overline{x})^2. \tag{C.46}$$

The corresponding estimator for $\mu$, $\overline{X}$, is unbiased. However, the estimator for $\sigma^2$ is biased: $\mathbb{E}\,\widehat{\sigma^2} = \sigma^2(n-1)/n$. An unbiased estimator is the *sample variance*

$$S^2 = \widehat{\sigma^2}\,\frac{n}{n-1} = \frac{1}{n-1}\sum_{i=1}^{n}(X_i-\overline{X})^2.$$

Its square root, $S = \sqrt{S^2}$, is called the *sample standard deviation*. $\blacksquare$

**Example C.12 (Sample Covariance Matrix).** The method of moments can also be used to estimate the covariance matrix of a random vector. In particular, let the $X_1,\ldots,X_n$ be iid copies of a $d$-dimensional random vector $\boldsymbol{X}$ with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$. We assume $n \geqslant d$. The moment estimator for $\boldsymbol{\mu}$ is, as in the $d=1$ case, $\overline{\boldsymbol{X}} = (\boldsymbol{X}_1+\cdots+\boldsymbol{X}_n)/n$. As the covariance matrix can be written (see (C.15)) as

$$\boldsymbol{\Sigma} = \mathbb{E}(\boldsymbol{X}-\boldsymbol{\mu})(\boldsymbol{X}-\boldsymbol{\mu})^\top,$$

the method of moments yields the estimator

$$\widehat{\boldsymbol{\Sigma}} = \frac{1}{n}\sum_{i=1}^{n}(\boldsymbol{X}_i-\overline{\boldsymbol{X}})(\boldsymbol{X}_i-\overline{\boldsymbol{X}})^\top. \tag{C.47}$$

Similar to the one-dimensional case ($d=1$), replacing the factor $1/n$ with $1/(n-1)$ gives an unbiased estimator, called the *sample covariance matrix*. $\blacksquare$

### C.12.2 Maximum Likelihood Method

The concept of *likelihood* is central in statistics. It describes in a precise way the information about model parameters that is contained in the observed data.

Let $\mathcal{T}$ be a (random) data object that is modeled as a draw from the pdf $g(\tau\mid\boldsymbol{\theta})$ (discrete or continuous) with parameter vector $\boldsymbol{\theta}\in\Theta$. Let $\tau$ be an outcome of $\mathcal{T}$. The function $L(\boldsymbol{\theta}\mid\tau) := g(\tau\mid\boldsymbol{\theta})$, $\boldsymbol{\theta}\in\Theta$, is called the *likelihood function* of $\boldsymbol{\theta}$, based on $\tau$. The (natural) logarithm of the likelihood function is called the *log-likelihood function* and is often denoted by a lower case $l$.

> Note that $L(\boldsymbol{\theta}\mid\tau)$ and $g(\tau\mid\boldsymbol{\theta})$ have the same formula, but the first is viewed as a function of $\boldsymbol{\theta}$ for fixed $\tau$, where the second is viewed as a function of $\tau$ for fixed $\boldsymbol{\theta}$.

The concept of likelihood is particularly useful when $\mathcal{T}$ is modeled as an iid sample $\{X_1,\ldots,X_n\}$ from some pdf $\mathring{g}$. In that case, the likelihood of the data $\tau = \{x_1,\ldots,x_n\}$, as a function of $\boldsymbol{\theta}$, is given by the product

$$L(\boldsymbol{\theta}\mid\tau) = \prod_{i=1}^{n} \mathring{g}(x_i\mid\boldsymbol{\theta}). \tag{C.48}$$

Let $\tau$ be an observation from $\mathcal{T}\sim g(\tau\mid\boldsymbol{\theta})$, and suppose that $g(\tau\mid\boldsymbol{\theta})$ takes its largest value at $\boldsymbol{\theta} = \widehat{\boldsymbol{\theta}}$. In a way this $\widehat{\boldsymbol{\theta}}$ is our best estimate for $\boldsymbol{\theta}$, as it maximizes the probability (density) for the observation $\tau$. It is called the *maximum likelihood estimate* (MLE) of $\boldsymbol{\theta}$. Note that $\widehat{\boldsymbol{\theta}} = \widehat{\boldsymbol{\theta}}(\tau)$ is a function of $\tau$. The corresponding random variable, also denoted $\widehat{\boldsymbol{\theta}}$, is the *maximum likelihood estimator* (also abbreviated as MLE).

Maximization of $L(\boldsymbol{\theta}\mid\tau)$ as a function of $\boldsymbol{\theta}$ is equivalent (when searching for the maximizer) to maximizing the log-likelihood $l(\boldsymbol{\theta}\mid\tau)$, as the natural logarithm is an increasing function. This is often easier, especially when $\mathcal{T}$ is an iid sample from some sampling distribution. For example, for $L$ of the form (C.48), we have

$$l(\boldsymbol{\theta}\mid\tau) = \sum_{i=1}^{n} \ln \mathring{g}(x_i\mid\boldsymbol{\theta}).$$

If $l(\boldsymbol{\theta}\mid\tau)$ is a differentiable function with respect to $\boldsymbol{\theta}$ and the maximum is attained in the *interior* of $\Theta$, *and there exists a unique maximum point*, then we can find the MLE of $\boldsymbol{\theta}$ by solving the equations

$$\frac{\partial}{\partial\theta_i} l(\boldsymbol{\theta}\mid\tau) = 0, \quad i = 1,\ldots,d.$$

**Example C.13 (Bernoulli Random Sample).** Suppose we have data $\tau_n = \{x_1,\ldots,x_n\}$ and assume the model $X_1,\ldots,X_n \sim_{\text{iid}} \mathsf{Ber}(\theta)$. Then, the likelihood function is given by

$$L(\theta\mid\tau) = \prod_{i=1}^{n}\theta^{x_i}(1-\theta)^{1-x_i} = \theta^s(1-\theta)^{n-s}, \quad 0 < \theta < 1, \tag{C.49}$$

where $s := x_1+\cdots+x_n =: n\overline{x}$. The log-likelihood is $l(\theta) = s\ln\theta + (n-s)\ln(1-\theta)$. Through differentiation with respect to $\theta$, we find the derivative

$$\frac{s}{\theta} - \frac{n-s}{1-\theta} = \frac{s}{\theta(1-\theta)} - \frac{n}{1-\theta}. \tag{C.50}$$

Solving $l'(\theta) = 0$ gives the ML estimate $\widehat{\theta} = \overline{x}$ and ML estimator $\widehat{\theta} = \overline{X}$. $\blacksquare$
