#print("Hello World!") ##the real test
x = [1, 2, 3, 4, 5]
#x = [5, 4, 3, 2, 1]
#x = [1, 2, 3, 2, 1]

if x == sorted(x):
    print("Monotonically increasing")
elif x == sorted(x, reverse=True):
    print("Monotonically decreasing")
else:
    print("Not monotonic")