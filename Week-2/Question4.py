fibonacci = [1, 1]

for place in range(2, 10):
    x = fibonacci[place - 1] + fibonacci[place - 2]
    fibonacci.append(x)

print(f"The holy Fibonacci sequence, which we been searching for is: {fibonacci}")
