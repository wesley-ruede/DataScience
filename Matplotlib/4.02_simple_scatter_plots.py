#!/usr/bin/env python
# coding: utf-8

'Simple Scatter Plots'
# scatter plots are common and cousin of line plots and are represented with points individually instead of lines

# setting up the enviroment
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

'Scatter Plot with plt.plot'
# plt.plot and ax.plot functions can be used with scatter plots
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black');

# scatter plots have symbols similar to '-' and '--' to control marker style
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label='marker="{0}"'.format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);

# using character codes with lines nd color codes to plot points along with a line connecting them
plt.plot(x, y, '-ok');

#specifying plt.plot keywords to set properties of the lines and markers
plt.plot(x, y, '-p', color='grey',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='grey',
         markeredgewidth=2)
plt.ylim(-1,2, 1.2);
# this flexibilit of the plt.plot() function allows for a many visilization options

'Scatter Plot with plt.scatter'
# a more powerful method of creating scatter plots is the plt.scatter function

# plt.scatter is similar to plt.plot
plt.scatter(x, y, marker='o');
# with plt.scatter the properties of each individual point can be indivdually controlled or mapped to data

# creating a random scatter plot with points of many differnt colors and size which overlapping results using the alpha 
# keyword to adjust the transparency level
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar(); # show color scale
# the color argument is automatically mpped to a color scale and the size of the argument is given in pixels

# using the Iris data from SciKit-learn where each sample is one of the three types of flowers that has had the size 
# of its petal and sepals 
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);
# the sctter plot allows explorations of four different dimensions of data. The (x,y) location of each point is related
# to the petal width, and the color is related to the particular species of flower

'plot Versus sctter: A Note on Efficiency'
# plt.scatter is not as efficient as plt.plot when dealing with datasets larger than a few thousand points
