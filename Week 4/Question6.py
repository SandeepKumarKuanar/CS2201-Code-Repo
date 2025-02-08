import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Array is\n", A)
for i in range(np.shape(A)[1]):
	print(f"The {i} column of {np.shape(A)} array is:", A[:, i])
