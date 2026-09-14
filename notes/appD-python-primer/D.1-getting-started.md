---
appendix: D
section: "D.1"
title: "Getting Started"
pdf_pages: "481-483"
---

Python has become the programming language of choice for many researchers and practitioners in data science and machine learning. This appendix gives a brief introduction to the language. As the language is under constant development and each year many new packages are being released, we do not pretend to be exhaustive in this introduction. Instead, we hope to provide enough information for novices to get started with this beautiful and carefully thought-out language.

## D.1 Getting Started

The main website for Python is

> https://www.python.org/,

where you will find documentation, a tutorial, beginners' guides, software examples, and so on. It is important to note that there are two incompatible "branches" of Python, called Python 3 and Python 2. Further development of the language will involve only Python 3, and in this appendix (and indeed the rest of the book) we only consider Python 3. As there are many interdependent packages that are frequently used with a Python installation, it is convenient to install a distribution — for instance, the *Anaconda* Python distribution, available from

> https://www.anaconda.com/.

The Anaconda installer automatically installs the most important packages and also provides a convenient interactive development environment (IDE), called *Spyder*.

> **Tip:** Use the *Anaconda Navigator* to launch *Spyder*, *Jupyter notebook*, install and update packages, or open a command-line terminal.

To get started[^1], try out the Python statements in the input boxes that follow. You can either type these statements at the IPython command prompt or run them as (very short) Python programs. The output for these two modes of input can differ slightly. For example, typing a variable name in the console causes its contents to be automatically printed, whereas in a Python program this must be done explicitly by calling the `print` function. Selecting (highlighting) several program lines in *Spyder* and then pressing function key[^2] F9 is equivalent to executing these lines one by one in the console.

In Python, data is represented as an *object* or relation between objects (see also Section D.2). Basic data types are numeric types (including integers, booleans, and floats), sequence types (including strings, tuples, and lists), sets, and mappings (currently, dictionaries are the only built-in mapping type).

Strings are sequences of characters, enclosed by single or double quotes. We can print strings via the `print` function.

```python
print("Hello World!")
```
Output:
```
Hello World!
```

For pretty-printing output, Python strings can be formatted using the `format` function. The bracket syntax `{i}` provides a placeholder for the *i*-th variable to be printed, with 0 being the first index. Individual variables can be formatted separately and as desired; formatting syntax is discussed in more detail in Section D.9. *(See page 476.)*

```python
print("Name:{1} (height {2} m, age {0})".format(111,"Bilbo",0.84))
```
Output:
```
Name:Bilbo (height 0.84 m, age 111)
```

Lists can contain different types of objects, and are created using square brackets as in the following example:

```python
x = [1,'string',"another string"]  # Quote type is not important
```
Output:
```
[1, 'string', 'another string']
```

Elements in lists are indexed starting from 0, and are *mutable* (can be changed):

```python
x = [1,2]
x[0] = 2  # Note that the first index is 0
x
```
Output:
```
[2,2]
```

In contrast, tuples (with round brackets) are *immutable* (cannot be changed). Strings are immutable as well.

```python
x = (1,2)
x[0] = 2
```
Output:
```
TypeError: 'tuple' object does not support item assignment
```

Lists can be accessed via the *slice* notation `[start:end]`. It is important to note that `end` is the index of the first element that will *not* be selected, and that the first element has index 0. To gain familiarity with the slice notation, execute each of the following lines.

```python
a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
a[1:4]  # Elements with index from 1 to 3
a[:4]   # All elements with index less than 4
a[3:]   # All elements with index 3 or more
a[-2:]  # The last two elements
```
Output:
```
[3, 5, 7]
[2, 3, 5, 7]
[7, 11, 13, 17, 19, 23]
[19, 23]
```

An *operator* is a programming language construct that performs an action on one or more operands. The action of an operator in Python depends on the type of the operand(s). For example, operators such as `+`, `*`, `-`, and `%` that are arithmetic operators when the operands are of a numeric type, can have different meanings for objects of non-numeric type (such as strings).

```python
'hello' + 'world'  # String concatenation
```
Output:
```
'helloworld'
```

```python
'hello' * 2   # String repetition
```
Output:
```
'hellohello'
```

```python
[1,2] * 2       # List repetition
```
Output:
```
[1, 2, 1, 2]
```

```python
15 % 4   # Remainder of 15/4
```
Output:
```
3
```

Some common Python operators are given in Table D.1 (see Section D.3).

[^1]: We assume that you have installed all the necessary files and have launched *Spyder*.
[^2]: This may depend on the keyboard and operating system.
