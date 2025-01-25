#Defining Equation
def equation(x):
    return x**3 + x**2 - x

def diff_equation(x):
    return 3*x**2 + 2*x - 1


#Defining Newton Raphson method
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
print("Here we can take x = 0, but the thats a trival root of the given equation, we would take 1 as the starting point.")
print(f"\nRoot via Newton Raphson method rounded upto 10 places in decimal is = {round(NewtonRaphson(1), 10)}")
