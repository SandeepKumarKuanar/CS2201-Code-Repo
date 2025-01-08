#print("Hello, World!") ## the real test
string = "The quick brown fox jumps over the lazy dog"
string_list = string.split()
print("Is the word “fox” is in this sentence:", bool((i) for i in range(len(string_list)) if i == "fox"))
reversed_string_list = string_list[::-1]
reversed_sentence = " ".join(reversed_string_list)
print("Reversed Sentence:", reversed_sentence)

character_list = list(reversed_sentence)
print("Printed on every 3rd place")
for i in range(len(character_list)):
    if i % 3 == 0:
        print(character_list[i])
print("Printed on every 4th place")
for i in range(len(character_list)):
    if i % 4 == 0:
        print(character_list[i])
print("The number of characters in sentence is:", len(character_list))

second_steps = string[::2]
togther_second = " ".join(second_steps[::-1])
print("At every second step, u found this:", togther_second)

y = string[:3:]
z = string[len(string) - 3 : len(string)]
print("Y:", y)
print("Z:", z)
print("Y + Z:", y+z)
print("The output of Y*10:", y*10)
