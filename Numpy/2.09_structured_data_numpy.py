#!/usr/bin/env python
# coding: utf-8

"Structed Data: NumPy's Sstructured Arrays"

# structured and record arrays which provide efficience
# storage for compound, heterogeneous data. This is somewhat
# similar to Pandas Dataframes.

import numpy as np

# different data catagories 
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

# this is clumsy and doesn't tell me that the arrays are related

x = np.zeros(4, dtype=int)

# use a compund data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

# 'U10' == Unicode string of maximum length 10
# 'i4' == 4-byte (i.e., 32 bit) integer
# 'f8' == 8-byte (i.e., 64 bit) float

# filling the array with our list of values
data['name'] = name
data['age'] = age
data['weight'] = weight
# all data is arranged together in one block of memory
print(data)

# it is now possible to refer to values either by index or name
# Get all names
data['name']

# Get first row of data
data[0]

# Get the name from the last row
data[-1]['name']

# Using Boolean masking alls for more sophisticated operations 
# such as filtering on age
# Get names where age is under 30
data[data['age'] < 30]['name']

'Creating Structured Arrays'

# Dictionary method

np.dtype({'names':('name', 'age', 'weight'),
          'formats':('U10', 'i4', 'f8')})

# numercal type
np.dtype({'names':('name', 'age', 'weight'),
          'formats':((np.str_, 10), int, np.float32)})

# compund list of tuples
np.dtype([('name', 'S10'), ('age,', 'i4'), ('weight', 'f8')])

# specifying types alone in a comma-seperated string
np.dtype('S10,i4,f8')

'More Advaned Compound Types '

# We can create a type where each element contains an array
# or matrix of value. We'll create a data type with a mat component
# consisting of a 3x3 floating-point matrix

tp = np.dtype([('id', 'i8'), ('mat', 'f8',(3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])

# Now each element in the X array consists of and 'id' and
# a 3x3 matrix. This NumPy dtype directly maps onto a C structure
# definition.

'RecordArrays: Structured Array with a Twist'

# Numpy also has the np.recarray class which is identical to
# structured arrays with a bonus: fields can be accessed as
# attributes rather than as dictionary key. 

data['age']

# viewing the data as a record array is a few keys shorter

data_rec = data.view(np.recarray)
data_rec.age

# THe downside is that there is quite a bit of overhead
# involved in accessing the fields.

get_ipython().run_line_magic('timeit', "data['age']")
get_ipython().run_line_magic('timeit', "data_rec['age']")
get_ipython().run_line_magic('timeit', 'data_rec.age')

