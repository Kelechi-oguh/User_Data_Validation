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
        rand_password = input("Enter a Password (at least 7 characters): ")
        while len(rand_password) < 7:
            rand_password = input("Password Length must be 7 or more characters: ")
        print("New password selected \n")
    return "Account Created \n"

def name_check(value): 
        while len(value)==0:
            value = input("Please do not leave blank!: ")
        return value

New_User = 'y'
while New_User == 'y':
    Firstname = input("Enter First name: ")
    Firstname = name_check(Firstname)
    Lastname = input("Enter Last name: ")
    Lastname = name_check(Lastname)
    Email = input("Enter Email Address: ")
    Email = name_check(Email)

    FullName = Lastname + " " + Firstname

    rand_password = Firstname[:2] + Lastname[-2:] + randomString()
    print("Your password is: ", rand_password, "\n")
    
    print(Password_Satisfaction())

    User_data[FullName] = [Email, rand_password]
    print("User Data: ", User_data)

    print("\n")
    New_User = input("New User? (y/n): ")