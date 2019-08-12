#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

# use pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set() #set plot style

plt.hist(inches, 40)

# how many rainy days were there in the year? 
# What is the average precipitation on those rainy days?
# How many days were there with more than half an inch of rain?

'Digging into the Data'

# instead of a loop with a counter variable that we increment 
# each time we iterate over the data it is much better to use
# NumPy's ufuncs which are more efficent as NumPy arrays
# are more effective for storing data

'Compariosn Operators as ufuncs'

x = np.array([1,2,3,4,5])
x < 3 3 # less than
x > 3 #greater than
x <= 3 #less than or equal
x >= 3 # greater than or equal
x != 2 # not equal
x == 3 # equal 
(2 * x) == (x ** 2) # element-wise compound expression

'arithmetic operators as ufuncs '

'''
| Operator	    | Equivalent ufunc    || Operator	   | Equivalent ufunc    |
|---------------|---------------------||---------------|---------------------|
|``==``         |``np.equal``         ||``!=``         |``np.not_equal``     |
|``<``          |``np.less``          ||``<=``         |``np.less_equal``    |
|``>``          |``np.greater``       ||``>=``         |``np.greater_equal`` |
'''

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3,4))
x

x < 3 # arithmetic operators work on any size array

'Working with Boolean Arrays'

print(x)

'Counting entries'

# how many values less than 6?
np.count_nonzero(x < 6)

np.sum(x < 6) # False = 0 and True = 1

# how many values less than 6 in each row?
np.sum(x < 6, axis=1)

# are there any alues greater than 8?
np.any(x > 8)

# are there any values less than zero?
np.any(x < 0)

# are there all values less than 10?
np.all(x < 10)

# are all values equal to 6?
np.all(x == 6)

# are all values in each row less than 8?
np.all(x < 8, axis=1)

# Python's built-in sum(), any(), and all() functions
# are not as efficient nor as effective nor viable
# for multi-dimensional arrays
# np.sum(), np.any(), and np.all() are the correct aggregations

'Boolean operators'

np.sum((inches > 0.5) & (inches < 1)) 
# all days with rain less than 1 inche and greater than 0.5 inch

np.sum(~( (inches <= 0.5) | (inches >= 1) )) # A and B

print("Number of days without rain:    ", np.sum(inches == 0))
print("Number of days with rain:       ", np.sum(inches != 0))
print("Days with more than 0.5 inches: ", np.sum(inches > 0.5))
print("Rainy days with < 0.2 inches:   ", np.sum((inches > 0) &
                                                (inches < 0.2)))

'Boolean Arrays as Masks'

# using Boolean arrays as masks is more powerful
# as it allows particular subsets of the data themselves
print(x)

x < 5 # conditional Boolean array

# select these values from the array and we can simply 
# index on this Boolean array. This is a masking operation
x[x < 5] 

# construct a mask of all rainy days
rainy = (inches > 0)

# construct a mask of all summer days (June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("Median precip on rainy days in 2014 (inches):    ", 
      np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches):   ",
      np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches):  ", 
      np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches): ", 
      np.median(inches[rainy & ~summer]))
# combining Boolean operations, masking operations, and aggregates

'Aside: Using the Keywords and/or Versus the Operators &/|'

# comparing the operators 'and' and 'or' vs '&' and '|'
# the difference is as such:
# 'and' and 'or' gauge the truth or falsehood of *entire object*,
# while '&' and '|' refer to *bits within each object*.
# 'and' or 'or' is the equivalent to asking Python to treat
# the object asa single Boolean entity. All nonzero integers
# with Oython will evaluate as True

bool(42), bool(0)

bool(42 and 0)

bool(42 or 0)

# '&' and 'or' when operated on integers, it operates 
# on the individual bits making up the number

bin(42)

bin(59)

bin(42 & 59)

bin(42 | 59)

A = np.array([1,0,1,0,1,0], dtype=bool) # Boolean array e.g., a string of bits
B = np.array([1,1,1,0,1,1], dtype=bool)
A | B

A or B # or attemps to evaluate the truth or falsehood
# of the entire array object which is not well-defined
