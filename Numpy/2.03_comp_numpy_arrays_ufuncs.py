# Computation on NumPy Arrays: Universal Functions

# THe slowness of loops
import numpy as np
np.random.seed(0)

# array of values and we'd like to compute the reciprocal of each
def compute_reciprocals(values): 
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
        
values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)

big_array = np.random.randint(1, 100, size=1000000) 
#%timeit compute_reciprocals(big_array) #benchmark

# Introducing UFUncs

print(compute_reciprocals(values))
print(1.0 / values)
#%timeit (1.0 / big_array) #vectorized operations via ufuncs
#scalar and array operation

x = np.arange(9).reshape((3, 3)) 
2 ** x #multi-dimensional ufunc operation

''' loops should be replaced with vectorized operations '''

# Exploring NumpPy's UFuncs

# Array arithmetic

x = np.arange(4)
print('x  =', x) 
print('x + 5 =', x + 5) #add 5 to all values in array
print('x - 5 =', x - 5)
print('x * 2 =', x * 2)
print('x / 2 =', x / 2)
print('x // 2 =', x // 2) #floor division
print('-x = ', -x) #unary ufunc for negation 
print('x ** 2 = ', x ** 2) #exponentation
print('x % 2 = ', x % 2) #modulus
print(-(0.5*x + 1) ** 2) # Numpy wrapper that allows all operations to be strug together

# Absolute Value

x = np.array([-2, -1, 0, 1, 2])
abs(x) #standard abs works with np arrays
np.absolute(x) #numpy unfunc for abs()
np.abs(x) #alias of ufunc 
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j]) #complex data
np.abs(x)


# Trionmetric functions

theta = np.linspace(0, np.pi, 3) #array of angels
print('theta      = ', theta)
print('sin(theta) = ', np.sin(theta)) #sine of theta
print('cos(theta) = ', np.cos(theta)) #cosine of theta
print('tan(theta) = ', np.tan(theta)) #tangent of theta

x = [-1, 0, 1]
print('x         = ', x)
print('arcsin(x) = ', np.arcsin(x)) #inverse trigonometric
print('arccos(x) = ', np.arccos(x)) 
print('arctan(x) = ', np.arctan(x))

# Exponents and logarithms

x = [1, 2, 3]
print('x         = ', x)
print('e^x       = ', np.exp(x)) #exponentation
print('2^x       = ', np.exp2(x)) 
print('3^x       = ', np.power(3,x))

x = [1, 2, 4, 10]
print('x         = ', x)
print('ln(x)     = ', np.log(x)) #logarithms
print('log2(x)   = ', np.log2(x)) 
print('log10(x)  = ', np.log10(x))

print('exp(x) - 1 = ', np.expm1(x)) #very precise exp for small numbers
print('log(1 + x) = ', np.log1p(x)) #very precise log for small numbers

# Specalized ufuncs

from scipy import special #special ufuncs

x = [1, 5, 10]
# Gamma function (general factorials) and related functions
print('gamma(x)     = ', special.gamma(x))
print('ln|gamma(x)| = ', special.gammaln(x))
print('beta(x, 2)   = ', special.beta(x, 2))

# Error function (integral of Gaussian)
# its complement, and its inverse
x = np.array([0, 0.3, 0.7, 1.0])
print('erf(x)    = ', special.erf(x))
print('erfc(x)   = ', special.erfc(x))
print('erfinv(x) = ', special.erfinv(x))

# Advanced Ufunc Features

# Specifying Output

x = np.arange(5)
y = np.empty(5) #empty array the same size as original 
np.multiply(x, 10, out=y) #output location is designated to y
print(y)

y = np.zeros(10)
np.power(2, x, out=y[::2]) #every other location in array
print(y)

# Aggregates

x = np.arange(1,6)
np.add.reduce(x) #binary ufunc that adds all elements in the array
np.multiply.reduce(x) # product of all elements in array
np.add.accumulate(x)  # store intermediate results of addition
np.multiply.accumulate(x) # store intermediate results of multiplication

# Outer products

x = np.arange(1,6)
np.multiply.outer(x, x) # compute the output of all pairs of two different inputs
