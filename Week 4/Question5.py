num = input("Enter me a list of numbers:\n").strip()
num_list = num.split()
results = []

for i in num_list :
    if num_list.count(i) == 1:
        results.append(i)

print(results)
