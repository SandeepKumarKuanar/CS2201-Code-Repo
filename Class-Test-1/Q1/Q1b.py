## Importing necessary modules
import math
import numpy as np

## creating a mathematically similar looking function, to make it more digestable
def e(x):
    return math.exp(x)
    
#print(e(1))  # <-- checking if the above function is working or not

## the equation provided to me goes in here
def equation(x):
    return e(x) - 5
    
## creating the differentiated equation 
def diff_equation(x):
    return e(x)
    
def tabulation(a, b, c):
    ## using a doc-string to say what does the function do
    """Gives us the interval within which we would possibly find the roots. Takes 3 parameters, "a" as start range, "b" as end range, and "c" as steps."""
    interval = list()
    for i in np.arange(a, b + c, c):  # <-- for loop is from interval 1 to 2.1, as the arange() takes into consideration till "b - c", so we take from "a" to "b + c"
        print(f"For the equation e**x - 5, at {round(i, 2)}, is {equation(i)}.")
        if equation(i) < 0 and equation(i + 0.1) > 0:
            interval.append(round(i, 2))
            interval.append(round(i + 0.1, 2))
    return interval[0], interval[1]
    
## calling the function, and extracting the desired interval
print("\nUsing Tabulation Method to find the intervals of roots.")
print("Generating. . .")
left_limit, right_limit = tabulation(1, 2, 0.1) ## storing the returned values into variables 
print()

## creating the Newton-Raphson method
def NewtonRaphson(x, t):
    ## using a doc-string to say what does the function do
    """ This is the NewtonRaphson Method, which takes "x" as 1 part of the guessed interval from the Tabulation method, takes "t" as the accuracy. """
    while abs(equation(x)) >= t: ## to set the tolerance value
        ## Mathematical implementation of the Newton-Raphson Method
        h = equation(x) / diff_equation(x)
        x -= h 
        print(f'x, f, df, h values: {x}, {equation(x)}, {diff_equation(x)}, {h}')
    print()
    print(f"Final value of the function is = {equation(x)}")
    print(f"which is approximately = {round(equation(x))}, under tolerance of {t}")
    return x

accuracy = 10**-8  ## desired accurary of the code being found 
## calling the Newton-Raphson method on the left handed limit
print(f"Now, using Newton-Raphson's Method to find the roots from the limit handed limit of {left_limit}")
print("Generating. . .")
print("This is the better approximation of the root to accuracy of", accuracy, "which is", NewtonRaphson(left_limit, accuracy))
## calling the Newton-Raphson method on the right handed limit
print(f"\nNow, using Newton-Raphson's Method to find the roots from the limit handed limit of {right_limit}")
print("Generating. . .")
print("This is the better approximation of the root to accuracy of", accuracy, "which is", NewtonRaphson(right_limit, accuracy))
























