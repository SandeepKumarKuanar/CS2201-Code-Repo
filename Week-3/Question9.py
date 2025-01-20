#print("Hello, World!") ## this is real test
#x = [1, 3, 2]
#y = [1, 3, 2]
x = [3, 2, 4]
y = [3, 2, 4]
y.sort()
if x == y:
    print("This is increasing monotone.")
elif x != y:
    for i in range(len(x)):
        if i == 0:
            continue
        else:
            if x[i] > x[i - 1] and x[i] < x[i + 1]:
                print("It's not an monotone")
                break
    print("It's an decreasing monotone")
