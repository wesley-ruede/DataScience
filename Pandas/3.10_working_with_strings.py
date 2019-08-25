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
'''
data = ['peter', 'paul', None, 'steve', 'rossum']
[s.capitalize() for s in data]
'''

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

'Example: Recipe Database'
# parsing the recipe data into ingredient lists so as to 
# find a recipe based on some ingredients on hand

# the database is in JSON form and will use a try block
# with the pd.read_json to read it
try:
    recipes = pd.read_json('data/recipeitems-latest.json')
except ValueError as e:
    print('ValueError:', e)
# each line is valid JSON data, but the entire file is not valid

# checking if the entire files is truly JSON
with open('data/recipeitems-latest.json') as f:
    line = f.readline()
    pd.read_json(line).shape

# constructing a string representation of all the JSON entries 
# and load the whole file with pd.read_json. 
# reading the file into a Python array
with open('data/recipeitems-latest.json', 'r') as f:
    # Extract each line
    data = (line.strip() for line in f)
    # reformat each line as an elemnt of a list
    data_json = "[{0}]".format(','.join(data))
# read the result as JSON
recipes = pd.read_json(data_json)

recipes.shape

# impicit indexing with the iloc attribute of Series and DataFrames
recipes.iloc[0]

# a closser look at the ingredients
recipes.ingredients.str.len().describe()
# perform simple aggfuncs on ingredients is reference to the 
# string lengths. The average (mean) is 250 characters long
# with a min() and a max() of almost 10000

# finding which recipes has the longest ingredient list
# using fancy indexing and pasing len() method with the str attribute
# of the dataframe index name attribute
recipes.name[np.argmax(recipes.ingredients.str.len())]

#  performing aggregates to explore how many of the 
# items are breakfast food
recipes.description.str.contains('[Bb]reakfast').sum()

# how many of the recipes require an ingredient
recipes.ingredients.str.contains('[Cc]innamon').sum()

# finding how many entries mispelled 'cinnamon' as 'cinamon'
recipes.ingredients.str.contains('[Cc]inamon').sum()

'A simple recipe reccomender'
# to create a recipe reccomender based on the dat is complicated
# by the herogeneity lof the data. This is no easy operation
# to extract a clean list of ingredients from each row

# creating list of common ingredients to simply search and 
# see wheter they are in each recipe's ingredient list.
spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley',
             'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']

# building a Boolean DataFrame indicating wheter this ingredient
# appears in the list
import re
spice_df = pd.DataFrame(dict((spice, recipes.ingredients.str.contains(spice, re.IGNORECASE))
                            for spice in spice_list))
spice_df.head()

# find the recipes that use parsley, paprika, and tarragon
# this is where query() method of DataFrame's high-performance comes in
selection = spice_df.query('parsley & paprika & tarragon')
len(selection)
# only 10 recipes have the combination requested

# using the index returned by the selection to discover the 
# names of the recipes that have this combo
recipes.name[selection.index]
# reduced the list by a factor of 20000 to make a more informed choice
