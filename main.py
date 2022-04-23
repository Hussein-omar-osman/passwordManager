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