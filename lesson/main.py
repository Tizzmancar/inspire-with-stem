#1/deskop/inspire with stem/lesson/main.py

######################################
#       file : main.py
#       Name : Carson Maina
#       Date : 27/5/2022
######################################

from students import student

from teachers import Teachers

import operations 
print(operations.add_numbers(3,5))
print(operations.divide_numbers(4,2))
print(operations.subtract_numbers(40,10))
print(operations.mult_numbers(30,10))

new_student = student("Sam","cycling",2004)
new_student.greet_student()

new_teacher = Teachers("John", 123456,"literature",456789)
new_teacher.get_tsc_no()