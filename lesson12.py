#1/deskop/inspire with stem/lesson12.py

######################################
#       dictionaries
#       Name : Carson Maina
#       Date : 27/5/2022
######################################
mary_fav_food = ['beef' , 'chicken' , ' vegetable']
jane_fav_food = ['rice', 'ugali', 'potato']
#food =mary_fav_food , jane_fav_food
foods ={
    'mary':['beef' , 'chicken' , 'vegetable'],
    'jane':['rice', 'ugali', 'potato']}
# print(foods)
# print(type(foods))
for mary,jane in foods.items():
    print(f"{mary}:{jane}")

# names ={
#     'mary' :{'female','45678','nai'},
#     'jane' :{'female','98766','thika'}}
# for mary,jane in names.items():
#     print(f"{mary}:{jane}")