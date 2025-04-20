def f(x):
    return 1 / x

def rectangular_rule(a, b, n): ## using recursion
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + (i * h)
        total += f(xi)
    return h * total

def trapezoidal_rule(a, b, n): ## using recursion
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        total += 2 * f(xi)
    return (h / 2) * total

def simpsons_rule(a, b, n): ## using recursion
    if n % 2 != 0:
        print("You have to enter even 'n' terms for simpsons to rules.")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0:
            total += 2 * f(xi)
        else:
            total += 4 * f(xi)
    return (h / 3) * total

# Example usage
a = 1
b = 2
n = 4  # You can increase n for better accuracy
import numpy as np
exact = np.log(2)

rectangular_result = rectangular_rule(a, b, n)
trapezoidal_result = trapezoidal_rule(a, b, n)
simpsons_result = simpsons_rule(a, b, n)

print(f"Rectangular Rule Approximation: {rectangular_result}")
print(f"Trapezoidal Rule Approximation: {trapezoidal_result}")
print(f"Simpson's Rule Approximation:   {simpsons_result}")

## for scipy approximation
import numpy as np
from scipy.integrate import trapezoid, simpson

# x values
x = np.linspace(1, 2, 100)
# y = f(x) = 1/x
y = 1 / x

# Trapezoidal Rule
trapz_result = trapezoid(y, x)

# Simpson's Rule
simpson_result = simpson(y, x)

# Exact value
exact = np.log(2)

print(f"Trapezoidal Result: {trapz_result}")
print(f"Simpson's Result:    {simpson_result}")
print(f"Exact Integral:      {exact}")
