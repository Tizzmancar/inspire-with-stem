#1/deskop/inspire with stem/lesson/arithmetic_progression.py

######################################
#       arithmetic progression
#       Name : Carson Maina
#       Date : 27/5/2022
######################################

a = int(input("enter first term "))
d = int(input("enter common difference "))
n = int(input("enter number of terms "))

# for i in range (1, n + 1):
#     n_term = a + d *(i-1)
#     print(n_term)

s_n = float((n/2)*(2*a+(n-1)*d))
print(s_n)

