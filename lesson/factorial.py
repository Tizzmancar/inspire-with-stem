#1/deskop/inspire with stem/factorial.py

######################################
#       factorial
#       Name : Carson Maina
#       Date : 27/5/2022
######################################
# method 1
n = int(input("enter number "))
factorial = 1
if(n<0):
    print("no factorial for negative number")
elif (n== 0):
    print("factorial of 0 is equal to 1")
else:
    for  i in range (1, n + 1):
        factorial = factorial * i
print("factorial of number is : " , factorial)

# or

# method 2
n = input("enter number ")
factorial = 1
if(int(n)<0):
    print("no factorial for negative number")
elif (int(n) == 0):
    print("factorial of 0 is equal to 1")
else:
    for  i in range (1, int(n) + 1):
        factorial = factorial * int(i) 
print("factorial of number is : " , factorial)

