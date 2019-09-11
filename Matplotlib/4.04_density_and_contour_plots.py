#!/usr/bin/env python
# coding: utf-8

'Density and contour plots'
# It may be useful to display three-dimensional data in a two-dimensional space using contours and color coded regions.
# Matplotlib has three functions for this task: plt.contour for contour plots, plt.contourf for filled contour plots, 
# and plt.imshow for showing images.

# setting up the notebook for plotting
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn-white")
import numpy as np

'Visulizing a Three-dimensional function'

# a contour plot can be created using a function z = f(x, y)
def f(x, y):
    return np.sin(x) ** 10  + np.cos(10 + y * x) * np.cos(x)

# a straightforward way to prepare data is with np.meshgrid which builds two-dimensional grids from one-dimensional arrays
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# creating a standard line-only contour plot
plt.contour(X, Y, Z, colors='black');
# negative values are represented by dashed lines when one color is used and positive values by solid lines.

# lines can be color coded by specifying a colormap using the cmap argument. the function is also specifying that there
# will be 20 equally spaced intervals within the data range
plt.contour(X, Y, Z, 20, cmap='RdGy');
# RdGy = Red-Grey
# we can change space between the lines by switching it to a filled contour plot. The plt.contourf() function which uses
# the plt.contour syntax.

# We'll use the plt.colorbar() command to create an additional axis with labeled color information for the plot
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar();
# the colorbar shows that black regions are peaks and red regions are valleys. While this plot is useful it is a bit 
# splotchy and lines are discrete whereas it may be preferred to be more continuous. Another option is to set the number
# of contours high, but that would lead to a highly inefficient plot: in that Matplotlib will have to render new 
# polygons for each step in the level.

# a more efficient way to handle this is with the plt.imshow() function which interprets a two-dimensional grid of data
# as an image.
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image');

# it can useful to combine contour plots and image plots. There will be a transparant background with transparacny set
# with the alpha parameter and overplot contours  with labels on themselves using plt.clabel() function.
contours =  plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0,5, 0, 5], origin='lower',
           cmap='RdGy', alpha=0.5)
plt.colorbar();
