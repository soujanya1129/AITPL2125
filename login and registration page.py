#login and registration page
from tkinter import *
from tkinter import ttk
class xyz:
    user = 'admin'
    passw ='adminadmin'
    def __init__(b,a):
        b.a = a
        b.a.title('LOGIN SCREEN')
        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        b.username = Entry()
        b.username.grid(row=1,column=2,columnspan=10)
        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        b.password = Entry(show='*')
        b.password.grid(row=2,column=2,columnspan=10)
        ttk.Button(text='LOGIN',command=b.login_user).grid(row=3,column=2)
    def login_user(b):
        if b.username.get() == b.user and b.password.get() == b.passw:
            a.destroy()
            newa = Tk()
        else:
            '''Prompt user that either id or password is wrong'''
            b.message = Label(text = 'Username or Password incorrect. Try again!',fg = 'Red')
            b.message.grid(row=6,column=2)
if __name__ == '__main__':
    a = Tk()
    a.geometry('425x225')
    application = xyz(a)
    a.mainloop()