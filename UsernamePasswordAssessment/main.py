from tkinter import *
from functools import partial
from LoginAssessmentClass import *


def validateLogin(username, password):
    username1 = username.get()
    password1 = password.get()
    abc = LoginAssessment(username1,password1)
    if len(abc.errorText)==0:
        pass
    else:
        print(abc.errorText)
        raise Exception('User credentials are invalid')
    
   
#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Enter Username and Password')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  


validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()

