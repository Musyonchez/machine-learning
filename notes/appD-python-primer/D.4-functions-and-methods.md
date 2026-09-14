---
appendix: D
section: "D.4"
title: "Functions and Methods"
pdf_pages: "486-488"
---

## D.4 Functions and Methods

Functions make it easier to divide a complex program into simpler parts. To create a *function*, use the following syntax:

```
def <function name>(<parameter_list>):
    <statements>
```

A function takes a list of input variables that are references to objects. Inside the function, a number of statements are executed which may modify the objects, but not the reference itself. In addition, the function may return an output object (or will return the value `None` if not explicitly instructed to return output). Think again of the shoe box analogy. The input variables of a function are labels of shoe boxes, and the objects to which they refer are the contents of the shoe boxes. The following program highlights some of the subtleties of variables and objects in Python.

> **Tip:** Note that the statements within a function must be indented. This is Python's way to define where a function begins and ends.

```python
x = [1,2,3]

def change_list(y):
    y.append(100) # Append an element to the list referenced by y
    y[0]=0         # Modify the first element of the same list
    y = [2,3,4]    # The local y now refers to a different list
                   # The list to which y first referred does not change
    return sum(y)

print(change_list(x))
print(x)
```
Output:
```
9
[0, 2, 3, 100]
```

Variables that are defined inside a function only have *local scope*; that is, they are recognized only within that function. This allows the same variable name to be used in different functions without creating a conflict. If any variable is used within a function, Python first checks if the variable has local scope. If this is not the case (the variable has not been defined inside the function), then Python searches for that variable outside the function (the global scope). The following program illustrates several important points.

```python
from numpy import array, square, sqrt

x = array([1.2,2.3,4.5])

def stat(x):
    n = len(x)          #the length of x
    meanx = sum(x)/n
    stdx = sqrt(sum(square(x - meanx))/n)
    return [meanx,stdx]

print(stat(x))
```
Output:
```
[2.6666666666666665, 1.3719410418171119]
```

1. Basic math functions such as `sqrt` are unknown to the standard Python interpreter and need to be imported. More on this in Section D.5 below.

2. As was already mentioned, indentation is crucial. It shows where the function begins and ends.

3. No semicolons[^3] are needed to end lines, but the first line of the function definition (here line 5) must end with a colon (`:`).

4. Lists are not arrays (vectors of numbers), and vector operations cannot be performed on lists. However, the `numpy` module is designed specifically with efficient vector/matrix operations in mind. On the second code line, we define `x` as a vector (`ndarray`) object. Functions such as `square`, `sum`, and `sqrt` are then applied to such arrays. Note that we used the default Python functions `len` and `sum`. More on `numpy` in Section D.10.

5. Running the program with `stat(x)` instead of `print(stat(x))` in line 11 will not show any output in the console.

> **Tip:** To display the complete list of built-in functions, type (using double underscores) `dir(__builtin__)` .

[^3]: Semicolons can be used to put multiple commands on a single line.
