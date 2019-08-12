#!/usr/bin/env python
# coding: utf-8

'Hierarchical Indexing'
# higher-dimensional data is data which is indexed by more
# than one or two keys. With multi-indexing it is possible
# to compactly represent the data in a one-dimensional Series
# or two-dimensional DataFrame object.

import pandas as pd
import numpy as np

'A multiply Indexed Series'
# how to represent two-dimensional data within a one-dimensional Series

'The bad way'

# tracking data about states from two different years
# using Python tuples as keys
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378192,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
pop

# slicing with a tuple indexing scheme
pop[('California', 2010):('Texas', 2000)]
# this is not clean nor efficient for large datasets

'The Better way: Pandas MultiIndex'

# creating a multiindex from the tuple-based index
index = pd.MultiIndex.from_tuples(index)
index
# the MultiIndex contain multiple levels of indexing --
# the state names and the years, as well as multiple labels
# for each data point

# re-indexing the series with the pop series,we get the 
# hierarchical representation of the data
pop = pop.reindex(index)
pop

# accessing all data which the second index is 2020 with slicing
pop[:, 2010]

'MultiIndex as extra dimension'
# this same data could have been stored as a DataFrame

# the unstack() method converts a multiply indexed Series
# into a conventionally indexed DataFrame
pop_df = pop.unstack()
pop_df

# converts a DataFrame to a multiply index Series
# the exact oppisite of unstack()
pop_df.stack()
# each extra level in a muli-index represents an extra dimension
# of data, with this is mind it means there is more flexibility
# in the data which can be handled. This is why we can represent
# data of three or more dimensions in a Series or DataFrame.

# adding a new column of demograghic data for each state
# into a DataFrame, by using MultiIndexing
pop_df = pd.DataFrame({'total': pop,
                       'under 18': [9267089, 9284094,
                                    4687374, 4318033,
                                    5906301, 6879014]})
pop_df

# computing the fraction of people under 18 by year, given
# the data above by using a ufunc
f_u18 = pop_df['under 18'] / pop_df['total']
f_u18.unstack()

'Methods of MultiIndex Creation'
# how to construct a multiply indexed Series or DataFrame

# passing two lists of index arras to the constructor
df = pd.DataFrame(np.random.rand(4,2),
                  index=[['a', 'a', 'b', 'b'],[0,1,1,2]],
                  columns=['data1', 'data2'])
df

# passing a dictionary with appropriate tuples as keys
# Pandas automatically recogizes this and will use a MuliIndex

data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)

'Explicit MultiIndex constructors'
# for flexibility use the class method constructor pd.MultiIndex

# from a list of arrays giving the index values within each level
a = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1,2,1,2]])
a

# from a list of tuples giving the multiple index values of each point
b = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b',1), ('b', 2)])
b

# from a Cartesian product of single indicies
c = pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
c

# directly constructing a MultiIndex usin its internal encoding
# by passing level (a list of list containing available index
# values for each level) and labels (a list of lists that reference
# these labels)
d = pd.MultiIndex(levels=[['a', 'b'], [1,2]],
                  labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
d

'MultiIndex level names'
# it is possible to name the levels of a MultiIndex.

# passing the names argument to any of the above MultiIndex
# constructors, or by setting the names attribute of the index
pop.index.names = ['state', 'year']
pop

'MultiIndex for columns'
# rows and columns can have a MultiIndex with a DataFrame

# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
# mock some data
data = np.round(np.random.rand(4,6), 1)
data[:, ::2] *= 10
data += 37

#create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data
# this is essentially four-dimensional data where the dimensions
# are paitent, measurement, year, visit

# indexing the top-level columns by the persons name and 
# getting a full DataFrame with the person's info
health_data['Guido']

'Indexing and Slicing a MultiIndex'
# it helps if you think of MultiIndex indices as added dimensions

'Multiply indexed Series'

pop

# accessing a single element by indexing with multiple terms
pop['California', 2000]

# MultiIndexing supports partial indexing with lower-level indices maintained
pop['California']

# partial slicing is possible with a sort MultiIndex
pop.loc['California':'New York']

# partial indexing performed on lower levels by passing an empty 
# slice in the first index
pop[:, 2000]

# selction based on a Boolean mask
pop[pop > 22000000]

# selection based on fancy indexing
pop[['California', 'Texas']]


# In[51]:


'Multiply indexed DataFrames'

# columns are primary in a DataFrame
health_data

# getting Guido's heart rate
health_data['Guido', 'HR']

# a single-index case using iloc
health_data.iloc[:2, :2]

# the loc and iloc indexers provide an array-like view of the
# underlying two-dimensional data. Each individual index can
# be passed as a tuple of multiple indices
health_data.loc[:, ('Bob', 'HR')]

'''
# trying to create a slice witnin a tuple will cause an error
health_data.loc[(:, 1), (:, 'HR')]
'''

# you can get around this error by building the desired slice with
# Python slice() function, but it is best to use Pandas IndexSlice object
idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, 'HR']]

'Rearranging Multi-Indices'
# there are many ways to finely control the rearrangement of data
# between hierarchical indices and columns. Knowing how to effectively
# transform data is fundamental.

'Sorted and unsorted indices'
# slicing operations will fail if the index is not sorted

# the data is not lexographically sorted
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
# creating the index labels in relation to the second dimension of
# data so each label has an index underneath it
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data

# partial slices cause an error
'''
try:
    data['a', 'b']
except KeyError as e:
    print(type(e))
    print(e)
'''

# this error is caused due to the MultiIndex levels not 
# being lexographically sorted

# Pandas provides convenience routines to sort the levels
# of a MultiIndex with sort_index() and sortlevel() methods
# of the DataFrame
data = data.sort_index()
data

# now partial slicing works with the index sorted
data['a':'b']

'Stacking and unstacking indices'
# it is possible to convert a dataset from a stacked multi-index
# to a simple two-dimensional representation while specifying the level
pop.unstack(level=0)

pop.unstack(level=1)

# stack() can be used to recover the original Series
pop.unstack().stack()

'Index setting and resetting'
# you can rearrange hierarchical data by turning the index labels
# into columns with the reset_index() method.

# turning this MultiIndexed Series into a DataFrame with no
# MultiIndex
pop

# calling the reset_index() method on the population dictionary
# will result in a DataFrame with a state and year column holding
# the information that was formerly in the index.

pop_flat = pop.reset_index(name='population')
pop_flat

# building a MultiIndex from the column values with the set_index()
# methd of the DataFrame which returns a multiply indexed DataFrame
pop_flat.set_index(['state', 'year'])

# this is typically the most useful pattern when dealing with
# real world datasets

'Data Aggregations on Multi-indices'
# for hierarically indexed data Pandas passes the aggregation
# methods, such as mean(), sum(), and max() as a level parameter
# which controls the subset of data the aggregate is computed on

health_data

# averaging the measurement in two visits each year by naming
# the index level year
data_mean = health_data.mean(level='year')
data_mean

# using the axis keyword to take the mean among levels on
# on the columns as well to find the average heart rate and
# temperature measured among all subjects in all visits each year
data_mean.mean(axis=1, level='type')
