#print("Hello, World!!")  ## the real test

# importing important modules 
import random as rand

## length of the capcha shall be 6 
types = [1, 2 ,3] ## here 3 == its a number, 1 == upper case letter, 2 == lower case letter 
capcha = ""
for i in range(0, 6):
    type_of_letter = rand.randint(1, 3)
    if type_of_letter == 2:
        capcha += chr(rand.randint(97, 122))
    if type_of_letter == 1:
        capcha += chr(rand.randint(65, 90))
    if type_of_letter == 3:
        capcha += str(rand.randint(0, 9))
        
print(f"This is your unique capcha: {capcha}")
