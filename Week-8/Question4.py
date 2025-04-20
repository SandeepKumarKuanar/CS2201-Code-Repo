import numpy as np
import matplotlib.pyplot as plt

names = input("Give student first names (space separated, put enter to finish): ").strip().split(" ")
marks1 = input("Give marks of student 1 (space separated, put enter to finish): ").strip().split(" ")
marks2 = input("Give marks of student 2 (space separated, put enter to finish): ").strip().split(" ")
marks3 = input("Give student marks of student 3 (space separated, put enter to finish): ").split(" ")

marks1_np = np.array(marks1, dtype='int')
marks2_np = np.array(marks2, dtype='int')
marks3_np = np.array(marks3, dtype='int')
avg = np.mean([marks1_np, marks2_np, marks3_np], axis = 0)
print(avg)
plt.bar(names, avg)
plt.xlabel("Students")
plt.ylabel("Average marks")
plt.show()