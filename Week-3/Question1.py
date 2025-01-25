## importing modules that are to be used
## 'print()' are used to make the output clearer to read
import math
import numpy as np

def sin(x):
    return math.sin(x)

def equation(x):
    return sin(x) + x**2 - 1

right_value = 0
left_value = 0

print()
print("Using Tabulation Method to find the closest guess to the interval on where the root exists.")   
for i in np.arange(0, 1, 0.1):
    print(f"This is the 'x':{i} and the sin(x) + x^2 - 1 is: {equation(i)}")
    if equation(i) > 0 and equation(i - 0.1) < 0:
        right_value += round(i, 2)
        left_value += round(i - 0.1, 2)	
        
# finding the roots via Tabulation method     
print()
print(f"This is the interval via Tabulation Method, rounded off: ({left_value}, {right_value})")
print()

## Defining Bisection method and tolerence 
tolerence = 10**-6 
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
            print(f"Shrinking the Actual left and right limits to: ({round(a, 10)}, {round(b, 10)})")
        else:
            a = c
            print(f"Shrinking the Actual left and right limits to: ({round(a, 10)}, {round(b, 10)})")

print("Now using Bisection Method.")
print("Proccessing . . .")
print()
print(f"\nRoot via Bisection Method, from ({left_value}, {right_value}): {round(Bisection(left_value, right_value, tolerence), 10)}")
