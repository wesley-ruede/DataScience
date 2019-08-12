#!/usr/bin/env python
# coding: utf-8

'Operating on Data in Pandas'

'Ufuncs: Index Preservation'
# NumPy ufuncs work on Pandas Dataframes and Series

import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
# call randint in an interval of 0 and 10, implicitly create
# a table with row-wise labels as the index, and finally
# create a column of data given an interval and a length
ser = pd.Series(rng.randint(0,10,4))
ser

# call randint in an interval of 0 and 10, implicitly create
# a table with columns-wise labels as the index, and finally
# create columns of data given an interval and shape
df = pd.DataFrame(rng.randint(0, 10, (3,4)),
                  columns=['A', 'B', 'C', 'D'])
df

# applying a numpy ufunc 
np.exp(ser)

# a complex calculation
np.sin(df * np.pi / 4)

'UFuncs: Index Alignment'

'Index alignment in Series'

area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                  'New York': 19651127}, name='population')

# didving the two series to compute the population density
population / area

# a union of indicies which can determine using standard Python
# set arithmetic
area.index | population.index

# missing tiems are marked as NaN 'Not a number'
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
# locations 0 + 0 (2 + missing = Nan), 1 + 1, 2 + 2, 3 + 3
A + B

# A.add(B) is the equivalent to calling A + B but allows
# for explicit specification of the fill_value keyword
# tht fills any missing values from A or B with a value
A.add(B, fill_value=0)

'Index alignment in a DataFrame'

A = pd.DataFrame(rng.randint(0,20, (2,2)),
                columns=list('AB'))
A

B = pd.DataFrame(rng.randint(0, 10, (3,3)),
                 columns=list('BAC'))
B

A + B

# the fill will be a mean of all values in A computed by
# first stacking the rows of A
fill = A.stack().mean()
A.add(B, fill_value=fill)

# Python object methods compared to Python operators
'''
Python Operator | Pandas Methods
+               | add()
-               | sub(), subtract()
*               | mul(), multiply()
/               | truediv(), div(), divide()
//              | floordiv()
%               | mod()
**              | pow()
'''

'Ufuncs: Operations Between DataFrame and Series'

# finding the difference between a two-dimensional and 
# one-dimensional NumPy arrays.

A = rng.randint(10, size=(3,4))
A

# find the difference of a two-dimensional array and one 
# of its rows

A - A[0]

# according to NumPy subtraction between a two-dimensional
# array and one of its rows is applied row-wise. In Pandas
# the convention operates row-wise by default

df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]

# operating column-wise with the object methods, while specifying
# the axis keyword
df.subtract(df['R'], axis=0)

halfrow = df.iloc[0, ::2]
halfrow

# Pandas preserves the alignment of indicies and columns
# with operations which means it can always maintain context
df = pd.DataFrame(A, columns=list('QRST'))
df - halfrow
