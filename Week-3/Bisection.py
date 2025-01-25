## imporing important modules
## using print() to clean out the output
import math

def sin(x):
    return math.sin(x)

def equation(x):
    return sin(x) + x**2 - 1    

tolerence = 10**-5 #defining the tolerance to find the values within this range

## definding and using Bisection method to find the roots
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
    
print(f"Root via Bisection Method, as the mid-point of those 2 limits and round upto 10th decimal place is: {round(Bisection(0, 1, tolerence), 10)}")
