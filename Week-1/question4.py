x = input("Give me a list of numbers, don't use '[]'s only ','s:\n")
list_x = x.split(",")
y = input("Give me another list of numbers, and don't use '[]'s only ','s:\n")
list_y = y.split(",")
combined_list = list_x + list_y
only_unique_list = list(set(combined_list))
if len(combined_list) != len(only_unique_list):
    print("You have at least 2 elements in common == True")
else:
    print("DaMn, A unique list this time!??")
