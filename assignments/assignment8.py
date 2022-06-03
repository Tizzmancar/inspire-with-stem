class Password:
    def __init__(self,user,password):
        self.user=user
        self.password=password
    def sayHi(self):
        print("username is " + self.user+ " password is " + self.password)
password1 = Password('Sam','07yerya')
password1.sayHi()