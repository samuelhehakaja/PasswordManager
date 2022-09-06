from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for i in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Alert", message="Password is still empty.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}",
                                       message=f"Is it correct?\nEmail: {username_entry.get()}\nPassword: {password_entry.get()}")
        if is_ok:
            with open("saved_pass.txt", "a") as file:
                file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

# website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# username label
username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

# username entry
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "samuel@gmail.com")

# password label
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# generate button
generate_button = Button(text="Generate Password", width=14, command=generate_pass)
generate_button.grid(column=2, row=3)

# add button
add_button = Button(text="add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
