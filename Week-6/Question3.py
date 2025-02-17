import numpy as np
# x + 2y + 3z = 2, 4x + 8y +66z = 3 and 7x + 81y + 9z = 4.

cofficient_array = np.array([[1, 2, 3], [4, 8, 66], [7, 81, 9]])
constant_array = np.array([2, 3, 4])

tolerance = 10 ** -6
if abs(np.linalg.det(cofficient_array)) > abs(tolerance):
    answer = np.linalg.solve(cofficient_array, constant_array)
    print(f"This is the point of intersection {answer}")
    
else:
    print(f"Determinate of above Cofficient matrix is zero! {np.linalg.det(cofficient_array)} which is nearly equal to zero")
