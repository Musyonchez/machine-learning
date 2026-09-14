---
chapter: 4
section: "exercises"
title: "Exercises"
pdf_pages: "178-184"
---

## Exercises

1. This exercise is to show that the Fisher information matrix $\mathbf{F}(\boldsymbol{\theta})$ in (4.8) is equal to the matrix $\mathbf{H}(\boldsymbol{\theta})$ in (4.9), in the special case where $f = g(\cdot\,|\,\boldsymbol{\theta})$, and under the assumption that integration and differentiation orders can be interchanged.

   (a) Let $\boldsymbol{h}$ be a vector-valued function and $k$ a real-valued function. Prove the following *quotient rule for differentiation*:

   $$\frac{\partial[\boldsymbol{h}(\boldsymbol{\theta})/k(\boldsymbol{\theta})]}{\partial\boldsymbol{\theta}} = \frac{1}{k(\boldsymbol{\theta})}\frac{\partial \boldsymbol{h}(\boldsymbol{\theta})}{\partial\boldsymbol{\theta}} - \frac{1}{k^2(\boldsymbol{\theta})}\frac{\partial k(\boldsymbol{\theta})}{\partial\boldsymbol{\theta}}\boldsymbol{h}(\boldsymbol{\theta})^\top. \tag{4.45}$$

   (b) Now take $\boldsymbol{h}(\boldsymbol{\theta}) = \dfrac{\partial g(\boldsymbol{X}\,|\,\boldsymbol{\theta})}{\partial\boldsymbol{\theta}}$ and $k(\boldsymbol{\theta}) = g(\boldsymbol{X}\,|\,\boldsymbol{\theta})$ in (4.45) and take expectations with respect to $\mathbb{E}_{\boldsymbol{\theta}}$ on both sides to show that

   $$-\mathbf{H}(\boldsymbol{\theta}) = \underbrace{\mathbb{E}_{\boldsymbol{\theta}}\left[\frac{1}{g(\boldsymbol{X}\,|\,\boldsymbol{\theta})}\frac{\partial \frac{\partial g(\boldsymbol{X}\,|\,\boldsymbol{\theta})}{\partial\boldsymbol{\theta}}}{\partial\boldsymbol{\theta}}\right]}_{\mathbf{A}} - \mathbf{F}(\boldsymbol{\theta}).$$

   (c) Finally show that $\mathbf{A}$ is the zero matrix.

2. Plot the mixture of $\mathcal{N}(0,1)$, $\mathcal{U}(0,1)$, and $\mathsf{Exp}(1)$ distributions, with weights $w_1 = w_2 = w_3 = 1/3$.

3. Denote the pdfs in Exercise 2 by $f_1, f_2, f_3$, respectively. Suppose that $X$ is simulated via the two-step procedure: First, draw $Z$ from $\{1,2,3\}$, then draw $X$ from $f_Z$. How likely is it that the outcome $x = 0.5$ of $X$ has come from the uniform pdf $f_2$?

4. Simulate an iid training set of size 100 from the $\mathsf{Gamma}(2.3, 0.5)$ distribution, and implement the Fisher scoring method in Example 4.1 to find the maximum likelihood estimate. Plot the true and approximate pdfs.

5. Let $\mathcal{T} = \{X_1,\ldots,X_n\}$ be iid data from a pdf $g(\boldsymbol{x}\,|\,\boldsymbol{\theta})$ with Fisher matrix $\mathbf{F}(\boldsymbol{\theta})$. Explain why, under the conditions where (4.7) holds,

   $$\boldsymbol{S}_{\mathcal{T}}(\boldsymbol{\theta}) := \frac{1}{n}\sum_{i=1}^n \boldsymbol{S}(X_i\,|\,\boldsymbol{\theta})$$

   for large $n$ has approximately a multivariate normal distribution with expectation vector $\boldsymbol{0}$ and covariance matrix $\mathbf{F}(\boldsymbol{\theta})/n$.

6. Figure 4.15 shows a Gaussian KDE with bandwidth $\sigma = 0.2$ on the points $-0.5, 0, 0.2, 0.9$, and $1.5$. Reproduce the plot in Python. Using the same bandwidth, plot also the KDE for the same data, but now with $\phi(z) = 1/2, z\in[-1,1]$.

   > **Figure 4.15:** The Gaussian KDE (solid line) is the equally weighted mixture of normal pdfs centered around the data points $\{-0.5, 0, 0.2, 0.9, 1.5\}$ (marked as red dots on the horizontal axis) and with standard deviation $\sigma = 0.2$ (dashed individual kernels).

7. For fixed $x'$, the Gaussian kernel function

   $$f(x\,|\,t) := \frac{1}{\sqrt{2\pi t}}\,\mathrm{e}^{-\frac{1}{2}\frac{(x-x')^2}{t}}$$

   is the solution to Fourier's *heat equation*

   $$\frac{\partial}{\partial t}f(x\,|\,t) = \frac{1}{2}\frac{\partial^2}{\partial x^2}f(x\,|\,t), \quad x\in\mathbb{R}, t>0,$$

   with initial condition $f(x\,|\,0) = \delta(x-x')$ (the Dirac function at $x'$). Show this. As a consequence, the Gaussian KDE is the solution to the same heat equation, but now with initial condition $f(x\,|\,0) = n^{-1}\sum_{i=1}^n \delta(x-x_i)$. This was the motivation for the theta KDE [14], which is a solution to the same heat equation but now on a *bounded* interval.

8. Show that the Ward linkage given in (4.41) is equal to

   $$d_{\mathrm{Ward}}(\mathcal{I},\mathcal{J}) = \frac{|\mathcal{I}|\,|\mathcal{J}|}{|\mathcal{I}|+|\mathcal{J}|}\,\|\overline{\boldsymbol{x}}_{\mathcal{I}} - \overline{\boldsymbol{x}}_{\mathcal{J}}\|^2.$$

9. Carry out the agglomerative hierarchical clustering of Example 4.8 via the `linkage` method from `scipy.cluster.hierarchy`. Show that the linkage matrices are the same. Give a scatterplot of the data, color coded into $K=3$ clusters.

10. Suppose that we have the data $\tau_n = \{x_1,\ldots,x_n\}$ in $\mathbb{R}$ and decide to train the two-component Gaussian mixture model

    $$g(x\,|\,\boldsymbol{\theta}) = w_1\,\frac{1}{\sqrt{2\pi\sigma_1^2}}\exp\left(-\frac{(x-\mu_1)^2}{2\sigma_1^2}\right) + w_2\,\frac{1}{\sqrt{2\pi\sigma_2^2}}\exp\left(-\frac{(x-\mu_2)^2}{2\sigma_2^2}\right),$$

    where the parameter vector $\boldsymbol{\theta} = [\mu_1,\mu_2,\sigma_1,\sigma_2,w_1,w_2]^\top$ belongs to the set

    $$\Theta = \{\boldsymbol{\theta} : w_1+w_2 = 1,\ w_1\in[0,1],\ \mu_i\in\mathbb{R},\ \sigma_i>0,\ \forall i\}.$$

    Suppose that the training is via the maximum likelihood in (2.28). Show that

    $$\sup_{\boldsymbol{\theta}\in\Theta} \frac{1}{n}\sum_{i=1}^n \ln g(x_i\,|\,\boldsymbol{\theta}) = \infty.$$

    In other words, find a sequence of values for $\boldsymbol{\theta}\in\Theta$ such that the likelihood grows without bound. How can we restrict the set $\Theta$ to ensure that the likelihood remains bounded?

11. A $d$-dimensional normal random vector $\boldsymbol{X}\sim\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma})$ can be defined via an affine transformation, $\boldsymbol{X} = \boldsymbol{\mu} + \boldsymbol{\Sigma}^{1/2}\boldsymbol{Z}$, of a standard normal random vector $\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},\mathbf{I}_d)$, where $\boldsymbol{\Sigma}^{1/2}(\boldsymbol{\Sigma}^{1/2})^\top = \boldsymbol{\Sigma}$. In a similar way, we can define a $d$-dimensional Student random vector $\boldsymbol{X}\sim \mathsf{t}_\alpha(\boldsymbol{\mu},\boldsymbol{\Sigma})$ via a transformation

    $$\boldsymbol{X} = \boldsymbol{\mu} + \frac{1}{\sqrt{S}}\boldsymbol{\Sigma}^{1/2}\boldsymbol{Z}, \tag{4.46}$$

    where $\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},\mathbf{I}_d)$ and $S\sim\mathsf{Gamma}\!\left(\frac{\alpha}{2},\frac{\alpha}{2}\right)$ are independent, $\alpha>0$, and $\boldsymbol{\Sigma}^{1/2}(\boldsymbol{\Sigma}^{1/2})^\top = \boldsymbol{\Sigma}$. Note that we obtain the multivariate normal distribution as a limiting case for $\alpha\to\infty$.

    (a) Show that the density of the $\mathsf{t}_\alpha(\boldsymbol{0},\mathbf{I}_d)$ distribution is given by

    $$t_\alpha(\boldsymbol{x}) := \frac{\Gamma((\alpha+d)/2)}{(\pi\alpha)^{d/2}\Gamma(\alpha/2)}\left(1+\frac{1}{\alpha}\|\boldsymbol{x}\|^2\right)^{-\frac{\alpha+d}{2}}.$$

    By the transformation rule (C.23), it follows that the density of $\boldsymbol{X}\sim \mathsf{t}_\alpha(\boldsymbol{\mu},\boldsymbol{\Sigma})$ is given by $t_{\alpha,\boldsymbol{\Sigma}}(\boldsymbol{x}-\boldsymbol{\mu})$, where

    $$t_{\alpha,\boldsymbol{\Sigma}}(\boldsymbol{x}) := \frac{1}{|\boldsymbol{\Sigma}^{1/2}|}\,t_\alpha(\boldsymbol{\Sigma}^{-1/2}\boldsymbol{x}).$$

    [Hint: conditional on $S = s$, $\boldsymbol{X}$ has a $\mathcal{N}(\boldsymbol{0},\mathbf{I}_d/s)$ distribution.]

    (b) We wish to fit a $\mathsf{t}_\nu(\boldsymbol{\mu},\boldsymbol{\Sigma})$ distribution to given data $\tau = \{\boldsymbol{x}_1,\ldots,\boldsymbol{x}_n\}$ in $\mathbb{R}^d$ via the EM method. We use the representation (4.46) and augment the data with the vector $\boldsymbol{S} = [S_1,\ldots,S_n]^\top$ of hidden variables. Show that the complete-data likelihood is given by

    $$g(\tau,\boldsymbol{s}\,|\,\boldsymbol{\theta}) = \prod_i \frac{(\alpha/2)^{\alpha/2}\,s_i^{(\alpha+d)/2-1}\exp\!\left(-\frac{s_i}{2}\alpha - \frac{s_i}{2}\|\boldsymbol{\Sigma}^{-1/2}(\boldsymbol{x}_i-\boldsymbol{\mu})\|^2\right)}{\Gamma(\alpha/2)(2\pi)^{d/2}|\boldsymbol{\Sigma}^{1/2}|}. \tag{4.47}$$

    (c) Show that, as a consequence, conditional on the data $\tau$ and parameter $\boldsymbol{\theta}$, the hidden data are mutually independent, and

    $$(S_i\,|\,\tau,\boldsymbol{\theta}) \sim \mathsf{Gamma}\!\left(\frac{\alpha+d}{2}, \frac{\alpha+\|\boldsymbol{\Sigma}^{-1/2}(\boldsymbol{x}_i-\boldsymbol{\mu})\|^2}{2}\right), \quad i=1,\ldots,n.$$

    (d) At iteration $t$ of the EM algorithm, let $g^{(t)}(\boldsymbol{s}) = g(\boldsymbol{s}\,|\,\tau,\boldsymbol{\theta}^{(t-1)})$ be the density of the missing data, given the observed data $\tau$ and the current parameter guess $\boldsymbol{\theta}^{(t-1)}$. Verify that the expected complete-data log-likelihood is given by:

    $$\mathbb{E}_{g^{(t)}}\ln g(\tau,\boldsymbol{S}\,|\,\boldsymbol{\theta}) = \frac{n\alpha}{2}\ln\frac{\alpha}{2} - \frac{nd}{2}\ln(2\pi) - n\ln\Gamma\!\left(\frac{\alpha}{2}\right) - \frac{n}{2}\ln|\boldsymbol{\Sigma}|$$
    $$+ \frac{\alpha+d-2}{2}\sum_{i=1}^n \mathbb{E}_{g^{(t)}}\ln S_i - \sum_{i=1}^n \frac{\alpha+\|\boldsymbol{\Sigma}^{-1/2}(\boldsymbol{x}_i-\boldsymbol{\mu})\|^2}{2}\mathbb{E}_{g^{(t)}}S_i.$$

    Show that

    $$\mathbb{E}_{g^{(t)}}S_i = \frac{\alpha^{(t-1)}+d}{\alpha^{(t-1)}+\|(\boldsymbol{\Sigma}^{(t-1)})^{-1/2}(\boldsymbol{x}_i-\boldsymbol{\mu}^{(t-1)})\|^2} =: w_i^{(t-1)}$$
    $$\mathbb{E}_{g^{(t)}}\ln S_i = \psi\!\left(\frac{\alpha^{(t-1)}+d}{2}\right) - \ln\!\left(\frac{\alpha^{(t-1)}+d}{2}\right) + \ln w_i^{(t-1)},$$

    where $\psi := (\ln\Gamma)'$ is the *digamma* function.

    (e) Finally, show that in the M-step of the EM algorithm $\boldsymbol{\theta}^{(t)}$ is updated from $\boldsymbol{\theta}^{(t-1)}$ as follows:

    $$\boldsymbol{\mu}^{(t)} = \frac{\sum_{i=1}^n w_i^{(t-1)}\boldsymbol{x}_i}{\sum_{i=1}^n w_i^{(t-1)}}$$
    $$\boldsymbol{\Sigma}^{(t)} = \frac{1}{n}\sum_{i=1}^n w_i^{(t-1)}(\boldsymbol{x}_i-\boldsymbol{\mu}^{(t)})(\boldsymbol{x}_i-\boldsymbol{\mu}^{(t)})^\top,$$

    and $\alpha^{(t)}$ is defined implicitly through the solution of the nonlinear equation:

    $$\ln\!\left(\frac{\alpha}{2}\right) - \psi\!\left(\frac{\alpha}{2}\right) + \psi\!\left(\frac{\alpha^{(t)}+d}{2}\right) - \ln\!\left(\frac{\alpha^{(t)}+d}{2}\right) + 1 + \frac{\sum_{i=1}^n\left(\ln(w_i^{(t-1)}) - w_i^{(t-1)}\right)}{n} = 0.$$

12. A generalization of both the gamma and inverse-gamma distribution is the *generalized inverse-gamma distribution*, which has density

    $$f(s) = \frac{(a/b)^{p/2}}{2K_p(\sqrt{ab})}\,s^{p-1}\mathrm{e}^{-\frac{1}{2}(as+b/s)}, \quad a,b,s>0,\ p\in\mathbb{R}, \tag{4.48}$$

    where $K_p$ is the *modified Bessel function of the second kind*, which can be defined as the integral

    $$K_p(x) = \int_0^\infty \mathrm{e}^{-x\cosh(t)}\cosh(pt)\,\mathrm{d}t, \quad x>0,\ p\in\mathbb{R}. \tag{4.49}$$

    We write $S\sim \mathsf{GIG}(a,b,p)$ to denote that $S$ has a pdf of the form (4.48). The function $K_p$ has many interesting properties. Special cases include

    $$K_{1/2}(x) = \sqrt{\frac{x\pi}{2}}\,\mathrm{e}^{-x}\,\frac{1}{x}$$
    $$K_{3/2}(x) = \sqrt{\frac{x\pi}{2}}\,\mathrm{e}^{-x}\left(\frac{1}{x}+\frac{1}{x^2}\right)$$
    $$K_{5/2}(x) = \sqrt{\frac{x\pi}{2}}\,\mathrm{e}^{-x}\left(\frac{1}{x}+\frac{3}{x^2}+\frac{3}{x^3}\right).$$

    More generally, $K_p$ satisfies the recursion

    $$K_{p+1}(x) = K_{p-1}(x) + \frac{2p}{x}K_p(x). \tag{4.50}$$

    (a) Using the change of variables $\mathrm{e}^z = s\sqrt{a/b}$, show that

    $$\int_0^\infty s^{p-1}\mathrm{e}^{-\frac{1}{2}(as+b/s)}\,\mathrm{d}s = 2K_p(\sqrt{ab})(b/a)^{p/2}.$$

    (b) Let $S\sim \mathsf{GIG}(a,b,p)$. Show that

    $$\mathbb{E}S = \frac{\sqrt{b}\,K_{p+1}(\sqrt{ab})}{\sqrt{a}\,K_p(\sqrt{ab})} \tag{4.51}$$

    and

    $$\mathbb{E}S^{-1} = \frac{\sqrt{a}\,K_{p+1}(\sqrt{ab})}{\sqrt{b}\,K_p(\sqrt{ab})} - \frac{2p}{b}. \tag{4.52}$$

13. In Exercise 11 we viewed the multivariate Student $\mathsf{t}_\alpha$ distribution as a *scale-mixture* of the $\mathcal{N}(\boldsymbol{0},\mathbf{I}_d)$ distribution. In this exercise, we consider a similar transformation, but now $\boldsymbol{\Sigma}^{1/2}\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},\boldsymbol{\Sigma})$ is not divided but is *multiplied* by $\sqrt{S}$, with $S\sim \mathsf{Gamma}(\alpha/2,\alpha/2)$:

    $$\boldsymbol{X} = \boldsymbol{\mu} + \sqrt{S}\,\boldsymbol{\Sigma}^{1/2}\boldsymbol{Z}, \tag{4.53}$$

    where $S$ and $\boldsymbol{Z}$ are independent and $\alpha>0$.

    (a) Show, using Exercise 12, that for $\boldsymbol{\Sigma}^{1/2} = \mathbf{I}_d$ and $\boldsymbol{\mu} = \boldsymbol{0}$, the random vector $\boldsymbol{X}$ has a $d$-dimensional *Bessel distribution*, with density:

    $$\kappa_\alpha(\boldsymbol{x}) := \frac{2^{1-(\alpha+d)/2}\alpha^{(\alpha+d)/4}\|\boldsymbol{x}\|^{(\alpha-d)/2}}{\pi^{d/2}\Gamma(\alpha/2)}K_{(\alpha-d)/2}\!\left(\|\boldsymbol{x}\|\sqrt{\alpha}\right), \quad \boldsymbol{x}\in\mathbb{R}^d,$$

    where $K_p$ is the modified Bessel function of the second kind given in (4.49). We write $\boldsymbol{X}\sim \mathsf{Bessel}_\alpha(\boldsymbol{0},\mathbf{I}_d)$. A random vector $\boldsymbol{X}$ is said to have a $\mathsf{Bessel}_\alpha(\boldsymbol{\mu},\boldsymbol{\Sigma})$ distribution if it can be written in the form (4.53). By the transformation rule (C.23), its density is given by $\frac{1}{\sqrt{|\boldsymbol{\Sigma}|}}\kappa_\alpha(\boldsymbol{\Sigma}^{-1/2}(\boldsymbol{x}-\boldsymbol{\mu}))$. Special instances of the Bessel pdf include:

    $$\kappa_2(x) = \frac{\exp(-\sqrt{2}\,|x|)}{\sqrt{2}}$$
    $$\kappa_4(x) = \frac{1+2|x|}{2}\exp(-2|x|)$$
    $$\kappa_4(x_1,x_2,x_3) = \frac{1}{\pi}\exp\!\left(-2\sqrt{x_1^2+x_2^2+x_3^2}\right)$$
    $$\kappa_{d+1}(\boldsymbol{x}) = \frac{((d+1)/2)^{d/2}\sqrt{\pi}}{(2\pi)^{d/2}\Gamma((d+1)/2)}\exp\!\left(-\sqrt{d+1}\,\|\boldsymbol{x}\|\right), \quad \boldsymbol{x}\in\mathbb{R}^d.$$

    Note that $\kappa_2$ is the (scaled) pdf of the double-exponential or *Laplace* distribution.

    (b) Given the data $\tau = \{\boldsymbol{x}_1,\ldots,\boldsymbol{x}_n\}$ in $\mathbb{R}^d$, we wish to fit a Bessel pdf to the data by employing the EM algorithm, augmenting the data with the vector $\boldsymbol{S} = [S_1,\ldots,S_n]^\top$ of missing data. We assume that $\alpha$ is known and $\alpha > d$. Show that conditional on $\tau$ (and given $\boldsymbol{\theta}$), the missing data vector $\boldsymbol{S}$ has independent components, with $S_i \sim \mathsf{GIG}(\alpha, b_i, (\alpha-d)/2)$, with $b_i := \|\boldsymbol{\Sigma}^{-1/2}(\boldsymbol{x}_i-\boldsymbol{\mu})\|^2$, $i=1,\ldots,n$.

    (c) At iteration $t$ of the EM algorithm, let $g^{(t)}(\boldsymbol{s}) = g(\boldsymbol{s}\,|\,\tau,\boldsymbol{\theta}^{(t-1)})$ be the density of the missing data, given the observed data $\tau$ and the current parameter guess $\boldsymbol{\theta}^{(t-1)}$. Show that the expected complete-data log-likelihood is given by:

    $$Q^{(t)}(\boldsymbol{\theta}) := \mathbb{E}_{g^{(t)}}\ln g(\tau,\boldsymbol{S}\,|\,\boldsymbol{\theta}) = -\frac{1}{2}\sum_{i=1}^n b_i(\boldsymbol{\theta})\,w_i^{(t-1)} + \text{constant}, \tag{4.54}$$

    where $b_i(\boldsymbol{\theta}) = \|\boldsymbol{\Sigma}^{-1/2}(\boldsymbol{x}_i-\boldsymbol{\mu})\|^2$ and

    $$w_i^{(t-1)} := \frac{\sqrt{\alpha}\,K_{(\alpha-d+2)/2}\!\left(\sqrt{\alpha\,b_i(\boldsymbol{\theta}^{(t-1)})}\right)}{\sqrt{b_i(\boldsymbol{\theta}^{(t-1)})}\,K_{(\alpha-d)/2}\!\left(\sqrt{\alpha\,b_i(\boldsymbol{\theta}^{(t-1)})}\right)} - \frac{\alpha-d}{b_i(\boldsymbol{\theta}^{(t-1)})}, \quad i=1,\ldots,n.$$

    (d) From (4.54) derive the M-step of the EM algorithm. That is, show how $\boldsymbol{\theta}^{(t)}$ is updated from $\boldsymbol{\theta}^{(t-1)}$.

14. Consider the ellipsoid $E = \{\boldsymbol{x}\in\mathbb{R}^d : \boldsymbol{x}\boldsymbol{\Sigma}^{-1}\boldsymbol{x} = 1\}$ in (4.42). Let $\mathbf{U}\mathbf{D}^2\mathbf{U}^\top$ be an SVD of $\boldsymbol{\Sigma}$. Show that the linear transformation $\boldsymbol{x}\mapsto \mathbf{U}^\top\mathbf{D}^{-1}\boldsymbol{x}$ maps the points on $E$ onto the unit sphere $\{\boldsymbol{z}\in\mathbb{R}^d : \|\boldsymbol{z}\|=1\}$.

15. Figure 4.13 shows how the centered "surfboard" data are projected onto the first column of the principal component matrix $\mathbf{U}$. Suppose we project the data instead onto the plane spanned by the first *two* columns of $\mathbf{U}$. What are $a$ and $b$ in the representation $ax_1+bx_2=x_3$ of this plane?

16. Figure 4.14 suggests that we can assign each feature vector $\boldsymbol{x}$ in the `iris` data set to one of two clusters, based on the value of $\boldsymbol{u}_1^\top\boldsymbol{x}$, where $\boldsymbol{u}_1$ is the first principal component. Plot the sepal lengths against petal lengths and color the points for which $\boldsymbol{u}_1^\top\boldsymbol{x} < 1.5$ differently to points for which $\boldsymbol{u}_1^\top\boldsymbol{x} \geqslant 1.5$. To which species of iris do these clusters correspond?
