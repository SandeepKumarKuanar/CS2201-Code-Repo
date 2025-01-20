#print("Hello, World!") ## this is real test
L1 = [1, 2, 3, 4, 5] 
L2 = [5, 4, 10, 12]
L3 = [number1 + number2 for number1 in L1 for number2 in L2 if number1 % 2 != 0 and number2 % 2 != 0]
print(L3)
