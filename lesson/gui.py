from tkinter import *
from turtle import color

window = Tk()
## window title
window.title("Welcome to my app")
#window background colour
window.configure(bg='black')
# window size
window.geometry("700x600")
#labels
f_name = Label(window, text="First_name", font=("Arial Bold",20) )
s_name = Label(window, text="Second_name", font=("Arial Bold",20) )
#label position
f_name.grid(column = 60, row = 100)
s_name.grid(column = 60, row = 120)

def open_pop_up():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg='green')
    msg=Label(top,text="signed in",font = ("rockwell 18 bold")).place(x=150,y=80)
    print(msg)


#buttons
btn=Button(text="sign up",bg='red',command= open_pop_up)
btn.pack

# button position 
btn.grid(column=120,row=150)
# text box
txt_box = Entry(window,width=20)
# text box position
txt_box.grid(column=100 , row= 120)

txt_box = Entry(window,width=20)
txt_box.grid(column=100 , row= 100)


# running app
window.mainloop()