## importing important modules 
import numpy as np
def f(x):
    return x ** 3 + 1
    
L = [i for i in range(1, 11)]
Lout = []
for i in range(len(L)):
    Lout.append(f(L[i]))

print(f"This is the list: {L}")
print(f"This is the functioned list: {Lout}")
ar = np.array(L)
arout = f(ar)
print(f"This is the array: {ar}")
print(f"This is the functioned array: {arout}")
