#print("hello, world!") ## the real test

name = input("Enter me your name:\n").strip()
list_name = name.split()
initials = []
for i in range(len(list_name)):
    if i != len(list_name) - 1:
        initials.append(list_name[i][0])

initials_string = ". ".join(initials)
print(initials_string + ". " + str(list_name[len(list_name) - 1]))
