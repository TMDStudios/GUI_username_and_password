import string
from tkinter import *


def click():
    username = username_box.get()
    password = pw_box.get()
    confirmed_pw = pw_confirm_box.get()

    users = ['Sam', 'Frank', 'Jane']
    caps = string.ascii_uppercase
    numbers = []
    for i in range(10):
        numbers.append(str(i))
    special_chars = ['!', '@', '#', '$']
    name_check = False

    def name_available(name):
        if name.title() in users:
            return False
        else:
            return True

    def number_found(name):
        found = False
        for number in numbers:
            if name.find(number) > -1:
                found = True
        return found

    def caps_found(pw):
        found = False
        for letter in caps:
            if pw.find(letter) > -1:
                found = True
        return found

    def special_found(pw):
        found = False
        for char in special_chars:
            if pw.find(char) > -1:
                found = True
        return found

    output.configure(text="Signup successful")
    if password != confirmed_pw and len(password) > 7:
        output.configure(text="Passwords do not match")
    if not number_found(password):
        output.configure(text="Password must contain a number")
    if not special_found(password):
        output.configure(text="Password must contain a special character (!, @, #, $)")
    if not caps_found(password):
        output.configure(text="Password must contain a capital letter")
    if len(password) < 8:
        output.configure(text="Password must be at least 8 characters long")
    if number_found(username):
        output.configure(text="Username cannot contain numbers")
    if not name_available(username):
        output.configure(text="Please choose another username")
    if len(username) < 3 or len(username) > 14:
        output.configure(text="Username must be between 3 and 14 characters long")


window = Tk()
window.title("Create an account")
window.configure(bg="grey")

Label(window, text="Enter your username:", bg="grey", fg='white', font="none 12 bold") \
    .grid(row=1, column=0, sticky=EW, pady=8)
Label(window, text="Enter your password:", bg="grey", fg='white', font="none 12 bold") \
    .grid(row=3, column=0, sticky=EW, pady=8)
Label(window, text="Confirm password:", bg="grey", fg='white', font="none 12 bold") \
    .grid(row=5, column=0, sticky=EW, pady=8)

username_box = Entry(window, width=40, bg="white")
username_box.grid(row=2, column=0)

pw_box = Entry(window, width=40, bg="white")
pw_box.grid(row=4, column=0)

pw_confirm_box = Entry(window, width=40, bg="white")
pw_confirm_box.grid(row=6, column=0)

Button(window, text="SUBMIT", width=6, command=click) .grid(row=7, column=0, pady=10)

output = Label(window, text="", bg="grey", fg="white", font="none 12", width=60)
output.grid(row=8, column=0, sticky=EW, pady=10)

window.mainloop()
