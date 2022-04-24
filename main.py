from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip
import json
NAME = 'hussein'
PASSWORD = '5868'


class User:
    """creates user login info"""
    def __init__(self):
        self.login_user = NAME
        self.login_password = PASSWORD


class Credentials:
    """creates user accounts"""
    def __init__(self, website, email, password):
        self.c_website = website
        self.c_email = email
        self.c_password = password


# ----------------------------  CHECKING LOGIN ------------------------------- #
def check_login():
    """checks if user has provided the right login info"""
    user_entry = entry_login.get()
    entry_login.delete(0, 'end')

    if user_entry == PASSWORD:
        window_login.destroy()

        # ---------------------------- PASSWORD GENERATOR ------------------------------- #

        def generate_password():
            """generate password by simply a click """
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
            """saves the users accounts to data.json"""
            user_email = email_input.get()
            user_web = web_input.get().title()
            user_pass = password_input.get()
            account = Credentials(user_web, user_email, user_pass)
            new_account = {
                user_web: {
                    "email": user_email,
                    "password": user_pass
                }
            }
            # print(account.c_email, account.c_website, account.c_password)
            if len(user_web) == 0 or len(user_email) == 0 or len(user_pass) == 0:
                messagebox.showinfo(title='Opps', message='Please fill all the inputs')
            else:
                is_ok = messagebox.askokcancel(title=user_web,
                                               message=f'These are the details entered:\n \nWebsite:  {user_web} \nEmail:  {user_email} '
                                                       f'\nPassword:  {user_pass}\n \nIs it okay to save')

                if is_ok:
                    with open('data.json', 'r') as data_file:
                        # Read old data
                        data_store = json.load(data_file)
                        # Update Old data
                        data_store.update(new_account)
                    with open('data.json', 'w') as data_file:
                        # Save new data
                        json.dump(data_store, data_file, indent=4)
                        web_input.delete(0, 'end')
                        password_input.delete(0, 'end')

        # ---------------------------- SEARCH ACCOUNT ------------------------------- #
        def search_account():
            """allows the user to search accounts in data.json file"""
            search_term = web_input.get().title()
            with open('data.json', 'r') as data_file:
                data_store = json.load(data_file)
                try:
                    account_received = data_store[search_term]
                except:
                    messagebox.showinfo(title='Opps', message="Sorry Account Doesn't Exit")
                else:
                    messagebox.showinfo(title=search_term, message=f"Website: {search_term}\n \nEmail: "
                                                                   f"{account_received['email']}\n "
                                                                   f"Password: {account_received['password']}\n "
                                                                   f"\n The Password is copied to your clipboard\n")
                    pyperclip.copy(account_received["password"])
                # print(data_store)

        # ---------------------------- UI SETUP ------------------------------- #

        window = Tk()

        window.title('Password Manager')
        window.config(padx=50, pady=50)
        window.eval('tk::PlaceWindow . center')
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

        web_input = Entry(width=17)
        web_input.focus()
        web_input.grid(column=1, row=1)

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

        search_btn = Button(text='Search', command=search_account)
        search_btn.grid(column=2, row=1)

        window.mainloop()

    else:
        messagebox.showinfo(title='Opps', message='Wrong Password')


window_login = Tk()
window_login.eval('tk::PlaceWindow . center')
window_login.title("LOGIN")
window_login.config(padx=50, pady=50)
label_login = Label(text='Password')
label_login.grid(column=0, row=0)
entry_login = Entry()
entry_login.focus()
entry_login.grid(column=0, row=1)
btn_login = Button(text='Click', command=check_login, bg='blue')
btn_login.grid(column=0, row=2)
window_login.mainloop()