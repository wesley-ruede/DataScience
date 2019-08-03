import numpy as np

np.random.seed(0) #seed for reproducibility 

x1 = np.random.randint(10, size=6) #one-dimensional array
x2 = np.random.randint(10, size=(3,4)) # two-dimensional array
x3 = np.random.randint(10, size=(3,4,5)) #three-dimensional array

# NumPy array attributes
print("x3 ndim ", x3.ndim) #ndim = number of dimensions  
print("x3 shape: ", x3.shape) #shape = size of each dimension
print("x3 size: ", x3.size) #size = total size of the array

print("x3 dtype: ", x3.dtype) #dtype = data type of the array

print("x3 itemsize: ", x3.itemsize, "bytes") #itemsize = lists the size in bytes of each array element
print("x3 nbytes:", x3.nbytes, "bytes") #nbytes = lists total size in bytes of the array

# Array indexing: Accessing single elements 
print(x1)
print(x1[0])
print(x1[4])
print(x1[-1]) #index from the end of the array
print(x1[-2])

print(x2) # multi-dimensional array
print(x2[0,0]) #access items using comma seperated tple of indicies
print(x2[2,0])
print(x2[2,-1])

x2[0,0] = 12  # modifying values using comma sperated index notation
print(x2)
x1[0] = 3.14159 # to be truncated as numpy arrays have a data type
print(x1)

# Array Slicing: Accessing Subarrays
x = np.arange(10) # One-dimensional subarrays
print(x)
print(x[:5]) # first five elements
print(x[5:]) # elements after index 5
print(x[4:7]) # middle sub-array
print(x[::2]) # every other element 
print(x[1::2]) # every other element, starting at index 1
print(x[::-1]) # all elements, reversed
print(x[5::-2]) # reversed ever other from index 5

# Multi-dimensional subarrays
print(x2)
print(x2[:3, ::2]) # two rows, three columns
print(x2[:3, ::2]) # all rows, every other column
print(x2[::-1, ::-1]) # subarray dimensions reversed together

# Accessing array rows and columns
print(x2[:, 0]) # first colum of x2
print(x2[0, :]) #first row of x2
print(x2[0]) # eqivalent to x2[0, :]

# Subarrays as no-copy views
print(x2)
x2_sub = x2[:2, :2] # extract 2X2 subarray of x2
print(x2_sub)
x2_sub[0,0] = 99 # modify extracted 2X2 of x2
print(x2_sub)
print(x2) # extracted 2X2 changes orignal x2

# Creating copies of arrays
x2_sub_copy = x2[:2, :2].copy() # explicitly copy the data within an array with copy() method
print(x2_sub_copy)
x2_sub_copy[0, 0] = 42 #modifying the subarray will not touch original subarray
print(x2_sub_copy)
print(x2)

# Reshaping of arrays 
grid = np.arange(1, 10).reshape((3,3)) # places numbers 1-10 in a 3X3 grid
print(grid)

x = np.array([1,2,3])
x.reshape((1,3)) # row vector via reshape
x[np.newaxis, :] # row vecotr via newaxis
x.reshape((3,1)) #column vector via reshape
x[:, np.newaxis] #column vector via reshape

# Array concatenation and splitting

# Concatenation of arrays
x = np.array([1,2,3])
y = np.array([3,2,1])
print(np.concatenate([x,y])) # takes a tuple or list of arrays as its first argument
z = [99,99,99]
print(np.concatenate([x,y,z])) #concatenate more than two arrays
grid = np.array([[1,2,3], #concatenate two-dimensional arrays
[4,5,6]])
np.concatenate([grid, grid]) #concatenate along the first axis
np.concatenate([grid, grid], axis=1) # concatenate along the second axis (zero-indexed)

x = np.array([1,2,3]) #working with arrays of mixed dimensions
grid = np.array([[9,8,7],
                 [6,5,4]])

print(np.vstack([x, grid])) #vertically stack the arrays

y = np.array([[99], #horizontally stack the array
              [99]])
np.hstack([grid, y])

# Splitting of arrays
x = [1,2,3,99,99,3,2,1]
x1, x2, x3 = np.split(x, [3,5]) #split indicies at given location with .split()
print(x1, x2, x3)
grid = np.arange(16).reshape((4,4,))
grid
upper, lower = np.vsplit(grid, [2]) #vertical split
print(upper)
print(lower)
left, right = np.hsplit(grid, [2]) #horizontal split
print(left)
print(right)
