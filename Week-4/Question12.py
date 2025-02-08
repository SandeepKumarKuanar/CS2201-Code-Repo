## importing important modules that would be used in the code 
import numpy as np 
given = [[1, 2, 3, 4, 11], 
        [100, 55, 80, 33, 22] 
]
given_array = np.array(given, dtype="float64")
print(given_array)

## applying slicing method
need = given_array[:,3:]
print(need) ## where the first position is for the "needed row", and the second position for the "needed column"