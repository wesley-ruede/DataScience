#!/usr/bin/env python
# coding: utf-8

'Combining Datasets: Concat and Append'
# one of the best parts of studying data is combining data from
# different sources. DataFrames and Series are built with 
# simple concatenation and complex database-style merge and joins

import pandas as pd
import numpy as np

# a function that creates a DataFrame off a particualr form
def make_df(cols, ind):
    '''Quickly create a DataFrame'''
    # using a dictionary to store a list compreshension
    # create an element C with the same name as the column name
    # and create element i aswell as concatenate the element 
    # with element C in relating to the rows and columns moving 
    # left to right abd top to bottom
    data = {c: [str(c) + str(i) for i in ind]
           for c in cols}
    return pd.DataFrame(data, ind)

# example DataFrame
make_df('ABC', range(3))

# a class that makes displaying multiple DataFrames side by
# side possible. The _repr_html_() method is used to implement 
# rich object display

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

'Recall: Concatenation of NumPy arrays'
# Series and DataFrame object concatenation is very similar 
# to NumPy arrays which can be performed with the np.concatenate() function

# combining the contents of two or more arrays into a single array
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
np.concatenate([x,y,z])

# the first argument is a list or tuple of arrays to concatenate
# you can use the axis keyword to specify the axis along which
x = [[1,2],
     [3,4]]
np.concatenate([x,x], axis=1)

'Simple Concatenation with pd.concat'
# pd.concat has a similar syntax to np.concatenate with more options

# signature in Pandas
'''
pd.concat(objs, axis=0, join='outer', join_axes=None, 
          ignore_index=False, keys=None, levels=None,
         names=None, verify_interity=False, copy=True)'''

# pd.concat be used with Series and DataFrames

ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['d','e','f'], index=[4,5,6])
pd.concat([ser1,ser2])

# pd.concat() works on higher-dimensional objects such as DataFrames
df1 = make_df('ab', [1,2])
df2 = make_df('ab', [3,4])
display('df1', 'df2', 'pd.concat([df1, df2])')
# concatenation takes places row-wise within the DataFrame (i.e., axis=0)

# pd.concat() allows specification of an axis
df3 = make_df('ab', [0,1])
df4 = make_df('cd', [0,1])
display('df3','df4', "pd.concat([df3,df4], axis=1)")

'Duplicate indices'
# Pandas pd.concat() function preserves indices 
# even with duplicate indices

x = make_df('ab', [0,1])
y = make_df('ab', [2,3])
y.index = x.index # creating a duplicate indices
display('x','x', 'pd.concat([x,y])')
# pd.concat() has a few ways to handle duplicate indices

'Catching the repeats as an error'
# specifying the verify_integrity flag as True will ensure 
# the resulting indices do not overlap while using pd.concat()

try:
    pd.concat([x,y], verify_integrity=True)
except ValueError as e:
    # raise an error if there is a duplicate indices and
    # print an error message if so
    print("ValueError:", e)

'Ignoring the index'
# it is possible to ignore the index by setting the ignore_index
# flag to True which will create a new integer index for the Series
display('x','y', 'pd.concat([x,y], ignore_index=True)')

'Adding MultiIndex keys'
# you can use the keys option to specify a label for data sources
# with a resulting hmultiply indexed DataFrame
display('x','y', 'pd.concat([x,y], keys=["x","y"])')

'Concatenation with joins'
# data from diferent source might have different sets of column
# names, and pd.concat offers several options to handle this case

df5 = make_df('ABC', [1,2])
df6 = make_df('BCD', [3,4])
# concatenating two DataFrames which have no columns in common
display('df5','df6', 'pd.concat([df5,df6])')

# to change data which is filled with NaN by default, we can 
# specify join parameter. Join is a union of the input columns
# but with a change to an intersection of the columns
display('df5','df6', 'pd.concat([df5,df6], join="inner")')


# In[34]:


# you can directly specify the index of the remaining columns 
# using the join_axes arguments which takes a list of index objects
display('df5','df6',
        'pd.concat([df5,df6], join_axes=[df5.columns])')

'The append() method'
# the append method can accomplish an operation such as
# pd.concat([df1,df2]) in fewer keystrokes by simply calling
# df1.append(df2)

# unlike Python's list method append(), Pandas methds do not
# modify the original object and instead create a new object
# with the data combined. The append() method is not efficient
# because it creates a new objects, thus it is more effective
# to build a list of DataFrames and pass them all to concat()
display('df1','df2', 'df1.append(df2)')
