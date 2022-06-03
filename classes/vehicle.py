#1/deskop/inspire with stem/classes/vehicle.py

######################################
#       classes
#       Name : Carson Maina
#       Date : 3/6/2022
######################################

class Vehicle:
    def  __init__(instance,_speed,_mileage):
        instance.speed=_speed
        instance.mileage= _mileage
        
    def sayHi(instance):
        print('maximum speed is ' + str(instance.speed) + ' Km/h while mileage is '+str(instance.mileage)+" kilometeres")

Toyota = Vehicle(200,307988)
Mercedes= Vehicle(300,236789)
Toyota.sayHi()