class Employee:
    def __init__(self,_name,_salary):
        self.name = _name
        self.salary = _salary
    def sayHi(self):
        print('hello my name is ' + str(self.name) + ' and i earn ' + str(self.salary) + ' as my salary')
employee1=Employee('Sam',987654)
employee1.sayHi()