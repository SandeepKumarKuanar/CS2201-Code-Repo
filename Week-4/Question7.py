#importing important modules
import math
pi = math.pi
def calc_area(r):
    area = []
    for i in r:
        area.append(i * pi * i)
    return area
    
radiuses = [i for i in range(1, 4)]
print(radiuses)
print(calc_area(radiuses))
