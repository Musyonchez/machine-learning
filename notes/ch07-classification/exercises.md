---
chapter: 7
section: "Exercises"
title: "Exercises"
pdf_pages: "297-304"
---

## Exercises

1. Let $0 \leqslant w \leqslant 1$. Show that the solution to the convex optimization problem

$$\min_{p_1,\dots,p_n} \sum_{i=1}^n p_i^2$$
$$\text{subject to:} \quad \sum_{i=1}^{n-1} p_i = w \text{ and } \sum_{i=1}^n p_i = 1, \tag{7.28}$$

is given by $p_i = w/(n-1)$, $i=1,\dots,n-1$ and $p_n = 1-w$.

2. Derive the formulas (7.14) by minimizing the cross-entropy training loss:

$$-\frac{1}{n}\sum_{i=1}^n \ln g(\boldsymbol{x}_i, y_i \mid \boldsymbol{\theta}),$$

where $g(\boldsymbol{x}, y \mid \boldsymbol{\theta})$ is such that:

$$\ln g(\boldsymbol{x}, y \mid \boldsymbol{\theta}) = \ln \alpha_y - \frac{1}{2}\ln|\boldsymbol{\Sigma}_y| - \frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu}_y)^\top \boldsymbol{\Sigma}_y^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_y) - \frac{p}{2}\ln(2\pi).$$

3. Adapt the code in Example 7.2 to plot the estimated decision boundary instead of the true one in Figure 7.3. Compare the true and estimated decision boundaries.

4. Recall from equation (7.16) that the decision boundaries of the multi-logit classifier are linear, and that the pre-classifier can be written as a conditional pdf of the form:

$$g(y \mid \mathbf{W}, \boldsymbol{b}, \boldsymbol{x}) = \frac{\exp(z_{y+1})}{\sum_{i=1}^c \exp(z_i)}, \quad y \in \{0,\dots,c-1\},$$

where $\boldsymbol{x}^\top = [1, \widetilde{\boldsymbol{x}}^\top]$ and $\boldsymbol{z} = \mathbf{W}\widetilde{\boldsymbol{x}} + \boldsymbol{b}$.

   (a) Show that the linear discriminant pre-classifier in Section 7.4 can also be written as a conditional pdf of the form ($\boldsymbol{\theta} = \{\alpha_y, \boldsymbol{\Sigma}_y, \boldsymbol{\mu}_y\}_{y=0}^{c-1}$):

   $$g(y \mid \boldsymbol{\theta}, \boldsymbol{x}) = \frac{\exp(z_{y+1})}{\sum_{i=1}^c \exp(z_i)}, \quad y \in \{0,\dots,c-1\},$$

   where $\boldsymbol{x}^\top = [1, \widetilde{\boldsymbol{x}}^\top]$ and $\boldsymbol{z} = \mathbf{W}\widetilde{\boldsymbol{x}} + \boldsymbol{b}$. Find formulas for the corresponding $\boldsymbol{b}$ and $\mathbf{W}$ in terms of the linear discriminant parameters $\{\alpha_y, \boldsymbol{\mu}_y, \boldsymbol{\Sigma}_y\}_{y=0}^{c-1}$, where $\boldsymbol{\Sigma}_y = \boldsymbol{\Sigma}$ for all $y$.

   (b) Explain which pre-classifier has smaller approximation error: the linear discriminant or multi-logit one? Justify your answer by proving an inequality between the two approximation errors.

5. Consider a binary classification problem where the response $Y$ takes values in $\{-1,1\}$. Show that optimal prediction function for the hinge loss $\text{Loss}(y,\widehat{y}) = (1-y\widehat{y})_+ := \max\{0, 1-y\widehat{y}\}$ is the same as the optimal prediction function $g^*$ for the indicator loss:

$$g^*(\boldsymbol{x}) = \begin{cases} 1 & \text{if } \mathbb{P}[Y=1 \mid \boldsymbol{X}=\boldsymbol{x}] > 1/2, \\ -1 & \text{if } \mathbb{P}[Y=1 \mid \boldsymbol{X}=\boldsymbol{x}] < 1/2. \end{cases}$$

That is, show that

$$\mathbb{E}(1 - Yh(\boldsymbol{X}))_+ \geqslant \mathbb{E}(1 - Yg^*(\boldsymbol{X}))_+ \tag{7.29}$$

for all functions $h$.

6. *(☞ 159)* In Example 4.12, we applied a principal component analysis (PCA) to the `iris` data, but refrained from classifying the flowers based on their feature vectors $\boldsymbol{x}$. Implement a 1-nearest neighbor algorithm, using a training set of 50 randomly chosen data pairs $(\boldsymbol{x},y)$ from the `iris` data set. How many of the remaining 100 flowers are correctly classified? Now classify these entries with an off-the-shelf multi-logit classifier, e.g., such as can be found in the `sklearn` and `statsmodels` packages.

7. Figure 7.13 displays two groups of data points, given in Table 7.8. The convex hulls have also been plotted. It is possible to separate the two classes of points via a straight line. In fact, many such lines are possible. SVM gives the best separation, in the sense that the gap (margin) between the points is maximal.

> **Figure 7.13:** A scatter plot of two groups of points (blue dots, upper-right cluster; red asterisks, lower-left cluster) from Table 7.8, each with its convex hull drawn as a polygon outline. The two convex hulls are disjoint, illustrating that the groups are linearly separable, and the exercise asks the reader to separate them by a straight line so that the separation between the two groups is maximal.

Table 7.8: Data for Figure 7.13.

| $x_1$ | $x_2$ | $y$ | $x_1$ | $x_2$ | $y$ |
|---|---|---|---|---|---|
| 2.4524 | 5.5673 | $-1$ | 0.5819 | $-1.0156$ | 1 |
| 1.2743 | 0.8265 | 1 | 1.2065 | 3.2984 | $-1$ |
| 0.8773 | $-0.5478$ | 1 | 2.6830 | 0.4216 | 1 |
| 1.4837 | 3.0464 | $-1$ | $-0.0734$ | 1.3457 | 1 |
| 0.0628 | 4.0415 | $-1$ | 0.0787 | 0.6363 | 1 |
| $-2.4151$ | $-0.9309$ | 1 | 0.3816 | 5.2976 | $-1$ |
| 1.8152 | 3.9202 | $-1$ | 0.3386 | 0.2882 | 1 |
| 1.8557 | 2.7262 | $-1$ | $-0.1493$ | $-0.7095$ | 1 |
| $-0.4239$ | 1.8349 | 1 | 1.5554 | 4.9880 | $-1$ |
| 1.9630 | 0.6942 | 1 | 3.2031 | 4.4614 | $-1$ |

   (a) Identify from the figure the three support vectors.

   (b) For a separating boundary (line) given by $\beta_0 + \boldsymbol{\beta}^\top \boldsymbol{x} = 0$, show that the margin width is $2/\lVert \boldsymbol{\beta} \rVert$.

   (c) Show that the parameters $\beta_0$ and $\boldsymbol{\beta}$ that solve the convex optimization problem (7.24) provide the maximal width between the margins.

   (d) Solve (7.24) using a penalty approach; see Section B.4 *(☞ 415)*. In particular, minimize the penalty function

   $$S(\boldsymbol{\beta},\beta_0) = \lVert \boldsymbol{\beta} \rVert^2 - C \sum_{i=1}^n \min\{(\beta_0 + \boldsymbol{\beta}^\top \boldsymbol{x}_i)y_i - 1,\, 0\}$$

   for some positive penalty constant $C$.

   (e) Find the solution the dual optimization problem (7.21) by using `sklearn`'s `SCV` method. Note that, as the two point sets are separable, the constraint $\lambda \leqslant 1$ may be removed, and the value of $\gamma$ can be set to 1.

8. In Example 7.6 we used the feature map $\boldsymbol{\phi}(\boldsymbol{x}) = [x_1, x_2, x_1^2+x_2^2]^\top$ to classify the points. An easier way is to map the points into $\mathbb{R}^1$ via the feature map $\phi(\boldsymbol{x}) = \lVert \boldsymbol{x} \rVert$ or any monotone function thereof. Translated back into $\mathbb{R}^2$ this yields a circular separating boundary. Find the radius and center of this circle, using the fact that here the sorted norms for the two groups are $\dots, 0.4889, 0.5528, \dots$.

9. Let $Y \in \{0,1\}$ be a response variable and let $h(\boldsymbol{x})$ be the regression function

$$h(\boldsymbol{x}) := \mathbb{E}[Y \mid \boldsymbol{X}=\boldsymbol{x}] = \mathbb{P}[Y=1 \mid \boldsymbol{X}=\boldsymbol{x}].$$

Recall that the Bayes classifier is $g^*(\boldsymbol{x}) = \mathbb{1}\{h(\boldsymbol{x}) > 1/2\}$. Let $g : \mathbb{R} \to \{0,1\}$ be any other classifier function. Below, we denote all probabilities and expectations conditional on $\boldsymbol{X}=\boldsymbol{x}$ as $\mathbb{P}_x[\cdot]$ and $\mathbb{E}_x[\cdot]$.

   (a) Show that

   $$\mathbb{P}_x[g(\boldsymbol{x}) \neq Y] = \underbrace{\mathbb{P}_x[g^*(\boldsymbol{x}) \neq Y]}_{\text{irreducible error}} + |2h(\boldsymbol{x})-1|\,\mathbb{1}\{g(\boldsymbol{x}) \neq g^*(\boldsymbol{x})\}.$$

   Hence, deduce that for a learner $g_\mathcal{T}$ constructed from a training set $\mathcal{T}$, we have

   $$\mathbb{E}[\mathbb{P}_x[g_\mathcal{T}(\boldsymbol{x}) \neq Y \mid \mathcal{T}]] = \mathbb{P}_x[g^*(\boldsymbol{x}) \neq Y] + |2h(\boldsymbol{x})-1|\, \mathbb{P}[g_\mathcal{T}(\boldsymbol{x}) \neq g^*(\boldsymbol{x})],$$

   where the first expectation and last probability operations are with respect to $\mathcal{T}$.

   (b) Using the previous result, deduce that for the unconditional error (that is, we no longer condition on $\boldsymbol{X}=\boldsymbol{x}$), we have

   $$\mathbb{P}[g^*(\boldsymbol{X}) \neq Y] \leqslant \mathbb{P}[g_\mathcal{T}(\boldsymbol{X}) \neq Y].$$

   (c) Show that, if $g_\mathcal{T} := \mathbb{1}\{h_\mathcal{T}(\boldsymbol{x}) > 1/2\}$ is a classifier function such that as $n \to \infty$

   $$h_\mathcal{T}(\boldsymbol{x}) \xrightarrow{\text{d}} Z \sim \mathcal{N}(\mu(\boldsymbol{x}), \sigma^2(\boldsymbol{x}))$$

   for some mean and variance functions $\mu(\boldsymbol{x})$ and $\sigma^2(\boldsymbol{x})$, respectively, then

   $$\mathbb{P}_x[g_\mathcal{T}(\boldsymbol{x}) \neq g^*(\boldsymbol{x})] \longrightarrow \Phi\!\left(\frac{\text{sign}(1-2h(\boldsymbol{x}))(2\mu(\boldsymbol{x})-1)}{2\sigma(\boldsymbol{x})}\right),$$

   where $\Phi$ is the cdf of a standard normal random variable.

10. The purpose of this exercise is to derive the dual program (7.21) from the primal program (7.20). The starting point is to introduce a vector of auxiliary variables $\boldsymbol{\xi} := [\xi_1,\dots,\xi_n]^\top$ and write the primal program as

$$\min_{\alpha_0,\boldsymbol{\alpha},\boldsymbol{\xi}} \sum_{i=1}^n \xi_i + \frac{\gamma}{2}\boldsymbol{\alpha}^\top \mathbf{K}\boldsymbol{\alpha}$$
$$\text{subject to:} \quad \boldsymbol{\xi} \geqslant \boldsymbol{0},$$
$$y_i(\alpha_0 + \{\mathbf{K}\boldsymbol{\alpha}\}_i) \geqslant 1-\xi_i,\ i=1,\dots,n. \tag{7.30}$$

    (a) Apply the Lagrangian optimization theory from Section B.2.2 to obtain the Lagrangian function $\mathcal{L}(\{\alpha_0,\boldsymbol{\alpha},\boldsymbol{\xi}\},\{\boldsymbol{\lambda},\boldsymbol{\mu}\})$, where $\boldsymbol{\mu}$ and $\boldsymbol{\lambda}$ are the Lagrange multipliers corresponding to the first and second inequality constraints, respectively. *(☞ 406)*

    (b) Show that the Karush–Kuhn–Tucker (see Theorem B.2) conditions for optimizing $\mathcal{L}$ are: *(☞ 407)*

    $$\boldsymbol{\lambda}^\top \boldsymbol{y} = 0$$
    $$\boldsymbol{\alpha} = \boldsymbol{y} \odot \boldsymbol{\lambda}/\gamma$$
    $$\boldsymbol{0} \leqslant \boldsymbol{\lambda} \leqslant \boldsymbol{1}$$
    $$(\boldsymbol{1}-\boldsymbol{\lambda}) \odot \boldsymbol{\xi} = \boldsymbol{0}, \quad \lambda_i(y_i g(\boldsymbol{x}_i) - 1 + \xi_i) = 0,\ i=1,\dots,n \tag{7.31}$$
    $$\boldsymbol{\xi} \geqslant \boldsymbol{0}, \quad y_i g(\boldsymbol{x}_i) - 1 + \xi_i \geqslant 0,\ i=1,\dots,n.$$

    Here $\odot$ stands for componentwise multiplication; e.g., $\boldsymbol{y} \odot \boldsymbol{\lambda} = [y_1\lambda_1,\dots,y_n\lambda_n]^\top$, and we have abbreviated $\alpha_0 + \{\mathbf{K}\boldsymbol{\alpha}\}_i$ to $g(\boldsymbol{x}_i)$, in view of (7.19). [Hint: one of the KKT conditions is $\boldsymbol{\lambda} = \boldsymbol{1}-\boldsymbol{\mu}$; thus we can eliminate $\boldsymbol{\mu}$.]

    (c) Using the KKT conditions (7.31), reduce the Lagrange dual function $\mathcal{L}^*(\boldsymbol{\lambda}) := \min_{\alpha_0,\boldsymbol{\alpha},\boldsymbol{\xi}} \mathcal{L}(\{\alpha_0,\boldsymbol{\alpha},\boldsymbol{\xi}\},\{\boldsymbol{\lambda},\boldsymbol{1}-\boldsymbol{\lambda}\})$ to

    $$\mathcal{L}^*(\boldsymbol{\lambda}) = \sum_{i=1}^n \lambda_i - \frac{1}{2\gamma}\sum_{i=1}^n\sum_{j=1}^n \lambda_i\lambda_j y_i y_j \kappa(\boldsymbol{x}_i,\boldsymbol{x}_j). \tag{7.32}$$

    (d) As a consequence of (7.19) and (a)–(c), show that the optimal prediction function $g_\tau$ is given by

    $$g_\tau(\boldsymbol{x}) = \alpha_0 + \frac{1}{\gamma}\sum_{i=1}^n y_i \lambda_i \kappa(\boldsymbol{x}_i,\boldsymbol{x}), \tag{7.33}$$

    where $\boldsymbol{\lambda}$ is the solution to

    $$\max_{\boldsymbol{\lambda}} \quad \mathcal{L}^*(\boldsymbol{\lambda})$$
    $$\text{subject to:} \quad \boldsymbol{\lambda}^\top \boldsymbol{y} = 0,\quad \boldsymbol{0} \leqslant \boldsymbol{\lambda} \leqslant \boldsymbol{1}, \tag{7.34}$$

    and $\alpha_0 = y_j - \frac{1}{\gamma}\sum_{i=1}^n y_i \lambda_i \kappa(\boldsymbol{x}_i,\boldsymbol{x}_j)$ for any $j$ such that $\lambda_j \in (0,1)$.

11. Consider SVM classification as illustrated in Figure 7.7. The goal of this exercise is to classify the training points $\{(\boldsymbol{x}_i,y_i)\}$ based on the value of the multipliers $\{\lambda_i\}$ in Exercise 10. Let $\xi_i$ be the auxiliary variable in Exercise 10, $i=1,\dots,n$.

    (a) For $\lambda_i \in (0,1)$ show that $(\boldsymbol{x}_i,y_i)$ lies exactly on the decision border.

    (b) For $\lambda_i = 1$, show that $(\boldsymbol{x}_i,y_i)$ lies strictly inside the margins.

    (c) Show that for $\lambda_i = 0$ the point $(\boldsymbol{x}_i,y_i)$ lies outside the margins and is correctly classified.

12. A well-known data set is the MNIST handwritten digit database, containing many thousands of digitalized numbers (from 0 to 9), each described by a $28 \times 28$ matrix of gray scales. A similar but much smaller data set is described in [63]. Here, each handwritten digit is summarized by a $8 \times 8$ matrix with integer entries from 0 (white) to 15 (black). Figure 7.14 shows the first 50 digitized images. The data set can be accessed with Python using the `sklearn` package as follows.

```python
from sklearn import datasets
digits = datasets.load_digits()
x_digits = digits.data    # explanatory variables
y_digits = digits.target  # responses
```

> **Figure 7.14:** A $5 \times 10$ grid of grayscale images, each an $8\times8$ pixel handwritten digit from the `sklearn` digits data set, showing the first 50 digitized images (roughly cycling through digits 0–9 in a noisy, imperfect order) that the exercise asks the reader to classify.

    (a) Divide the data into a 75% training set and 25% test set.

    (b) Compare the effectiveness of the $K$-nearest neighbors and naïve Bayes method to classify the data.

    (c) Assess which $K$ to use in the $K$-nearest neighbors classification.

13. Download the `winequality-red.csv` data set from UCI's wine-quality website. The response here is the wine quality (from 0 to 10) as specified by a wine "expert" and the explanatory variables are various characteristics such as acidity and sugar content. Use the `SVC` classifier of `sklearn.svm` with a linear kernel and penalty parameter $C=1$ (see Remark 7.2) to fit the data. Use the method `cross_val_score` from `sklearn.model_selection` to obtain a five-fold cross-validation score as an estimate of the probability that the predicted class matches the expert's class.

14. Consider the credit approval data set `crx.data` from UCI's credit approval website. The data set is concerned with credit card applications. The last column in the data set indicates whether the application is approved (+) or not (−). With the view of preserving data privacy, all 15 explanatory variables were anonymized. Note that some explanatory variables are continuous and some are categorical.

    (a) Load and prepare the data for analysis with `sklearn`. First, eliminate data rows with missing values. Next, encode categorical explanatory variables using a `OneHotEncoder` object from `sklearn.preprocessing` to create a model matrix $\mathbf{X}$ with indicator variables for the categorical variables, as described in Section 5.3.5 *(☞ 177)*.

    (b) The model matrix should contain 653 rows and 46 columns. The response variable should be a 0/1 variable (reject/approve). We will consider several classification algorithms and test their performance (using a zero-one loss) via ten-fold cross validation.

       i. Write a function which takes 3 parameters: $\mathbf{X}$, $\boldsymbol{y}$, and a model, and returns the ten-fold cross-validation estimate of the expected generalization risk.

       ii. Consider the following `sklearn` classifiers: `KNeighborsClassifier` ($k=5$), `LogisticRegression`, and `MPLClassifier` (multilayer perceptron). Use the function from (i) to identify the best performing classifier.

15. Consider a synthetic data set that was generated in the following fashion. The explanatory variable follows a standard normal distribution. The response label is 0 if the explanatory variable is between the 0.95 and 0.05 quantiles of the standard normal distribution, and 1, otherwise. The data set was generated using the following code.

```python
import numpy as np
import scipy.stats
# generate data

np.random.seed(12345)
N = 100
X = np.random.randn(N)
q = scipy.stats.norm.ppf(0.95)
y = np.zeros(N)
y[X>=q] = 1
y[X<=-q] = 1
X = X.reshape(-1,1)
```

Compare the $K$-nearest neighbors classifier with $K=5$ and logistic regression classifier. Without computation, which classifier is likely to be better for these data? Verify your answer by coding both classifiers and printing the corresponding training 0–1 loss.

16. Consider the `digits` data set from Exercise 12. In this exercise, we would like to train a binary classifier for the identification of digit 8.

    (a) Divide the data such that the first 1000 rows are used as the training set and the rest are used as the test set.

    (b) Train the `LogisticRegression` classifier from the `sklearn.linear_model` package.

    (c) "Train" a naïve classifier that always returns 0. That is, the naïve classifier identifies each instance as being not 8.

    (d) Compare the zero-one test losses of the logistic regression and naïve classifiers.

    (e) Find the confusion matrix, the precision, and the recall of the logistic regression classifier.

    (f) Find the fraction of eights that are correctly detected by the logistic regression classifier.

17. Repeat Exercise 16 with the original MNIST data set. Use the first 60,000 rows as the train set and the remaining 10,000 rows as the test set. The original data set can be obtained using the following code.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
```

18. *(☞ 277, ☞ 253)* For the breast cancer data in Section 7.8, investigate and discuss whether *accuracy* is the relevant metric to use or if other metrics discussed in Section 7.2 are more appropriate.
