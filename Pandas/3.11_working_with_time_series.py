#!/usr/bin/env python
# coding: utf-8

'Working with Time Series'
# Pandas was built in the context of Financial modeling date and time data are accessed a few ways: Time Stamps, Time Intervals
# Periods, Time Deltas, and Durations

'Dates and Times in Python'
# Pandas time series tools are the most useful for data science applications

'Native Python date and times: datetime and dateutil'
# Python basic built-in object for date and time is datetime module

from datetime import datetime
datetime(year=2015, month=7, day=4)

from dateutil import parser
date = parser.parse('4th of July, 2015')
date

# printing the day of the week with the datetime object
date.strftime('%A')
# using one of the standard string format codes

'Typed arrays of times: NumPy\'s datetime64'
# datetime64 encode dates as 64-bit integers

import numpy as np
date = np.array('2015-07-04', dtype=np.datetime64)
date

# performing vectorized operation on Nmpys datetime object
date + np.arange(12)
# this is much quicker than Python's built in

# numpy will infer the desired unit from the input for
# example this day-based datetime:
np.datetime64('2015-07-04')

# minute based datetime based on local timezone
np.datetime64('2015-07-04 12:00')

# force nanosecond-based time
np.datetime64('2015-07-04 12:59:59.50', 'ns')
# datetime64[ns] is acceptable in most real world data

'Dates and times in pandas: best of both worlds'
# from a group of Timestamp objects, Pandas can construct a 
# DatetimeIndex as an index to be useed in DataFrames and  Series

import pandas as pd
date = pd.to_datetime('4th of July, 2015')
date

date.strftime('%A')

# doing a NumPy-style vectorized operation directly on an objects day
date + pd.to_timedelta(np.arange(12), 'D')

'Pandas Time Series: Indexing by Time'

# constructing a Series object that has time indexed data
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                         '2015-07-04', '2015-08-04'])
data = pd.Series([0,1,2,3], index=index)
data

# indexing by passing a range of indices to be displayed
data['2014-07-04':'2015-07-04']

# obtaining a slice of all data within a year
data['2015']

'Pandas Time Series Data Structures'
# for time stamps Pandas uses the DatetimeIndex structure
# for time Periods Pandas uses the PeriodIndex structure
# for time deltas or durations Pandas uses TimedeltaIndex structure
# the most fundamental objects are Timestamp and DatetimeIndex


# passing a seriesing of dates by default yields a DatetimeIndex
dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                        '2015-Jul-6', '07-07-2015', '20150708'])
dates

# any DatetimeIndex can be converted to a PeriodIndex with
# to_period() function and using format code 'D' for days
dates.to_period('D')

# creating a TimedeltaIndex when a date is subtracted from another
dates - dates[0]

'Regualr sequences: pd.date_range()'
# pd.date_range() for timestamps
# pd.period_range() for periods
# pd.timedelta_range() for time deltas
# pd.date_range() accepts a start date and end date

pd.date_range('2015-07-03', '2015-07-10')

# using a start point and a number of periods instead of a start and end point
pd.date_range('2019-08-26', periods=10)

# using the freq argument which defaults to D can be altered to a an hourly timestamps
pd.date_range('2019-08-26', periods=14, freq='H')

# creating monthly periods 
pd.period_range('2019-08', periods=12, freq='M')

# creating a sequence of durations increasing by hour
pd.timedelta_range(0, periods=10, freq='H')

'Frequencies and Offsets'
# Pandas time series has code to designate desirred frequency and spacing
# such as W for weekly and H for hours which can be augmented
# with S at the end will have them marked as the beginning

# for a frequency of 2 hours and 3 minutes we can combine 
# hour with H and minutes with T
pd.timedelta_range(0, periods=9, freq='2H30T')

# creating a business day offset directly
from pandas.tseries.offsets import BDay
pd.date_range('2015-07-01', periods=5, freq=BDay())

'Resampling, shifting, and Windowing'
# Pandas DataFreader knows how to import financial dats from different sources

# loading Google's closing price history
from pandas_datareader import data
# attempting to use google , quandl, or iex as a data_source causes an error
yahoo =  data.DataReader('GOOGL', 'yahoo', start='2017', end='2019')
yahoo.head()

yahoo['Close']

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

yahoo.plot();

'Resampling and converting frequencies'
# one of the key uses of time series is resampling at a higher or lower frequency which can be implemented with the 
# resample() method and asfreq() method. resample() is for data aggregation and asfreq() is for data selection

# resampling the data at the end of the busines year
yahoo.plot(alpha=0.5, style='-')
yahoo.resample('BA').mean().plot(style=':')
yahoo.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'],
           loc='upper left');

# resampling the business day data at a daily frequency including weekends
fig, ax = plt.subplots(2, sharex=True)
data = yahoo.iloc[:10]

data.asfreq('D').plot(ax=ax[0], marker='o')

data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(['back-fill', 'forward-fill']);
# the top panel is the default, non-business days as marked as NA, and no shown on the plot
# the bottom shows different strategies for forward-filling and backward-filling the gap

'Time-shifts'
# a Series specific operation in Pandas is th shifting of data in time. This can performed with the shift() and tshift() 
# methods. shift() shifts the data while tshift() shifts the index

fig, ax = plt.subplots(3, sharey=True)

# apply a frequency to the data
yahoo1 = yahoo.asfreq('D', method='pad')

yahoo1.plot(ax=ax[0])
yahoo1.shift(900).plot(ax=ax[1])
yahoo1.tshift(900).plot(ax=ax[2])

# legends and annotations
local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900, 'D')

ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[2].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')

ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[2].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')

ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');

ROI = 100 * (yahoo1.tshift(-365) / yahoo1 - 1)
ROI.plot()
plt.ylabel('% Return on Investment');

'Rolling windows'
# rolling widow operations can be performed with the rolling() attribute of Series and DataFrames which returns 
# a view similar to GroupBy and allows for aggregations

# a one-year centered rolling mean and standard deviation
rolling = yahoo.rolling(365, center=True)

data = pd.DataFrame({'input': yahoo,
                     'one-year rolling_mean': rolling.mean(),
                     'one-year rolling_std': rolling.std()},
                     index=['a', 'b', 'c', 'd', 'e', 'f'])
# this is not working for me so I'll be back some day
# ax = data.plot(style=['-', '--', ':'])
#ax.lines[0].set_alpha(0.3)
data

'Example: Visulizing Seattle Bicycle Counts'

# read the CSV ouput into a DataFrame and specifiy the Date as an index with dates automaticalled parsed
data = pd.read_csv('data/FremontBridge.csv', index_col='Date', parse_dates=True)
data.head()

# processing the data by shortening the column names and adding a 'Total' column
data.columns = ['West', 'East']
data['Total'] = data.eval('West + East')

# take a look at the summary statistics for the data
data.dropna().describe()

'Visulize the data'

# gain insight from a visual representation by potting the raw data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn; seaborn.set()

data.plot()
plt.ylabel('Hourly Bicycle Count');

# reampling the data to a coarser grid by week because it is too dense
weekly = data.resample('W').sum()
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count');

# utilizing pd.rolling_mean() function we'll do a 30 day rolling mean of the data and center the window
daily = data.resample('D').sum()
# a hard cutoff of the window at 30
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count');

# smoothing the cutoff of the rolling mean using a Gaussian window
daily.rolling(50, center=True,
              win_type='gaussian').sum(std=10).plot(style=[':', '--', '-']);

'Digging into the data'
# while smothed over and a general trend may appear the more interesting structure is hidden

# looking at the average trafic as a function of the time of day using GroupBy
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-']);
# there is a strong bimodal distribution with peaks at 8 am and 5 pm which most is most likely in relation to commuter trafic

# figuring out how things changed based on the day of the week with groupby
by_weekday = data.groupby(data.index.dayofweek).mean()
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
by_weekday.plot(style=[':', '--', '-']);

# doing a compund GroupBy looking at the hourly trend on weekdays versus weekends.
# grouping by both a flag marking the weekend, and the time of day
weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()

# using MatPlotLib to plot two panels side by side
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(14,5))
by_time.loc['Weekday'].plot(ax=ax[0], title='Weekdays',
                          xticks=hourly_ticks, style=[':', '--', '-'])
by_time.loc['Weekend'].plot(ax=ax[1], title='Weekend',
                          xticks=hourly_ticks, style=[':', '--', '-']);
# there is a bimdal commute pattern during the work week 
# and a unimodal recreational patten during the weekends
