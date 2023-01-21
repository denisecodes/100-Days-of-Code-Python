from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

def convert_miles():
    km_num_label.config(text=(float(user_input.get()) * 1.609))

user_input = Entry()
user_input.config(width=7)
user_input.grid(column=1, row=0)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label()
equal_to_label.config(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_num_label = Label()
km_num_label.config(text=0)
km_num_label.grid(column=1, row=1)

km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button()
calculate_button.config(text="Calculate", command=convert_miles)
calculate_button.grid(column=1, row=2)

window.mainloop()