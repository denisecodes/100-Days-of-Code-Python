from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


#TODO Create a scoreboard that knows how to keep track of the score
# and displays in the program
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Your score:{self.score} Your high score:{self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.write_score()

   #def game_over(self):
   #    self.goto(0,0)
   #    self.write("GAME OVER", move=False, align=ALIGNMENT,
   #               font=FONT)
