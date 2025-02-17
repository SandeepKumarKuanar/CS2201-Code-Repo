## importing important modules 
import numpy as np

arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[3, 3], [1,1]])

print(f"This is the first array\n{arr1}")
print(f"This is the second array\n{arr2}")

print(f"This the use of np.multiply() function: \n{np.multiply(arr1, arr2)}")
print(f"This the use of np.matmul() function: \n{np.matmul(arr1, arr2)}")
