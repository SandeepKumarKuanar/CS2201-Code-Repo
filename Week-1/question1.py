#print("Hello, World!") ## the proper test
x = list(i for i in range(0, 10)) # well till 10, as the range would stop on 9.
y = list(i for i in range(3, 13))
x_reveresed = x[::-1]
print(list(x[i] for i in range(len(x)) if i%2 != 0), list((i) for i in range(len(x)) if i%2 == 0))
print(list(x[i] for i in range(len(x)) if i%2 != 0), list((i) for i in range(len(x)) if i%2 != 0))

from_x = x[3] # extracting them up
from_y = y[0]
print("Is the 4th item of x (0th index element is the 1st element) is same as the 1st item of y:")
print( from_x is from_y)

try:
    print("The location of 10 in X is:", x.index(10))
except:
    print("10 is not in the list X")

try:
    print("The location of 7 in Y is:", y.index(7))
except:
    print("7 is not in the list Y")

appended_x_and_y = x + y
print(appended_x_and_y)
print("The location of the maximum number in combined list of x and y:", appended_x_and_y.index(max(appended_x_and_y)))
print("The location of the minimum number in combined list of x and y:", appended_x_and_y.index(min(appended_x_and_y)))




