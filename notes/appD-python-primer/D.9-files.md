---
appendix: D
section: "D.9"
title: "Files"
pdf_pages: "494-496"
---

## D.9 Files

To write to or read from a file, a file first needs to be opened. The `open` function in Python creates a file object that is iterable, and thus can be processed in a sequential manner in a `for` or `while` loop. Here is a simple example.

```python
fout = open('output.txt','w')
for i in range(0,41):
    if i%10 == 0:
        fout.write('{:3d}\n'.format(i))
fout.close()
```

The first argument of `open` is the name of the file. The second argument specifies if the file is opened for reading (`'r'`), writing (`'w'`), appending (`'a'`), and so on. See `help(open)`. Files are written in text mode by default, but it is also possible to write in binary mode. The above program creates a file `output.txt` with 5 lines, containing the strings 0, 10, ..., 40. Note that if we had written `fout.write(i)` in the fourth line of the code above, an error message would be produced, as the variable `i` is an integer, and not a string. Recall that the expression `string.format()` is Python's way to specify the format of the output string.

The formatting syntax `{:3d}` indicates that the output should be constrained to a specific width of three characters, each of which is a decimal value. As mentioned in the introduction, bracket syntax `{i}` provides a placeholder for the *i*-th variable to be printed, with 0 being the first index. The format for the output is further specified by `{i:format}`, where `format` is typically[^4] of the form:

```
[width][.precision][type]
```

In this specification:

- `width` specifies the minimum width of output;
- `precision` specifies the number of digits to be displayed after the decimal point for a floating point values of type `f`, or the number of digits before *and* after the decimal point for a floating point values of type `g`;
- `type` specifies the type of output. The most common types are `s` for strings, `d` for integers, `b` for binary numbers, `f` for floating point numbers (floats) in fixed-point notation, `g` for floats in general notation, `e` for floats in scientific notation.

The following illustrates some behavior of formatting on numbers.

```python
'{:5d}'.format(123)
'{:.4e}'.format(1234567890)
'{:.2f}'.format(1234567890)
'{:.2f}'.format(2.718281828)
'{:.3f}'.format(2.718281828)
'{:.3g}'.format(2.718281828)
'{:.3e}'.format(2.718281828)
```
Output:
```
'  123'
'1.2346e+09'
'1234567890.00'
'2.72'
'2.718'
'2.72'
'2.718e+00'
```

```python
'{0:3.3f}; {1:.4e};'.format(123.456789,  0.00123456789)
```
Output:
```
'123.457; 1.2346e-03;'
```

The following code reads the text file `output.txt` line by line, and prints the output on the screen. To remove the newline `\n` character, we have used the `strip` method for strings, which removes any whitespace from the start and end of a string.

```python
fin = open('output.txt','r')
for line in fin:
    line = line.strip()   # strips a newline character
    print(line)
fin.close()
```
Output:
```
0
10
20
30
40
```

When dealing with file input and output it is important to always close files. Files that remain open, e.g., when a program finishes unexpectedly due to a programming error, can cause considerable system problems. For this reason it is recommended to open files via *context management*. The syntax is as follows.

```python
with open('output.txt', 'w') as f:
    f.write('Hi there!')
```

Context management ensures that a file is correctly closed even when the program is terminated prematurely. An example is given in the next program, which outputs the most-frequent words in Dicken's *A Tale of Two Cities*, which can be downloaded from the book's GitHub site as `ataleof2cities.txt`.

Note that in the next program, the file `ataleof2cities.txt` must be placed in the current working directory. The current working directory can be determined via `import os` followed by `cwd = os.getcwd()`.

```python
numline = 0
DICT = {}
with open('ataleof2cities.txt', encoding="utf8") as fin:
    for line in fin:
        words = line.split()
        for w in words:
            if w not in DICT:
                DICT[w] = 1
            else:
                DICT[w] +=1
        numline += 1

sd = sorted(DICT,key=DICT.get,reverse=True) #sort the dictionary

print("Number of unique words: {}\n".format(len(DICT)))
print("Ten most frequent words:\n")
print("{:8} {}".format("word", "count"))
print(15*'-')
for i in range(0,10):
    print("{:8} {}".format(sd[i], DICT[sd[i]]))
```
Output:
```
Number of unique words: 19091

Ten most frequent words:

word     count
---------------
the      7348
and      4679
of       3949
to       3387
a        2768
in       2390
his      1911
was      1672
that     1650
I        1444
```

[^4]: More formatting options are possible.
