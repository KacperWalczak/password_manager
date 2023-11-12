from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT_NAME = "Courier"
FONT_SIZE = 8
DEFAULT_EMAIL = 'jankowalski@gmail.com'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    return password


def generate():
    pass_entry.delete(0, END)
    pass_entry.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {web: {"email": email, "password": password}}

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Info', message="Your password hasn't been saved! Missing information!")
    else:
        is_ok = messagebox.askokcancel(title='Save?', message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                messagebox.showinfo(title='Info', message="Your password has been saved!")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                # email_entry.delete(0, END)
                # email_entry.insert(0, DEFAULT_EMAIL)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    web = web_entry.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found!")
    else:
        if web in data:
            email = data[web]['email']
            password = data[web_entry.get()]['password']
            messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
            web_entry.delete(0, END)
        else:
            messagebox.showinfo(title='Error', message="No details for the website exist.")
            web_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
pass_label = Label(text='Password:')
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, DEFAULT_EMAIL)
pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

# Buttons
search_but = Button(width=17, text="Search", command=search_password)
search_but.grid(row=1, column=2)
gen_pass_but = Button(text="Generate Password", width=17, command=generate)
gen_pass_but.grid(row=3, column=2)
add_but = Button(width=46, text="Add", command=add)
add_but.grid(row=4, column=1, columnspan=2)


window.mainloop()
