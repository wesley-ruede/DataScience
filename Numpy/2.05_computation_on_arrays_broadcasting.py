# coding: utf-8
# Computation on Arrays: Broadcasting 
# broadcasting allows for bianry operation multi-dimensional 
# arrays of different sizes
# Introducing Broadcasting
import numpy as np
a = np.array([0,1,2])
b = np.array([5,5,5])
a + b
a + 5 # scalar binary operation that maps over a field or array
M = np.ones((3,3)) # two-dimension array 
M + a # a is mapped over M 0+1 = 1, 1+1 = 2, 2+1 = 3 
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print(a)
print(b)
a + b
# a and b are broadcast or stretched over each other to reach
# a common shape
# Rules of Broadcasting
'''strict set of rules tp determine the interaction between arrays
Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones
on its leading (left) side
Ruel 2: If the shape of the two arrays, does not match in any dimension, the array with shape equal to 1 in that dimension
is stretched to match the other shape
Ruel 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised'''
# Broadcasting example 1
M = np.ones((2,3))
a = np.arange(3)
print(M.shape)
print(a.shape)
# a has fewer dimensions so we pad it on the left with ones
print(a)
print(M)
# a.shape -> (1,3)
# the first dimension of a disarees with the first dimension of M
# so we stretch the dimension to match M.shape -> (2,3)
# e.g., a.shape -> (2,3)
M + a
# Broadcasting example 2
a = np.arange(3).reshape((3,1))
b = np.arange(3)
print(a)
print(b)

