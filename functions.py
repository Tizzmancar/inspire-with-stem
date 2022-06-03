#1/deskop/inspire with stem/functions.py

######################################
#       functions
#       Name : Carson Maina
#       Date : 31/5/2022
######################################

# functions is a block of code which gets executed altogether

# defining a funtion
def say_hello():
    print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    print(z)
# say_hello()

def bark():
    print("dogs bark woof woof")

def moo():
    print("cows go moo")

def meow():
    print("cats go meow")

def neigh():
    print("horse neighs")
# neigh()
# bark()
# moo()
# meow()

##function parameters

#functions for addition
def add_numbers(x,y):
    sum_nums=x + y
    print("the sum of numbers:",sum_nums)

# add_numbers(40,50)
# add_numbers(100,400)
# add_numbers(1,4)

##functions for products
def product_numbers(x,y):
    prod= x*y
    print("the product of the numbers is:",prod)

# product_numbers(80,30)
# product_numbers(4,89)
# product_numbers(7,9)


def print_name(name='Bob Afwata'):
    print(name)
# print_name("sam")

## returning a function
def get_sum (num1,num2):
    sum_nums=num1+num2
    return sum_nums
# print(get_sum(7,12))

def get_square (num1,power):
    squares=num1**power
    return squares
# print(get_square(6,4))

def get_full_name(f_name,s_name):
    full_name=f_name + " " + s_name
    return full_name.title()
# print(get_full_name("Bob","Afwata"))

## returning a dictionary from a function
def create_full_name(first_name,second_name):
    person = {'first':first_name, 'second':second_name}
    return person

student =create_full_name('Bob','Afwata')
# print(student)

## passing a list in a function
def greet_friends(names):
    for name in names:
        msg="hello " + name.title() + "!"
        print(msg)
friends=['Curtis','Judah','Joshua','Edwin','John']
greet_friends(friends)
