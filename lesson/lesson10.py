#1/deskop/inspire with stem/lesson/lesson10.py

######################################
#       dictionaries
#       Name : Carson Maina
#       Date : 24/5/2022
######################################

#dictionary is a collection of key value pairs
#syntax: dictionary = {'key' : 'value'}
colours ={'colour': 'red'}
vehicle = {'type': 'toyota','plate_no': '1234'}

# print(type(colours))#use the type method to check data type

##accessing values in a dictionary
# print(vehicle['type']) #you can access value of an element inside a dictionary
print(vehicle.get('plate_no'))

person = {'name':'Sam',
    'gender': 'male',
    'phone_no': '1234',
    'residence' : 'nai'}

## adding something to dictionary
# person['age']= '21'
# person['fav_colour']= 'black'

##deleting an item in a list
# del person['phone_no']

# print(vehicle['type'],vehicle['plate_no'])
# print(type(person))
# print(person)

## Looping over dictionaries
# for key, value in person.items() :
#     print(f"{key}:{value}")

print(person.get('password'))
