## importing important modules to used in the code 
import numpy as np

wants = []
for i in range(1, 10):
    number = input(f"Give me your {i}th number, in alphanumeric form:\n").lower().strip()
    wants.append(int(number))
    
print(f"This is the list of numbers that u have given me as an input: {wants}")
pre_results = np.array(wants, dtype="float64")
print(f"This is the same list in the form of an numpy array: {pre_results}")
print(f"This is the array, but in reverse form: {np.array(wants[::-1], dtype='float64')}")
print(f"This is the array in reverse form, but using another method: {pre_results[::-1]}")
