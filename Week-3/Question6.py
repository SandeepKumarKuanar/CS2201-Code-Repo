#print("Hello, World!") ## this is real test
inputted_numbers = list()
while True:
    print("This 'While' loop will not stop, until you will input any even number\nAs soon as u input an Even number, it exits!!!")
    number = input("What is the number, that You wanna input to the loop\n")
    int_number = int(number)
    inputted_numbers.append(int_number)
    if int_number % 2 == 0:
        print(f"U took this many attempts to do it: {len(inputted_numbers)}")
        print(f"List of your inputted numbers: {inputted_numbers}")
        break
