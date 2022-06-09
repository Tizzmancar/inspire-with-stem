#1/deskop/inspire with stem/lesson/gui_examples.py

######################################
#       gui examples
#       Name : Carson Maina
#       Date : 7/6/2022
######################################

#Import the required Libraries
from tkinter import *


window = Tk()
## window title
window.title("Welcome to my app")
#window background colour
window.configure(bg='black')
# window size
window.geometry("700x600")
#labels
f_namelabel = Label(window, text="First_name").grid(column = 0, row = 0)
f_name = StringVar()
f_name_entry = Entry(window,width=20).grid(column=1 , row= 0)

s_name = Label(window, text="Second_name").grid(column = 0, row = 1)
s_name = StringVar()
s_name_entry = Entry(window,width=20).grid(column=1 , row= 1)


passwordLabel = Label(window,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=2, column=1)


def open_signin():
   top= Toplevel(window)
   top.geometry("750x250")
   top.title("Welcome")
   Label(top, text= "You are signed in", font=('rockwell 18 bold')).place(x=150,y=80)


#Create a button in the main Window to open the popup
btn = Button(window, text="Login",command=open_signin)
btn.grid(column=120,row=150)

window.mainloop()
