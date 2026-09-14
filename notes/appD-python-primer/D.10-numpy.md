---
appendix: D
section: "D.10"
title: "NumPy"
pdf_pages: "496-501"
---

## D.10 NumPy

The package NumPy (module name `numpy`) provides the building blocks for scientific computing in Python. It contains all the standard mathematical functions, such as `sin`, `cos`, `tan`, etc., as well as efficient functions for random number generation, linear algebra, and statistical computation.

```python
import numpy as np    #import the package
x = np.cos(1)
data = [1,2,3,4,5]
y = np.mean(data)
z = np.std(data)
print('cos(1) = {0:1.8f}  mean = {1}  std = {2}'.format(x,y,z))
```
Output:
```
cos(1) = 0.54030231  mean = 3.0  std = 1.4142135623730951
```

### D.10.1 Creating and Shaping Arrays

The fundamental data type in `numpy` is the `ndarray`. This data type allows for fast matrix operations via highly optimized numerical libraries such as LAPACK and BLAS; this in contrast to (nested) lists. As such, `numpy` is often essential when dealing with large amounts of quantitative data.

`ndarray` objects can be created in various ways. The following code creates a 2×3×2 array of zeros. Think of it as a 3-dimensional matrix or two stacked 3×2 matrices.

```python
A = np.zeros([2,3,2])  # 2 by 3 by 2 array of zeros
print(A)
print(A.shape)   # number of rows and columns
print(type(A))   # A is an ndarray
```
Output:
```
[[[ 0.  0.]
  [ 0.  0.]
  [ 0.  0.]]

 [[ 0.  0.]
  [ 0.  0.]
  [ 0.  0.]]]
(2, 3, 2)
<class 'numpy.ndarray'>
```

We will be mostly working with 2D arrays; that is, `ndarrays` that represent ordinary matrices. We can also use the `range` method and lists to create ndarrays via the `array` method. Note that `arange` is `numpy`'s version of `range`, with the difference that `arange` returns an `ndarray` object.

```python
a = np.array(range(4))    # equivalent to np.arange(4)
b = np.array([0,1,2,3])
C = np.array([[1,2,3],[3,2,1]])
print(a, '\n', b,'\n' , C)
```
Output:
```
[0 1 2 3]
[0 1 2 3]
 [[1 2 3]
 [3 2 1]]
```

The dimension of an `ndarray` can be obtained via its `shape` method, which returns a tuple. Arrays can be reshaped via the `reshape` method. This does not change the current `ndarray` object. To make the change permanent, a new instance needs to be created.

```python
a = np.array(range(9)) #a is an ndarray of shape (9,)
print(a.shape)
A = a.reshape(3,3)   #A is an ndarray of shape (3,3)
print(a)
print(A)
```
Output:
```
[0 1 2 3 4 5 6 7 8]
(9,)
[[0, 1, 2]
 [3, 4, 5]
 [6, 7, 8]]
```

> **Tip:** One shape dimension for `reshape` can be specified as −1. The dimension is then inferred from the other dimension(s).

The `'T'` attribute of an `ndarray` gives its transpose. Note that the transpose of a "vector" with shape `(n, )` is the same vector. To distinguish between column and row vectors, reshape such a vector to an *n*×1 and 1×*n* array, respectively.

```python
a = np.arange(3)   #1D array (vector) of shape (3,)
print(a)
print(a.shape)
b = a.reshape(-1,1) # 3x1 array (matrix) of shape (3,1)
print(b)
print(b.T)
A = np.arange(9).reshape(3,3)
print(A.T)
```
Output:
```
[0 1 2]
(3,)
[[0]
 [1]
 [2]]
[[0 1 2]]
[[0 3 6]
 [1 4 7]
 [2 5 8]]
```

Two useful methods of joining arrays are `hstack` and `vstack`, where the arrays are joined horizontally and vertically, respectively.

```python
A = np.ones((3,3))
B = np.zeros((3,2))
C = np.hstack((A,B))
print(C)
```
Output:
```
[[ 1.  1.  1.  0.  0.]
 [ 1.  1.  1.  0.  0.]
 [ 1.  1.  1.  0.  0.]]
```

### D.10.2 Slicing

Arrays can be sliced similarly to Python lists. If an array has several dimensions, a slice for each dimension needs to be specified. Recall that Python indexing starts at `'0'` and ends at `'len(obj)-1'`. The following program illustrates various slicing operations.

```python
A = np.array(range(9)).reshape(3,3)
print(A)
print(A[0])    # first row
print(A[:,1])  # second column
print(A[0,1])  # element in first row and second column
print(A[0:1,1:2])  # (1,1) ndarray containing A[0,1] = 1
print(A[1:,-1]) # elements in 2nd and 3rd rows, and last column
```
Output:
```
[[0 1 2]
 [3 4 5]
 [6 7 8]]
[0 1 2]
[1 4 7]
1
[[1]]
[5 8]
```

Note that `ndarrays` are mutable objects, so that elements can be modified directly, without having to create a new object.

```python
A[1:,1] = [0,0] # change two elements in the matrix A above
print(A)
```
Output:
```
[[0, 1, 2]
 [3, 0, 5]
 [6, 0, 8]]
```

### D.10.3 Array Operations

Basic mathematical operators and functions act *element-wise* on `ndarray` objects.

```python
x = np.array([[2,4],[6,8]])
y = np.array([[1,1],[2,2]])
print(x+y)
```
Output:
```
[[ 3,  5]
 [ 8, 10]]
```

```python
print(np.divide(x,y))   # same as x/y
```
Output:
```
[[ 2.  4.]
 [ 3.  4.]]
```

```python
print(np.sqrt(x))
```
Output:
```
[[1.41421356  2.        ]
 [2.44948974  2.82842712]]
```

In order to compute matrix multiplications and compute inner products of vectors, `numpy`'s `dot` function can be used, either as a method of an `ndarray` instance or as a method of `np`.

```python
print(np.dot(x,y))
```
Output:
```
[[10, 10]
 [22, 22]]
```

```python
print(x.dot(x))   # same as np.dot(x,x)
```
Output:
```
[[28, 40]
 [60, 88]]
```

Since version 3.5 of Python, it is possible to multiply two `ndarrays` using the `@` operator (which implements the `np.matmul` method). For matrices, this is similar to using the `dot` method. For higher-dimensional arrays the two methods behave differently.

```python
print(x @ y)
```
Output:
```
[[10 10]
 [22 22]]
```

NumPy allows arithmetic operations on arrays of different shapes (dimensions). Specifically, suppose two arrays have dimensions (*m*₁, *m*₂, ..., *m*ₚ) and (*n*₁, *n*₂, ..., *n*ₚ), respectively. The arrays or shapes are said to be *aligned* if for all *i* = 1, ..., *p* it holds that

- *mᵢ* = *nᵢ*, or
- min{*mᵢ*, *nᵢ*} = 1, or
- either *mᵢ* or *nᵢ*, or both are missing.

For example, shapes (1, 2, 3) and (4, 2, 1) are aligned, as are (2, ) and (1, 2, 3). However, (2, 2, 2) and (1, 2, 3) are not aligned. NumPy "duplicates" the array elements across the smaller dimension to match the larger dimension. This process is called *broadcasting* and is carried out without actually making copies, thus providing efficient memory use. Below are some examples.

```python
import numpy as np
A= np.arange(4).reshape(2,2) # (2,2) array

x1 = np.array([40,500])         # (2,) array
x2 = x1.reshape(2,1)           # (2,1) array

print(A + x1) # shapes (2,2) and (2,)
print(A * x2) # shapes (2,2) and (2,1)
```
Output:
```
[[ 40 501]
 [ 42 503]]
[[   0   40]
 [1000 1500]]
```

Note that above `x1` is duplicated row-wise and `x2` column-wise. Broadcasting also applies to the matrix-wise operator `@`, as illustrated below. Here, the matrix `b` is duplicated across the third dimension resulting in the two matrix multiplications of the 2×2 matrix `b` with each of the two 2×2 slices of the 2×2×2 array `B`.

```python
B = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print(B@b)
```
Output:
```
[[[ 2  3]
  [ 6 11]]

 [[10 19]
  [14 27]]]
```

Functions such as `sum`, `mean`, and `std` can also be executed as methods of an `ndarray` instance. The argument `axis` can be passed to specify along which dimension the function is applied. By default `axis=None`.

```python
a = np.array(range(4)).reshape(2,2)
print(a.sum(axis=0)) #summing over rows gives column totals
```
Output:
```
[2, 4]
```

### D.10.4 Random Numbers

One of the sub-modules in `numpy` is `random`. It contains many functions for random variable generation.

```python
import numpy as np
np.random.seed(123)  # set the seed for the random number generator
x = np.random.random()      # uniform (0,1)
y = np.random.randint(5,9)  # discrete uniform 5,...,8
z = np.random.randn(4)      # array of four standard normals
print(x,y,'\n',z)
```
Output:
```
0.6964691855978616 7
 [ 1.77399501 -0.66475792 -0.07351368  1.81403277]
```

For more information on random variable generation in `numpy`, see

> https://docs.scipy.org/doc/numpy/reference/random/index.html.
