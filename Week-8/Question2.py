import numpy as np
N = 10
xs, h = np.linspace(0, 5, N, endpoint=False, retstep=True)
ys = np.sqrt(25 - xs*xs)
print(ys)

#Rectangular
Irect = h*np.sum(ys)
print("Rectangular=%.5f" %(Irect))
import scipy.integrate as spi

#Trapezoidal rule
xs, h = np.linspace(0, 5, N, endpoint=True, retstep=True)
ys = np.sqrt(25 - xs*xs)
Itrap = h*(0.5*(ys[0] + ys[-1]) + np.sum(ys[1:-1]))
print("Trapezoidal=%.5f" %(Itrap))
Itrap1 = spi.trapezoid(ys, xs)
print("Trapezoidal " %(Itrap1))
#from scipy.integrate import simps
#Simpson's rule
xs, h = np.linspace(0, 5, N+1, endpoint=True, retstep=True)
ys = np.sqrt(25 - xs*xs)
print(ys)
print(xs)
Isimp = (h/3.)*(ys[0] + ys[-1] + 4*np.sum(ys[1:-1:2]) +
2*np.sum(ys[2:-1:2]))
print("Simp=%.5f" %(Isimp))
import math
actual = math.pi*5*5*0.25
print("Actual=%f" %(actual))
Isimp1 = spi.simpson(ys, xs)
print("Simp scipy = %f" %(Isimp1))
print("Error rect = %.5f" %((abs(Irect-actual)/actual)*100))
print("Error trap original = %.5f" %((abs(Itrap-actual)/actual)*100))
print("Error trap scipy = %.5f" %((abs(Itrap1-actual)/100)*100))
print("Error simp original = %.5f" %((abs(Isimp-actual)/actual)*100))
print("Error trap scipy = %.5f" %((abs(Isimp1-actual)/actual)*100))