## importing important modules 
import numpy as np
x = np.linspace(20, 21, num=10, endpoint=True)

print(f"In numpy generated 10 equispaced points in the interval [20, 21] where endpoint 21 is included \n{x}")

y = x = np.linspace(20, 21, num=10, endpoint=False)
print(f"In numpy generated 10 equispaced points in the interval [20, 21] where endpoint 21 is not included \n{y}")

z = np.shape(x)[0]
print(f"Interval lengths of the first answer = {z}")
