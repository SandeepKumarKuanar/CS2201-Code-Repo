## importing important modules 
from matplotlib import pyplot as plt

plt.style.use("petroff10")
months = ["Jan", "Feb", "Mar", "Apr"]
values = [12, 14, 16, 10]

plt.pie(values, labels = months)
plt.title("Rain in pie")
plt.tight_layout()
plt.show()