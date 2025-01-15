## taking inputs from the user
height = input("What is the height from which you have dropped your ball, in CMs?:\n")
bounces = input("How much time you wanna make it bounce?(This should not be a decimal):\n")
num_height = float(height) ## using floats so it becomes more accessible for coding
num_bounces = int(bounces) ## as they won't be in decimal
loop = True # for looping
def halfer(value, times): 
    if value < 0.05: ## proper formatting, and messages
        return f"Ball has stopped, as the current height it dropped from is: {value}\nAnd bounces allowed are more than that it actually took"
    elif times == 0:
        return f"Ball has stopped, as the numbers of bounces allowed has ended, at height: {value}"
    else:
        times -= 1
        print(f"Height is: {value}")
        return halfer(value / 2, times)

## prints things 
print(halfer(num_height, num_bounces))