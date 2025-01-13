#print("Hello, World!") <--the real test

name = "mitochondria" #defined the name
list_of_name = list(name)#turned it into a list
length = len(list_of_name) + 1  #adding it
for i in range(0, len(list_of_name)):
    length -= 1 
    print(name[:length]) #well it works
    

#turn into functions to be honest!
