import matplotlib.pyplot as plt
import math
x = [100, 90, 95, 89, 55, 70, 65, 70]
y = [100, 90, 80, 80, 65, 70, 70, 65]
labels = [0, 0, 0, 0, 1, 1, 1, 1]
#plt.scatter(x, y, c=labels)
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
        indices_covered = []
        for i in range(0, l):
            if i not in indices_covered and distance(x_temp[i], y_temp[i], point) <  min_distance:
                min_distance = distance(x_temp[i], y_temp[i], point)
                x_coord_min = x_temp[i]
                y_coord_min = y_temp[i]
                min_label = i
                indices_covered.append(i) #considered
        print("%d %d" %(x_coord_min, y_coord_min))
        knn_labels.append(labels[min_label])
    print(knn_labels)
    knn_class = majority(knn_labels)
    return knn_class


test_set = [(90, 90, 0), (50, 60, 1), (85, 80, 1), (20, 20, 0)]
TP = 0
TN = 0
FP = 0
FN = 0
for t in test_set: #1 -- positive class
    point = (t[0], t[1])
    class_label = kNN(x, y, labels, 3, point)
    print(class_label)
    if t[2] == 1 and class_label == 1:
        TP = TP + 1
    elif t[2] == 0 and class_label == 0:
        TN = TN + 1
    elif t[2] == 1 and class_label == 0:
        FN = FN + 1
    else:
        FP = FP + 1
print("TP = %d" %TP)
print("FP = %d" %FP)
print("TN = %d" %TN)
print("FN = %d" %FN)

Accuracy = (TP + TN)/len(test_set)
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
Fscore = 2*((Recall*Precision)/(Recall+Precision))
print("Accuracy = %f" %(Accuracy))
print("Precision = %f" %(Recall))
print("Recall = %f" %(Precision))
print("F-score = %f" %Fscore)