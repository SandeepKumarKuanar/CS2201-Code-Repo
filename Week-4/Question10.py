## importing important modules that would be used in the code 
import numpy as np 
database = {}


roll_number = input("What is your roll number?\n")
marks1 = int(input("What is the marks out of 100 in your first course?\n"))
marks2 = int(input("What is the marks out of 100 in your second course?\n"))
marks3 = int(input("What is the marks out of 100 in your third and final course?\n"))

marks = []
marks.append(marks1)
marks.append(marks2)
marks.append(marks3)
mark = np.array(marks, dtype="float64")
total = np.sum(mark, axis=0, dtype="float64")
database[roll_number] = total
print(database)