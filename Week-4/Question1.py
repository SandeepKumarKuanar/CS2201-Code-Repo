# print("Hello, World!") ## the real test
L1 = [(i) for i in range(0, 10)]
L2 = [(i) for i in range(4, 12)]

print(f"\nI have take this as List number 1 --> {L1}\n")
print(f"I have take this as List number 2 --> {L2}\n")

only_L1 = [(j) for j in L1 if j not in L2]

print(f"This is the unique list of the numbers solely in L1, and not in L2 --> {only_L1}\n")
