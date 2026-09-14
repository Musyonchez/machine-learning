---
chapter: 9
section: "Exercises"
title: "Exercises"
pdf_pages: "368-372"
---

## Exercises

1. Show that the softmax function

$$\text{softmax} : \boldsymbol{z} \mapsto \frac{\exp(\boldsymbol{z})}{\sum_k \exp(z_k)}$$

satisfies the invariance property:

$$\text{softmax}(\boldsymbol{z}) = \text{softmax}(\boldsymbol{z}+c\times\mathbf{1}), \quad \text{for any constant } c.$$

2. *Projection pursuit* is a network with one hidden layer that can be written as:

$$g(\boldsymbol{x}) = S(\boldsymbol{\omega}^\top\boldsymbol{x}),$$

where $S$ is a univariate *smoothing cubic spline*. (☞ Cross-reference: p. 235) If we use squared-error loss with $\tau_n = \{y_i,\boldsymbol{x}_i\}_{i=1}^{n}$, we need to minimize the training loss:

$$\frac{1}{n}\sum_{i=1}^{n}\left(y_i - S(\boldsymbol{\omega}^\top\boldsymbol{x}_i)\right)^2$$

with respect to $\boldsymbol{\omega}$ and all cubic smoothing splines. This training of the network is typically tackled iteratively in a manner similar to the *EM algorithm*. (☞ Cross-reference: p. 139) In particular, we iterate ($t = 1,2,\dots$) the following steps until convergence.

   (a) Given the *missing data* $\boldsymbol{\omega}_t$, compute the spline $S_t$ by training a cubic smoothing spline on $\{y_i, \boldsymbol{\omega}_t^\top \boldsymbol{x}_i\}$. The smoothing coefficient of the spline may be determined as part of this step.

   (b) Given the spline function $S_t$, compute the next projection vector $\boldsymbol{\omega}_{t+1}$ via *iterative reweighted least squares*:

$$\boldsymbol{\omega}_{t+1} = \operatorname*{argmin}_{\boldsymbol{\beta}} (\boldsymbol{e}_t - \mathbf{X}\boldsymbol{\beta})^\top \boldsymbol{\Sigma}_t (\boldsymbol{e}_t - \mathbf{X}\boldsymbol{\beta}), \tag{9.11}$$

where

$$e_{t,i} := \boldsymbol{\omega}_t^\top\boldsymbol{x}_i + \frac{y_i - S_t(\boldsymbol{\omega}_t^\top\boldsymbol{x}_i)}{S_t'(\boldsymbol{\omega}_t^\top\boldsymbol{x}_i)}, \quad i = 1,\dots,n,$$

is the adjusted response, and $\boldsymbol{\Sigma}_t^{1/2} = \text{diag}(S_t'(\boldsymbol{\omega}_t^\top\boldsymbol{x}_1),\dots,S_t'(\boldsymbol{\omega}_t^\top\boldsymbol{x}_n))$ is a diagonal matrix.

   Apply Taylor's Theorem B.1 to the function $S_t$ and derive the iterative reweighted least-squares optimization program (9.11). (☞ Cross-reference: p. 400)

3. Suppose that in the *stochastic gradient descent* method we wish to repeatedly draw minibatches of size $N$ from $\tau_n$, where we assume that $N\times m = n$ for some large integer $m$. (☞ Cross-reference: p. 336) Instead of repeatedly resampling from $\tau_n$, an alternative is to reshuffle $\tau_n$ via a random permutation $\mathbf{\Pi}$ and then advance sequentially through the reshuffled training set to construct $m$ non-overlapping minibatches. (☞ Cross-reference: p. 115) A single traversal of such a reshuffled training set is called an *epoch*. The following pseudo-code describes the procedure.

**Algorithm 9.5.1: Stochastic Gradient Descent with Reshuffling**

**input:** Training set $\tau_n = \{(\boldsymbol{x}_i,\boldsymbol{y}_i)\}_{i=1}^{n}$, initial weight matrices and bias vectors $\{\mathbf{W}_l,\boldsymbol{b}_l\}_{l=1}^{L} \to \boldsymbol{\theta}_1$, activation functions $\{\boldsymbol{S}_l\}_{l=1}^{L}$, learning rates $\{\alpha_1,\alpha_2,\dots\}$.
**output:** The parameters of the trained learner.

1. $t \leftarrow 1$ and epoch $\leftarrow 0$
2. **while** stopping condition is not met **do**
3. $\quad$ Draw $U_1,\dots,U_n \overset{\text{iid}}{\sim} \mathcal{U}(0,1)$.
4. $\quad$ Let $\mathbf{\Pi}$ be the permutation of $\{1,\dots,n\}$ that satisfies $U_{\Pi_1} < \cdots < U_{\Pi_n}$.
5. $\quad (\boldsymbol{x}_i,\boldsymbol{y}_i) \leftarrow (\boldsymbol{x}_{\Pi_i}, \boldsymbol{y}_{\Pi_i})$ for $i=1,\dots,n$ *// reshuffle $\tau_n$*
6. $\quad$ **for** $j = 1,\dots,m$ **do**
7. $\quad\quad \widehat{\ell_\tau} \leftarrow \dfrac{1}{N}\sum_{i=(j-1)N+1}^{jN} \text{Loss}(\boldsymbol{y}_i, \boldsymbol{g}(\boldsymbol{x}_i\mid\boldsymbol{\theta}))$
8. $\quad\quad \boldsymbol{\theta}_{t+1} \leftarrow \boldsymbol{\theta}_t - \alpha_t\dfrac{\partial\widehat{\ell_\tau}}{\partial\boldsymbol{\theta}}(\boldsymbol{\theta}_t)$
9. $\quad\quad t \leftarrow t+1$
10. $\quad$ epoch $\leftarrow$ epoch $+ 1$ *// number of reshuffles or epochs*
11. **return** $\boldsymbol{\theta}_t$ as the minimizer of the training loss

Write Python code that implements the stochastic gradient descent with data reshuffling, and use it to train the neural net in Section 9.5.1. (☞ Cross-reference: p. 341)

4. Denote the pdf of the $\mathcal{N}(\mathbf{0},\boldsymbol{\Sigma})$ distribution by $\varphi_{\boldsymbol{\Sigma}}(\cdot)$, and let

$$\mathcal{D}(\boldsymbol{\mu}_0,\boldsymbol{\Sigma}_0\mid\boldsymbol{\mu}_1,\boldsymbol{\Sigma}_1) = \int_{\mathbb{R}^d} \varphi_{\boldsymbol{\Sigma}_0}(\boldsymbol{x}-\boldsymbol{\mu}_0)\ln\frac{\varphi_{\boldsymbol{\Sigma}_0}(\boldsymbol{x}-\boldsymbol{\mu}_0)}{\varphi_{\boldsymbol{\Sigma}_1}(\boldsymbol{x}-\boldsymbol{\mu}_1)}\,\mathrm{d}\boldsymbol{x}$$

be the Kullback–Leibler divergence between the densities of the $\mathcal{N}(\boldsymbol{\mu}_0,\boldsymbol{\Sigma}_0)$ and $\mathcal{N}(\boldsymbol{\mu}_1,\boldsymbol{\Sigma}_1)$ distributions on $\mathbb{R}^d$. (☞ Cross-reference: p. 42) Show that

$$2\mathcal{D}(\boldsymbol{\mu}_0,\boldsymbol{\Sigma}_0\mid\boldsymbol{\mu}_1,\boldsymbol{\Sigma}_1) = \text{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0) - \ln|\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0| + (\boldsymbol{\mu}_1-\boldsymbol{\mu}_0)^\top\boldsymbol{\Sigma}_1^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_0) - d.$$

Hence, deduce the formula in (B.22).

5. Suppose that we wish to compute the inverse and log-determinant of the matrix

$$\mathbf{I}_n + \mathbf{U}\mathbf{U}^\top,$$

where $\mathbf{U}$ is an $n\times h$ matrix with $h \ll n$. Show that

$$(\mathbf{I}_n+\mathbf{U}\mathbf{U}^\top)^{-1} = \mathbf{I}_n - \mathbf{Q}_n\mathbf{Q}_n^\top,$$

where $\mathbf{Q}_n$ contains the first $n$ rows of the $(n+h)\times h$ matrix $\mathbf{Q}$ in the QR factorization of the $(n+h)\times h$ matrix: (☞ Cross-reference: p. 375)

$$\begin{bmatrix}\mathbf{U}\\ \mathbf{I}_h\end{bmatrix} = \mathbf{Q}\mathbf{R}.$$

In addition, show that $\ln|\mathbf{I}_n+\mathbf{U}\mathbf{U}^\top| = \sum_{i=1}^{h}\ln r_{ii}^2$, where $\{r_{ii}\}$ are the diagonal elements of the $h\times h$ matrix $\mathbf{R}$.

6. Suppose that

$$\mathbf{U} = [\boldsymbol{u}_0,\boldsymbol{u}_1,\dots,\boldsymbol{u}_{h-1}],$$

where all $\boldsymbol{u} \in \mathbb{R}^n$ are column vectors and we have computed $(\mathbf{I}_n+\mathbf{U}\mathbf{U}^\top)^{-1}$ via the QR factorization method in Exercise 5. If the columns of matrix $\mathbf{U}$ are updated to

$$[\boldsymbol{u}_1,\dots,\boldsymbol{u}_{h-1},\boldsymbol{u}_h],$$

show that the inverse $(\mathbf{I}_n+\mathbf{U}\mathbf{U}^\top)^{-1}$ can be updated in $O(hn)$ time (rather than computed from scratch in $O(h^2n)$ time). Deduce that the computing cost of updating the Hessian approximation (9.10) is the same as that for the *limited-memory BFGS* Algorithm 9.4.3.

   In your solution you may use the following facts from [29]. Suppose we are given the $\mathbf{Q}$ and $\mathbf{R}$ factors in the QR factorization of a matrix $\mathbf{A} \in \mathbb{R}^{n\times h}$. If a row/column is added to matrix $\mathbf{A}$, then the $\mathbf{Q}$ and $\mathbf{R}$ factors need not be recomputed from scratch (in $O(h^2n)$ time), but can be updated efficiently in $O(hn)$ time. Similarly, if a row/column is removed from matrix $\mathbf{A}$, then the $\mathbf{Q}$ and $\mathbf{R}$ factors can be updated in $O(h^2)$ time.

7. Suppose that $\mathbf{U} \in \mathbb{R}^{n\times h}$ has its $k$-th column $\boldsymbol{v}$ replaced with $\boldsymbol{w}$, giving the updated $\widetilde{\mathbf{U}}$.

   (a) If $\boldsymbol{e} \in \mathbb{R}^h$ denotes the unit-length vector such that $e_k = \|\boldsymbol{e}\| = 1$ and

$$\boldsymbol{r}_{\pm} := \frac{\sqrt{2}}{2}\mathbf{U}^\top(\boldsymbol{w}-\boldsymbol{v}) + \frac{\sqrt{2}\|\boldsymbol{w}-\boldsymbol{v}\|^2}{4}\boldsymbol{e} \pm \frac{\sqrt{2}}{2}\boldsymbol{e},$$

show that

$$\widetilde{\mathbf{U}}^\top\widetilde{\mathbf{U}} = \mathbf{U}^\top\mathbf{U} + \boldsymbol{r}_+\boldsymbol{r}_+^\top - \boldsymbol{r}_-\boldsymbol{r}_-^\top.$$

[Hint: You may find Exercise 16 in Chapter 6 useful.] (☞ Cross-reference: p. 247)

   (b) Let $\mathbf{B} := (\mathbf{I}_h+\mathbf{U}^\top\mathbf{U})^{-1}$. Use the *Woodbury identity* (A.15) to show that (☞ Cross-reference: p. 371)

$$(\mathbf{I}_n+\widetilde{\mathbf{U}}\widetilde{\mathbf{U}}^\top)^{-1} = \mathbf{I}_n - \widetilde{\mathbf{U}}\left(\mathbf{B}^{-1}+\boldsymbol{r}_+\boldsymbol{r}_+^\top-\boldsymbol{r}_-\boldsymbol{r}_-^\top\right)^{-1}\widetilde{\mathbf{U}}^\top.$$

   (c) Suppose that we have stored $\mathbf{B}$ in computer memory. Use Algorithm 6.8.1 and parts (a) and (b) to write pseudo-code that updates $(\mathbf{I}_n+\mathbf{U}\mathbf{U}^\top)^{-1}$ to $(\mathbf{I}_n+\widetilde{\mathbf{U}}\widetilde{\mathbf{U}}^\top)^{-1}$ in $O((n+h)h)$ computing time.

8. Equation (9.7) gives the rank-two BFGS update of the inverse Hessian $\mathbf{C}_{t-1}$ to $\mathbf{C}_t$. Instead of using a two-rank update, we can consider a one-rank update, in which $\mathbf{C}_{t-1}$ is updated to $\mathbf{C}_t$ by the general rank-one formula:

$$\mathbf{C}_t = \mathbf{C}_{t-1} + \upsilon_t \boldsymbol{r}_t\boldsymbol{r}_t^\top.$$

Find values for the scalar $\upsilon_t$ and vector $\boldsymbol{r}_t$, such that $\mathbf{C}_t$ satisfies the secant condition $\mathbf{C}_t\boldsymbol{g}_t = \boldsymbol{\delta}_t$.

9. Show that the *BFGS formula* (B.23) can be written as:

$$\mathbf{C} \leftarrow \left(\mathbf{I}-\upsilon\boldsymbol{g}\boldsymbol{\delta}^\top\right)^\top \mathbf{C}\left(\mathbf{I}-\upsilon\boldsymbol{g}\boldsymbol{\delta}^\top\right) + \upsilon\boldsymbol{\delta}\boldsymbol{\delta}^\top,$$

where $\upsilon := (\boldsymbol{g}^\top\boldsymbol{\delta})^{-1}$.

10. Show that the *BFGS formula* (B.23) is the solution to the constrained optimization problem:

$$\mathbf{C}_{\text{BFGS}} = \operatorname*{argmin}_{\mathbf{A} \text{ subject to } \mathbf{A}\boldsymbol{g}=\boldsymbol{\delta}, \mathbf{A}=\mathbf{A}^\top} \mathcal{D}(\mathbf{0},\mathbf{C}\mid\mathbf{0},\mathbf{A}),$$

where $\mathcal{D}$ is the Kullback–Leibler discrepancy defined in (B.22). On the other hand, show that the *DFP formula* (B.24) is the solution to the constrained optimization problem:

$$\mathbf{C}_{\text{DFP}} = \operatorname*{argmin}_{\mathbf{A} \text{ subject to } \mathbf{A}\boldsymbol{g}=\boldsymbol{\delta}, \mathbf{A}=\mathbf{A}^\top} \mathcal{D}(\mathbf{0},\mathbf{A}\mid\mathbf{0},\mathbf{C}).$$

11. Consider again the logistic regression model in Exercise 5.18, which used *iterative reweighted least squares* for training the learner. (☞ Cross-reference: p. 213) Repeat all the computations, but this time using the *limited-memory BFGS* Algorithm 9.4.4. Which training algorithm converges faster to the optimal solution?

12. Download the `seeds_dataset.txt` data set from the book's GitHub site, which contains 210 independent examples. The categorical output (response) here is the type of wheat grain: Kama, Rosa, and Canadian (encoded as 1, 2, and 3), so that $c=3$. The seven continuous features (explanatory variables) are measurements of the geometric properties of the grain (area, perimeter, compactness, length, width, asymmetry coefficient, and length of kernel groove). Thus, $\boldsymbol{x} \in \mathbb{R}^7$ (which does not include the constant feature 1) and the multi-logit pre-classifier in Example 9.2 can be written as $\boldsymbol{g}(\boldsymbol{x}) = \text{softmax}(\mathbf{W}\boldsymbol{x}+\boldsymbol{b})$, where $\mathbf{W} \in \mathbb{R}^{3\times 7}$ and $\boldsymbol{b} \in \mathbb{R}^3$. (☞ Cross-reference: p. 329) Implement and train this pre-classifier on the first $n=105$ examples of the seeds data set using, for example, Algorithm 9.4.1. Use the remaining $n'=105$ examples in the data set to estimate the generalization risk of the learner using the cross-entropy loss. [Hint: Use the cross-entropy loss formulas from Example 9.4.]

13. In Exercise 12 above, we train the multi-logit classifier using a weight matrix $\mathbf{W} \in \mathbb{R}^{3\times 7}$ and bias vector $\boldsymbol{b} \in \mathbb{R}^3$. Repeat the training of the multi-logit model, but this time keeping $z_1$ as an arbitrary constant (say $z_1=0$), and thus setting $c=0$ to be a "reference" class. This has the effect of removing a node from the output layer of the network, giving a weight matrix $\mathbf{W} \in \mathbb{R}^{2\times 7}$ and bias vector $\boldsymbol{b} \in \mathbb{R}^2$ of smaller dimensions than in (7.16). (☞ Cross-reference: p. 267)

14. Consider again Example 9.4, where we used a *softmax* output function $\boldsymbol{S}_L$ in conjunction with the *cross-entropy* loss: $C(\boldsymbol{\theta}) = -\ln g_{y+1}(\boldsymbol{x}\mid\boldsymbol{\theta})$. (☞ Cross-reference: p. 334) Find formulas for $\dfrac{\partial C}{\partial \boldsymbol{g}}$ and $\dfrac{\partial \boldsymbol{S}_L}{\partial \boldsymbol{z}_L}$. Hence, verify that:

$$\frac{\partial \boldsymbol{S}_L}{\partial\boldsymbol{z}_L}\frac{\partial C}{\partial\boldsymbol{g}} = \boldsymbol{g}(\boldsymbol{x}\mid\boldsymbol{\theta}) - \boldsymbol{e}_{y+1},$$

where $\boldsymbol{e}_i$ is the unit length vector with an entry of 1 in the $i$-th position.

15. Derive the formula (B.25) for a diagonal Hessian update in a quasi-Newton method for minimization. (☞ Cross-reference: p. 412) In other words, given a current minimizer $\boldsymbol{x}_t$ of $f(\boldsymbol{x})$, a diagonal matrix $\mathbf{C}$ of approximating the Hessian of $f$, and a gradient vector $\boldsymbol{u} = \nabla f(\boldsymbol{x}_t)$, find the solution to the constrained optimization program:

$$\min_{\mathbf{A}} \mathcal{D}(\boldsymbol{x}_t, \mathbf{C}\mid \boldsymbol{x}_t - \mathbf{A}\boldsymbol{u}, \mathbf{A})$$
$$\text{subject to: } \mathbf{A}\boldsymbol{g} \geqslant \boldsymbol{\delta}, \ \mathbf{A} \text{ is diagonal},$$

where $\mathcal{D}$ is the Kullback–Leibler distance defined in (B.22) (see Exercise 4).

16. Consider again the Python implementation of the polynomial regression in Section 9.5.1, where the *stochastic gradient descent* was used for training.

    Using the polynomial regression data set, implement and run the following four alternative training methods:

    (a) the steepest-descent Algorithm 9.4.1;

    (b) the Levenberg–Marquardt Algorithm B.3.3, in conjunction with Algorithm 9.4.2 for computing the matrix of Jacobi; (☞ Cross-reference: p. 415)

    (c) the *limited-memory BFGS* Algorithm 9.4.4;

    (d) the *Adam* Algorithm 9.4.5, which uses past gradient values to determine the next search direction.

    For each training algorithm, using trial and error, tune any algorithmic parameters so that the network training is as fast as possible. Comment on the relative advantages and disadvantages of each training/optimization method. For example, comment on which optimization method makes rapid initial progress, but gets trapped in a suboptimal solution, and which method is slower, but more consistent in finding good optima.

17. Consider again the `Pytorch` code in Section 9.5.2. Repeat all the computations, but this time using the *momentum* method for training of the network. Comment on which method is preferable: the *momentum* or the *Adam* method?
