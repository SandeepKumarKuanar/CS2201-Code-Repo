list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
dupli = [1, 2, 3, 4, 5, 6, 7]
print("I have this is bunch of numbers in a list ==>", list_of_numbers)
pop_place = int(input("Give me the index of the number you want to drop:\n"))
try:
    poped_list = dupli.pop(pop_place)
    print(dupli)
except:
    print("The index you have given is more than the number of numbers in the list.")
