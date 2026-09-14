---
appendix: D
section: "D.11"
title: "Matplotlib"
pdf_pages: "501-504"
---

## D.11 Matplotlib

The main Python graphics library for 2D and 3D plotting is `matplotlib`, and its subpackage `pyplot` contains a collection of functions that make plotting in Python similar to that in MATLAB.

### D.11.1 Creating a Basic Plot

The code below illustrates various possibilities for creating plots. The style and color of lines and markers can be changed, as well as the font size of the labels. Figure D.1 shows the result.

**sqrtplot.py**
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.1)
u = np.arange(0,10)
y = np.sqrt(x)
v = u/3
plt.figure(figsize = [4,2])  # size of plot in inches
plt.plot(x,y, 'g--')         # plot green dashed line
plt.plot(u,v,'r.')           # plot red dots
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('sqrtplot.pdf',format='pdf')  # saving as pdf
plt.show()                      # both plots will now be drawn
```

**Figure D.1:** A simple plot created using pyplot. *(A green dashed curve traces √x for x from 0 to 10; red dots plot u/3 at the integers u = 0, ..., 9, tracking close to the curve.)*

The library `matplotlib` also allows the creation of subplots. The scatterplot and histogram in Figure D.2 have been produced using the code below. When creating a histogram there are several optional arguments that affect the layout of the graph. The number of bins is determined by the parameter `bins` (the default is 10). Scatterplots also take a number of parameters, such as a string `c` which determines the color of the dots, and `alpha` which affects the transparency of the dots.

**histscat.py**
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
u = np.random.randn(100)
v = np.random.randn(100)
plt.subplot(121)                # first subplot
plt.hist(x,bins=25, facecolor='b')
plt.xlabel('X Variable')
plt.ylabel('Counts')
plt.subplot(122)                # second subplot
plt.scatter(u,v,c='b', alpha=0.5)
plt.show()
```

**Figure D.2:** A histogram and scatterplot. *(Left: a blue, roughly bell-shaped histogram of 1000 standard normal draws. Right: a blue scatterplot of 100 pairs of standard normal draws.)*

One can also create three-dimensional plots as illustrated below.

**surf3dscat.py**
```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def npdf(x,y):
    return np.exp(-0.5*(pow(x,2)+pow(y,2)))/np.sqrt(2*np.pi)

x, y  = np.random.randn(100), np.random.randn(100)
z = npdf(x,y)

xgrid, ygrid = np.linspace(-3,3,100), np.linspace(-3,3,100)

Xarray, Yarray = np.meshgrid(xgrid,ygrid)
Zarray = npdf(Xarray,Yarray)

fig = plt.figure(figsize=plt.figaspect(0.4))
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(x,y,z, c='g')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_zlabel('$f(x,y)$')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(Xarray,Yarray,Zarray,cmap='viridis',
                                  edgecolor='none')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_zlabel('$f(x,y)$')

plt.show()
```

**Figure D.3:** Three-dimensional scatter- and surface plots. *(Left: a green 3D scatterplot of 100 points (x, y, f(x,y)) computed from the bivariate standard normal density. Right: a smooth 3D surface plot of the same density function, rendered with the 'viridis' colormap.)*
