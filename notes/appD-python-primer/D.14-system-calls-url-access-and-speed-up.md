---
appendix: D
section: "D.14"
title: "System Calls, URL Access, and Speed-Up"
pdf_pages: "512-513"
---

## D.14 System Calls, URL Access, and Speed-Up

Operating system commands (whether in Windows, MacOS, or Linux) for creating directories, copying or removing files, or executing programs from the system shell can be issued from within Python by using the package `os`. Another useful package is `requests` which enables direct downloads of files and webpages from URLs. The following Python script uses both. It also illustrates a simple example of exception handling in Python.

**misc.py**
```python
import os
import requests
for c in "123456":
  try:                        # if it does not yet exist
    os.mkdir("MyDir"+ c)  # make a directory
  except:                     # otherwise
      pass                    # do nothing

uname = "https://github.com/DSML-book/Programs/tree/master/
    Appendices/Python Primer/"
fname = "ataleof2cities.txt"
r = requests.get(uname + fname)
print(r.text)
open('MyDir1/ato2c.txt', 'wb').write(r.content) #write to a file
                                # bytes mode is important here
```

The package `numba` can significantly speed up calculations via smart compilation. First run the following code.

**jitex.py**
```python
import timeit
import numpy as np
from numba import jit
n = 10**8

#@jit
def myfun(s,n):
   for i in range(1,n):
       s = s+ 1/i
   return s

start = timeit.time.clock()
print("Euler's constant is approximately {:9.8f}".format(
                        myfun(0,n) - np.log(n)))
end = timeit.time.clock()
print("elapsed time: {:3.2f} seconds".format(end-start))
```
Output:
```
Euler's constant is approximately 0.57721566
elapsed time: 5.72 seconds
```

Now remove the `#` character before the `@` character in the code above, in order to activate the "just in time" compiler. This gives a 15-fold speedup:

```
Euler's constant is approximately 0.57721566
elapsed time: 0.39 seconds
```

## Further Reading

To learn Python, we recommend [82] and [110]. However, as Python is constantly evolving, the most up-to-date references will be available from the Internet.
