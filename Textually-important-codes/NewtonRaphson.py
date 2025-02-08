## importing modules
import math
import numpy as np

def e(x):
    return math.exp(x)

def equation(x):
    return e(x) - 5

def diff_equation(x):
    return e(x)

interval = []
print("From Tabular")
for i in np.arange(1, 2.1, 0.1):
    print(f"This is the used i: {round(i, 2)}, and this is the value of it in the equation e^x - 5, {equation(i)}")
    if equation(i) < 0 and equation(i + 0.1) > 0:
        interval.append(round(i, 2))
        interval.append(round(i + 0.1, 2))
        
print(f"\nGiven interval is {interval}")

## creating the Newton-Raphson method
def NewtonRaphson(x, t):
    while abs(equation(x)) >= t:
        h = equation(x) / diff_equation(x)
        x -= h 
        print(f'x, f, df, h values: {x}, {equation(x)}, {diff_equation(x)}, {h}')
    print()
    print(f"Final value of the function is = {equation(x)}")
    print(f"which is approximately = {round(equation(x))}, under tolerance of {t}")
    return x

tolerance = 10**-10
print("From Newton Raphson")
print(f"for interval {interval[0]}", NewtonRaphson(interval[0], tolerance))

print()

print(f"for interval {interval[1]}", NewtonRaphson(interval[1], tolerance))
