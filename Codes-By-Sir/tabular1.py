def f(x):
    return 10**x + x - 4



import numpy as np

def tabular(low, hi, accuracy):
    x = []
    y = []
    step = hi - low
    while step != accuracy:
        step = step/10.0
        i1 = low
        i2 = hi

        l = i1
        r = i2

        f1=f(l)
        l1 = l

        

        l+=step

        for n in np.arange(l, r+step, step):
            f2=f(n)
            print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2))
            x.append(l1)
            y.append(n) 
            if f1*f2 < 0.0:
                print("Found in: " + str(l1)+ " " + str(n))
                
                break
            
              

            l1 = n
            f1 = f(l1)
            
    return l1, n, x, y


l, r, x, y = tabular(0, 1, 0.1)

print("The final interval: (%f, %f)" %(l, r))