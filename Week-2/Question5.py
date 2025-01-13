#print("Hello, World!") ## ← the real test
list_of_number = list()
# print(list_of_number)
for i in range(1, 6):
    list_of_number.append(str(i)) # here I am converting "i" from int to string cause, .join() takes only strs as arguments
    print(" ".join(list_of_number)) # joing for neater presentation