import matplotlib.pyplot as plt
import math
x = [44, 40, 41, 50, 1000, 1500, 2000, 1000, 25, 50] #No. of Transactions
y = [870, 600, 790, 900, 100000, 350000, 250000, 150000, 1001, 500] #Balance (INR)
labels = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1] #Churn
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

## adding the meat layer around the rough skeleton, to make it look polished 
print("Warm Greeting, from entire family of BankOnUs")
print("Hello customer, we need your details of balance and number of transactions done by you, please proceed ahead\nit would not take much time, just fill the form out, so that we would keep providing better facilities to u. Thank you for your consideration.\n")

number_of_transactions = input("Kindly enter your the number of transactions you have made with this bank account., Thank you!\n").strip()
balance = input("Kindly enter your balance without any preffix (eg. Neither '$400' accepted, nor '400 dollars', or similar accepted), enter the number, thank you!\n").strip()
point = (int(number_of_transactions), int(balance))
class_label = kNN(x, y, labels, 2, point)
if class_label == 1:
    print("We have an exciting offer for you! Would you like to know more? Stay tuned on the website for updates on u!")
else:
    print("Thank you for banking with us! Please let us know how we can serve you better, on the bank website.")
plt.scatter([point[0]], [point[1]], color="magenta")
plt.show()







