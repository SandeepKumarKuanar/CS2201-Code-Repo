import random
x = []
y = []
for i in range(1, 1000):
    x.append(i)
    r = random.uniform(0, 6)
    if r < 1:
        print("One")
        y.append(1)
    elif r < 2:
        print("Two")
        y.append(2)
    elif r < 3:
        print("Three")
        y.append(3)
    elif r < 4:
        print("Four")
        y.append(4)
    elif r < 5:
        print("Five")
        y.append(5)
    else:
        print("Six")
        y.append(6)
        break
print(x)
print(y)
## mapping
import matplotlib.pyplot as plt
plt.xkcd()
plt.text(x[0], y[0]-0.5, "start") #prints "start" at coordinates (x[0], y[0]-0.5)
plt.text(x[-1], y[-1]-0.5, "six") #print "six" at the last throw
plt.plot(x, y, 'o:r') # using marker string 
plt.xlabel("throws")
plt.ylabel("number on dice")
plt.tight_layout()
plt.show()
