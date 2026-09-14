---
chapter: 5
section: "Exercises"
title: "Exercises"
pdf_pages: "225-232"
---

## Exercises

1. Following his mentor Francis Galton, the mathematician/statistician Karl Pearson conducted comprehensive studies comparing hereditary traits between members of the same family. Figure 5.10 depicts the measurements of the heights of 1078 fathers and their adult sons (one son per father). The data is available from the book's GitHub site as `pearson.csv`.

   (a) Show that sons are on average 1 inch taller than the fathers.

   (b) We could try to "explain" the height of the son by taking the height of his father and adding 1 inch. The prediction line $y=x+1$ (red dashed) is given Figure 5.10. The black solid line is the fitted regression line. This line has a slope less than 1, and demonstrates Galton's "regression" to the average. Find the intercept and slope of the fitted regression line.

> **Figure 5.10:** A scatterplot of heights from Pearson's data — father's height (in) on the horizontal axis against son's height (in) on the vertical axis. The red dashed line is $y=x+1$, and the black solid line is the fitted least-squares regression line, which has a shallower slope than the dashed line, illustrating regression to the mean.

2. For the simple linear regression model, show that the values for $\widehat{\beta}_1$ and $\widehat{\beta}_0$ that solve the equations (5.9) are:

$$\widehat{\beta}_1 = \frac{\sum_{i=1}^n (x_i-\overline{x})(y_i-\overline{y})}{\sum_{i=1}^n (x_i-\overline{x})^2} \tag{5.40}$$

$$\widehat{\beta}_0 = \overline{y} - \widehat{\beta}_1\overline{x}, \tag{5.41}$$

provided that not all $x_i$ are the same.

3. Edwin Hubble discovered that the universe is expanding. If $v$ is a galaxy's recession velocity (relative to any other galaxy) and $d$ is its distance (from that same galaxy), Hubble's law states that

$$v = Hd,$$

where $H$ is known as Hubble's constant. The following are distance (in millions of light-years) and velocity (thousands of miles per second) measurements made on five galactic clusters.

| distance | 68 | 137 | 315 | 405 | 700 |
|---|---|---|---|---|---|
| velocity | 2.4 | 4.7 | 12.0 | 14.4 | 26.0 |

State the regression model and estimate $H$.

4. The multiple linear regression model (5.6) can be viewed as a first-order approximation of the general model

$$Y = g(\boldsymbol{x}) + \varepsilon, \tag{5.42}$$

where $\mathbb{E}\,\varepsilon=0$, $\mathbb{V}\text{ar}\,\varepsilon=\sigma^2$, and $g(\boldsymbol{x})$ is some known or unknown function of a $d$-dimensional vector $\boldsymbol{x}$ of explanatory variables. To see this, replace $g(\boldsymbol{x})$ with its first-order Taylor approximation around some point $\boldsymbol{x}_0$ and write this as $\beta_0+\boldsymbol{x}^\top\boldsymbol{\beta}$. Express $\beta_0$ and $\boldsymbol{\beta}$ in terms of $g$ and $\boldsymbol{x}_0$.

5. Table 5.6 shows data from an agricultural experiment where crop yield was measured for two levels of pesticide and three levels of fertilizer. There are three responses for each combination.

**Table 5.6: Crop yields for pesticide and fertilizer combinations.**

| Pesticide | Fertilizer: Low | Fertilizer: Medium | Fertilizer: High |
|---|---|---|---|
| No | 3.23, 3.20, 3.16 | 2.99, 2.85, 2.77 | 5.72, 5.77, 5.62 |
| Yes | 6.78, 6.73, 6.79 | 9.07, 9.09, 8.86 | 8.12, 8.04, 8.31 |

   (a) Organize the data in standard form, where each row corresponds to a single measurement and the columns correspond to the response variable and the two factor variables.

   (b) Let $Y_{ijk}$ be the response for the $k$-th replication at level $i$ for factor 1 and level $j$ for factor 2. To assess which factors best explain the response variable, we use the ANOVA model

   $$Y_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk}, \tag{5.43}$$

   where $\sum_i\alpha_i = \sum_j\beta_j = \sum_i\gamma_{ij} = \sum_j\gamma_{ij} = 0$. Define $\boldsymbol{\beta} = [\mu,\alpha_1,\alpha_2,\beta_1,\beta_2,\beta_3,\gamma_{11},\gamma_{12},\gamma_{13},\gamma_{21},\gamma_{22},\gamma_{23}]^\top$. Give the corresponding $18\times12$ model matrix.

   (c) Note that the parameters are linearly dependent in this case. For example, $\alpha_2=-\alpha_1$ and $\gamma_{13}=-(\gamma_{11}+\gamma_{12})$. To retain only 6 linearly independent variables consider the 6-dimensional parameter vector $\widetilde{\boldsymbol{\beta}} = [\mu,\alpha_1,\beta_1,\beta_2,\gamma_{11},\gamma_{12}]^\top$. Find the matrix $\mathbf{M}$ such that $\mathbf{M}\widetilde{\boldsymbol{\beta}} = \boldsymbol{\beta}$.

   (d) Give the model matrix corresponding to $\widetilde{\boldsymbol{\beta}}$.

6. Show that for the birthweight data in Section 5.6.6.2 there is no significant decrease in birthweight for smoking mothers. [Hint: create a new variable `nonsmoke = 1-smoke`, which reverses the encoding for the smoking and non-smoking mothers. Then, the parameter $\beta_1+\beta_3$ in the original model is the same as the parameter $\beta_1$ in the model

$$\texttt{Bwt} = \beta_0 + \beta_1\,\texttt{age} + \beta_2\,\texttt{nonsmoke} + \beta_3\,\texttt{age}\times\texttt{nonsmoke} + \varepsilon.$$

Now find a 95% for $\beta_3$ and see if it contains zero.]

7. Prove (5.37) and (5.38).

8. In the *Tobit regression* model with normally distributed errors, the response is modeled as:

$$Y_i = \begin{cases}Z_i, & \text{if } u_i < Z_i \\ u_i, & \text{if } Z_i \leqslant u_i\end{cases}, \qquad \boldsymbol{Z}\sim\mathcal{N}(\mathbf{X}\boldsymbol{\beta},\sigma^2\mathbf{I}_n),$$

where the model matrix $\mathbf{X}$ and the thresholds $u_1,\dots,u_n$ are given. Typically, $u_i=0, i=1,\dots,n$. Suppose we wish to estimate $\boldsymbol{\theta} := (\boldsymbol{\beta},\sigma^2)$ via the Expectation–Maximization method, similar to the censored data Example 4.2. Let $\boldsymbol{y}=[y_1,\dots,y_n]^\top$ be the vector of observed data.

   (a) Show that the likelihood of $\boldsymbol{y}$ is:

   $$g(\boldsymbol{y}\mid\boldsymbol{\theta}) = \prod_{i:y_i>u_i}\varphi_{\sigma^2}(y_i-\boldsymbol{x}_i^\top\boldsymbol{\beta}) \times \prod_{i:y_i=u_i}\Phi((u_i-\boldsymbol{x}_i^\top\boldsymbol{\beta})/\sigma),$$

   where $\Phi$ is the cdf of the $\mathcal{N}(0,1)$ distribution and $\varphi_{\sigma^2}$ the pdf of the $\mathcal{N}(0,\sigma^2)$ distribution.

   (b) Let $\overline{\boldsymbol{y}}$ and $\underline{\boldsymbol{y}}$ be vectors that collect all $y_i>u_i$ and $y_i=u_i$, respectively. Denote the corresponding matrix of predictors by $\overline{\mathbf{X}}$ and $\underline{\mathbf{X}}$, respectively. For each observation $y_i=u_i$ introduce a latent variable $z_i$ and collect these into a vector $\boldsymbol{z}$. For the same indices $i$ collect the corresponding $u_i$ into a vector $\boldsymbol{c}$. Show that the complete-data likelihood is given by

   $$g(\boldsymbol{y},\boldsymbol{z}\mid\boldsymbol{\theta}) = \frac{1}{(2\pi\sigma^2)^{n/2}}\exp\left(-\frac{\|\overline{\boldsymbol{y}}-\overline{\mathbf{X}}\boldsymbol{\beta}\|^2}{2\sigma^2} - \frac{\|\boldsymbol{z}-\underline{\mathbf{X}}\boldsymbol{\beta}\|^2}{2\sigma^2}\right)\mathbb{1}\{\boldsymbol{z}\leqslant\boldsymbol{c}\}.$$

   (c) For the E-step, show that, for a fixed $\boldsymbol{\theta}$,

   $$g(\boldsymbol{z}\mid\boldsymbol{y},\boldsymbol{\theta}) = \prod_i g(z_i\mid\boldsymbol{y},\boldsymbol{\theta}),$$

   where each $g(z_i\mid\boldsymbol{y},\boldsymbol{\theta})$ is the pdf of the $\mathcal{N}((\underline{\mathbf{X}}\boldsymbol{\beta})_i,\sigma^2)$ distribution, truncated to the interval $(-\infty,c_i]$.

   (d) For the M-step, compute the expectation of the complete log-likelihood

   $$-\frac{n}{2}\ln\sigma^2 - \frac{n}{2}\ln(2\pi) - \frac{\|\overline{\boldsymbol{y}}-\overline{\mathbf{X}}\boldsymbol{\beta}\|^2}{2\sigma^2} - \frac{\mathbb{E}\|\boldsymbol{Z}-\underline{\mathbf{X}}\boldsymbol{\beta}\|^2}{2\sigma^2}.$$

   Then, derive the formulas for $\boldsymbol{\beta}$ and $\sigma^2$ that maximize the expectation of the complete log-likelihood.

9. Download data set `WomenWage.csv` from the book's website. This data set is a tidied-up version of the women's wages data set from [91]. The first column of the data (`hours`) is the response variable $Y$. It shows the hours spent in the labor force by married women in the 1970s. We want to understand what factors determine the participation rate of women in the labor force. The predictor variables are:

**Table 5.7: Features for the women's wage data set.**

| Feature | Description |
|---|---|
| `kidslt6` | Number of children younger than 6 years. |
| `kidsge6` | Number of children older than 6 years. |
| `age` | Age of the married woman. |
| `educ` | Number of years of formal education. |
| `exper` | Number of years of "work experience". |
| `nwifeinc` | Non-wife income, that is, the income of the husband. |
| `expersq` | The square of `exper`, to capture any nonlinear relationships. |

   We observe that some of the responses are $Y=0$, that is, some women did not participate in the labor force. For this reason, we model the data using the Tobit regression model, in which the response $Y$ is given as:

   $$Y_i = \begin{cases}Z_i, & \text{if } Z_i>0 \\ 0, & \text{if } Z_i\leqslant0\end{cases}, \qquad \boldsymbol{Z}\sim\mathcal{N}(\mathbf{X}\boldsymbol{\beta},\sigma^2\mathbf{I}_n).$$

   With $\boldsymbol{\theta}=(\boldsymbol{\beta},\sigma^2)$, the likelihood of the data $\boldsymbol{y}=[y_1,\dots,y_n]^\top$ is:

   $$g(\boldsymbol{y}\mid\boldsymbol{\theta}) = \prod_{i:y_i>0}\varphi_{\sigma^2}(y_i-\boldsymbol{x}_i^\top\boldsymbol{\beta}) \times \prod_{i:y_i=0}\Phi((u_i-\boldsymbol{x}_i^\top\boldsymbol{\beta})/\sigma),$$

   where $\Phi$ is the standard normal cdf. In Exercise 8, we derived the EM algorithm for maximizing the log-likelihood.

   (a) Write down the EM algorithm in pseudo code as it applies to this Tobit regression.

   (b) Implement the EM algorithm pseudo code in Python. Comment on which factor you think is important in determining the labor participation rate of women living in the USA in the 1970s.

10. Let $\mathbf{P}$ be a projection matrix. Show that the diagonal elements of $\mathbf{P}$ all lie in the interval $[0,1]$. In particular, for $\mathbf{P}=\mathbf{X}\mathbf{X}^+$ in Theorem 5.1, the leverage value $p_i := \mathbf{P}_{ii}$ satisfies $0\leqslant p_i\leqslant 1$ for all $i$.

11. Consider the linear model $\boldsymbol{Y}=\mathbf{X}\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ in (5.8), with $\mathbf{X}$ being the $n\times p$ model matrix and $\boldsymbol{\varepsilon}$ having expectation vector $\mathbf{0}$ and covariance matrix $\sigma^2\mathbf{I}_n$. Suppose that $\widehat{\boldsymbol{\beta}}_{-i}$ is the least-squares estimate obtained by omitting the $i$-th observation, $Y_i$; that is,

$$\widehat{\boldsymbol{\beta}}_{-i} = \underset{\boldsymbol{\beta}}{\text{argmin}}\sum_{j\neq i}(Y_j-\boldsymbol{x}_j^\top\boldsymbol{\beta})^2,$$

where $\boldsymbol{x}_j^\top$ is the $j$-th row of $\mathbf{X}$. Let $\widehat{Y}_{-i} = \boldsymbol{x}_i^\top\widehat{\boldsymbol{\beta}}_{-i}$ be the corresponding fitted value at $\boldsymbol{x}_i$. Also, define $\boldsymbol{B}_i$ as the least-squares estimator of $\boldsymbol{\beta}$ based on the response data

$$\boldsymbol{Y}^{(i)} := [Y_1,\dots,Y_{i-1},\widehat{Y}_{-i},Y_{i+1},\dots,Y_n]^\top.$$

   (a) Prove that $\widehat{\boldsymbol{\beta}}_{-i} = \boldsymbol{B}_i$; that is, the linear model obtained from fitting all responses except the $i$-th is the same as the one obtained from fitting the data $\boldsymbol{Y}^{(i)}$.

   (b) Use the previous result to verify that

   $$Y_i - \widehat{Y}_{-i} = (Y_i-\widehat{Y}_i)/(1-\mathbf{P}_{ii}),$$

   where $\mathbf{P}=\mathbf{X}\mathbf{X}^+$ is the projection matrix onto the columns of $\mathbf{X}$. Hence, deduce the PRESS formula in Theorem 5.1.

12. Take the linear model $\boldsymbol{Y}=\mathbf{X}\boldsymbol{\beta}+\boldsymbol{\varepsilon}$, where $\mathbf{X}$ is an $n\times p$ model matrix, $\boldsymbol{\varepsilon}=\mathbf{0}$, and $\mathbb{C}\text{ov}(\boldsymbol{\varepsilon})=\sigma^2\mathbf{I}_n$. Let $\mathbf{P}=\mathbf{X}\mathbf{X}^+$ be the projection matrix onto the columns of $\mathbf{X}$.

   (a) Using the properties of the pseudo-inverse (see Definition A.2), show that $\mathbf{P}\mathbf{P}^\top=\mathbf{P}$.

   (b) Let $\boldsymbol{E}=\boldsymbol{Y}-\widehat{\boldsymbol{Y}}$ be the (random) vector of residuals, where $\widehat{\boldsymbol{Y}}=\mathbf{P}\boldsymbol{Y}$. Show that the $i$-th residual has a normal distribution with expectation 0 and variance $\sigma^2(1-\mathbf{P}_{ii})$ (that is, $\sigma^2$ times 1 minus the $i$-th leverage).

   (c) Show that $\sigma^2$ can be unbiasedly estimated via

   $$S^2 := \frac{1}{n-p}\|\boldsymbol{Y}-\widehat{\boldsymbol{Y}}\|^2 = \frac{1}{n-p}\|\boldsymbol{Y}-\mathbf{X}\widehat{\boldsymbol{\beta}}\|^2. \tag{5.44}$$

   [Hint: use the cyclic property of the trace as in Example 2.3.]

13. Consider a normal linear model $\boldsymbol{Y}=\mathbf{X}\boldsymbol{\beta}+\boldsymbol{\varepsilon}$, where $\mathbf{X}$ is an $n\times p$ model matrix and $\boldsymbol{\varepsilon}\sim\mathcal{N}(\mathbf{0},\sigma^2\mathbf{I}_n)$. Exercise 12 shows that for any such model the $i$-th standardized residual $E_i/(\sigma\sqrt{1-\mathbf{P}_{ii}})$ has a standard normal distribution. This motivates the use of the leverage $\mathbf{P}_{ii}$ to assess whether the $i$-th observation is an outlier depending on the size of the $i$-th residual relative to $\sqrt{1-\mathbf{P}_{ii}}$. A more robust approach is to include an estimate for $\sigma$ using all data except the $i$-th observation. This gives rise to the *studentized residual* $T_i$, defined as

$$T_i := \frac{E_i}{S_{-i}\sqrt{1-\mathbf{P}_{ii}}},$$

where $S_{-i}$ is an estimate of $\sigma$ obtained by fitting all the observations except the $i$-th and $E_i=Y_i-\widehat{Y}_i$ is the $i$-th (random) residual. Exercise 12 shows that we can take, for example,

$$S_{-i}^2 = \frac{1}{n-1-p}\|\boldsymbol{Y}_{-i}-\mathbf{X}_{-i}\widehat{\boldsymbol{\beta}}_{-i}\|^2, \tag{5.45}$$

where $\mathbf{X}_{-i}$ is the model matrix $\mathbf{X}$ with the $i$-th row removed, is an unbiased estimator of $\sigma^2$. We wish to compute $S_{-i}^2$ efficiently, using $S^2$ in (5.44), as the latter will typically be available once we have fitted the linear model. To this end, define $\boldsymbol{u}_i$ as the $i$-th unit vector $[0,\dots,0,1,0,\dots,0]^\top$, and let

$$\boldsymbol{Y}^{(i)} := \boldsymbol{Y} - (Y_i-\widehat{Y}_i)\boldsymbol{u}_i = \boldsymbol{Y} - \frac{E_i}{1-\mathbf{P}_{ii}}\boldsymbol{u}_i,$$

where we have used the fact that $Y_i-\widehat{Y}_{-i} = E_i/(1-\mathbf{P}_{ii})$, as derived in the proof of Theorem 5.1. Now apply Exercise 11 to prove that

$$S_{-i}^2 = \frac{(n-p)S^2 - E_i^2/(1-\mathbf{P}_{ii})}{n-p-1}.$$

14. Using the notation from Exercises 11–13, *Cook's distance* for observation $i$ is defined as

$$D_i := \frac{\|\widehat{\boldsymbol{Y}}-\widehat{\boldsymbol{Y}}^{(i)}\|^2}{p\,S^2}.$$

    It measures the change in the fitted values when the $i$-th observation is removed, relative to the residual variance of the model (estimated via $S^2$).

    By using similar arguments as those in Exercise 13, show that

    $$D_i = \frac{\mathbf{P}_{ii}E_i^2}{(1-\mathbf{P}_{ii})^2\,p\,S^2}.$$

    It follows that there is no need to "omit and refit" the linear model in order to compute Cook's distance for the $i$-th response.

15. Prove that if we add an additional feature to the general linear model, then $R^2$, the coefficient of determination, is necessarily non-decreasing in value and hence cannot be used to compare models with different numbers of predictors.

16. Let $\boldsymbol{X} := [X_1,\dots,X_n]^\top$ and $\boldsymbol{\mu} := [\mu_1,\dots,\mu_n]^\top$. In the fundamental Theorem C.9, we use the fact that if $X_i \sim \mathcal{N}(\mu_i,1)$, $i=1,\dots,n$ are independent, then $\|\boldsymbol{X}\|^2$ has (per definition) a noncentral $\chi^2_n$ distribution. Show that $\|\boldsymbol{X}\|^2$ has moment generating function

$$\frac{\mathrm{e}^{t\|\boldsymbol{\mu}\|^2/(1-2t)}}{(1-2t)^{n/2}}, \quad t<1/2,$$

and so the distribution of $\|\boldsymbol{X}\|^2$ depends on $\boldsymbol{\mu}$ only through the norm $\|\boldsymbol{\mu}\|$.

17. Carry out a logistic regression analysis on a (partial) *wine* data set classification problem. The data can be loaded using the following code.

```python
from sklearn import datasets
import numpy as np
data = datasets.load_wine()
X = data.data[:, [9,10]]
y = np.array(data.target==1,dtype=np.uint)
X = np.append(np.ones(len(X)).reshape(-1,1),X,axis=1)
```

    The model matrix has three features, including the constant feature. Instead of using Newton's method (5.39) to estimate $\boldsymbol{\beta}$, implement a simple gradient descent procedure

    $$\boldsymbol{\beta}_t = \boldsymbol{\beta}_{t-1} - \alpha\nabla r_\tau(\boldsymbol{\beta}_{t-1}),$$

    with learning rate $\alpha=0.0001$, and run it for $10^6$ steps. Your procedure should deliver three coefficients; one for the intercept and the rest for the explanatory variables. Solve the same problem using the `Logit` method of `statsmodels.api` and compare the results.

18. Consider again Example 5.10, where we train the learner via the Newton iteration (5.39). If $\mathbf{X}^\top := [\boldsymbol{x}_1,\dots,\boldsymbol{x}_n]$ defines the matrix of predictors and $\boldsymbol{\mu}_t := \boldsymbol{h}(\mathbf{X}\boldsymbol{\beta}_t)$, then the gradient (5.37) and Hessian (5.38) for Newton's method can be written as:

$$\nabla r_\tau(\boldsymbol{\beta}_i) = \frac{1}{n}\mathbf{X}^\top(\boldsymbol{\mu}_t-\boldsymbol{y}) \quad \text{and} \quad \mathbf{H}(\boldsymbol{\beta}_i) = \frac{1}{n}\mathbf{X}^\top\mathbf{D}_t\mathbf{X},$$

    where $\mathbf{D}_t := \text{diag}(\boldsymbol{\mu}_t\odot(\mathbf{1}-\boldsymbol{\mu}_t))$ is a diagonal matrix. Show that the Newton iteration (5.39) can be written as the *iterative reweighted least-squares* method:

    $$\boldsymbol{\beta}_t = \underset{\boldsymbol{\beta}}{\text{argmin}}\ (\widetilde{\boldsymbol{y}}_{t-1}-\mathbf{X}\boldsymbol{\beta})^\top\mathbf{D}_{t-1}(\widetilde{\boldsymbol{y}}_{t-1}-\mathbf{X}\boldsymbol{\beta}),$$

    where $\widetilde{\boldsymbol{y}}_{t-1} := \mathbf{X}\boldsymbol{\beta}_{t-1} + \mathbf{D}_{t-1}^{-1}(\boldsymbol{y}-\boldsymbol{\mu}_{t-1})$ is the so-called *adjusted response*. [Hint: use the fact that $(\mathbf{M}^\top\mathbf{M})^{-1}\mathbf{M}^\top\boldsymbol{z}$ is the minimizer of $\|\mathbf{M}\boldsymbol{\beta}-\boldsymbol{z}\|^2$.]

19. In *multi-output linear regression*, the response variable is a real-valued vector of dimension, say, $m$. Similar to (5.8), the model can be written in matrix notation:

$$\mathbf{Y} = \mathbf{X}\mathbf{B} + \begin{bmatrix}\boldsymbol{\varepsilon}_1^\top\\\vdots\\\boldsymbol{\varepsilon}_n^\top\end{bmatrix},$$

    where:

    - $\mathbf{Y}$ is an $n\times m$ matrix of $n$ independent responses (stored as row vectors of length $m$);
    - $\mathbf{X}$ is the usual $n\times p$ model matrix;
    - $\mathbf{B}$ is an $p\times m$ matrix of model parameters;
    - $\boldsymbol{\varepsilon}_1,\dots,\boldsymbol{\varepsilon}_n\in\mathbb{R}^m$ are independent error terms with $\mathbb{E}\,\boldsymbol{\varepsilon}=\mathbf{0}$ and $\mathbb{E}\,\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top=\boldsymbol{\Sigma}$.

    We wish to learn the matrix parameters $\mathbf{B}$ and $\boldsymbol{\Sigma}$ from the training set $\{\mathbf{Y},\mathbf{X}\}$. To this end, consider minimizing the training loss

    $$\frac{1}{n}\text{tr}\left((\mathbf{Y}-\mathbf{X}\mathbf{B})\boldsymbol{\Sigma}^{-1}(\mathbf{Y}-\mathbf{X}\mathbf{B})^\top\right),$$

    where $\text{tr}(\cdot)$ is the trace of a matrix.

    (a) Show that the minimizer of the training loss, denoted $\widehat{\mathbf{B}}$, satisfies the normal equations:

    $$\mathbf{X}^\top\mathbf{X}\widehat{\mathbf{B}} = \mathbf{X}^\top\mathbf{Y}.$$

    (b) Noting that

    $$(\mathbf{Y}-\mathbf{X}\mathbf{B})^\top(\mathbf{Y}-\mathbf{X}\mathbf{B}) = \sum_{i=1}^n \boldsymbol{\varepsilon}_i\boldsymbol{\varepsilon}_i^\top,$$

    explain why

    $$\widehat{\boldsymbol{\Sigma}} := \frac{(\mathbf{Y}-\mathbf{X}\widehat{\mathbf{B}})^\top(\mathbf{Y}-\mathbf{X}\widehat{\mathbf{B}})}{n}$$

    is a method-of-moments estimator of $\boldsymbol{\Sigma}$, just like the one given in (5.10).
