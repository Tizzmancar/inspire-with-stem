import random
print("Welcome to our passsword generator")
character= 'qwertyuiopasdfghjklzxcvbnm1234567890'
num_password= int(input("How many passwords do you want to generate "))
len_password= int(input("What is the length for your password "))
print("\n Here are your passwords")
for password in range (num_password):
    password= ''
    for c in range(len_password):
        password+= random.choice(character)
    print(password)