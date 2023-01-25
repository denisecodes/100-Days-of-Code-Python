from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    # Makes sure we are putting in quiz_brain and ensuring it's quiz brain data type
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("arial", 20, "italic"),
            width=280
        )

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.user_choose_true)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.user_choose_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            #Disables buttons from being used
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_choose_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def user_choose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        timer = self.window.after(1000, self.get_next_question)







