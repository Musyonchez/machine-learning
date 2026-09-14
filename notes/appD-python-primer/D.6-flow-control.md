---
appendix: D
section: "D.6"
title: "Flow Control"
pdf_pages: "489-490"
---

## D.6 Flow Control

Flow control in Python is similar to that of many programming languages, with conditional statements as well as `while` and `for` loops. The syntax for if-then-else flow control is as follows.

```
if <condition1>:
   <statements>
elif <condition2>:
   <statements>
else:
   <statements>
```

Here, `<condition1>` and `<condition2>` are logical conditions that are either `True` or `False`; logical conditions often involve comparison operators (such as `==`, `>`, `<=`, `!=`). In the example above, there is one `elif` part, which allows for an "else if" conditional statement. In general, there can be more than one `elif` part, or it can be omitted. The `else` part can also be omitted. The colons are essential, as are the indentations.

The `while` and `for` loops have the following syntax.

```
while <condition>:
   <statements>

for <variable> in <collection>:
   <statements>
```

Above, `<collection>` is an iterable object (see Section D.7 below). For further control in `for` and `while` loops, one can use a `break` statement to exit the current loop, and the `continue` statement to continue with the next iteration of the loop, while abandoning any remaining statements in the current iteration. Here is an example.

```python
import numpy as np
ans = 'y'
while ans != 'n':
  outcome = np.random.randint(1,6+1)
  if outcome == 6:
      print("Hooray a 6!")
      break
  else:
      print("Bad luck, a", outcome)
  ans = input("Again? (y/n) ")
```
