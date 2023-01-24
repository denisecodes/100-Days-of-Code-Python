BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
from random import choice


# ---------------------------- Next Card ------------------------------- #

current_card = {}

def next_card():
    global current_card, flip_timer
    current_card = choice(to_learn)
    canvas.itemconfig(flash_card, image=front_card_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(5000, flip_card)

# ---------------------------- Flip Card ------------------------------- #

def flip_card():
    canvas.itemconfig(flash_card, image=back_card_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    window.after_cancel(flip_timer)


# ---------------------------- Remove Card ------------------------------- #

def remove_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Create a canvas for front card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
flash_card = canvas.create_image(400, 263, image=front_card_img)
title = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

know_button_img = PhotoImage(file="images/right.png")
know_button = Button(image=know_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_card)
know_button.grid(column=0, row=1)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=1, row=1)

# ---------------------------- Running Flashy------------------------------- #
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
finally:
    next_card()

window.mainloop()

