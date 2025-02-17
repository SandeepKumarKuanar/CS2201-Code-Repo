## importing important modules 
import numpy as np
def f(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return x % 3


L = [i for i in range(1, 11)]
ar = np.array(L)
arout = []
print(f"This is the array: {ar}")
for i in range(len(L)):
    arout.append(f(L[i]))
print(f"This is functioned array: {np.array(arout)}")
