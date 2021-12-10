import numpy as np
import random

arr = np.random.rand(7,5)
print("Arr: ",arr)
print("Maximum value from array: ",arr.max())
print("Minimum value from array: ",arr.min())
row = arr[2:3]
print("Printing 2nd row: ",row)

x = np.array([2,2,2,2,2,2,2])
arr[:,3] = x
print("Setting all the values of column4 to 2: ")
print(arr)

print("Shape of array:",arr.shape)
print("Size of array: ",arr.size)

print("Reshaping array with 5 rows and 7 columns: ")
print(arr.reshape(5,7))

row2 = arr[2,3]
print("Mean: ",np.mean(row2))
print("Mode: ",np.unique(row2))
print("Standard Deviation: ",np.std(row2))