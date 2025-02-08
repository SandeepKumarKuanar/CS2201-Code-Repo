# print("""
# $$\   $$\                                   $$\                 $$\                           $$$$$$$\                      
# $$ | $$  |                                  $$ |                $$ |                          $$  __$$\                     
# $$ |$$  / $$$$$$$\   $$$$$$\  $$\  $$\  $$\ $$ | $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\        $$ |  $$ |$$\   $$\ $$$$$$$\  
# $$$$$  /  $$  __$$\ $$  __$$\ $$ | $$ | $$ |$$ |$$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\       $$$$$$$  |$$ |  $$ |$$  __$$\ 
# $$  $$<   $$ |  $$ |$$ /  $$ |$$ | $$ | $$ |$$ |$$$$$$$$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |      $$  __$$< $$ |  $$ |$$ |  $$ |
# $$ |\$$\  $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$   ____|$$ |  $$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ |  $$ |
# $$ | \$$\ $$ |  $$ |\$$$$$$  |\$$$$$\$$$$  |$$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ |  $$ |
# \__|  \__|\__|  \__| \______/  \_____\____/ \__| \_______| \_______| \____$$ | \_______|      \__|  \__| \______/ \__|  \__|
#                                                                     $$\   $$ |                                              
#                                                                     \$$$$$$  |                                              
#                                                                      \______/                                               
# """)
Questions = {
    "1. Which of the following methods is used to determine the eigenvalues of a matrix?" : [
        ("A. Gaussian Elimination", 0, 0), #(--Option to be displayed--, --correct or not--, --marks--)
        ("B. Power Iteration", 1, 2),
        ("C. Gram-Schmidt Process", 0, 0),
        ("D. Cholesky Decomposition", 0, 0),
    ],
    # Add more questions here in the same format
    "2. Which of the following methods is used to determine the eigenvalues of a matrix?" : [
        ("A. Gaussian Elimination", 0, 0), #(--Option to be displayed--, --correct or not--, --marks--)
        ("B. Power Iteration", 1, 2),
        ("C. Gram-Schmidt Process", 0, 0),
        ("D. Cholesky Decomposition", 0, 0),
    ],
}

print("Play the quiz and answer the following questions wisely, and cross the threshold of 10 marks to take on the Jackpot Question: ")
print("The Jackpot Question is worth 5 marks, and you need to answer it correctly to win the game, but no options given.")
print()

status = 0 # changes to 1 if the player answers any question incorrectly
threshold = 10 # the threshold to cross to take on the Jackpot Question
marks = 0 # the marks the player has scored yet

for Question in Questions:
    print(Question)
    for i in Questions[Question]:
        print(f"    {i[0]}")
    print()
    answer = input("Enter your answer option: ").strip().upper()
    for i in Questions[Question]:
        if i[1] == 1:
            if i[0][0] == answer:
                marks += i[2]
                print(f"Correct Answer!, current marks is {marks}")
            else:
                print(f"Incorrect Answer!, current marks is {marks}")
print(marks, status, threshold)