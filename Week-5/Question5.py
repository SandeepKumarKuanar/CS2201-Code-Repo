## importing important modules to used in the code 
import numpy as np

pre_A = np.array([i for i in range(1, 17)])
A = pre_A.reshape(4, 4)
print(f"This is the 4 x 4 array named as 'A':\n{A}")
B = np.zeros((4, 2, 2))

for i in range(len(A)):
    if i % 2 == 0:
        try: 
            x = A[:i, :i]
            B[0] = x
        except:
            continue
            
for i in range(len(A)):
    if i % 2 == 0:
        try: 
            x = A[i:, i:]
            B[3] = x
        except:
            continue
            
for i in range(len(A)):
    if i % 2 == 0:
        try: 
            x = A[:i, i:]
            B[1] = x
        except:
            continue
            
for i in range(len(A)):
    if i % 2 == 0:
        try: 
            x = A[i:, :i]
            B[2] = x
        except:
            continue
            

print(f"This is the required Matrix: \n{B}")
