## importing important modules 
import numpy as np

A = np.array([i for i in range(1, 11)])
B = np.array([i for i in range(5, 16)])

print(f"This is the first matrix I took \n{A}")
print(f"This is the second matrix I took \n{B}")

list_A = list(A)
list_B = list(B)
results = set(list_A + list_B)
c = np.array(list(results))

print(f"This the set of things that only in A or only in B {c}")
