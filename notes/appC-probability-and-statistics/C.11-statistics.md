---
appendix: C
section: "C.11"
title: "Statistics"
pdf_pages: "471-472"
---

## C.11 Statistics

Statistics deals with the gathering, summarization, analysis, and interpretation of data. The two main branches of statistics are:

1. *Classical or frequentist statistics*: Here the observed data $\tau$ is viewed as the outcome of random data $\mathcal{T}$ described by a probabilistic model — usually the model is specified up to a (multidimensional) parameter; that is, $\mathcal{T}\sim g(\cdot\mid\boldsymbol{\theta})$ for some $\boldsymbol{\theta}$. The statistical inference is then purely concerned with the model and in particular with the parameter $\boldsymbol{\theta}$. For example, on the basis of the data one may wish to

   (a) estimate the parameter,

   (b) perform statistical tests on the parameter, or

   (c) validate the model.

2. *Bayesian statistics*: In this approach we average over all possible values of the parameter $\boldsymbol{\theta}$ using a user-specified weight function $g(\boldsymbol{\theta})$ and obtain the model $\mathcal{T} \sim \int g(\cdot\mid\boldsymbol{\theta})\,g(\boldsymbol{\theta})\,\mathrm{d}\boldsymbol{\theta}$. For practical computations, this means that we can treat $\boldsymbol{\theta}$ as a random variable with pdf $g(\boldsymbol{\theta})$. Bayes' formula $g(\boldsymbol{\theta}\mid\tau)\propto g(\tau\mid\boldsymbol{\theta})\,g(\boldsymbol{\theta})$ is used to learn $\boldsymbol{\theta}$ based on the observed data $\tau$.

**Example C.10 (Iid Sample).** The most fundamental statistical model is where the data $\mathcal{T} = X_1,\ldots,X_n$ is such that the random variables $X_1,\ldots,X_n$ are assumed to be independent and identically distributed:

$$X_1,\ldots,X_n \overset{\text{iid}}{\sim} \mathsf{Dist},$$

according to some known or unknown distribution $\mathsf{Dist}$. An iid sample is often called a *random sample* in the statistics literature. Note that the word "sample" can refer to both a collection of random variables and to a single random variable. It should be clear from the context which meaning is being used.

Often our guess or model for the true distribution is specified up to an unknown parameter $\boldsymbol{\theta}$, with $\boldsymbol{\theta}\in\Theta$. The most common model is:

$$X_1,\ldots,X_n \overset{\text{iid}}{\sim} \mathcal{N}(\mu,\sigma^2),$$

in which case $\boldsymbol{\theta} = (\mu,\sigma^2)$ and $\Theta = \mathbb{R}\times\mathbb{R}_+$. $\blacksquare$
