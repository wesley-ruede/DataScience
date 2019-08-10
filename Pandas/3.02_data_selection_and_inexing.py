#!/usr/bin/env python
# coding: utf-8

'Data Indexing and Selection'
# a lot of the indexing is does in a similar fashion to NumPy

'Data Selection in Series'

'Series as dictionaries'
# the Series object provides a mapping from a collection of keys
# to a collection of values

import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data

data['b']

# using a Python dictionary-like expression
'a' in data

data.keys()

list(data.items())

# Series objects can be modified with a dictionary-like syntax
data['e'] = 1.25
data

'Series as one-dimensional array'
# a Series provides NumPy array syles item selection such as,
# slices, masking, and fancy indexing

# slicing by explicit index
data['a':'c']

# slicing by implicit integer index
data[0:2]
# the final index is excluded with a slice

# masking
data[(data > 0.3) & (data < 0.8)]

# fancy indexing
data[['a', 'e']]

'Indexers: loc, ilock, and ix'

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data

# explicit index when indexing
data[1]

# implicit index when slicing
data[1:3]

# the loc attribute allows indexing and slicing that always
# reference the explicit index
data.loc[1]

data.loc[3:5]

# the iloc attributes allows indexing and slicing that always 
# references the implicit Python-style inexing
data.iloc[1]

data.iloc[1:3]

# explicit is better than implicit

'Data selection in DataFrame'

'DataFrame as a dictionary'
# a dictionary of related series objects

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})
data

# individual Series can be accesed by the columns in the DataFrame
# via dictionary style indexing of the column name

data['area']

# attribute-style access with column names that are strings
data.area

# attribute-style column access actually accesses the same
# object as the dictionar-style access
data.area is data['area']

# if column names conflict it will not be possible to use
# attribut style access or if the column names ar not strings

data.pop is data['pop']

# attribute-style column assignment should not be done
# dictionary-style should be used instead suh as adding a new
# column

data['density'] = data['pop'] / data['area']
data

'DataFrames as a two-dimensional array'

# the values attribute shows the raw underlying nature of DataFrames
data.values

# transpose the full DataFrame to swap rows and columns
data.T

# passing a single index to an array accesses a row
data.values[0]

# passing a single 'index' to a DataFrame accesses a coulmn
data['area']

# for array style indexing we will se the indexers. We can
# index the underlying array as a NumPy array using implicit
# Python-style indexiing, with the DatFrames index and column
# labels intact

data.iloc[:3, :2]
# three rows down and 2 columns over

# using loc to index the underlying data in an array-like
# style but using the explicit index and column names
data.loc[:'New York', :'pop']

# ix allows for a hybrid of the these two approaches
data.ix[:3, :'pop']

# loc can combine masking and fancy indexing
data.loc[data.density > 100, ['pop', 'density']]

# modifying values in a standard NumPy style
data.iloc[0, 2] = 90
# row 0 and column 2
data

'Additional indexing conventions'

# slicing refers to rows
data['Florida':'Illinois']

# refer to rows by number rather than index
data[1:3]

# direct masing operations which interpret row-wise rather
# than column-wise
data[data.density > 100]
