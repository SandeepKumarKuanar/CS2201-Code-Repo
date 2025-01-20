#print("Hello, World!") ## the real test

repeats_list = ["Sandeep", "Kumar", "Kumar", "Kumar", "Kuanar", "YO", "YO", "YO", "YO", 1, 2, 3, 3, 3]
set_list = set(repeats_list)
unique_list = list(set_list)
print(f"This is the list of items which I will be using: {repeats_list}")
print(f"This is the Unique list of items, which has lost it's original order: {unique_list}")

unique_list = [repeats_list[i] for i in range(len(repeats_list)) if repeats_list[i] != repeats_list[i - 1]]
print(f"This is the Unique list of items, which retains its original order: {unique_list}")
