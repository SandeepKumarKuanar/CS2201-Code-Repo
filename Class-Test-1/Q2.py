## Importing necessary modules
import math
import numpy as np

# steps we take to create the pattern
steps = 10 

## printing the results
print(f"This below is the pattern due to {steps} number of steps.")
for i in range(1, 2):
    pattern = []
    for j in range(1, steps):
        if j % 2 == 0:
            pattern.append("*")
        else:
            pattern.append("#")
        print(" ".join(pattern))


