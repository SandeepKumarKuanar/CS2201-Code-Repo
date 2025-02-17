turns = True
list_of_details = []
while turns == True:
    name = input("Input the name of the person u want to enter to see the magic unfold!\n")
    age = input("Input the age of the person u want to enter to see the magic unfold!\n")
    list_of_details.append(name)
    list_of_details.append(age)
    exit = input("You u want to exit the while loop? Input in 'Yes/No' or 'y/n':\n").strip().lower()
    if exit == 'yes' or exit == 'y':
        turns = False

print(f"This is the list of the entries:{list_of_details}")
age_field = []
name_field = []
for i in range(len(list_of_details)):
    if i % 2 == 0:
        name_field.append(list_of_details[i])
    else:
        age_field.append(list_of_details[i])

print(f"List of all names: {name_field}")        
print(f"List of all ages: {age_field}")

fields = {}
for i in range(len(name_field)):
    fields[name_field[i]] = age_field[i]
    
print(f"This is the dictionary of fields {fields}")
