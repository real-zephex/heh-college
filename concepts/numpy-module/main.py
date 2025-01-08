# NumPy - A powerful library for numerical computing in Python
# Key features: multi-dimensional arrays, mathematical operations, and scientific computing tools

import numpy as np

# Creating a 2D array - Basic building block of NumPy
arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2 dimensional array
print(arr)

# Printing the dimensions of the array
print("The dimensions of the array is: ",arr.ndim)

# Printint the shape of the array
print("The shape of the array is: ",arr.shape)

# Matrix Creation Operations
# Identity matrix - diagonal elements are 1, rest are 0
print("\nIdentity matrix")
identity = np.identity(3)
print(identity)

# Creating a zero matrix
print("\nZero matrix")
zeroes = np.zeros(3)
print(zeroes)

# Creating a matrix with only ones
print("\nOnes matrix")
ones = np.ones((3, 3))
print(ones)

# Creating a matrix with random element
print("\nMatrix with random elements")
random = np.random.rand(3, 3)
print(random)

# Matrix Arithmetic Operations
# Demonstrates how NumPy can perform element-wise operations efficiently
print("\nAddition of matrices")
addition = ones + random
print(addition)

print("\nSubtraction of matrices")
subtraction = random - identity
print(subtraction)

print("\nMultiplication of matrices")
multiplicaiton = random * addition
print(multiplicaiton)

print("\nDivison of matrices")
division = random / multiplicaiton
print(division)

# Array Statistics
# NumPy provides efficient functions for array computations
add = np.sum(division)
print("Sum of the divisoion matrix is: ", add)

print("\nSquare root of the multiplication matrix")
square_root = np.sqrt(multiplicaiton)
print(square_root)

# Printing the type of elements of an array
print()
print(np.dtype(add))  # the number at the end of the type indicates the memory it is consuming.
print(type(add))


# Array Manipulation
# Demonstrating various ways to access and modify array elements
print("\nIndexing and slicing")

print(arr[0])
print(arr[0][1] + arr[1][1]) # you can also access the elements as [0, 1] and [1, 1]

print(arr[0][0: 2])
print(arr[0][0 : 2] + arr[1][0 : 2])

# Type Conversion
# NumPy supports various data types and easy conversion between them
print("\nDatatypes and conversion")
# converting an integer array to string
strignfied_array = arr.astype('S')
print(strignfied_array)

new_arr = np.array([1.2, 3.43, 43.4], dtype="i") 
"""
i : integer
It will truncate the decimal part.

i4 - 4 bytes integer
i8 - 8 bytes integer
and so on...

S : string
Well, it will convert the elements into string
"""

print(new_arr)

boolified_array = new_arr.astype(bool) # all non zero elements are True and 0 elements are False
print(boolified_array)

# Memory Management
# Understanding how NumPy handles data in memory
print("\nCopy and View")
print("Demonstrating copy")
copied = arr.copy()
copied[0][1] = 100

print(copied)
print(arr)

print("Demonstrating view")
viewed = arr.view()
viewed[0][2] = 9
print(viewed)
print(arr)

# Array Reshaping
# Changing array dimensions while preserving data
one_d = np.array(range(8))
print(one_d.reshape(2, 4))

# Array Joining
# Combining multiple arrays into one
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
joined_arr = np.concatenate((arr1, arr2))

print(joined_arr)

# Linespcaes : used to create a sequence of evenly spaced numbers over a specified range.

"""
Syntax:
  np.linespace(start, stop, quantity)

Example:
  np.linespace(1, 10, 5)
  It will generate 5 evenly spaced numbers between 1 to 10
"""

evenly_spaced = np.linspace(0, 10, 5)
print(evenly_spaced)