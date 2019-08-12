#!/usr/bin/env python
# coding: utf-8

'Handling Missing Data'
# real world data isn't clean and is typically missing values.

'Trade-Offs in Missing Data Conventions'
# NaN is not available for all data types


'Missing Data in Pandas'
# NumPy supports 14 basic integer types
# Pandas uses sentinels for missing data, by choosing two
# Oython null values: the special floating-point NaN value and
# the Python None object.

'None: Pythonic missing data'
# the first Pandas sentinal value in Pandas is Python's None
# object. The one requirement for NumPy/Pandas is that None
# does not work with any arbitrary array and instead only
# works with the data type object.

import numpy as np
import pandas as pd

# NumPy infered that the contents of the array are Python objects
vals1 = np.array([1, None, 3, 4])
vals1

for dtype in ['object', 'int']:
    print('dtype =', dtype)
    get_ipython().run_line_magic('timeit', 'np.arange(1E6, dtype=dtype).sum()')
    print()

# Aggregations are not possible because of the use of Python
# objects such as None in the array. Note: sum() and min() 
vals1.sum()
# addition between an integer and None is undefined

'Nan: Missing Numerical data'
# NaN (Not a Number) is the other missing data representation
# which is recognized by all systems that use standard
# IEEE floating-point representation

vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype
# regardless of the the operation, and if a NaN object comes in
# contact with another NaN object, the results of arithmetic with
# NaN will be another NaN

1 + np.nan

0 * np.nan

# aggregates also return a nan value
vals2.sum(), vals2.min(), vals2.max()

# special NumPy aggregates which ignore missing values
np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)
# Note: NaN is a floating-point value, there is no NaN
# for integers, strings, or other types

'NaN and None in Pandas'

pd.Series([1, np.nan, 2, None])

x = pd.Series(range(2), dtype=int)
x

# setting an integer value in an array to np.nan will automatically
# upcast the values to a floating-point to accommodate the None value
x[0] = None
x
# Pandas automatially converts None to a NaN
# strings are always stored with an object dtype


'Operating on Null Values'
# there are methods for handling missing data in Panda sthat include
# detecting, removing, and replaing null values.

'Detecting null values'
# Pandas has two useful methoods for detecting null data:
# isnull() and notnull() which return a Boolean mask over
# the data

data = pd.Series([1, np.nan, 'hello', None])
data.isnull()

# using a Boolean mask directly on a series
# only returns elements that are not null
data[data.notnull()]

'Dropping null values'

# dropna() removes NA  (NaN or None) values
data.dropna()

df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6 ]])
df

# dropna cannot drop only a single value from a DataFrame,
# the only option is full rows or full columns. By default
# dropna() will drop all row with ANY null value
df.dropna()

# an option of dropna() is to drop by column with the axis=1
# parameter
df.dropna(axis='columns')

# creating a new column with all locations populated with NaN
df[3] = np.nan
df

# drop all columns with NaN data when all data in the column
# is NaN, this preserves "good data"
df.dropna(axis='columns', how='all')

# the thresh parameter lets you specify the minumum number
# of non-nullvalues for the row/column to be kept e.g.,
# if the row has less than 3 non-null values drop it
df.dropna(axis='rows', thresh=3)

'Filling null values'
# Pandas provides the fillna() method, which returns a copy
# of the array with the null values replaced

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data

# fill all NA entries with a 0
data.fillna(0)

# forward fill
data.fillna(method='ffill')

# back-fill
data.fillna(method='bfill')

df

# forward-fill per row
df.fillna(method='ffill', axis=1)
# a previous value needs to be available for a forward-fill
# or it will be left as NA
