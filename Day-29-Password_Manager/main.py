from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    num_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = char_list + symbol_list + num_list
    random.shuffle(password_list)

    password = "".join(password_list)

    global password_entry
    password_entry.insert(0, password)
    #copies password ready to be pasted
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Amazon | email | password
# Trigger function to save data.txt when add button pressed,
# appended to the file for new entries
# Insert method - Tkinter
# Delete function - Tkinter
# Wipe clear website and password entry

def save():
    global website_entry
    global email_entry
    global password_entry
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(email) < 1 or len(password) <1:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Website: {website} \n Email: {email} \n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
#Puts cursor at the beginning of website entry box
website_entry.focus()

#Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'denise.chan112@gmail.com')

#Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

#Generate password button
password_button = Button(text="Generate Password", width=11, command=generate_password)
password_button.grid(column=2, row=3)

#Add button
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()

