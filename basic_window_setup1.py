import tkinter
from tkinter import messagebox


window=tkinter.Tk()
window.title("Login Form")
window.geometry("340x440")
window.configure(bg="#333333") #background colour set up

def login():
    username="Johnsmit"
    password="123456"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in!")
        #print("Successfully logged in!")
    else:
        messagebox.showinfo(title="Error!", message="Your login failed and please check username or password!")
        #print("Invalid login!")

frame=tkinter.Frame(bg="#333333") # creating a frame with background colour to place all of widgets

#creating widgets
login_label=tkinter.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial",30))
username_label=tkinter.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial",16))
username_entry=tkinter.Entry(frame, font=("Arial",16))
password_entry=tkinter.Entry(frame, show="*", font=("Arial",16))
password_label=tkinter.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial",16))
login_buttom=tkinter.Button(frame, text="Enter", bg="#FF3399", fg="#FFFFFF", font=("Arial",16), command=login) # command is to enter your login and login to call login function.

#placing widgets on the screen
login_label.grid(row=0,column=0,columnspan=2, sticky="news", pady=40) #pady for space between 2 rows
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1, pady=20)
password_entry.grid(row=2,column=1, pady=20)
password_label.grid(row=2,column=0)
login_buttom.grid(row=3,column=0,columnspan=2, pady=30)

frame.pack()



window.mainloop()