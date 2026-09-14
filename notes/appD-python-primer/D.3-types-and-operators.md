---
appendix: D
section: "D.3"
title: "Types and Operators"
pdf_pages: "484-486"
---

## D.3 Types and Operators

Each object has a *type*. Three basic data types in Python are `str` (for string), `int` (for integers), and `float` (for floating point numbers). The function `type` returns the type of an object.

```python
t1 = type([1,2,3])
t2 = type((1,2,3))
t3 = type({1,2,3})
print(t1,t2,t3)
```
Output:
```
<class 'list'> <class 'tuple'> <class 'set'>
```

The *assignment* operator, `=`, assigns an object to a variable; e.g., `x = 12`. An *expression* is a combination of values, operators, and variables that yields another value or variable.

> **Tip:** Variable names are case sensitive and can only contain letters, numbers, and underscores. They must start with either a letter or underscore. Note that reserved words such as `True` and `False` are case sensitive as well.

Python is a dynamically typed language, and the type of a variable at a particular point during program execution is determined by its most recent object assignment. That is, the type of a variable does not need to be explicitly declared from the outset (as is the case in C or Java), but instead the type of the variable is determined by the object that is currently assigned to it.

It is important to understand that a variable in Python is a *reference* to an object — think of it as a label on a shoe box. Even though the label is a simple entity, the *contents* of the shoe box (the object to which the variable refers) can be arbitrarily complex. Instead of moving the contents of one shoe box to another, it is much simpler to merely move the label.

```python
x = [1,2]
y = x    # y refers to the same object as x
print(id(x) == id(y))  # check that the object id's are the same
y[0] = 100   # change the contents of the list that y refers to
print(x)
```
Output:
```
True
[100,2]
```

```python
x = [1,2]
y = x    # y refers to the same object as x
y = [100,2]   # now y refers to a different object
print(id(x) == id(y))
print(x)
```
Output:
```
False
[1,2]
```

Table D.1 shows a selection of Python operators for numerical and logical variables.

**Table D.1: Common numerical (left) and logical (right) operators.**

| Operator | Meaning |
|---|---|
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `**` | power |
| `/` | division |
| `//` | integer division |
| `%` | modulus |

| Operator | Meaning |
|---|---|
| `~` | binary NOT |
| `&` | binary AND |
| `^` | binary XOR |
| `\|` | binary OR |
| `==` | equal to |
| `!=` | not equal to |

Several of the numerical operators can be combined with an assignment operator, as in `x += 1` to mean `x = x + 1`. Operators such as `+` and `*` can be defined for other data types as well, where they take on a different meaning. This is called operator *overloading*, an example of which is the use of `<List> * <Integer>` for list repetition as we saw earlier.
