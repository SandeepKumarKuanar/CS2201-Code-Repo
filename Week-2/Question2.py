#print("Hello, World!") ##real test

names = input("Give me a list of Chemical elements, don't give '[]'s, u can seperate them using ','s\n")

list_of_names = names.split(",")

longest = []
for i in range(len(list_of_names)):
    for j in range(len(list_of_names)):
        if len(list_of_names[i]) > len(list_of_names[j]):
            longest.append(list_of_names[i])


print(f"The longest element on the basis of words is: {longest[len(longest) - 1]}")


