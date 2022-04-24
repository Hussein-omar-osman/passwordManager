from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip


class User:
    def __init__(self):
        self.login_user = 'hussein'
        self.login_password = '586868'


class Credentials:
    def __init__(self, website, email, password):
        self.c_website = website
        self.c_email = email
        self.c_password = password

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

    if len(user_web) == 0 or len(user_email) == 0 or len(user_pass) == 0:
        messagebox.showinfo(title='Opps', message='Please fill all the inputs')
    else:
        is_ok = messagebox.askokcancel(title=user_web,
                                       message=f'These are the details entered:\n \nWebsite:  {user_web} \nEmail:  {user_email} '
                                               f'\nPassword:  {user_pass}\n \nIs it okay to save')

        if is_ok:
            with open('data.txt', mode='a') as data:
                data.write(f'{user_web}      |      {user_email}      |      {user_pass}\n')
                web_input.delete(0, 'end')
                password_input.delete(0, 'end')


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
spinbox = Spinbox(from_=12, to=30, width=5)
spinbox.grid(column=1, row=4)
add_btn = Button(text='Add', width=36, bg='blue', command=save)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()