# Fancy Indexing

import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)

[x[3], x[7], x[2]] # how to access three different elements

ind = [3, 7, 4] # 3,7,4 are location in the array
x[ind] # passing a list of indicies

ind = np.array([[3,7], # the results of the array will
               [4,5]]) #mirror the shape of the index array
x[ind] #the data is now in a 2x2 array

X = np.arange(12).reshape((3, 4))
X

row = np.array([0,1,2]) # X is accessed as X[0, 2] so row 0 and column 2 
col = np.array([2,1,3])
X[row, col]

X[row[:, np.newaxis], col]
# for each row create a copy and a new axis with the column as a pair to the row
# iterate over the array in locations row1(X[0,2], X[0,1], X[0,3])
# row2(X[1,0], X[1,1], X[1,2])
# row3(X[2,2], X[2,1], X[2,3])

row[:, np.newaxis] * col
# follows broadcasting rules and row is spread across the 3 dimension to 
# allow multiplicaton of the elemnts spread across from col array is as follows
# 000 -> 000
# 111 -> 213
# 222 -> 426

# Combined Indexing

print(X)

X[2, [2,0,1]]
# combining simple and fancy indexing 2 is the row and the list
# holds the locations in the list

X[1:, [2,0,1]]
# copy up to index row 1 and search locations in the list

mask = np.array([1,0,1,0], dtype=bool) # True, False, True, False
test = X[:, np.newaxis] # added a simple test to see how X looks flipped and it still doesn't help
X[row[:, np.newaxis], mask] # I'm not sure how this works
# for each row create a copy and a new axis with the mask as a pair 
# to the row and iterate over the array in locations: 
# row1(X[0,1], X[0,0], X[0,1], X[0,0])
# row2(X[1,1], X[1,0], X[1,1], X[1,0])
# row3(X[2,1], X[2,0], X[2,1], X[2,0])

print(np.outer(X[row[:, np.newaxis]], mask)) # attempt to figure it out failed

# Example: Selecting Random Points

mean = [0,0]
cov = [[1,2],
       [2,5]]
X = np.random.multivariate_normal(mean, cov, 100)
X.shape

# A selection of subsets of rows from a matrix. An N by D matrix 
# representing N points in D dimensions, such as the following
# points drawn from a two-dimensional normal distribution

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

plt.scatter(X[:, 0], X[:, 1]);

# using fancy indexing to select 20 random points by first choosing 20
# random indicies with no repeat , and then use those indicies
# to select a portion of the original array

indicies = np.random.choice(X.shape[0], 20, replace=False)
indicies

selection = X[indicies] #fancy indexing 
selection.shape

plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
           facecolor='none', s=200);
# over-plot large circles at the locations of the selected points
# a strategy is often used to quickly partition datasets, 
# as is often needed in train/test splitting for validation of statistical models

# Modifying Values with Fancy Indexing

x = np.arange(10)
i = np.array([2,1,8,4])
x[i] = 99
print(x)
# fancy indexing changes the values of x in the locations
# given by i

x[i] -= 10 # minus 10 from each location given by i
print(x)

x = np.zeros(10)
x[[0, 0]] = [4, 6] # 4 is assigned first and then 6 overwitres
print(x)

i = [2,3,3,4,4,4] 
# increment position 2, position 3, and position 4 of x 
# in respect to i only once
x[i] += 1
x

x = np.zeros(10)
np.add.at(x, i, 1)
print(x)
# at() method does an in place application of the given operation
# e.g., adds 1 to the given location

# Example: Binning Data

#efficiently bin data to create a histogram by hand
np.random.seed(42)
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# find the appropriate bin for each x
i = np.searchsorted(bins, x)

# add 1 to each of these bins
np.add.at(counts, i, 1)
# counts now reflect the number of points 
# within each bin–a histogram

# plot the results
plt.plot(bins, counts, linestyle='steps');

# this algorithm is not very effective on small data
print("NumPy routine:")
get_ipython().run_line_magic('timeit', 'counts, edges = np.histogram(x, bins)')

print("Custom routine:")
get_ipython().run_line_magic('timeit', 'np.add.at(counts, np.searchsorted(bins, x), 1)')

# this algorithm is much effective on big data
x = np.random.randn(100000)
print("NumPy routine:")
get_ipython().run_line_magic('timeit', 'counts, edges = np.histogram(x, bins)')

print("Custom routine:")
get_ipython().run_line_magic('timeit', 'np.add.at(counts, np.searchsorted(bins, x), 1)')

