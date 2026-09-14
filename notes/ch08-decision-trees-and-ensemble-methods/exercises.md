---
chapter: 8
section: "Exercises"
title: "Exercises"
pdf_pages: "339-340"
---

## Exercises

1. Show that any training set $\tau = \{(\boldsymbol{x}, y_i), i = 1, \ldots, n\}$ can be fitted via a tree with zero training loss.

2. Suppose during the construction of a decision tree we wish to specify a constant regional prediction function $g^w$ on the region $\mathcal{R}_w$, based on the training data in $\mathcal{R}_w$, say $\{(\boldsymbol{x}_1, y_1), \ldots, (\boldsymbol{x}_k, y_k)\}$. Show that $g^w(\boldsymbol{x}) := k^{-1} \sum_{i=1}^k y_i$ minimizes the squared-error loss.

3. Using the program from Section 8.2.4, write a basic implementation of a decision tree for a binary classification problem. Implement the misclassification, Gini index, and entropy impurity criteria to split nodes. Compare the results.

4. Suppose in the decision tree of Example 8.1, there are 3 blue and 2 red data points in a certain tree region. Calculate the misclassification impurity, the Gini impurity, and the entropy impurity. Repeat these calculations for 2 blue and 3 red data points.

5. Consider the procedure of finding the best splitting rule for a categorical variable with $k$ labels from Section 8.3.4. Show that one needs to consider $2^k$ subsets of $\{1, \ldots, k\}$ to find the optimal partition of labels.

6. Reproduce Figure 8.6 using the following classification data.

```python
from sklearn.datasets import make_blobs
X, y =  make_blobs(n_samples=5000, n_features=10, centers=3,
                    random_state=10, cluster_std=10)
```

7. Prove (8.13); that is, show that

$$
\sum_{w \in \mathcal{W}} \left( \sum_{i=1}^n \mathbb{1}\{\boldsymbol{x}_i \in \mathcal{R}_w\} \text{Loss}(y_i, g^w(\boldsymbol{x}_i)) \right) = n\, \ell_\tau(g).
$$

8. Suppose $\tau$ is a training set with $n$ elements and $\tau^*$, also of size $n$, is obtained from $\tau$ by bootstrapping; that is, resampling with replacement. Show that for large $n$, $\tau^*$ does not contain a fraction of about $\mathrm{e}^{-1} \approx 0.37$ of the points from $\tau$.

9. Prove Equation (8.17).

10. Consider the following training/test split of the data. Construct a random forest regressor and identify the optimal subset size $m$ in the sense of $R^2$ score (see Remark 8.3).

```python
import numpy as np
from sklearn.datasets import make_friedman1
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# create regression problem
n_points = 1000 # points
x, y =  make_friedman1(n_samples=n_points, n_features=15,
                        noise=1.0, random_state=100)

# split to train/test set
x_train, x_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.33, random_state=100)
```

11. Explain why bagging decision trees are a special case of random forests.

12. Show that (8.28) holds.

13. Consider the following classification data and module imports:

```python
from sklearn.datasets import make_blobs
from sklearn.metrics import zero_one_loss
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier

X_train, y_train =  make_blobs(n_samples=5000, n_features=10,
    centers=3, random_state=10, cluster_std=5)
```

Using the gradient boosting algorithm with $B = 100$ rounds, plot the training loss as a function of $\gamma$, for $\gamma = 0.1, 0.3, 0.5, 0.7, 1$. What is your conclusion regarding the relation between $B$ and $\gamma$?
