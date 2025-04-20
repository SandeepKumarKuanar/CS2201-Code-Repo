import matplotlib.pyplot as plt
import math
x = [100, 90, 95, 89, 55, 70, 65, 70] #CS1101 marks
y = [100, 90, 80, 80, 65, 70, 70, 65] #CS2201 marks
labels = [0, 0, 0, 0, 1, 1, 1, 1] #labels
plt.scatter(x, y, c=labels)
def distance(x, y, point):
    return math.sqrt((x-point[0])**2 + (y-point[1])**2)
def majority(labels):
    label_freq = {}
    for lb in labels:
        if lb not in label_freq:
            label_freq[lb] = 1
        else:
            label_freq[lb] = label_freq[lb] + 1
    max_freq = -1
    max_freq_label = -1
    for lb in label_freq:
        if label_freq[lb] > max_freq:
            max_freq = label_freq[lb]
            max_freq_label = lb
    print(label_freq)
    print("max label = %d max label freq = %d" %(max_freq, max_freq_label))
    return max_freq_label

def kNN(x, y, labels, k, point):
    x_temp = x
    y_temp = y
    l = len(x_temp)
    knn_labels = []
    for j in range(1, k+1):
        min_distance = 1000
        x_coord_min = -1
        y_coord_min = -1
        min_label = -1
        for i in range(0, l):
            if x_temp[i] != -1 and distance(x_temp[i], y_temp[i], point) < min_distance:
                min_distance = distance(x_temp[i], y_temp[i], point)
                x_coord_min = x_temp[i]
                y_coord_min = y_temp[i]
                min_label = i
                x_temp[i] = -1 #considered
        print("%d %d" %(x_coord_min, y_coord_min))
        knn_labels.append(labels[min_label])
    print(knn_labels)
    knn_class = majority(knn_labels)
    return knn_class

point = (85, 90)
class_label = kNN(x, y, labels, 3, point)
if class_label == 1:
    print("No worries, the instructor and the TAs will help you!")
else:
    print("Great to know you are doing well!")
plt.scatter([point[0]], [point[1]], color="magenta")