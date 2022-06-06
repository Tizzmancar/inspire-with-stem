#1/deskop/inspire with stem/lesson/pyramids.py

######################################
#       half pyramid
#       Name : Carson Maina
#       Date : 27/5/2022
######################################
#half pyramid
#**
rows = int(input("enter number of  rows: "))
for i in range (rows):
    for j in range (i + 1):
        print("*" , end= " ")
    print("\n")

row = int(input("enter number of rows"))
for i in range (rows):
    for j in range (i + 1):
        print(j+1 , end=" " )
    print("\n")

