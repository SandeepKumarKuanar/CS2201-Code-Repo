import numpy as np
N = 10
#circle
xs, h = np.linspace(0, 4, N, endpoint=False, retstep=True)
#print(xs)
#print(h)
ys = np.sqrt(16 - xs*xs)
#print(ys)
#Rectangular
Irect_c = h*np.sum(ys)
#ellipse
xs, h = np.linspace(0, 5, N, endpoint=False, retstep=True)
#print(xs)
#print(h)
ys = 6*np.sqrt(1 - xs*xs/25)
#print(ys)
#Rectangular
Irect_e = h*np.sum(ys)
print("Rectangular=%.5f" %(Irect_e-Irect_c))
#---------------------------------------
import scipy.integrate as spi
#Trapezoidal rule
#print("Actual=%f" %(1/11.))
#circle
xs, h = np.linspace(0, 4, N, endpoint=True, retstep=True)
ys = np.sqrt(16 - xs*xs)
#print(ys)
Itrap_c = h*(0.5*(ys[0] + ys[-1]) + np.sum(ys[1:-1]))
#print("Trapezoidal=%.5f" %(Itrap))
Itrap1_c = spi.trapezoid(ys, xs)
#ellipse
xs, h = np.linspace(0, 5, N, endpoint=True, retstep=True)
ys = 6*np.sqrt(1 - xs*xs/25)
#print(ys)
Itrap_e = h*(0.5*(ys[0] + ys[-1]) + np.sum(ys[1:-1]))
#print("Trapezoidal=%.5f" %(Itrap))
Itrap1_e = spi.trapezoid(ys, xs)
print("Trapezoidal ori=%f" %(Itrap_e - Itrap_c))
print("Trapezoidal scipy=%f" %(Itrap1_e - Itrap1_c))
# from scipy.integrate import simpson
#Simpson's rule
#circle
xs, h = np.linspace(0, 4, N+1, endpoint=True, retstep=True)
ys = np.sqrt(16 - xs*xs)
#print(ys)
#print(xs)
Isimp_c = (h/3.)*(ys[0] + ys[-1] + 4*np.sum(ys[1:-1:2]) + 2*np.sum(ys[2:-1:2]))
#print("Simp=%.5f" %(Isimp))
#import math
Isimp1_c = spi.simpson(ys, xs)
#ellipse
xs, h = np.linspace(0, 5, N+1, endpoint=True, retstep=True)
ys = 6*np.sqrt(1 - xs*xs/25)
#print(ys)
#print(xs)
Isimp_e = (h/3.)*(ys[0] + ys[-1] + 4*np.sum(ys[1:-1:2]) + 2*np.sum(ys[2:-1:2]))
#print("Simp=%.5f" %(Isimp))
Isimp1_e = spi.simpson(ys, xs)
#import math
print("Simpson ori=%f" %(Isimp_e - Isimp_c))
print("Simpson scipy=%f" %(Isimp1_e - Isimp1_c))
import math
actual = (math.pi*6*5 - math.pi*4*4)*0.25
print("Actual=%f" %(actual))