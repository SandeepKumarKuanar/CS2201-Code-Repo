## importing important modules to used in the code 
import numpy as np
pre_A = np.array([i for i in range(1, 17)])
A = pre_A.reshape(4, 4)
pre_B = np.array([i * -1 for i in range(1, 17)])
B = pre_B.reshape(4, 4)

print(f"This is the 4 x 4 array named as 'A'\n{A}")
print(f"This is the 4 x 4 array named as 'B'\n{B}")

for i in range(len(A)):
    for j in range(len(A)):
        if i % 2 == 0 and j % 2 == 0:
            A[i, j] = B[i, j]
            
print(f"Now printing A, updated \n{A}")
