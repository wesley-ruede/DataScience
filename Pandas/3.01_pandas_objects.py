# 08/08/19
#!/usr/bin/env python
# coding: utf-8

"Introducing Pandas Objects"
# Pandas is an enhanced version of NumPy's structured arrays
# with labels instead of simple integer indicies. The fundametal 
# Pandas data structures are: Series, DataFrame, Index.
# Pandas requires an import of NumPy

import numpy as np
import pandas as pd

'Pandas Series Object'

# A Pandas Series is a one-dimensional array of indexed data

data = pd.Series([0.23,0.5,0.75,1.0])
data

# The Series wraps the sequnce of values and index attributes.
# The values are simply a familiar NumPy array.

data.values

# the index is an array-like object of type pd.Index
data.index

data[1]

data[1:3]

'Series as generalized NumPy arrays'

data = pd.Series([0.25,0.5,0.75,1.0],
                index=['a','b','c','d'])
data

data['b']

data = pd.Series([0.25,5,8,9.1,],
                index=[5,90,'a',True])
data

data['a']

'Series as specialized dictionaries'
# a Series is a structure that maps typed keys to a set
# of typed values. This similar to a dictionary as
# a dictionary maps arbitrary keys to arbitrary values. The 
# info which is similar to a NumPy strucutured array is
# what makes a Pandas series so efficient compared to a dictionary

population_dict = {'California': 39332521,
                   'Florida': 19552860,
                   'Illinois': 12882135,
                   'New York': 19651127,
                   'Texas': 26448193,}
# construting a Series from a Python dictionary
population = pd.Series(population_dict)
population

# typical dictionary style item access can br preformed
population['California']

# a Series also support array style operations such as slicing
population['California':'Illinois']

'Constructing Seres objects'
# all Series are constructed by some verion of the following:
# pd.Series(data, index=index)

# data can be a list or a NumPy array
pd.Series([2, 4, 6])

# data can be a scalar, which is repeated to fill the specified index
pd.Series(5, index=[100, 200, 200])

# data can be a dictionary,in which the index deafults to 
# sorted dictionary keys
pd.Series({2:'a', 1:'b', 3:'c'})

# no matter what the index can be explicitly set
# the Series is only populated with the explicit id keys
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])

'Pandas DataFrame Object'
# a DataFrame can be looked at as a generalization of a NumPy
# array or a specialization of a Python dictionary

# a one-dimensional array with flexible indicies
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area

# constructing a two-dimensional object from the population
# and area Series with dictionary
states = pd.DataFrame({'population': population,
                       'area': area})
states

# a DataFrame has an index attribute ust like a Series
states.index

# a DataFrame also has another attribute named columns 
# which is an Index object holding the coluns labels
states.columns

'DataFrames as specialized dictionaries'
# a dictionary maps to a key value, whereas a DataFrame
# maps a colmn name to a Series of column data.

# calling the 'area' attribute returns the Series object 
# containing the areas from before
states['area']
# take note that in a two-dimensional NumPy array, data[0]
# returns the first row. For a DataFrame, data['col0'] will
# return the first column. A DataFrame in its essence are better
# thought of a generalized dictionaries rather than generalized arrays

'Construting DataFrame Objects'
# DataFrames can be constructed in quite a few ways

'From a single Series object'
# A DataFrame is a collection of Series objects, and a 
# single-column DataFrame can be constructed from a sinvle Series
pd.DataFrame(population, columns=['population'])

'From a list of dict'

# a simple list comprehension
data = [{'a':i, 'b':2 * i}
        for i in range(3)]
pd.DataFrame(data)

# missing values will be fillied with Nan -- 'not a number'
pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

'From a dictionary of Series objects'

# a DataFram constructed froma a dictionary of Series objects
pd.DataFrame({'population': population,
              'area': area})

'From a two-dimensional NumPy array'

# with a two-dimensional array, we can create a DataFrame
# by specifying columns and index names
pd.DataFrame(np.random.rand(3,2),
             columns=['foo', 'bar'],
             index=['a','b','c'])

'From a Numpy structured array'

# a DataFrame is a lot like a structured array, and can be
# created directly from one

A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A
pd.DataFrame(A)

'The Pandas Index Object'
# the index object contains an explicit index and can be looked
# at as an immutable array or an ordered-set

ind = pd.Index([2, 3, 5, 7, 11])
ind

'Index as immutable aray'

# standard Python indexing notation to retrieve a value
ind[1]

# slicing
ind[::2]

# Index onjects have most of the typical NumPy attributes
print(ind.size, ind.shape, ind.ndim, ind.dtype)

# trying to alter an Index object is not possible
# ind[1] = 0
# this immutability is a safety net which makes it safer to share
# indicies between multiple DataFrames and arrays and avoid
# possible index modifications.

'Index as ordered set'
# Pandas facilitates set arithmetic.

indA = pd.Index([1, 3, 5, 7,9])
indB = pd.Index([2, 3, 5, 7, 11])

indA & indB # intersection

indA | indB # union

indA ^ indB # symmetric difference

