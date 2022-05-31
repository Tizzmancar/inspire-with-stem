#1/deskop/inspire with stem/quadratic_equations.py

######################################
#       quadratic equations
#       Name : Carson Maina
#       Date : 31/5/2022
######################################


import math
a=int(input("enter quoefficient of first term "))
b=int(input("enter quoefficient of second term "))
c=int(input("enter constant "))

# def find_roots(a,b,c):
#     y1=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
#     y2=(-b-math.sqrt((b**2)-4*a*c))/(2*a)
#     print("the roots of the quadratic equation are:",y1,y2)
# find_roots(a,b,c)


w=math.sqrt((b**2)-4*a*c)
def look_roots(a,b,c):
    y1=(-b+w)/(2*a)
    y2=(-b-w)/(2*a)
    print("the roots of the quadratic equation are:",y1,y2)
look_roots(a,b,c)