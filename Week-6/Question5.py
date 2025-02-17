## important modules 
import numpy as np

given = np.array(
    [[50, 60, 70], 
    [67, 88, 90], 
    [60, 78, 97]])


student_wise_marks = []    
print(f"This is the given array\n{given}")
for i in range(np.shape(given)[0]):
    student_wise_marks.append(np.sum(given[i, :]))
    
print(f"This is the student wise marks of his/her marks per subject == {student_wise_marks}")

subject_wise_marks = []
for i in range(np.shape(given)[1]):
    subject_wise_marks.append(np.sum(given[:, i]))

print(f"\nThis is the subject wise marks of all students combined == {subject_wise_marks}")
