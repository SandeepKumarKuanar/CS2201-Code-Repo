import numpy as np
s = abs(np.random.normal(0, 0.5, 100)) #random sample of size 100 generated from a
                                        #normal distribution of mean 0 and s.d. 0.5
print(s)
max1 = np.max(s)
min1 = np.min(s)
s1 = [(x-min1)/(max1-min1) for x in s]
print(s1)
sc = np.zeros(6)
for x in s1:
    if x < 0.2:
        sc[0] = sc[0] + 1
    elif x < 0.4:
        sc[1] = sc[1] + 1
    elif x < 0.6:
        sc[2] = sc[2] + 1
    elif x < 0.8:
        sc[3] = sc[3] + 1
    elif x < 0.95:
        sc[4] = sc[4] + 1
    else:
        sc[5] = sc[5] + 1
print(sc)
import matplotlib.pyplot as plt
plt.pie(sc, labels = ['miss', 'beginner', 'improver', 'seasoned', 'pro', 'bulls eye']) 
#Note that ‘miss’ is modelled on an event with the highest probability, with x-value close to the
#mean (0); similarly ‘bull’s eye’ is modelled on the rare events, i.e. with low probabilities

plt.show()