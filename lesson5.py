# methods
name = "Mathenge Mugo"
user_name= "Ada Lovelace"
age = 15
#person = " I am " + str(name) + " and my age is " + str(age)
#print(person)
# the format() method
#print("My name is {} and I am {} ".format(name, age))
print(f"My name is {name} and I am {age} years old")
#n ->new line
#t ->tab
print(f"My \t name is {name} \n and I am")
print("Monday\t Tuesday\t Wednesday \t Thursday \t Friday \t Saturday \t sunday")

user_name = "Lovelace"
print(user_name.strip)
print(user_name.rstrip)
print(user_name.lstrip)

#Multiline strings
msg= '''WERTYUI56783H Mpesa confirmed
        you have received 2300 from 
        James Muoki 
        18th May 2022
        safaricom transparent for you
        '''
print(msg)
txt= """Holla! I am Bob Afwata
        I come from Kiambu county
         """
print(txt)

city = "Nairobi"
print(city[:5])
print(city[2:])
print(city[-1:])

f_name = "bob afwata"
# .upper converts to uppercase
print(f_name.upper())

s_name = "KENNEDY MUOKI"
#.lower() converts to lower case
print(s_name.lower())

#concatination - converting from one data type to another
#int -> float
#float-> int
number = 6 
print(str(number))

x = 4
print(float (x))
y = 3.24
print(int(y))

f_name = "James"
s_name = "Corden"
full_name = f_name + s_name
print(full_name)

#the replace() method replaces a string  with another
 
name = "Brett Cooper"

print(name.replace('t','G'))

msg = "Hello from Bob Afwata how are you"
print(msg.split())

print(len(msg))
 
