# print("Hello, World!") ## ← the real test
list_of_numbers = [str(i) for i in range(1, 6)] # here I am converting "i" from int to string cause, .join() takes only strs as argument
for i in range(len(list_of_numbers), 0, -1):
    print(" ".join(list_of_numbers[:i])) # joing for neater presentation

# everything in one
