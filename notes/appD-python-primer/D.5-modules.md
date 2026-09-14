---
appendix: D
section: "D.5"
title: "Modules"
pdf_pages: "488-489"
---

## D.5 Modules

A Python *module* is a programming construct that is useful for organizing code into manageable parts. To each module with name `module_name` is associated a Python file `module_name.py` containing any number of definitions, e.g., of functions, classes, and variables, as well as executable statements. Modules can be imported into other programs using the syntax: `import <module_name> as <alias_name>`, where `<alias_name>` is a shorthand name for the module.

When imported into another Python file, the module name is treated as a *namespace*, providing a naming system where each object has its unique name. For example, different modules `mod1` and `mod2` can have different `sum` functions, but they can be distinguished by prefixing the function name with the module name via the dot notation, as in `mod1.sum` and `mod2.sum`. For example, the following code uses the `sqrt` function of the `numpy` module.

```python
import numpy as np
np.sqrt(2)
```
Output:
```
1.4142135623730951
```

A Python *package* is simply a directory of Python modules; that is, a collection of modules with additional startup information (some of which may be found in its `__path__` attribute). Python's built-in module is called `__builtins__`. Of the great many useful Python modules, Table D.2 gives a few.

**Table D.2: A few useful Python modules/packages.**

| Module | Description |
|---|---|
| `datetime` | Module for manipulating dates and times. |
| `matplotlib` | MATLAB-type plotting package |
| `numpy` | Fundamental package for scientific computing, including random number generation and linear algebra tools. Defines the ubiquitous `ndarray` class. |
| `os` | Python interface to the operating system. |
| `pandas` | Fundamental module for data analysis. Defines the powerful `DataFrame` class. |
| `pytorch` | Machine learning library that supports GPU computation. |
| `scipy` | Ecosystem for mathematics, science, and engineering, containing many tools for numerical computing, including those for integration, solving differential equations, and optimization. |
| `requests` | Library for performing HTTP requests and interfacing with the web. |
| `seaborn` | Package for statistical data visualization. |
| `sklearn` | Easy to use machine learning library. |
| `statsmodels` | Package for the analysis of statistical models. |

The `numpy` package contains various subpackages, such as `random`, `linalg`, and `fft`. More details are given in Section D.10.

> **Tip:** When using *Spyder*, press Ctrl+I in front of any object, to display its help file in a separate window.

As we have already seen, it is also possible to import only specific functions from a module using the syntax: `from <module_name> import <fnc1, fnc2, ...>`.

```python
from numpy import sqrt, cos
sqrt(2)
cos(1)
```
Output:
```
1.4142135623730951
0.5403023058681398
```

This avoids the tedious prefixing of functions via the (alias) of the module name. However, for large programs it is good practice to always use the prefix/alias name construction, to be able to clearly ascertain precisely which module a function being used belongs to.
