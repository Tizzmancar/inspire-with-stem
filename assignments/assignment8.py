import random
print("Welcome to our passsword generator")

class Password:
    def __init__(self,user,password):
        self.user=user
        self.password=password
    def sayHi(self):
        print("username is " + self.user+ " password is " + self.password)


print("Welcome to our passsword generator")
character= str(input("enter characters to be used for password generation "))
user = str(input("enter username "))
num_password= int(input("How many passwords do you want to generate "))
len_password= int(input("What is the length for your password "))
print("\nHere are your passwords")
for password in range (num_password):
    password= ''
    for c in range(len_password):
        password+= random.choice(character)
    password1=Password(user,password)
    password1.sayHi()