from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, 'end')
    pick = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '0', '1', '2', '3', '4', '5', 'L', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', '6', '7', '8', '!', '#', '$', '%', '&', '(', '*', '+']
    password_len = int(spinbox.get())

    password_list = [choice(pick) for _ in range(password_len)]
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD -------------------------------#


def save():
    user_email = email_input.get()
    user_web = web_input.get()
    user_pass = password_input.get()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

web_label = Label(text='Website:')
web_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35)
email_input.insert(0, 'hussein@gmail.com')
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

generate_btn = Button(text='Generate Password', command=generate_password)
generate_btn.grid(column=2, row=4)
num_char = Label(text='Password Length')
num_char.grid(column=0, row=4)
spinbox = Spinbox(from_=12, to=20, width=5)
spinbox.grid(column=1, row=4)
add_btn = Button(text='Add', width=36, bg='blue', command=save)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()