#importing the necessary modules 
# import numpy as np
from matplotlib import pyplot as plt

# setting up the control 
x_axis = [1, 2, 3, 4] # the series in which u enter the values, matters
y_axis_one = [12, 13, 14, 15]
y_axis_second = [26, 22, 23, 18]

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
## dividing the plot into 2 axes
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols =1)
## giving it life to plot of rain
ax1.set_ylabel("Rain (in milliliters)")
ax1.set_title("The average amount of rain per square meters in my area") ## giving titles to the graphs we make 
ax1.grid(True)
ax1.legend() ## if u have given a legend, just run this too
ax1.plot(x_axis, y_axis_one, color="#f00", marker = "^", linewidth = 2, label="for rain")

## giving it life to plot of rain
ax2.set_xlabel("The month of the year")
ax2.set_ylabel("Temperature (in degree celsius)")
ax2.set_title("The average temperature in my area") ## giving titles to the graphs we make 
ax2.grid(True)
ax2.legend() ## if u have given a legend, just run this too
ax2.plot(x_axis, y_axis_second, marker = "o", linewidth = 2, label="for temperature")

## changes in the entire figure
plt.tight_layout() ### ← makes the plot look neater with better padding 
plt.show() ## ← finally to show it word