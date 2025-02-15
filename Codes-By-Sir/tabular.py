import math

def f(x):
    #return (1/x)*math.sin(x)
    #return x*math.cos(x)
    return 10**x + x - 4
    #return math.sin(x) + x*x  - 1


import numpy as np

#f = lambda x: 10**x + x - 4

i1 = 0.0 #left interval point
i2 = 1.0 #right interval point

l = i1
r = i2

f1=f(l) #value at 0.0
l1 = l #0.0

step = 0.1

l+=step #0.1

for n in np.arange(l, r+step, step):
    f2=f(n)
    print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
    if f1*f2 < 0.0:
        print("Desired interval :" + str(l1)+ " " + str(n))
        
        break

       

    l1 = n
    f1 = f(l1)    

    #print(n)