#importing important modules
import math
import numpy as np
pi = math.pi
def calc_area(r):
    area = []
    for i in r:
        area.append(i * pi * i)
    return area
    
radiuses = [i for i in range(1, 4)]
print(np.array(radiuses))
print(np.array(calc_area(radiuses)))

def array_calc_area(r):
    area = np.array([])
    for i in r:
        area = np.append(area, i * i * pi)
    return area
    
print(np.array(array_calc_area(radiuses)))
