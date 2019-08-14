#!/usr/bin/env python
# coding: utf-8

'Combining Datasets: Merge and Join'
# Pandas offers high-performance, in-memory join and merge operations with the pd.merge() function.

# a new display function
import pandas as pd
import numpy as np

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

'Relational Algebra'
# the function pd.merge() is a subset of relational algebra, which is a formal ruleset for manipulating relational data
# and is the foundation of most databases.

'Catagories of joins'
# pd.merge() implements different joins such as one-to-one, many-to-one, and many-to-many. The type of join depends on
# the form of input data.

'One-to-one joins'
# the simplest join is a one-to-one join which isvery similar to column-wise concatenation

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
display('df1', 'df2')

# combining two DataFrames into a single DataFrame with the pd.merge() function
df3 = pd.merge(df1,df2)
df3
# pd.merge() recognizes similar columns and automatically joins them together using the columns as keys

'Many-to-one joins'
# many-to-one join are joins with one of the teo key columns containing duplicate entries. Many-to-one will preserve 
# duplicates as needed

df4 =pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
       'supervisor': ['Carly', 'Guido', 'Steve']})
display('df3','df4', 'pd.merge(df3,df4)')
# the resulting DataFrame has a new column 'supervisor' and duplicate data is kept as per the input

'Many-to-many joins'
# if the key in both the left and right array contains duplicates, then the result is a many-to-many.

# a DataFrame showing one or more skills associated with a group. A many-to-many join can recover the skills associated 
# with each person

df5 = pd.DataFrame({'group': ['Accounting', 'Accounting', 'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux', 'spreadsheets', 'organizing']})
display('df1','df5', "pd.merge(df1,df5)")
# pd.merge() has options to tune how join operations work

'Specifications of the Merge Key'
# the default behavior of pd.merge() is look for one or more matching column names between the two inputs and use this
# as the key.

'The "on" keyword'
# you can explicitly specify the name of the key columns using the on keyword which takes a column ame or a list of column names

# this ooperation only works if both DataFrames have the same column names 
display('df1', 'df2', "pd.merge(df1, df2, on='employee')")

'The left_on and right_on keywords'
# it is possible to merge two datasets with different column names

# with a dataset that has employee names labeled as names instead of employee we can use the left_on and right_on keywords
# to specify the two column names
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
display('df1', 'df3', 'pd.merge(df1,df3, left_on="employee", right_on="name")')
# the result has a redundant column name

# we can drop the redundant column with the drop() method of DataFrames
pd.merge(df1,df3, left_on="employee", right_on="name").drop("name", axis=1)

'The left_index and right_index keywords'
# it is possible to merge on an index rather than the column

df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
display('df1a','df2a')

# you can use the index as the key for merging by specifying the left_index and right_index flags in pd.merge()
display('df1a','df2a', "pd.merge(df1a,df2a, left_index=True, right_index=True)")

# the join() method of DataFrames performs a join() that defaults to joining th indices
display('df1a','df2a', 'df1a.join(df2a)')

# it is possible to mix indices and columns by combining left_index with right_on or left_on with right_index
display('df1a','df3',"pd.merge(df1a,df3, left_index=True, right_on='name')")

'Specifying Set Arithmetic for Joins'
# there is a special consideration of performing a join which is the type of set arithmetic used in the join

# a value appears in one key column but not in another
df6 = pd.DataFrame({'name': ['Peter','Paul','Mary'],
                    'food': ['fish','beans','bread']},
                    columns=['name','food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine','beer']},
                    columns=['name','drink'])
display('df6','df7',"pd.merge(df6,df7)")
# only a single 'name' identifier is in common with the merged data sets. The results contains an intersection of the two
# sets of input. This is an inner join.

# specifying an inner join with the how keyword
pd.merge(df6,df7, how='inner')

# there are other options for the how arguemnt which are outer, left, and right. An outer join returns a join over the 
# union of the input columns and fills all missing values with NaN
display('df6','df7', "pd.merge(df6,df7, how='outer')")

# the left join and right join return over the left entries and right entries, respectively
display('df6','df7', "pd.merge(df6,df7, how='left')")
# the output rows now correspond with the entries in the left input

'Overlapping Column Names: The suffix Keyword'
# DataFrames may have conflicting column names

df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1,2,3,4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3,1,4,2]})
display('df8', 'df9', "pd.merge(df8,df9, on='name')")
# the output would have two conflicting name so the pd.merge() function automatically appends a suffix _x or _y to make
# th output columns unique.

# it is possible to specify custom column names using the suffixes keyword
display('df8','df9', 'pd.merge(df8,df9, on="name", suffixes=["_L", "_R"])')

'Examples: US States Data'

# using Pandas read_csv function
pop = pd.read_csv('data/state-population.csv')
areas = pd.read_csv('data/state-areas.csv')
abbrevs = pd.read_csv('data/state-abbrevs.csv')

display('pop.head()', 'areas.head()', 'abbrevs.head()')

# to compute the rank of US states and territories by their 2010 population density we'll need to combine the datasets 
# with a many-to-one merge based on the state/region column of pop and the abbreviation column of abbrevs. The how parameter
# will be set to out so as not to throw data away
merged = pd.merge(pop,abbrevs, how="outer", left_on="state/region", right_on="abbreviation")
merged = merged.drop('abbreviation', 1) # drop duplicate info
merged.head()

# check if there are any mismatches by looking for rows with nulls
merged.isnull().any()

# figuring out what info in population is null
merged[merged['population'].isnull()].head()
# clearly it is Puerto Rico before 2000 most liekly due to the data not being in the source

# now there are some new state entries which are null which means there was no corresponding abbrevs entry
merged.loc[merged['state'].isnull(), 'state/region'].unique()
# it is now possible to tell that out population data includes entries for Puerto Rico and the United Sates while these
# entries do not appear in the state abbreviation key

# this can be fixed this by filling in the appropriate entries
merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()
# now all nulls have been handled in the state column

# time to merge the result with the area data by joining on the state column in both datasets
final = pd.merge(merged, areas, on='state', how='left')
final.head()

# chacking again for nulls to see if there were any mismatches
final.isnull().any()
# there are nulls in the area column

# looking for the regions that were ignored
final['state'][final['area (sq. mi)'].isnull()].unique()
# the areas DataFrame does not contain the area of the United States as a whole

# dopping the null values will be the best case as the population density of the whole United States is not relavant to the
# calculations we are to perform on the data
final.dropna(inplace=True)
final.head()

# now the data is prepared to asnswer the orginal question. First we'll select the data corresponding with the year 2000
# and the total population. We'll use the query() function to perform the computations quickly
data2010 = final.query("year == 2010 & ages == 'total'")
data2010.head()

# now it is time to compute the population and it will be necessary to re-index the data on the state and then compute the result
data2010.set_index('state', inplace=True)
density = data2010['population'] /data2010['area (sq. mi)']

density.sort_values(ascending=False, inplace=True)
density.head()
# the result is a ranking of the US states including DC and Puerto Rice in order of their 2010 population density
# in resident per square mile. We can see that Washington, DC is by far the densest  in the dataset

# can also check the end of th list
density.tail()
# Alaska is the least dense state averaging slightly over one person per square mile
# this kind of messy data merging is common with real-world datasets.
