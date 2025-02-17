## importing important modules 
import numpy as np
def d2b(x):
    return np.binary_repr(x)

bins = []
def numpy_DecimalToBinary(x):
    y = list(x)
    for i in range(len(y)):
        bins.append(d2b(y[i]))

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"This is the array of all numbers: {arr}")
numpy_DecimalToBinary(arr)
print(f"This is the array of all binaries: {np.array(bins)}")
