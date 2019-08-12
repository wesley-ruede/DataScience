L = np.random.random(100) #array can be added
sum(L) 
np.sum(L) #ufunc the same as built-in sum() function

big_array = np.random.rand(100000)
%timeit sum(big_array) # 18.2 ms ± 22.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each
%timeit np.sum(bigarray) # 77.7 µs ± 400 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each
# np.sum can handle multi-dimensional arrays

'Minumum and Maximum'

min(big_array), max(big_array) 
np.min(big_array), np.max(big_array) # much quicker than built-in min/max
M = np.random.random((3,4))
M.sum()
print(M)

M.sum() # adds all values in the array
M.min(axis=0) #returns lowest value per column 
M.max(axis=1) #returns highest value per row

'Other Aggregation Functions'
# NaN functions can handle missing data

'Examples: What is the average height of US Presidents?'

!head -4 data/president_heights.csv # 5 is the range that is being iterated over

import pandas as pd
data = pd.read_csv('data/president_heights.csv')#pandas open
heights = np.array(data['height(cm)']) #store pandas data in a numpy array
print(heights)

print("Mean height:        ", heights.mean()) #using aggregation funcs
print("Standard deviation: ", heights.std())
print("Minumum height:     ", heights.min()) 
print("Maximum height:     ", heights.max())

print("25th percentile: ", np.percentile(heights, 25)) #quntile functions
print("Median:          ", np.median(heights))
print("75th percentile: ", np.percentile(heights, 75))

%matplotlib inline #only useful in jupyter

import matplotlib.pyplot as plt
import seaborn; seaborn.set() #set plot type

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)') #define labels 
plt.ylabel('numbers')
