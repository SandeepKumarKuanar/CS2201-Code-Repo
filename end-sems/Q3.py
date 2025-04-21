#print("Hello, World!") ## <- the real test
 
print("Welcome to ChemLab!!")
code = input("Please Input your CODE:\n").strip() 
passwords = {
    'A071': 'FOX',
    'A213': 'MAVIN',
    "A204": 'EGSY',
    'B071': 'PAULING',
}

list_of_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

if code in passwords:
    ciphered_password = input("Please enter your ciphered PASSCODE:\n").upper().strip()
    bias = len(ciphered_password)
    cip = ""
    for i in passwords[code]:
        position = list_of_characters.index(str(i))
        cip += list_of_characters[position - bias]
    if ciphered_password == cip:
        print("Access Granted!" + " Dr." + passwords[code])
    else:
        print("Acesss denied"+ " Dr." + passwords[code])	
else:
    print("Acesss denied")
