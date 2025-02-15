## importing modules
import math
import numpy as np

def e(x):
    return math.exp(x)

def equation(x):
    return e(x) - 5

interval = []
print()
for i in np.arange(1, 2.1, 0.1):
    print(f"This is the used i: {round(i, 2)}, and this is the value of it in the equation e^x - 5, {equation(i)}")
    if equation(i) < 0 and equation(i + 0.1) > 0:
        interval.append(round(i, 2))
        interval.append(round(i + 0.1, 2))
        
print(f"\nGiven interval is {interval}")
