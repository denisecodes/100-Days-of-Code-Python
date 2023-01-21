from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


paddle_positions = [(350, 0), (-350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create two paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#Create a ball
ball = Ball()

#Create a scoreboard
scoreboard = Scoreboard()

#TODO make paddle move up and down

screen.listen()
#right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
#left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        bounce = ball.bounce_x()
    # Detect collision with left and right wall
    # hit right wall, left paddle gets 1 point, move towards left paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    ## hit left wall, right paddle gets 1 point, move towards right paaddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()