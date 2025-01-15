Database = {
    "Sandeep Kumar Kuanar": "Sandeep@123",
    "user2": "securePass456",
    "admin": "admin@2025",
    "guest": "welcome@123",
    "testUser": "testPass789"
}

userID = input("Hello, What is your UserID?:\n")
for ID in Database:
    if ID == userID:
        password = input("Then, What is your password?:\n")
        if Database[ID] == password:
            print("Welcome to the portal!")
        else:
            print("Invalid Credentials!")
            ## changing password if you get your password wrong!
            change_password = input("Do you want to change your password?:\n").lower()
            if change_password == "yes":
                userID = input("Then, What is your UserID?:\n")
                for ID in Database:
                    if userID == ID:
                        new_password = input("What would be your new password?:\n")
                        reenter_password = input("Please, re-enter your new password?:\n")
                        if new_password == reenter_password and new_password != Database[ID]:
                            print("Changing your Password. . . . . . .")
                            Database[ID] = new_password
                            print("Password Changed Successfully ✅")
                            print("Updated the 'Database'✅")
                        else:
                            print("Your New Password is same as the OLD one")

print("Thank you, for using my portal!")