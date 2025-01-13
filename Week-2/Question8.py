# print("Hello, World") # ← the real test
list_of_numbers = [" ", "1", "2", "3", "4", "5", "4", "3", "2", "1"]
for i in range(6):
    # if i == 0:
    #     continue
    list_of_numbers[i] = " "
    list_of_numbers[i * -1] = " "
    print(" ".join(list_of_numbers))
