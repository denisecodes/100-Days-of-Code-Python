from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK_MARKS = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global REPS
    REPS = 0
    global CHECK_MARKS
    CHECK_MARKS = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it's the 8th rep
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(long_break_sec)
    #if it's the 1st/3rd/5th/7th rep:
    elif REPS % 2 != 0:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(work_sec)
    #if its the 2nd/4th/6th rep:
    else:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_mins = math.floor(count/60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        # method that takes an amount of time it should wait, after the amount of time, calls particular function
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global REPS
        global CHECK_MARKS
        if REPS % 2 == 0:
            CHECK_MARKS += "✔"
            check_marks.config(text=f"{CHECK_MARKS}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

#Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

#Check Marks Label
check_marks = Label(text=f"", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

#Start button
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#Reset button
rest_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
rest_button.grid(column=2, row=2)

window.mainloop()

