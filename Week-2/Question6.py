# print("Hello, World!") ## ← the real test
list_of_numbers = [i for i in range(1, 11)]
odd_numbers = list()
for i in list_of_numbers:
    if i % 2 != 0:
        odd_numbers.append(str(i)) # here I am converting "i" from int to string cause, .join() takes only strs as arguments
        print(" ".join(odd_numbers)) # joing for neater presentation