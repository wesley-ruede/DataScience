#!/usr/bin/env python
# coding: utf-8

'Aggregation and Grouping'
# using the mean(), median(), sum(), min(), and max() functions of Pandas to gain some insight from a single integer in 
# a data set

# a new magic display class

import numpy as np
import pandas as pd

class display(object):
    """Display a HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family: "Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    
    def __init__(self,*args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                        for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                          for a in self.args)

'Planets Data'
# the Seaborn package has datasets that can be downloaded

# using Seaborn datasets with the load_dataset() function
import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape

planets.head()

'Simple Aggregation in Pandas'

# using a one-dimensional NumPy array to create a Pandas Series
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser

# using Pandas sum() function
ser.sum()

ser.mean()

# with DataFrames, by defaul the aggregates return results witin
# each column
df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df

# a mean based on the columns
df.mean()

# specifying the axis argument can aggregate within each row
df.mean(axis='columns')

# Pandas Series and DataFrames have a convenience method describe()
# which computes several common aggregates
planets.dropna().describe()
# exoplanets were discovered as far back as 1989 based on the year column
# simple aggregations are not enough which is where groupby comes in
# which allows aggregations on a subset of data

'GroupBy: split, Apply, Combine'
# it is preferential to aggregate conditionally based on some
# index which is implemented by the groupby operation. Groupby
# comes from SQL database language

'Split, apply, combine'
# groupby accomplishes:
# the split step involves breaking up and grouping a DataFrame
# depending on the value of the specified key
# the apply step involves computing some function usually an
# aggregate, transformation, or filtering, within the individual groups
# the combine step merges the results of these operation in an
# output array.
# essentially intermidiate splits don't need to be explicitly instantiated

# simple DataFrame for input
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])
df

# passing the desired key column to perform a basic split-apply-combine
# with the groupby method of DataFrames
df.groupby('key')
# groupby returns a DataFrameGroupBy object instead of a DataFrame
# but does no actual computation until an aggregate is applied to it

# producing a result with the sum() aggregate applied to the
# DataFrameGroupBy object. Itis possible to use any Pandas or 
# NumPy aggregation as well as any valid DataFrame operation
df.groupby('key').sum()

'The GroupBy object'
# the GroupBy object in a lot of ways is a colection of DataFrames.
# the most import operations of GroupBy are aggregate, filter, transform, and apply

'Column indexing'
# GroupBy supports column indexing the same as DataFrames and
# returns a modified GroupBy object
planets.groupby('method')

# selecting a particlar Series group from the original DataFrame
# group by reference to the column name.
planets.groupby('method')['orbital_period']

# again, no computation is done with the GroupBy object until
# an aggregate function is called on the object
planets.groupby('method')['orbital_period'].median()
# the general scale of orbital periods in days that
# the method is sensitive to

'Iteration over groups'
# GroupBy object supports direct iteration over the groups
# and returns each group as a Series or DataFrame

# this oepration is useful to do things manually though it is
# normally better to use the built-in apply functionality
for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))

'Dispatch methods'
# with Python class magic  any method not explicitly implemented by the GroupBy object
# will be passed through and called on the groups, whether they
# are Series or DataFrame objects

# using the describe() method of DataFrames to perform a set of
# aggregation that describe each group in the data
data = planets.groupby('method')['year'].describe().unstack()
data

test = pd.DataFrame(data)
check = test.reset_index(inplace=True)
check

test

'Aggregate, filter, transform, apply'
# GroupBy objects have aggregate(), filter(), transform(), and apply() methods

rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A','B','C','A','B','C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                   columns= ['key', 'data1', 'data2'])
df

'Aggregation'
# the aggregate() method allows flexible data types including 
# a string, a function, or a list and compute all the aggregates at once

# combining aggregates min(), median(), and max() with the
# aggregate() method
df.groupby('key').aggregate(['min', np.median, max])

# passing a dictionary mapping the column names to operation applied on the column
df.groupby('key').aggregate({'data1':'min',
                             'data2':'max'})

'Filtering'# fitering allows for data to be dropped based on the group ptoperties

def filter_func(x):
    # keeping all groups in which the standard deviation is larger
    # than a critical value (4)
    return x['data2'].std() > 4

display('df', "df.groupby('key').std()", "df.groupby('key').filter(filter_func)")

'Transformation'
# aggregation returns a reduced version of data while transformation returns
# a transformed version to recombine with the output being the same 
# shape as the input

# centering the data by subtracting the group-wise mean
df.groupby('key').transform(lambda x: x.mean())

'The apply() method'
# the apply() method allows you to apply an arbitrary function
# to the group by results. The function takes a DataFrame and returns 
# a Pandas object (either a Series or DataFrame) or a scalar

# the apply() method normalizes the first column by the number of seconds
def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x

display('df', "df.groupby('key').apply(norm_by_data2)")

'Specifying the split key'

'A list, array, series, or index providing the grouping keys'
# A key can be any series or list with a length matching that of the DataFrame

L = [0,1,0,1,2,0]
display('df', 'df.groupby(L).sum()')

# a more verbose way of accomplishing the df.groupby('key')
display('df', "df.groupby(df['key']).sum()")

'A dictionary or series mapping index to group'

# a method to provide a dictionary that maps index values to the group key
df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
display('df2', 'df2.groupby(mapping).sum()')

'Any Python function'

# you can pass any Python function that will input the index value
# and output the group
display('df2', 'df2.groupby(str.lower).mean()')

'A list of valid keys'

# any of the preceeding key choices can be combined to group 
# on a multi-index
df2.groupby([str.lower, mapping]).mean()

'Grouping example'

# counting discovered planets by method and by decade
decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)
