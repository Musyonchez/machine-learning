---
chapter: 6
section: "Exercises"
title: "Further Reading and Exercises"
pdf_pages: "263-268"
---

## Further Reading

For a good overview of the ridge regression and the lasso, we refer the reader to [36, 56]. For overviews of the theory of RKHS we refer to [3, 115, 126], and for in-depth background on splines and their connection to RKHSs we refer to [123]. For further details on GP regression we refer to [97] and for kernel PCA in particular we refer to [12, 92]. Finally, many facts about kernels and their corresponding RKHSs can be found in [115].

## Exercises

1. Let $\mathcal{G}$ be an RKHS with reproducing kernel $\kappa$. Show that $\kappa$ is a positive semidefinite function.

2. Show that a reproducing kernel, if it exists, is unique.

3. Let $\mathcal{G}$ be a Hilbert space of functions $g:\mathcal{X}\to\mathbb{R}$. Recall that the *evaluation functional* is the map $\delta_{\boldsymbol{x}} : g\mapsto g(\boldsymbol{x})$ for a given $\boldsymbol{x}\in\mathcal{X}$. Show that evaluation functionals are linear operators.

4. Let $\mathcal{G}_0$ be the pre-RKHS $\mathcal{G}_0$ constructed in the proof of Theorem 6.2. Thus, $g\in\mathcal{G}_0$ is of the form $g=\sum_{i=1}^n \alpha_i\kappa_{\boldsymbol{x}_i}$ and

$$\langle g,\kappa_{\boldsymbol{x}}\rangle_{\mathcal{G}_0} = \sum_{i=1}^n \alpha_i\langle\kappa_{\boldsymbol{x}_i},\kappa_{\boldsymbol{x}}\rangle_{\mathcal{G}_0} = \sum_{i=1}^n \alpha_i\kappa(\boldsymbol{x}_i,\boldsymbol{x}) = g(\boldsymbol{x}).$$

   Therefore, we may write the evaluation functional of $g\in\mathcal{G}_0$ at $\boldsymbol{x}$ as $\delta_{\boldsymbol{x}}g := \langle g,\kappa_{\boldsymbol{x}}\rangle_{\mathcal{G}_0}$. Show that $\delta_{\boldsymbol{x}}$ is bounded on $\mathcal{G}_0$ for every $\boldsymbol{x}$; that is, $|\delta_{\boldsymbol{x}}f| < \gamma\|f\|_{\mathcal{G}_0}$, for some $\gamma<\infty$.

5. Continuing Exercise 4, let $(f_n)$ be a Cauchy sequence in $\mathcal{G}_0$ such that $|f_n(\boldsymbol{x})|\to 0$ for all $\boldsymbol{x}$. Show that $\|f_n\|_{\mathcal{G}_0}\to 0$.

6. Continuing Exercises 5 and 4, to show that the inner product (6.14) is well defined, a number of facts have to be checked.

   (a) Verify that the limit converges.

   (b) Verify that the limit is independent of the Cauchy sequences used.

   (c) Verify that the properties of an inner product are satisfied. The only non-trivial property to verify is that $\langle f,f\rangle_{\mathcal{G}} = 0$ if and only if $f=0$.

7. Exercises 4–6 show that $\mathcal{G}$ defined in the proof of Theorem 6.2 is an inner product space. It remains to prove that $\mathcal{G}$ is an RKHS. This requires us to prove that the inner product space $\mathcal{G}$ is complete (and thus Hilbert), and that its evaluation functionals are bounded and hence continuous (see Theorem A.16). This is done in a number of steps.

   > Margin cross-reference: see p. 389 (Theorem A.16).

   (a) Show that $\mathcal{G}_0$ is dense in $\mathcal{G}$ in the sense that every $f\in\mathcal{G}$ is a limit point (with respect to the norm on $\mathcal{G}$) of a Cauchy sequence $(f_n)$ in $\mathcal{G}_0$.

   (b) Show that every evaluation functional $\delta_{\boldsymbol{x}}$ on $\mathcal{G}$ is continuous at the $0$ function. That is,

   $$\forall\varepsilon>0 : \exists\delta>0 : \forall f\in\mathcal{G} : \|f\|_{\mathcal{G}}<\delta \implies |f(\boldsymbol{x})|<\varepsilon. \tag{6.40}$$

   Continuity of $\delta_{\boldsymbol{x}}$ at all functions $g\in\mathcal{G}$ then follows automatically from linearity.

   (c) Show that $\mathcal{G}$ is complete; that is, every Cauchy sequence $(f_n)\in\mathcal{G}$ converges in the norm $\|\cdot\|_{\mathcal{G}}$.

8. If $\kappa_1$ and $\kappa_2$ are kernels on $\mathcal{X}$ and $\mathcal{Y}$, then $\kappa_+((x,y),(x',y')) := \kappa_1(x,x')+\kappa_2(y,y')$ and $\kappa_\times((x,y),(x',y')) := \kappa_1(x,x')\kappa_2(y,y')$ are kernels on the Cartesian product $\mathcal{X}\times\mathcal{Y}$. Prove this.

9. An RKHS enjoys the following desirable smoothness property: if $(g_n)$ is a sequence belonging to RKHS $\mathcal{G}$ on $\mathcal{X}$, and $\|g_n-g\|_{\mathcal{G}}\to 0$, then $g(\boldsymbol{x}) = \lim_n g_n(\boldsymbol{x})$ for all $\boldsymbol{x}\in\mathcal{X}$. Prove this, using Cauchy–Schwarz.

10. Let $\boldsymbol{X}$ be an $\mathbb{R}^d$-valued random variable that is symmetric about the origin (that is, $\boldsymbol{X}$ and $(-\boldsymbol{X})$ are identically distributed). Denote by $\mu$ its distribution and $\psi(\boldsymbol{t}) = \mathbb{E}\,\mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{X}} = \int \mathrm{e}^{\mathrm{i}\boldsymbol{t}^\top\boldsymbol{x}}\mu(\mathrm{d}\boldsymbol{x})$ for $\boldsymbol{t}\in\mathbb{R}^d$ is its characteristic function. Verify that $\kappa(\boldsymbol{x},\boldsymbol{x}') = \psi(\boldsymbol{x}-\boldsymbol{x}')$ is a real-valued positive semidefinite function.

11. Suppose an RKHS $\mathcal{G}$ of functions from $\mathcal{X}\to\mathbb{R}$ (with kernel $\kappa$) is invariant under a group $\mathcal{T}$ of transformations $T:\mathcal{X}\to\mathcal{X}$; that is, for all $f,g\in\mathcal{G}$ and $T\in\mathcal{T}$, we have (i) $f\circ T\in\mathcal{G}$ and (ii) $\langle f\circ T, g\circ T\rangle_{\mathcal{G}} = \langle f,g\rangle_{\mathcal{G}}$. Show that $\kappa(T\boldsymbol{x},T\boldsymbol{x}') = \kappa(\boldsymbol{x},\boldsymbol{x}')$ for all $\boldsymbol{x},\boldsymbol{x}'\in\mathcal{X}$ and $T\in\mathcal{T}$.

12. Given two Hilbert spaces $\mathcal{H}$ and $\mathcal{G}$, we call a mapping $A:\mathcal{H}\to\mathcal{G}$ a *Hilbert space isomorphism* if it is

   > **Margin note — HILBERT SPACE ISOMORPHISM.**

   (i) a linear map; that is, $A(af+bg) = aA(f)+bA(g)$ for any $f,g\in\mathcal{H}$ and $a,b\in\mathbb{R}$.

   (ii) a surjective map; and

   (iii) an isometry; that is, for all $f,g\in\mathcal{H}$, it holds that $\langle f,g\rangle_{\mathcal{H}} = \langle Af,Ag\rangle_{\mathcal{G}}$.

   Let $\mathcal{H} = \mathbb{R}^p$ (equipped with the usual Euclidean inner product) and construct its (continuous) *dual space* $\mathcal{G}$, consisting of all continuous linear functions from $\mathbb{R}^p$ to $\mathbb{R}$, as follows: (a) For each $\boldsymbol{\beta}\in\mathbb{R}^p$, define $g_{\boldsymbol{\beta}}:\mathbb{R}^p\to\mathbb{R}$ via $g_{\boldsymbol{\beta}}(\boldsymbol{x}) = \langle\boldsymbol{\beta},\boldsymbol{x}\rangle = \boldsymbol{\beta}^\top\boldsymbol{x}$, for all $\boldsymbol{x}\in\mathbb{R}^p$. (b) Equip $\mathcal{G}$ with the inner product $\langle g_{\boldsymbol{\beta}},g_{\boldsymbol{\gamma}}\rangle_{\mathcal{G}} := \boldsymbol{\beta}^\top\boldsymbol{\gamma}$.

   Show that $A:\mathcal{H}\to\mathcal{G}$ defined by $A(\boldsymbol{\beta}) = g_{\boldsymbol{\beta}}$ for $\boldsymbol{\beta}\in\mathbb{R}^p$ is a Hilbert space isomorphism.

13. Let $\mathbf{X}$ be an $n\times p$ model matrix. Show that $\mathbf{X}^\top\mathbf{X} + n\gamma\mathbf{I}_p$ for $\gamma>0$ is invertible.

14. As Example 6.8 clearly illustrates, the pdf of a random variable that is symmetric about the origin is not in general a valid reproducing kernel. Take two such iid random variables $X$ and $X'$ with common pdf $f$, and define $Z = X+X'$. Denote by $\psi_Z$ and $f_Z$ the characteristic function and pdf of $Z$, respectively.

   Show that if $\psi_Z$ is in $L^1(\mathbb{R})$, $f_Z$ is a positive semidefinite function. Use this to show that $\kappa(x,x') = f_Z(x-x') = \mathbb{1}\{|x-x'|\leqslant 2\}(1-|x-x'|/2)$ is a valid reproducing kernel.

15. For the smoothing cubic spline of Section 6.6, show that $\kappa(x,u) = \dfrac{\max\{x,u\}\min\{x,u\}^2}{2} - \dfrac{\min\{x,u\}^3}{6}$.

16. Let $\mathbf{X}$ be an $n\times p$ model matrix and let $\boldsymbol{u}\in\mathbb{R}^p$ be the unit-length vector with $k$-th entry equal to one ($u_k = \|\boldsymbol{u}\| = 1$). Suppose that the $k$-th column of $\mathbf{X}$ is $\boldsymbol{v}$ and that it is replaced with a new predictor $\boldsymbol{w}$, so that we obtain the new model matrix:

   $$\widetilde{\mathbf{X}} = \mathbf{X} + (\boldsymbol{w}-\boldsymbol{v})\boldsymbol{u}^\top.$$

   (a) Denoting

   $$\boldsymbol{\delta} := \mathbf{X}^\top(\boldsymbol{w}-\boldsymbol{v}) + \frac{\|\boldsymbol{w}-\boldsymbol{v}\|^2}{2}\boldsymbol{u},$$

   show that

   $$\widetilde{\mathbf{X}}^\top\widetilde{\mathbf{X}} = \mathbf{X}^\top\mathbf{X} + \boldsymbol{u}\boldsymbol{\delta}^\top + \boldsymbol{\delta}\boldsymbol{u}^\top = \mathbf{X}^\top\mathbf{X} + \frac{(\boldsymbol{u}+\boldsymbol{\delta})(\boldsymbol{u}+\boldsymbol{\delta})^\top}{2} - \frac{(\boldsymbol{u}-\boldsymbol{\delta})(\boldsymbol{u}-\boldsymbol{\delta})^\top}{2}.$$

   In other words, $\widetilde{\mathbf{X}}^\top\widetilde{\mathbf{X}}$ differs from $\mathbf{X}^\top\mathbf{X}$ by a symmetric matrix of rank two.

   (b) Suppose that $\mathbf{B} := (\mathbf{X}^\top\mathbf{X} + n\gamma\mathbf{I}_p)^{-1}$ is already computed. Explain how the Sherman–Morrison formulas in Theorem A.10 can be applied twice to compute the inverse and log-determinant of the matrix $\widetilde{\mathbf{X}}^\top\widetilde{\mathbf{X}} + n\gamma\mathbf{I}_p$ in $O((n+p)p)$ computing time, rather than the usual $O((n+p^2)p)$ computing time.[^3]

   > Margin cross-reference: see p. 371 (Theorem A.10, Sherman–Morrison formulas).

   (c) Write a Python program for updating a matrix $\mathbf{B} = (\mathbf{X}^\top\mathbf{X} + n\gamma\mathbf{I}_p)^{-1}$ when we change the $k$-th column of $\mathbf{X}$, as shown in the following pseudo-code.

   **Algorithm 6.8.1: Updating via Sherman–Morrison Formula**

   > **input:** Matrices $\mathbf{X}$ and $\mathbf{B}$, index $k$, and replacement $\boldsymbol{w}$ for the $k$-th column of $\mathbf{X}$.
   > **output:** Updated matrices $\mathbf{X}$ and $\mathbf{B}$.
   > 1. Set $\boldsymbol{v}\in\mathbb{R}^n$ to be the $k$-th column of $\mathbf{X}$.
   > 2. Set $\boldsymbol{u}\in\mathbb{R}^p$ to be the unit-length vector such that $u_k = \|\boldsymbol{u}\| = 1$.
   > 3. $\mathbf{B} \leftarrow \mathbf{B} - \dfrac{\mathbf{B}\boldsymbol{u}\boldsymbol{\delta}^\top\mathbf{B}}{1+\boldsymbol{\delta}^\top\mathbf{B}\boldsymbol{u}}$
   > 4. $\mathbf{B} \leftarrow \mathbf{B} - \dfrac{\mathbf{B}\boldsymbol{\delta}\boldsymbol{u}^\top\mathbf{B}}{1+\boldsymbol{u}^\top\mathbf{B}\boldsymbol{\delta}}$
   > 5. Update the $k$-th column of $\mathbf{X}$ with $\boldsymbol{w}$.
   > 6. **return** $\mathbf{X}, \mathbf{B}$

   [^3]: This Sherman–Morrison updating is not always numerically stable. A more numerically stable method will perform two consecutive rank-one updates of the Cholesky decomposition of $\mathbf{X}^\top\mathbf{X}+n\gamma\mathbf{I}_p$.

17. Use Algorithm 6.8.1 from Exercise 16 to write Python code that computes the ridge regression coefficient $\boldsymbol{\beta}$ in (6.5) and use it to replicate the results on Figure 6.1. The following pseudo-code (with running cost of $O((n+p)p^2)$) may help with the writing of the Python code.

   > Margin cross-reference: see p. 217 (Figure 6.1).

   **Algorithm 6.8.2: Ridge Regression Coefficients via Sherman–Morrison Formula**

   > **input:** Training set $\{\mathbf{X},\boldsymbol{y}\}$ and regularization parameter $\gamma>0$.
   > **output:** Solution $\widehat{\boldsymbol{\beta}} = (n\gamma\mathbf{I}_p + \mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{y}$.
   > 1. Set $\mathbf{A}$ to be an $n\times p$ matrix of zeros and $\mathbf{B} \leftarrow (n\gamma\mathbf{I}_p)^{-1}$.
   > 2. **for** $j = 1,\ldots,p$ **do**
   > 3. $\quad$ Set $\boldsymbol{w}$ to be the $j$-th column of $\mathbf{X}$.
   > 4. $\quad$ Update $\{\mathbf{A},\mathbf{B}\}$ via Algorithm 6.8.1 with inputs $\{\mathbf{A},\mathbf{B},j,\boldsymbol{w}\}$.
   > 5. $\widehat{\boldsymbol{\beta}} \leftarrow \mathbf{B}(\mathbf{X}^\top\boldsymbol{y})$
   > 6. **return** $\widehat{\boldsymbol{\beta}}$

18. Consider Example 2.10 with $\mathbf{D} = \mathrm{diag}(\lambda_1,\ldots,\lambda_p)$ for some nonnegative vector $\boldsymbol{\lambda}\in\mathbb{R}^p$, so that twice the negative logarithm of the *model evidence* can be written as

   > Margin cross-reference: see p. 56 (Example 2.10).

   $$-2\ln g(\boldsymbol{y}) = l(\boldsymbol{\lambda}) := n\ln\big[\boldsymbol{y}^\top(\mathbf{I}-\mathbf{X}\boldsymbol{\Sigma}\mathbf{X}^\top)\boldsymbol{y}\big] + \ln|\mathbf{D}| - \ln|\boldsymbol{\Sigma}| + c,$$

   where $c$ is a constant that depends only on $n$.

   (a) Use the *Woodbury identities* (A.15) and (A.16) to show that

   > Margin cross-reference: see p. 371.

   $$\mathbf{I} - \mathbf{X}\boldsymbol{\Sigma}\mathbf{X}^\top = (\mathbf{I}+\mathbf{X}\mathbf{D}\mathbf{X}^\top)^{-1}$$
   $$\ln|\mathbf{D}| - \ln|\boldsymbol{\Sigma}| = \ln|\mathbf{I}+\mathbf{X}\mathbf{D}\mathbf{X}^\top|.$$

   Deduce that $l(\boldsymbol{\lambda}) = n\ln[\boldsymbol{y}^\top\mathbf{C}\boldsymbol{y}] - \ln|\mathbf{C}| + c$, where $\mathbf{C} := (\mathbf{I}+\mathbf{X}\mathbf{D}\mathbf{X}^\top)^{-1}$.

   (b) Let $[\boldsymbol{v}_1,\ldots,\boldsymbol{v}_p] := \mathbf{X}$ denote the $p$ columns/predictors of $\mathbf{X}$. Show that

   $$\mathbf{C}^{-1} = \mathbf{I} + \sum_{k=1}^p \lambda_k\boldsymbol{v}_k\boldsymbol{v}_k^\top.$$

   Explain why setting $\lambda_k = 0$ has the effect of excluding the $k$-th predictor from the regression model. How can this observation be used for model selection?

   (c) Prove the following formulas for the gradient and Hessian elements of $l(\boldsymbol{\lambda})$:

   $$\frac{\partial l}{\partial\lambda_i} = \boldsymbol{v}_i^\top\mathbf{C}\boldsymbol{v}_i - n\frac{(\boldsymbol{v}_i^\top\mathbf{C}\boldsymbol{y})^2}{\boldsymbol{y}^\top\mathbf{C}\boldsymbol{y}}$$
   $$\frac{\partial^2 l}{\partial\lambda_i\partial\lambda_j} = (n-1)(\boldsymbol{v}_i^\top\mathbf{C}\boldsymbol{v}_j)^2 - n\left[\boldsymbol{v}_i^\top\mathbf{C}\boldsymbol{v}_j - \frac{(\boldsymbol{v}_i^\top\mathbf{C}\boldsymbol{y})(\boldsymbol{v}_j^\top\mathbf{C}\boldsymbol{y})}{\boldsymbol{y}^\top\mathbf{C}\boldsymbol{y}}\right]^2. \tag{6.41}$$

   (d) One method to determine which predictors in $\mathbf{X}$ are important is to compute

   $$\boldsymbol{\lambda}^* := \operatorname*{argmin}_{\boldsymbol{\lambda}\geqslant\mathbf{0}} l(\boldsymbol{\lambda})$$

   using, for example, the interior-point minimization Algorithm B.4.1 with gradient and Hessian computed from (6.41). Write Python code to compute $\boldsymbol{\lambda}^*$ and use it to select the best polynomial model in Example 2.10.

   > Margin cross-reference: see p. 419 (Algorithm B.4.1).

19. (Exercise 18 continued.) Consider again Example 2.10 with $\mathbf{D} = \mathrm{diag}(\lambda_1,\ldots,\lambda_p)$ for some nonnegative model-selection parameter $\boldsymbol{\lambda}\in\mathbb{R}^p$. A Bayesian choice for $\boldsymbol{\lambda}$ is the maximizer of the marginal likelihood $g(\boldsymbol{y}\mid\boldsymbol{\lambda})$; that is,

   > Margin cross-reference: see p. 56.

   $$\boldsymbol{\lambda}^* = \operatorname*{argmax}_{\boldsymbol{\lambda}\geqslant\mathbf{0}} \iint g(\boldsymbol{\beta},\sigma^2,\boldsymbol{y}\mid\boldsymbol{\lambda})\,\mathrm{d}\boldsymbol{\beta}\,\mathrm{d}\sigma^2,$$

   where

   $$\ln g(\boldsymbol{\beta},\sigma^2,\boldsymbol{y}\mid\boldsymbol{\lambda}) = -\frac{\|\boldsymbol{y}-\mathbf{X}\boldsymbol{\beta}\|^2+\boldsymbol{\beta}^\top\mathbf{D}^{-1}\boldsymbol{\beta}}{2\sigma^2} - \frac{1}{2}\ln|\mathbf{D}| - \frac{n+p}{2}\ln(2\pi\sigma^2) - \ln\sigma^2.$$

   To maximize $g(\boldsymbol{y}\mid\boldsymbol{\lambda})$, one can use the EM algorithm with $\boldsymbol{\beta}$ and $\sigma^2$ acting as *latent variables* in the *complete-data log-likelihood* $\ln g(\boldsymbol{\beta},\sigma^2,\boldsymbol{y}\mid\boldsymbol{\lambda})$. Define

   > Margin cross-reference: see p. 128 (EM algorithm).

   $$\boldsymbol{\Sigma} := (\mathbf{D}^{-1}+\mathbf{X}^\top\mathbf{X})^{-1}$$
   $$\overline{\boldsymbol{\beta}} := \boldsymbol{\Sigma}\mathbf{X}^\top\boldsymbol{y} \tag{6.42}$$
   $$\widehat{\sigma^2} := \big(\|\boldsymbol{y}\|^2 - \boldsymbol{y}^\top\mathbf{X}\overline{\boldsymbol{\beta}}\big)/n.$$

   (a) Show that the conditional density of the latent variables $\boldsymbol{\beta}$ and $\sigma^2$ is such that

   $$(\sigma^{-2}\mid\boldsymbol{\lambda},\boldsymbol{y}) \sim \mathsf{Gamma}\left(\frac{n}{2},\frac{n}{2}\widehat{\sigma^2}\right)$$
   $$(\boldsymbol{\beta}\mid\boldsymbol{\lambda},\sigma^2,\boldsymbol{y}) \sim \mathcal{N}(\overline{\boldsymbol{\beta}},\sigma^2\boldsymbol{\Sigma}).$$

   (b) Use Theorem C.2 to show that the expected complete-data log-likelihood is

   > Margin cross-reference: see p. 430 (Theorem C.2).

   $$-\frac{\overline{\boldsymbol{\beta}}^\top\mathbf{D}^{-1}\overline{\boldsymbol{\beta}}}{2\widehat{\sigma^2}} - \frac{\mathrm{tr}(\mathbf{D}^{-1}\boldsymbol{\Sigma})+\ln|\mathbf{D}|}{2} + c_1,$$

   where $c_1$ is a constant that does not depend on $\boldsymbol{\lambda}$.

   (c) Use Theorem A.2 to simplify the expected complete-data log-likelihood and to show that it is maximized at $\lambda_i = \boldsymbol{\Sigma}_{ii}+(\overline{\beta}_i/\widehat{\sigma})^2$ for $i=1,\ldots,p$. Hence, deduce the following E and M steps in the EM algorithm:

   > Margin cross-reference: see p. 359 (Theorem A.2).

   **E-step.** Given $\boldsymbol{\lambda}$, update $(\boldsymbol{\Sigma},\overline{\boldsymbol{\beta}},\widehat{\sigma^2})$ via the formulas (6.42).

   **M-step.** Given $(\boldsymbol{\Sigma},\overline{\boldsymbol{\beta}},\widehat{\sigma^2})$, update $\boldsymbol{\lambda}$ via $\lambda_i = \boldsymbol{\Sigma}_{ii}+(\overline{\beta}_i/\widehat{\sigma})^2$, $i=1,\ldots,p$.

   (d) Write Python code to compute $\boldsymbol{\lambda}^*$ via the EM algorithm, and use it to select the best polynomial model in Example 2.10. A possible stopping criterion is to terminate the EM iterations when

   $$\ln g(\boldsymbol{y}\mid\boldsymbol{\lambda}_{t+1}) - \ln g(\boldsymbol{y}\mid\boldsymbol{\lambda}_t) < \varepsilon$$

   for some small $\varepsilon>0$, where the marginal log-likelihood is

   $$\ln g(\boldsymbol{y}\mid\boldsymbol{\lambda}) = -\frac{n}{2}\ln(n\pi\widehat{\sigma^2}) - \frac{1}{2}\ln|\mathbf{D}| + \frac{1}{2}\ln|\boldsymbol{\Sigma}| + \ln\Gamma(n/2).$$

20. In this exercise we explore how the *early stopping* of the *gradient descent* iterations (see Example B.10),

   > Margin cross-reference: see p. 412 (Example B.10).
   > **Margin note — EARLY STOPPING.**

   $$\boldsymbol{x}_{t+1} = \boldsymbol{x}_t - \alpha\nabla f(\boldsymbol{x}_t), \quad t=0,1,\ldots,$$

   is (approximately) equivalent to the global minimization of $f(\boldsymbol{x}) + \frac{1}{2}\gamma\|\boldsymbol{x}\|^2$ for certain values of the *ridge regularization* parameter $\gamma>0$ (see Example 6.1). We illustrate the *early stopping* idea on the quadratic function $f(\boldsymbol{x}) = \frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^\top\mathbf{H}(\boldsymbol{x}-\boldsymbol{\mu})$, where $\mathbf{H}\in\mathbb{R}^{n\times n}$ is a symmetric positive-definite (Hessian) matrix with eigenvalues $\{\lambda_k\}_{k=1}^n$.

   (a) Verify that for a symmetric matrix $\mathbf{A}\in\mathbb{R}^n$ such that $\mathbf{I}-\mathbf{A}$ is invertible, we have

   $$\mathbf{I} + \mathbf{A} + \cdots + \mathbf{A}^{t-1} = (\mathbf{I}-\mathbf{A}^t)(\mathbf{I}-\mathbf{A})^{-1}.$$

   (b) Let $\mathbf{H} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ be the diagonalization of $\mathbf{H}$ as per Theorem A.8. If $\boldsymbol{x}_0 = \mathbf{0}$, show that the formula for $\boldsymbol{x}_t$ is

   > Margin cross-reference: see p. 366 (Theorem A.8).

   $$\boldsymbol{x}_t = \boldsymbol{\mu} - \mathbf{Q}(\mathbf{I}-\alpha\boldsymbol{\Lambda})^t\mathbf{Q}^\top\boldsymbol{\mu}.$$

   Hence, deduce that a necessary condition for $\boldsymbol{x}_t$ to converge is $\alpha < 2/\max_k\lambda_k$.

   (c) Show that the minimizer of $f(\boldsymbol{x}) + \frac{1}{2}\gamma\|\boldsymbol{x}\|^2$ can be written as

   $$\boldsymbol{x}^* = \boldsymbol{\mu} - \mathbf{Q}(\mathbf{I}+\gamma^{-1}\boldsymbol{\Lambda})^{-1}\mathbf{Q}^\top\boldsymbol{\mu}.$$

   (d) For a fixed value of $t$, let the learning rate $\alpha\downarrow 0$. Using part (b) and (c), show that if $\gamma\simeq 1/(t\alpha)$ as $\alpha\downarrow 0$, then $\boldsymbol{x}_t\simeq\boldsymbol{x}^*$. In other words, $\boldsymbol{x}_t$ is approximately equal to $\boldsymbol{x}^*$ for small $\alpha$, provided that $\gamma$ is inversely proportional to $t\alpha$.
