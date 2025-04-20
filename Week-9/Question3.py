n = 5
x = [ 5, 15, 30, 42, 55 ]
y = [250, 200, 150, 102, 75]
value = 50
result = 0.0
for i in range(n):
    # Compute individual terms of above formula
    term = y[i]
    for j in range(n):
        if j != i:
            term = term * (value - x[j]) / (x[i] - x[j])
# Add current term to result
result += term
print("\nValue at", value, "is", round(result, 6))