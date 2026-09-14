---
appendix: D
section: "D.13"
title: "Scikit-learn"
pdf_pages: "509-512"
---

## D.13 Scikit-learn

Scikit-learn is an open-source machine learning and data science library for Python. The library includes a range of algorithms relating to the chapters in this book. It is widely used due to its simplicity and its breadth. The module name is `sklearn`. Below is a brief introduction into modeling the data with `sklearn`. The full documentation can be found at

> https://scikit-learn.org/.

### D.13.1 Partitioning the Data

Randomly partitioning the data in order to test the model may be achieved easily with `sklearn`'s function `train_test_split`. For example, suppose that the training data is described by the matrix `X` of explanatory variables and the vector `y` of responses. Then the following code splits the data set into training and testing sets, with the testing set being half of the total set.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                        test_size = 0.5)
```

As an example, the following code generates a synthetic data set and splits it into equally-sized training and test sets.

**syndat.py**
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

np.random.seed(1234)

X=np.pi*(2*np.random.random(size=(400,2))-1)
y=(np.cos(X[:,0])*np.sin(X[:,1])>=0)

X_train , X_test , y_train , y_test = train_test_split(X, y,
    test_size=0.5)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X_train[y_train==0,0],X_train[y_train==0,1], c='g',
           marker='o',alpha=0.5)
ax.scatter(X_train[y_train==1,0],X_train[y_train==1,1], c='b',
           marker='o',alpha=0.5)
ax.scatter(X_test[y_test==0,0],X_test[y_test==0,1], c='g',
           marker='s',alpha=0.5)
ax.scatter(X_test[y_test==1,0],X_test[y_test==1,1], c='b',
           marker='s',alpha=0.5)

plt.savefig('sklearntraintest.pdf',format='pdf')
plt.show()
```

### D.13.2 Standardization

In some instances it may be necessary to standardize the data. This may be done in `sklearn` with scaling methods such as `MinMaxScaler` or `StandardScaler`. Scaling may improve the convergence of gradient-based estimators and is useful when visualizing data on vastly different scales. For example, suppose that `X` is our explanatory data (e.g., stored as a `numpy` array), and we wish to standardize such that each value lies between 0 and 1.

```python
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
x_scaled = min_max_scaler.fit_transform(X)
# equivalent to:
x_scaled = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
```

**Figure D.5:** Example training (circles) and test (squares) set for two class classification. Explanatory variables are the (*x*, *y*) coordinates, classes are zero (green) or one (blue).

### D.13.3 Fitting and Prediction

Once the data has been partitioned and standardized if necessary, the data may be fitted to a statistical model, e.g., a classification or regression model. For example, continuing with our data from above, the following fits a model to the data and predicts the responses for the test set.

```python
from sklearn.someSubpackage import someClassifier
clf = someClassifier()      # choose appropriate classifier
clf.fit(X_train, y_train)   # fit the data
y_prediction = clf.predict(X_test)  # predict
```

Specific classifiers for logistic regression, naïve Bayes, linear and quadratic discriminant analysis, *K*-nearest neighbors, and support vector machines are given in Section 7.8. *(See page 277.)*

### D.13.4 Testing the Model

Once the model has made its prediction we may test its effectiveness, using relevant metrics. For example, for classification we may wish to produce the confusion matrix for the test data. The following code does this for the data shown in Figure D.5, using a support vector machine classifier.

```python
from sklearn import svm
clf = svm.SVC(kernel = 'rbf')
clf.fit(X_train , y_train)
y_prediction = clf.predict(X_test)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test , y_prediction))
```
Output:
```
[[102  12]
 [  1  85]]
```
