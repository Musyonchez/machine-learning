---
appendix: D
section: "D.7"
title: "Iteration"
pdf_pages: "490-492"
---

## D.7 Iteration

Iterating over a sequence of objects, such as used in a `for` loop, is a common operation. To better understand how iteration works, we consider the following code.

```python
s = "Hello"
for c in s:
    print(c,'*', end=' ')
```
Output:
```
H * e * l * l * o *
```

A string is an example of a Python object that can be iterated. One of the methods of a string object is `__iter__`. Any object that has such a method is called an *iterable*. Calling this method creates an *iterator* — an object that returns the next element in the sequence to be iterated. This is done via the method `__next__`.

```python
s = "Hello"
t = s.__iter__()   # t is now an iterator. Same as iter(s)
print(t.__next__() ) # same as next(t)
print(t.__next__() )
print(t.__next__() )
```
Output:
```
H
e
l
```

The inbuilt functions `next` and `iter` simply call these corresponding double-underscore functions of an object. When executing a `for` loop, the sequence/collection over which to iterate must be an iterable. During the execution of the `for` loop, an iterator is created and the `next` function is executed until there is no next element. An iterator is also an iterable, so can be used in a `for` loop as well. Lists, tuples, and strings are so-called *sequence* objects and are iterables, where the elements are iterated by their index.

The most common iterator in Python is the *range* iterator, which allows iteration over a range of indices. Note that `range` returns a range object, not a list.

```python
for i in range(4,20):
    print(i, end=' ')
print(range(4,20))
```
Output:
```
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
range(4,20)
```

> **Warning:** Similar to Python's slice operator `[i : j]`, the iterator `range(i, j)` ranges from `i` to `j`, *not including* the index `j`.

Two other common iterables are sets and dictionaries. Python *sets* are, as in mathematics, unordered collections of unique objects. Sets are defined with curly brackets `{}`, as opposed to round brackets `()` for tuples, and square brackets `[]` for lists. Unlike lists, sets do not have duplicate elements. Many of the usual set operations are implemented in Python, including the union `A | B` and intersection `A & B`.

```python
A = {3, 2, 2, 4}
B = {4, 3, 1}
C = A & B
for i in A:
    print(i)
print(C)
```
Output:
```
2
3
4
{3, 4}
```

A useful way to construct lists is by *list comprehension*; that is, by expressions of the form

```
<expression> for <element> in <list> if <condition>
```

For sets a similar construction holds. In this way, lists and sets can be defined using very similar syntax as in mathematics. Compare, for example, the mathematical definition of the sets *A* := {3, 2, 4, 2} = {2, 3, 4} (no order and no duplication of elements) and *B* := {*x*² : *x* ∈ *A*} with the Python code below.

```python
setA = {3, 2, 4, 2}
setB = {x**2 for x in setA}
print(setB)
listA = [3, 2, 4, 2]
listB = [x**2 for x in listA]
print(listB)
```
Output:
```
{16, 9, 4}
[9, 4, 16, 4]
```

A *dictionary* is a set-like data structure, containing one or more `key:value` pairs enclosed in curly brackets. The keys are often of the same type, but do not have to be; the same holds for the values. Here is a simple example, storing the ages of Lord of the Rings characters in a dictionary.

```python
DICT = {'Gimly': 140, 'Frodo':51, 'Aragorn': 88}
for key in DICT:
    print(key, DICT[key])
```
Output:
```
Gimly 140
Frodo 51
Aragorn 88
```
