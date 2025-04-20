## importing important modules from the library
import random
from matplotlib import pyplot as plt

## for the chart 
attempts = []
probability = []
number_of_repeats = 500
heads_came_in = 0

## meat of the product
for i in range(1, number_of_repeats + 1):
    instance = random.random()
    attempts.append(i)
    if instance < 0.5:
        heads_came_in += 1

    probability.append(heads_came_in / i)

plt.plot(attempts, probability, color="#4b4a45", label="Probability of heads came in")
plt.xlabel("number of tosses")
plt.ylabel("Probability of head")
plt.title("Probability of heads in the unbiased coin flip")
plt.tight_layout()
plt.legend()
plt.show()