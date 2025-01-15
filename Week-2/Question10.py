## imporing important modules
import math
import numpy as np

def sin(x):
    return math.sin(x)

def equation(x):
    return sin(x) + x**2 - 1

for i in np.arange(0, 1, 0.1):
    print(f"This is the 'x':{i} and the sin(x) + x^2 - 1 is: {equation(i)}")
    if equation(i) > 0 and equation(i - 0.1) < 0:
        print(f"This is the interval, which we been looking for: ({i - 0.1}, {i})")
        print(f"This is the interval, rounded off: ({round(i - 0.1, 2)}, {round(i, 2)})")
        break