---
appendix: D
section: "D.2"
title: "Python Objects"
pdf_pages: "483-484"
---

## D.2 Python Objects

As mentioned in the previous section, data in Python is represented by objects or relations between objects. We recall that basic data types included strings and numeric types (such as integers, booleans, and floats).

As Python is an object-oriented programming language, functions are objects too (everything is an object!). Each object has an identity (unique to each object and immutable — that is, cannot be changed — once created), a type (which determines which operations can be applied to the object, and is considered immutable), and a value (which is either mutable or immutable). The unique identity assigned to an object `obj` can be found by calling `id`, as in `id(obj)`.

Each object has a list of *attributes*, and each attribute is a reference to another object. The function `dir` applied to an object returns the list of attributes. For example, a string object has many useful attributes, as we shall shortly see. Functions are objects with the `__call__` attribute.

A class (see Section D.8) can be thought of as a template for creating a custom type of object.

```python
s = "hello"
d = dir(s)
print(d,flush=True)  # Print the list in "flushed" format
```
Output:
```
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 ... (many left out) ... 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']
```

Any attribute `attr` of an object `obj` can be accessed via the *dot notation*: `obj.attr`. To find more information about any object use the `help` function.

```python
s = "hello"
help(s.replace)
```
Output:
```
replace(...) method of builtins.str instance
    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.
```

This shows that the attribute `replace` is in fact a function. An attribute that is a function is called a *method*. We can use the `replace` method to create a new string from the old one by changing certain characters.

```python
s = 'hello'
s1 = s.replace('e','a')
print(s1)
```
Output:
```
hallo
```

> **Tip:** In many Python editors, pressing the TAB key, as in `objectname.<TAB>`, will bring up a list of possible attributes via the editor's autocompletion feature.
