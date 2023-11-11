from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
FONT_NAME = "Courier"
FONT_SIZE = 8
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

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Info', message="Your password hasn't been saved! Missing information!")
        # web_entry.delete(0, END)
        # pass_entry.delete(0, END)
    else:
        is_ok = messagebox.askokcancel(title='Save?', message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as data_file:
                text = f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n"
                data_file.write(text)
            messagebox.showinfo(title='Info', message="Your password has been saved!")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


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
web_entry = Entry(width=55)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jankowanlski@gmail.com")
pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

# Buttons
gen_pass_but = Button(text="Generate Password", font=(FONT_NAME, 8), width=17, command=generate)
gen_pass_but.grid(row=3, column=2)
add_but = Button(width=46, text="Add", command=add)
add_but.grid(row=4, column=1, columnspan=2)


window.mainloop()
