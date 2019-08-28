#!/usr/bin/env python
# coding: utf-8

'High-Performance Pandas: eval() and query()'
# Pandas allows for C-speed operations without costly allocation 
#of intermediate arrays via eval() and query() which rely on Numexpr

'Motivating query() and eval(): Compund Expressions'
# Pandas and NumPy support fast vectorized operations

# adding the elements of two arrays
import numpy as np
rng = np.random.RandomState(42)
x = rng.rand(1000000)
y = rng.rand(1000000)
get_ipython().run_line_magic('timeit', 'x + y')

# this is much faster than doing addition with a Python loop or comprehension
get_ipython().run_line_magic('timeit', 'np.fromiter((xi + yi for xi, yi in zip(x,y)), dtype=x.dtype, count=len(x))')

# a compound expression
msk = (x > 0.5) & (y < 0.5)

# NumPy evaluates each expression this is nearly equivalent
tmp1 = (x > 0.5)
tmp2 = (y < 0.5)
mask = tmp1 & tmp2
# every intermediate step is explicitly allocated in memory

# Numexpr has the abilty to compute compound expresions element by element 
# Numexpr accepts a string giving the NumPy style expresion
import numexpr
mask_numexpr = numexpr.evaluate('(x > 0.5) & (y < 0.5)')
np.allclose(mask, mask_numexpr)
# Pandas eval() and query() is conceptually similar and depend on Numexpr $

'pandas.eval() for Efficient Operations'
# the eval() funtion uses string expressions to efficiently compute operation on DataFrames

import pandas as pd
nrows, ncols = 100000, 100
rng = np.random.RandomState(42)
df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows, ncols))
                                  for i in range(4))

get_ipython().run_line_magic('timeit', 'df1 + df2 + df3 + df4')

# computing via pd.eval by constructing the expression as a string
get_ipython().run_line_magic('timeit', "pd.eval('df1 + df2 + df3 + df4')")

# with evl() it is 50% faster and uses less memory
np.allclose(df1 + df2 + df3 + df4,
            pd.eval('df1 + df2 + df3 + df4'))

'Operations supported by pd.eval()'

df1, df2, df3, df4, df5 = (pd.DataFrame(rng.randint(0, 1000, (100, 3)))
                           for i in range(5))

'Arithmetic operators'
# pd.eval accepts all arithmetic operators

result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
np.allclose(result1, result2)

'Comprison opertors'
# pd.eval accepts all comparison operators including chained expresions

# chained expression
result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
result2 = pd.eval('df1 < df2 <= df3 != df4')
np.allclose(result1, result2)

'Bitwise opertors'
# pd.eval() accepts only & and | bitwise operators

result1 = (df1 < 0.5) & (df2 < 0.5) | (df3 < df4)
result2 = pd.eval('(df1 < 0.5) & (df2 < 0.5) | (df3 < df4)')
np.allclose(result1, result2)

# pd.eval() support literal and and or Boolean expressions
result3 = pd.eval('(df1 < 0.5) and (df2 < 0.5) or (df3 < df4)')
np.allclose(result1, result2)

'Object attributes and indices'
# pd.eval() supports access to object attributes via the obj.attr syntax

# indexing via the obj[index] syntax
result1 = df2.T[0] + df3.iloc[1]
result2 = pd.eval('df2.T[0] + df3.iloc[1]')
np.allclose(result1, result2)

'Other opertions'
# function calls, conditional statements, and loops are not implemented in pd.eval()

'DataFrame.eval() for Column-Wise Operations'
# DataFrmes have an eval() method similr to pd.eval() which allows columns to be referrenced by name

# labeling an array
df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
df.head()

# using the pd.eval() to compute expressions with the columns
result1 = (df['A'] + df['B']) / (df['C'] - 1)
result2 = pd.eval("(df.A + df.B) / (df.C - 1)")
np.allclose(result1, result2)

# DataFrame.eval() allows for concise evluation of expresions based on columns
# treating the column names as variables within the expression
result3 = df.eval('(A + B) / (C - 1)')
np.allclose(result1, result3)

'Assignment in DataFrame.eval()'

df.head()

# using df.eval() to create a new column 'D' and assign the value computed from the other columns
df.eval('D = (A + B) / C', inplace=True)
df.head()

# modifying an existing column
df.eval('D = (A - B) / C', inplace=True)
df.head()

'Local vriables in DataFrame.eval()'
# DataFrame.eval() can operate on local varibles wiht a speicifed syntax

column_mean = df.mean(1)
result1 = df['A'] + column_mean
# the @ character marks a variable name instead of a column name which lets you evaluate to namespaces
result2 = df.eval('A + @column_mean')
np.allclose(result1, result2)
# the @ character is supported by the DataFrame.eval() method only and not pandas.eval() function

'DataFrame.query() Method'
# DataFrame.query() evaluates strings just as DataFrame.eval()

result1 = df[(df.A < 0.5) & (df.B < 0.5)]
result2 = pd.eval("df[(df.A < 0.5) & (df.B < 0.5)]")
np.allclose(result1, result2)


# In[44]:


# performing a filtering operation with query()
result2 = df.query("A < 0.5 and B < 0.5")
np.allclose(result1, result2)
# query() is more efficient than masking expressions and accept @ flag as a local vriable marker

Cmean = df['C'].mean()
result1 = df[(df.A < Cmean) & (df.B < Cmean)]
result2 = df.query('A < @Cmean and B < @Cmean')
np.allclose(result1, result2)

'Performnce: When to Use These Functions'
# computation time nd memory use are the two reason to use these functions especially with compound expressions

# a compund expression
x = df[(df.A < 0.5) & (df.B < 0.5)]

# an equivlent expression
tmp1 = df.A < 0.5
tmp2 = df.B < 0.5
tmp3 = tmp1 & tmp2
x = df[tmp3]
# if the size of the temporary DataFrame is signifigant 
# compared to available system memory then it is a good idea to use eval() and query()

# check the size of an array in bytes
df.values.nbytes
# the computationl time of classic methods such as a Boolen mask are typically faster for samll arrays
# and gains are not that signifignt even when not mxing out system memory 
