#print("Hello, World!") ## the real test

name = input("What is your name?:\n").strip().lower()
list_name = list(name)

if len(list_name) % 2 != 0:
    y = list_name[:len(list_name) // 2]
    z = list_name[len(list_name) // 2 + 1:]
    a = list_name[len(list_name) // 2]
    result = z + list(a) + y
    str_results = "".join(result)
    print(f"This is the encrypted name {str_results}")

else:
    y = list_name[:len(list_name) // 2]
    z = list_name[len(list_name) // 2:]
    result = z + y
    str_results = "".join(result)
    print(f"This is the encrypted name {str_results}")
