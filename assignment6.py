## geometric progression
a = int(input("enter first term "))
r = int(input("enter common ratio "))
n = int(input("enter number of terms "))

for i in range (1, n + 1):
    n_term = a * r *(i-1)
    print(n_term)

#sum
s_n = float((a*(1-r**n) /1-r))