## importing important modules to used in the code 
import numpy as np
wants = np.array([i for i in range(1, 17)])
matrix = wants.reshape(4, 4)
print(f"This is the 4 x 4 array\n{matrix}")
print(f"This is the last 2 columns\n{matrix[:,len(matrix) - 2:len(matrix)]}")
print(f"This is the first 2 rows\n{matrix[:2,:]}")
print(f"This is the maximum value in the matrix: {np.max(matrix)}")

need = np.copy(matrix)
need[1:3, 1:3] = np.max(matrix)
print(need)
