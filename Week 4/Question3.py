#print("Hello, World!") ## the real test

string = input("Enter a string u would like to run the function on:\n").lower().strip()

def encrypt(string):
    list_string = list(string)
    alphabets = [chr(i) for i in range(97, 123)]
    reverse_alphabets = alphabets[::-1]
    
    results = [reverse_alphabets[alphabets.index(i)] for i in list_string]
    return results


print(f"Your inputed string is, '{string}'")
encrypt = "".join(encrypt(string))
print(f"your encrypted string is, '{encrypt}'")
