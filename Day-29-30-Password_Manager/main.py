from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    new_data = {
        website: {
            "email":email,
            "password": password
        }
    }

    if len(website) < 1 or len(email) < 1 or len(password) <1:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    global website_entry
    global email_entry
    website = website_entry.get()
    email = email_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        for key in data:
            if website == key:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Password", message=f"Email: {email} \n Password: {password}")
            else:
                messagebox.showinfo(title="Password", message="No details for the website exists")
    finally:
        website_entry.delete(0, END)

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

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
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

#Search button
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()

