## importing important modules to used in the code 
import numpy as np

wants = []
for i in range(1, 10):
    number = input(f"Give me your {i}th number, in alphanumeric form:\n").lower().strip()
    wants.append(int(number))	
    
print(f"This is the list of numbers that u have given me as an input: {wants}")
pre_results = np.array(wants, dtype="float64")

print(f"\nThis are the last 3 elements from the array, {pre_results[len(pre_results) - 3:len(pre_results):]}")
print(f"\nThis are the first 3 elements from the array, {pre_results[:3:]}")

length = len(pre_results)
middle = length // 2
print(f"\nThis are the 3 elements from the middle of the array, {pre_results[middle - 1: middle + 2:]}")
print(f"\nThis are the last 3 elements from the array, {pre_results[-2:-5:-1][::-1]}")
to_be_zeroed = np.copy(pre_results)
for i in range(len(to_be_zeroed)):
    if i % 2 != 0:
        to_be_zeroed[i] = 0
        
print(f"\nThis are the array with every second element starting from index 1 of the array with 0,, {to_be_zeroed}")
