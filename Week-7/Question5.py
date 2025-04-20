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

## making the plot
# that the lines are added in the same manner as they are called in the code
plt.bar(x_axis, y_axis_one, color="#4b4a43", label="for rain")
## giving it life
plt.xlabel("The month of the year")
plt.ylabel("Rain (in milliliters)")
plt.title("The average  amount of rain per square meters in my area") ## giving titles to the graphs we make 
plt.grid(True)
plt.tight_layout() ### ← makes the plot look neater with better padding 
plt.legend() ## if u have given a legend, just run this too
plt.show() ## ← finally to show it word 