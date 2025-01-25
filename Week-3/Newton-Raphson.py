## imporing important modules
## using print() to clean out the output
import math
import numpy as np

def sin(x):
    return math.sin(x)

def equation(x):
    return sin(x) + x**2 - 1

def cos(x):
    return math.cos(x)

def diff_equation(x):
    return cos(x) + 2 * x 
    

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
print(f"This is the interval, rounded off: ({left_value}, {right_value})")
print()
#defining Newton Raphson method
def NewtonRaphson(x):
    """ This is the NewtonRaphson Method, which takes 1 part of the guessed interval from the Tabulation method. """
    while abs(equation(x)) >= 10**-5: ## to set the tolerance value
        h = equation(x) / diff_equation(x)
        x -= h 
        print(f'x, f, df, h values: {x}, {equation(x)}, {diff_equation(x)}, {h}')
    print()
    print(f"Final value of the function is = {equation(x)}")
    print(f"which is approximately = {round(equation(x))}, under tolerance of 0.00001")
    return x

print("Now using Newton Raphson Method.")
print("Proccessing . . .")
print(f"Root via Newton Raphson method rounded upto 10 places in decimal is = {round(NewtonRaphson(right_value), 10)}")
