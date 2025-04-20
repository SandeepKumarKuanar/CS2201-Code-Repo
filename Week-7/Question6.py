#importing the necessary modules 
import numpy as np
from matplotlib import pyplot as plt

# setting up the control 
x_axis = ["Jan", "Feb", "Mar", "April"] # the series in which u enter the values, matters
y_axis_one = [12, 16, 18, 20]
y_axis_second = [32, 26, 22, 18]

# #meat of the program 
# while True:
#     month = input("What is the month of the year that you have in your mind?\n")
#     rain = input("What is the amount of rain that your area have received that month (in milliliters)\n")
#     temperature = input("What is the average temperature of your region throughout the month? (in degree celsius?)\n")

#     x_axis.append(month)
#     y_axis_one.append(rain)
#     y_axis_second.append(temperature)
#     run_again = input("DO you wanna continue adding the info? Enter 'Yes' or 'No' accordingly.\n")
#     if run_again == "yes" or run_again == "y":
#         continue 
#     else:
#         break

## defining the width of the plots so i can shift one of those to the side to show them as one
x_indexes = np.arange(len(x_axis))
width = 0.4
## making the plot
# that the lines are added in the same manner as they are called in the code
plt.bar(x_indexes - (width / 2), y_axis_one, color="#f00", label="for rain", width = width)
plt.bar(x_indexes + (width / 2), y_axis_second, label="for temperature", width = width)
## changing the labels of ticks in the graph 
plt.xticks(ticks=x_indexes, labels = x_axis)
## giving it life
plt.xlabel("The month of the year")
plt.ylabel("Rain (in milliliters)")
plt.title("The average  amount of rain per square meters in my area") ## giving titles to the graphs we make 
plt.grid(True)
plt.tight_layout() ### ← makes the plot look neater with better padding 
plt.legend() ## if u have given a legend, just run this too
plt.show() ## ← finally to show it word