import numpy as np
import math

def f(x):
    return 10**x + x - 4
    #return math.exp(x) - 5
    #return x*x -5*x + 6

def df(x):
    return math.log(10)*10**x + 1
    #return 2*x - 5
    #return math.exp(x)

def df_num(x):
    h = 0.0001
    return (f(x+h) - f(x))/h

def tabular(low, hi, step):
 i1 = low
 i2 = hi

 l = i1
 r = i2

 f1=f(l)
 l1 = l
	
 l += step
 
 print("%f %f %f" %(low, hi, step))

 for n in np.arange(l, r+step, step):
  f2=f(n)
  print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
  if f1*f2 < 0.0:
   print(str(l1)+ " " + str(n))
   break
   

  l1 = n
  f1 = f(l1)

 return l1, n


    

def newtonRaphson(x):
    h = f(x)/df(x)
    #h = f(x)/df_num(x)
    
    

    
    
    while abs(f(x)) >= 0.00001:

        h = f(x)/df(x)
        #h = f(x)/df_num(x)
        x = x - h
        
       

        print('x, f, df, h values: %f %f %f %f' %(x, f(x), df(x), h))

       
    print("Final f-value %f" %(f(x)))
    
    return x


l, r = tabular(0, 1, 0.1)
print("The root is ", "%.4f"%newtonRaphson(r))
#print("The root is ", "%.4f"%newtonRaphson(0.6))
