#!/usr/bin/env python
# coding: utf-8

'Simple Line Plots'
# the simplest plot to visulize is a single function y = f(x)

# importing the necessary packages
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# starting by creating a figure and an axes. The simplest form of a figure and axes
fig = plt.figure()
ax = plt.axes()
# the figure is an instance of plt.figure() and is essentially a single container for all the objects representing axes
# graphics, text, and labels.
# the axes is an instance of plt.Axes() which is a bounding box with ticks and labels which eventully contain the plot 
# elements which make up the visulization. fig is a common variable name for figure instances and ax is for axes instances

# with the axes created we are using the ax.plot function to plot data. This will be a simple sinusoid
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));

# using the pylab interface to let the figure and axes be created in the background 
plt.plot(x, np.sin(x));

# creating a single figure with multiple lines by simply calling the plot function multiple time
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));

'Adjusting the Plot: Line Colors and Styles'
# the plt.plot() function takes arguemnts that allow you to specify color and style. The color keyword takes a string
plt.plot(x, np.sin(x - 0), color='blue')        # specifying color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # grey scale betwen 0 and 1
plt.plot(x, np.sin(x - 3), color='#ffdd44')     # Hex code requires a hash before the code (RRGGBB from 00 to FF) 
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
# if color is not chosen Matplotlib will cycle default colors

# setting the line style with the linspace keyword
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# for short, it is possible to use codes
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':'); # dotted

# linestyle and color code can be combined into a very terse, single non=keyword argument with the plt.plot() function
plt.plot(x, x + 0, '-g')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r'); # dotted red
# single character color codes are abbreviations RGB (Red/Green/Blue) and CMYK (Cyan/Magenta/Yellow/Black)

'Adjusting the Plot: Axes Limits'
# Matplotlib chooses default axes though it is possible to fine tune them with plt.xlim() and plt.ylim()

# setting axes limits
plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);

# displaying the axis in reverse by reversing the order of the arguments
plt.plot(x, np.sin(x))

plt.xlim(10, 0)
plt.ylim(1.2, -1.2);

# plt.axis() allows you to set the x and y limits in a single call which specifies [xmin, xmax, ymin, ymax]
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5]);

# the plt.axis() method allows automatic tightening of the bounds around the plot
plt.plot(x, np.sin(x))
plt.axis('tight');

# ensueing an equal aspect ratio so that one unit of x is equal to one unit in y
plt.plot(x, np.sin(x))
plt.axis('equal');

'Labeling Plots'
# it is possible to label the the plots: title, axis labels, and simple legend

# title and axix labels are the easiest to set
plt.plot(x, np.sin(x))
plt.title('A Sine Curve')
plt.xlabel('X')
plt.ylabel('sin(x)');
# label position, size, and style can be adjusted using optionl arguments

# having multiple lines within a single axes it can be helpful to plot a legend that labels each line type. It is 
# possible to use the plt.legend() method however it is easiest to specify the label of each line using the label keyword
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
# the plt.legend() function keeps track of linestyle, color, and mathces the correct labels
plt.legend();

'Aside: Matplotlib Gotchas'
# most plt functions translate directly to ax methods (plt.plot() -> ax.plot(), plt.legend() -> ax.legend()), however
# this is not true with functions to set limits, labels and titles.

# it is easier to use the ax.set() method to set all properties at once
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2,2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot');
