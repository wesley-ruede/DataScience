#!/usr/bin/env python
# coding: utf-8

'Pivot Tables'
# Pivot tables take column-wise data as input and groups the entries into a two-dimensional table that provides 
# a multidimensional summarization of the data. A pivot table is a multidimensional version of groupby aggregation

'Motivating Pivot Tables'

import numpy as np
import pandas as pd
import seaborn as sns 
# using the Titanic data set through the load_dataset() method of seaborn which downloads the data
titanic = sns.load_dataset('titanic')

# the head() method returns the top n (5 by default) rows of a dataset with DataFrames and Series
titanic.head()

'Pivot Tables by Hand'
# it would be possible to use the groupby operations

# using groupby
titanic.groupby('sex')[['survived']].mean()
# three in four women survivied while on one in five men survived

# grouping by class and gender, selecting survival, applying a mean aggregate, combining the resulting groups, and 
# unstacking the hierarchocal index to reveal the hidden multidimensionality
titanic.groupby(['sex','class'])['survived'].aggregate('mean').unstack()
# this is a two-dimnensional GroupBy

'Pivot Table Syntx'
# the pivot_table method of DataFrames is equivalent to a two-dimensional GroupBy

# equivalent syntax to GroupBy
titanic.pivot_table('survived', index='sex', columns='class')
# first-class women survival rate is almost 100% where as third-class males survival rate is barely over 10%

'Multi-level pivot tables'
# pivot tables can be specified with multiple levels 

# binning age as a thrid dimension by using the pd.cut function
age = pd.cut(titanic['age'], [0,18,80])
titanic.pivot_table('survived', ['sex', age], 'class')

# adding the fare paid to the columns using pd.qcut to automatically compute quantities
fare = pd.qcut(titanic['fare'], 2)
titanic.pivot_table('survived', ['sex', age], [fare, 'class'])
# a four dimensional aggregation with hierarchical indicies

'Additional pivot table options'
# call signiture of Pandas 0.18
'''
DataFrame.pivot_table(data, values=None, index=None, columns=None,
                     aggfunc='mean', fill_value=None, margins=False,
                     dropna=True, margins_name='All')'''
# aggfunc controls the type of aggregations applied which mean by default

# specifying a dictionary to map a column to any aggregation
titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived': sum, 'fare':'mean'})

# computing totals along each grouping wiht the margins keyword
titanic.pivot_table('survived', index='sex', columns='class', margins=True)

'Example: Birthrate Data'
# new data on birthrates in United States from the Center for Disease Control

births = pd.read_csv('data/births.csv')

# births grouped by date and gender
births.head()

# add a decade column with male and female births as a function of decade
births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')

# a pivot table with the plot() method
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year')
