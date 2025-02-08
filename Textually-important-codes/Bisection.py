## importing modules
import math
import numpy as np

def e(x):
    return math.exp(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def equation(x):
    return e(x) * (3.2 * sin(x) - 0.5 * cos(x))

def diff_equation(x):
    return e(x)

interval = []
print("From Tabular")
for i in np.arange(3, 4.1, 0.1):
    print(f"This is the used i: {round(i, 2)}, and this is the value of it in the equation e^x - 5, {equation(i)}")
    if equation(i) > 0 and equation(i + 0.1) < 0:
        interval.append(round(i, 2))
        interval.append(round(i + 0.1, 2))
        
print(f"\nGiven interval is {interval}")

## Bisection function
def Bisection(a, b, error):
    print(f"The actual left and right limits are: ({a}, {b})")
    while abs(b - a) > error:
        c = (a + b) / 2
        # if the value in hand is the actual root or not
        if abs(equation(c)) < error:
            return c

        #change the interval
        if equation(c) * equation(a) < 0:
            b = c
            print(f"Shrinking the Actual left and right limits to: ({a}, {b})")
        else:
            a = c
            print(f"Shrinking the Actual left and right limits to: ({a}, {b})")
            
            
print("For Bisection. . .\n")
error = 10**-10
Bisection(interval[0], interval[1], error)
