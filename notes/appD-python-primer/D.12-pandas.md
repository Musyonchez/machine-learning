---
appendix: D
section: "D.12"
title: "Pandas"
pdf_pages: "504-509"
---

## D.12 Pandas

The Python package Pandas (module name `pandas`) provides various tools and data structures for data analytics, including the fundamental `DataFrame` class.

> For the code in this section we assume that `pandas` has been imported via `import pandas as pd`.

### D.12.1 Series and DataFrame

The two main data structures in `pandas` are `Series` and `DataFrame`. A `Series` object can be thought of as a combination of a dictionary and an 1-dimensional `ndarray`. The syntax for creating a `Series` object is

```
series = pd.Series(<data>, index=['index'])
```

Here, `<data>` some 1-dimensional data structure, such as a 1-dimensional `ndarray`, a list, or a dictionary, and `index` is a list of names of the same length as `<data>`. When `<data>` is a dictionary, the `index` is created from the keys of the dictionary. When `<data>` is an `ndarray` and `index` is omitted, the default index will be `[0, ..., len(data)-1]`.

```python
DICT = {'one':1, 'two':2, 'three':3, 'four':4}
print(pd.Series(DICT))
```
Output:
```
one      1
two      2
three    3
four     4
dtype: int64
```

```python
years =  ['2000','2001','2002']
cost = [2.34, 2.89, 3.01]
print(pd.Series(cost,index = years, name = 'MySeries')) #name it
```
Output:
```
2000    2.34
2001    2.89
2002    3.01
Name: MySeries, dtype: float64
```

The most commonly-used data structure in `pandas` is the two-dimensional `DataFrame`, which can be thought of as `pandas`' implementation of a spreadsheet or as a dictionary in which each "key" of the dictionary corresponds to a column name and the dictionary "value" is the data in that column. To create a `DataFrame` one can use the `pandas` `DataFrame` method, which has three main arguments: data, index (row labels), and columns (column labels).

```
DataFrame(<data>, index=['<row_name>'], columns=['<column_name>'])
```

If the index is not specified, the default index is `[0, ..., len(data)-1]`. Data can also be read directly from a CSV or Excel file, as is done in Section 1.1. *(See page 1.)* If a dictionary is used to create the data frame (as below), the dictionary keys are used as the column names.

```python
DICT = {'numbers':[1,2,3,4], 'squared':[1,4,9,16] }
df = pd.DataFrame(DICT, index = list('abcd'))
print(df)
```
Output:
```
   numbers  squared
a        1        1
b        2        4
c        3        9
d        4       16
```

### D.12.2 Manipulating Data Frames

Often data encoded in `DataFrame` or `Series` objects need to be extracted, altered, or combined. Getting, setting, and deleting columns works in a similar manner as for dictionaries. The following code illustrates various operations.

```python
ages = [6,3,5,6,5,8,0,3]
d={'Gender':['M', 'F']*4, 'Age': ages}
df1 = pd.DataFrame(d)

df1.at[0,'Age']= 60  # change an element
df1.at[1,'Gender'] = 'Female' # change another element
df2 = df1.drop('Age',1)  # drop a column
df3 = df2.copy();     # create a separate copy of df2
df3['Age'] = ages   # add the original column
dfcomb = pd.concat([df1,df2,df3],axis=1)  # combine the three dfs
print(dfcomb)
```
Output:
```
  Gender  Age  Gender  Gender  Age
0      M   60       M       M    6
1  Female    3  Female  Female    3
2      M    5       M       M    5
3      F    6       F       F    6
4      M    5       M       M    5
5      F    8       F       F    8
6      M    0       M       M    0
7      F    3       F       F    3
```

Note that the above `DataFrame` object has two `Age` columns. The expression `dfcomb['Age']` will return a `DataFrame` with both these columns.

**Table D.3: Useful `pandas` methods for data manipulation.**

| Method | Description |
|---|---|
| `agg` | Aggregate the data using one or more functions. |
| `apply` | Apply a function to a column or row. |
| `astype` | Change the data type of a variable. |
| `concat` | Concatenate data objects. |
| `replace` | Find and replace values. |
| `read_csv` | Read a CSV file into a `DataFrame`. |
| `sort_values` | Sort by values along rows or columns. |
| `stack` | Stack a `DataFrame`. |
| `to_excel` | Write a `DataFrame` to an Excel file. |

It is important to correctly specify the data type of a variable before embarking on data summarization and visualization tasks, as Python may treat different types of objects in dissimilar ways. Common data types for entries in a `DataFrame` object are `float`, `category`, `datetime`, `bool`, and `int`. A generic object type is `object`.

```python
d={'Gender':['M', 'F', 'F']*4, 'Age': [6,3,5,6,5,8,0,3,6,6,7,7]}
df=pd.DataFrame(d)
print(df.dtypes)
df['Gender'] = df['Gender'].astype('category')  #change the type
print(df.dtypes)
```
Output:
```
Gender    object
Age        int64
dtype: object
Gender    category
Age          int64
dtype: object
```

### D.12.3 Extracting Information

Extracting statistical information from a `DataFrame` object is facilitated by a large collection of methods (functions) in `pandas`. Table D.4 gives a selection of data inspection methods. See Chapter 1 for their practical use. *(See page 1.)* The code below provides several examples of useful methods. The `apply` method allows one to apply general functions to columns or rows of a `DataFrame`. These operations do not change the data. The `loc` method allows for accessing elements (or ranges) in a data frame and acts similar to the slicing operation for lists and arrays, *with the difference that the "stop" value is included*, as illustrated in the code below.

```python
import numpy as np
import pandas as pd
ages = [6,3,5,6,5,8,0,3]
np.random.seed(123)
df = pd.DataFrame(np.random.randn(3,4), index = list('abc'),
                   columns = list('ABCD'))
print(df)
df1 = df.loc["b":"c","B":"C"]      # create a partial data frame
print(df1)
meanA = df['A'].mean()             # mean of 'A' column
print('mean of column A = {}'.format(meanA))
expA = df['A'].apply(np.exp) # exp of all elements in 'A' column
print(expA)
```
Output:
```
          A         B         C         D
a -1.085631  0.997345  0.282978 -1.506295
b -0.578600  1.651437 -2.426679 -0.428913
c  1.265936 -0.866740 -0.678886 -0.094709
          B         C
b  1.651437 -2.426679
c -0.866740 -0.678886
mean of column A = -0.13276486552118785
a    0.337689
b    0.560683
c    3.546412
Name: A, dtype: float64
```

The `groupby` method of a `DataFrame` object is useful for summarizing and displaying the data in manipulated ways. It groups data according to one or more specified columns, such that methods such as `count` and `mean` can be applied to the grouped data.

```python
df = pd.DataFrame({'W':['a','a','b','a','a','b'],
          'X':np.random.rand(6),
          'Y':['c','d','d','d','c','c'], 'Z':np.random.rand(6)})
print(df)
```
Output:
```
   W         X  Y         Z
0  a  0.993329  c  0.641084
1  a  0.925746  d  0.428412
2  b  0.266772  d  0.460665
3  a  0.201974  d  0.261879
4  a  0.529505  c  0.503112
5  b  0.006231  c  0.849683
```

**Table D.4: Useful `pandas` methods for data inspection.**

| Method | Description |
|---|---|
| `columns` | Column names. |
| `count` | Counts number of non-NA cells. |
| `crosstab` | Cross-tabulate two or more categories. |
| `describe` | Summary statistics. |
| `dtypes` | Data types for each column. |
| `head` | Display the top rows of a `DataFrame`. |
| `groupby` | Group data by column(s). |
| `info` | Display information about the `DataFrame`. |
| `loc` | Access a group or rows or columns. |
| `mean` | Column/row mean. |
| `plot` | Plot of columns. |
| `std` | Column/row standard deviation. |
| `sum` | Returns column/row sum. |
| `tail` | Display the bottom rows of a `DataFrame`. |
| `value_counts` | Counts of different non-null values. |
| `var` | Variance. |

```python
print(df.groupby('W').mean())
```
Output:
```
          X         Z
W
a  0.662639  0.458622
b  0.136502  0.655174
```

```python
print(df.groupby(['W', 'Y']).mean())
```
Output:
```
            X         Z
W Y
a c  0.761417  0.572098
  d  0.563860  0.345145
b c  0.006231  0.849683
  d  0.266772  0.460665
```

To allow for multiple functions to be calculated at once, the `agg` method can be used. It can take a list, dictionary, or string of functions.

```python
print(df.groupby('W').agg([sum,np.mean]))
```
Output:
```
          X                    Z
        sum      mean        sum      mean
W
a  2.650555  0.662639  1.834487  0.458622
b  0.273003  0.136502  1.310348  0.655174
```

### D.12.4 Plotting

The `plot` method of a `DataFrame` makes plots of a `DataFrame` using Matplotlib. Different types of plot can be accessed via the `kind = 'str'` construction, where `str` is one of `line` (default), `bar`, `hist`, `box`, `kde`, and several more. Finer control, such as modifying the font, is obtained by using `matplotlib` directly. The following code produces the line and box plots in Figure D.4.

```python
import numpy as np
import pandas as pd
import matplotlib
df = pd.DataFrame({'normal':np.random.randn(100),
        'Uniform':np.random.uniform(0,1,100)})
font = {'family' : 'serif', 'size'   : 14} #set font
matplotlib.rc('font', **font)   # change font
df.plot()   # line plot (default)
df.plot(kind = 'box')  # box plot
matplotlib.pyplot.show()  #render plots
```

**Figure D.4:** A line and box plot using the `plot` method of `DataFrame`. *(Left: a line plot of 100 'Normal' and 'Uniform' random draws against their index. Right: box plots comparing the 'Normal' and 'Uniform' distributions.)*
