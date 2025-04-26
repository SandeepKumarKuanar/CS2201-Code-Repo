#print("Hello, World!!") ## real test


while True:
    str_one = input("Input the first string of numbers here:\n").lower().strip()
    str_two = input("Input the second string of numbers here:\n").lower().strip()

    if len(str_one) != len(str_two):
        print("Both the strings are not of same length, hence stopping the process.")
        break

    p = int(input("Enter the position where you want to do the crossover:\n").lower().strip())
    print(f"This are the inputs you have given to the system: '{str_one}' and '{str_two}'")
    a = str_one[:p] 
    b = str_one[p:]
    c = str_two[:p]
    d = str_two[p:]
    str_one = a + d
    str_two = c + b
    print(f"This are the outputs you received after crossover: '{str_one}' and '{str_two}'")
    break
