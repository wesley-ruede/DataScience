#!/usr/bin/env python
# coding: utf-8

'Vectorized String Operations'
# vecortoized string operations are an essential piece of data munging (e.g., cleaning data)

'Introducing Pandas String Operations'
# NumPy and Pandas generalie arithmetic opertions

import numpy as np
x = np.array([2,3,5,7,11,13])
x * 2
# a vectorized operations to simplify operating on data

# numpy does not provide a way of operating on string and a
# verbose loop syntax is required instead
data = ['peter', 'paul', 'steve', 'rossum']
[s.capitalize() for s in data]

# This will break if any values are missing
data = ['peter', 'paul', None, 'steve', 'rossum']
[s.capitalize() for s in data]

# creating a Series from the data
import pandas as pd
names = pd.Series(data)
names

# handing missing data with the str attribute of Pandas Series
# and capitalizing all enties without skipping a missing value
names.str.capitalize()

'Tables of Pandas String Methods'

monte = pd.Series(['Grahm Chapman', 'John Cleese','Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])

'Methods similar to Python string methods'
# Pandas str methods mirror Python string methods
# |len() | lower() | translate() | islower() | |ljust() 
# | upper() | startswith() | isupper() | |rjust() | find() 
# | endswith() | isnumeric() | |center() | rfind() | isalnum() 
# | isdecimal() | |zfill() | index() | isalpha() | split() 
# | |strip() | rindex() | isdigit() | rsplit() | |rstrip() 
# | capitalize() | isspace() | partition() | |lstrip() | swapcase() 
# | istitle() | rpartition() |

# makes all letters lowercase
monte.str.lower()

# returns a literal length value as an integer
monte.str.len()

# returns a Boolean values
monte.str.startswith('T')

# returns a subarray for each element within the series 
monte.str.split()

'Methods using regular expressions'
# several Pandas methods accept regular expressions and follow the 
# API conventions of Python's re module

# extracting the first name from each element  of the contiguous
# group of character at the begining of each element
monte.str.extract('([A-Za-z]+)', expand=False)
# remove the expand parameter and it wil return a DataFrame

# finding all names that start and end with a consonant
monte.str.findall(r'^[^AEIOU].*[^aeiou]$')

'Miscellaneous methods'
# get() -> Index each element
# slice() -> Slice each element
# slice_replace() -> Replace slice in each element with passed value
# cat() -> Concatenate strings
# repeat() -> Repeat values
# normalize() -> Return Unicode form of string
# pad() -> Add whitespace to left, right, or both sides of strings
# wrap() -> Split long strings into lines with length less than a given width
# join() -> Join strings in each element of the Series with passed separator
# get_dummies() -> extract dummy variables as a dataframe

'Vectorized item access and slicing'
# get() and the slice() operation enable vectoried element 
# access from each array

# Pythons normal indexing syntax monte.str.slice(0,3) is the 
# same as monte.str[0:3]
# getting the first three characters of each array
monte.str[0:3]

#extracting the last name of each entry by combing split() and get()
monte.str.split().str.get(-1)

'Indicator variables'
# the get_dummies() is useful when your data has a column contains some sort of 
# coded indicator

full_monte = pd.DataFrame({'name': monte,
                           'info': ['B|C|D', 'B|D', 'A|C',
                                    'B|D', 'B|C', 'B|C|D']})
full_monte

# the get_dummies() routine lets you quickly split-out the
# indicator variables into a DataFrama
full_monte['info'].str.get_dummies('|')
