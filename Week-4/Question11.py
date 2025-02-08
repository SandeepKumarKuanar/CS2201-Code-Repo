## importing important modules that would be used in the code 
import numpy as np 
a1 = np.array([1, 2, 3])
a2 = np.array([1, 2, 3])
a3 = np.array([2, 3, 4])

print(f"This are the arrays:\nArray1 is == {a1}\nArray2 is == {a2}\nArray3 is == {a3}")
# equal_pair1 = all(a == b for a, b in zip(a1.tolist(), a2.tolist()))
## tolist() converts array into list, zip compares in turples for the 2 lists entered
## all compares for the, but cannot by used

print(f"Is Array1 is same as Array2 == {a1 == a2}")
print(f"Is Array1 is same as Array3 == {a1 == a3}")
print(f"Is Array1 is same as Array2 using the built-in numpy functions == {np.array_equal(a1, a2)}")
print(f"Is Array1 is same as Array3 using the built-in numpy functions == {np.array_equal(a1, a3)}")
