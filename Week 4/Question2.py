#print("Hello, World!") ## the real test
## importing important modules 
import numpy as np
lines = input("Enter the number of lines/rows u want in this pattern:\n")
int_lines = int(lines) ## converts string formatted "Lines" to interger of python


for i in range(0, int_lines):
    results = []
    for j in np.arange(1, i + 1.5, 0.5):
        results.append(str(j))
    print(" ".join(results))
