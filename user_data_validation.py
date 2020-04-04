import random
import string

User_data = {}

def randomString():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(5))

def Password_Satisfaction():
    password_satisfy = input("Are u satisfied with password(y/n): ")
    if password_satisfy == 'y':
        pass
    elif password_satisfy == 'n':
        rand_password = input("Enter a Password: ")
        while len(rand_password) < 7:
            rand_password = input("Password Length must be 7 or more: ")
        print("New password selected \n")
    return "Account Created \n"

New_User = 'y'
while New_User == 'y':
    Firstname = input("Enter First name: ")
    Lastname = input("Enter Last name: ")
    Email = input("Enter Email Address: ")
    FullName = Lastname + " " + Firstname

    rand_password = Firstname[:2] + Lastname[-2:] + randomString()
    print("Your password is: ", rand_password, "\n")
    
    print(Password_Satisfaction())

    User_data[FullName] = [Email, rand_password]
    print("User Data: ", User_data)

    print("\n")
    New_User = input("New User? (y/n): ")