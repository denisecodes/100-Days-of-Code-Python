from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#TODO create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#TODO Create snake
snake = Snake()
#TODO Create food
food = Food()
#TODO Create scoreboard
scoreboard = Scoreboard()

#TODO Listen to key strokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    #the line of code after time.sleep() will be excecuted after 0.1 secs
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        #checking if snake segments is close to another segment
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()