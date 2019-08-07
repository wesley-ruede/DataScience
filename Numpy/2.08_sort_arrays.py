#!/usr/bin/env python
# coding: utf-8

'Sorting Arrays'

import numpy as np

# selection sort algorithm
def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

# selection sort algorithm is much too slow to be useful for 
# larger arrays. For a list of N values, it requires N loops,
# each of which does on order ~N comparisons to find the swap value.

x = np.array([2,1,4,3,5])
selection_sort(x)

def bogosort(x):
    while np.any(x[:-1] > x[:1]):
        np.random.shuffle(x)
    return x

x = np.array([2,1,4,3,5])
bogosort(x)

'Fast Sorting in NumPy: np.sort and np.argsort'

# np.sort() is much more efficient than Python's built in 
# functions sort() and sorted().

x = np.array([2,1,4,35])
np.sort(x)

x.sort() #using sort in place
print(x)

# argsort returns the indicies of the sorted elements
x = np.array([2,1,4,3,5])
i = np.argsort(x)
print(i)

x[i] # fancy index

'Sorting along row or columns'
# NumPy can sort a designated axis

rand = np.random.RandomState(42)
X = rand.randint(0,10, (4,6))
print(X)

# sort each colum of X
np.sort(X, axis=0)

# sort each row of X
np.sort(X, axis=1)

'Partial Sorts: Partitioning'
# sometimes we just want to sort k* smallest alues in the array
# NumPy provides np.partition function. The function takes an 
# array and a number K*.The result is a new array with the 
# the smallest K values to the left of the partition and
# the remaining values to the right

x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)
# the first 3 locations have the smallest values
# while the remaining are in an arbitrary order

np.partition(X, 2, axis=1) # partitioning along an axis
# the first two locations in the array are sorted by the row

'Example: k-Nearest Neighbors'

X = rand.rand(10, 2) #random set of 10 points on a two-dimensional plane

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # plot style 
plt.scatter(X[:, 0], X[:, 1], s=100)

# compute the distance between each pair of points
# the squared-distance between two points is the 
# sum of the squard differences in each dimension
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) **2, axis=1)
# computing the matrix of sqared distance

# breaking the previous code down into components
# for each pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
differences.shape

# square the coordiante differences
sq_differences = differences ** 2
sq_differences.shape

# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
dist_sq.shape

# check that the diagonal of the this matrix (i.e., the set
# of distances between each point and itself) is all zero
dist_sq.diagonal()

# with pairwise square-distances converted, we can now use
# np.argsor to sort along each row. The leftmost columns will
# then give the indices of the nearest neighbor
nearest = np.argsort(dist_sq, axis=1) # first row is 0-9

print(nearest)

# partition each row so that the smallest k + 1 squared distances
# come first, with larger distances filling the remaining positions
# of the array by using the np.argpartition function.
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

# broadcasted and row-wise vector plotting operation
# this is much more efficient algorithm that looping
# through the data and sorting each set of neighbors

plt.scatter(X[:, 0], X[:, 1], s=100)

# draw lines from each point to its two nearst neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, :k+1]:
        # plot a line from X[i] to X[j]
        # use some zip magi to make it happen:
        plt.plot(*zip(X[j], X[i]), color='black')

# if point A is one of the two nearest neighbors of point B
# this does not necessarily imply that point B is on of the
# two nearest neightbor of point A

print(differences)
