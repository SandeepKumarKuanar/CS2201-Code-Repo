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

## creating a tabulation function for better modularatity of code 
def tabulation(a, b, c):
    ## using a doc-string to say what does the function do
    """Gives us the interval within which we would possibly find the roots. Takes 3 parameters, "a" as start range, "b" as end range, and "c" as steps."""
    interval = list() ## stores the interval
    ## using the numpy library's built-in function "arange(a, b, c)" that moves from a to b with increaments of "c", where c can be a float
    
    for i in np.arange(a, b + c, c):  # <-- for loop is from interval 1 to 2.1, as the arange() takes into consideration till "b - c"
        print(f"For the equation e**x - 5, at {round(i, 2)}, is {equation(i)}.")
        ## round(a, b) ==> round "a" to "b"th number of decimal place
        if equation(i) < 0 and equation(i + 0.1) > 0:
            interval.append(round(i, 2))
            interval.append(round(i + 0.1, 2))
    return interval[0], interval[1]
    
## calling the function
print("\nUsing Tabulation Method to find the intervals of roots.")
print("Generating. . .")
left_limit, right_limit = tabulation(1, 2, 0.1) ## storing the returned values into variables 
print() ## to make it look cleaner
print(f"Hence, the limit where the root exists is between [{left_limit}, {right_limit}] as we can observe from above.")
