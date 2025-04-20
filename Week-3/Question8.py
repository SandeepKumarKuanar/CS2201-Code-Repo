#print("Hello, World!") ## this is real test
d = {1 : 'ONE', 
    2 : 'TWO', 
    3 : 'THREE', 
    4 : 'FOUR', 
    5 : 'FIVE', 
    6 : 'SIX', 
    7 : 'SEVEN', 
    8 : 'EIGHT', 
    9 : 'NINE'
}
print("I will convert all number into words only")
number = input("What is the number, that You wanna input to the program\n")
str_number = str(number)
list_number = [str_number[i] for i in range(len(str_number))]
in_words = list()
for i in list_number:
    for elements in d:
        if d[int(i)] not in in_words:
            in_words.append(d[int(i)])
words = " ".join(in_words)
print(f"Your number in just words: {words}")
