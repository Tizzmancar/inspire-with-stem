#1/deskop/inspire with stem/classes/person.py

######################################
#       classes
#       Name : Carson Maina
#       Date : 2/6/2022
######################################

class Person:
    def __init__(self,_name,_age):
            self.name=_name
            self.age= _age

    def sayHi(self):
        print('Hello my name is ' +str(self.name)+' and i am ' +str(self.age) + ' years old')
person1 = Person('Bob',16)
person1.sayHi()
person2 = Person('Sam',21)
person2.sayHi()