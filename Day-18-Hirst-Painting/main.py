import colorgram

#TODO print out a list of all colours from image, with each item on the list as a tuple -
# each colour saved as a tuple (RBG)

#extract 100 colors from damien hirt spot painting
#color_list = []
#colors = colorgram.extract('image.jpg', 100)
#
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    color_list.append(new_color)
#
#print(color_list)

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
                (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
                (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
                (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
                (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]

#TODO 10 x 10 rows of spots - 100 dots
#TODO 20 in size, spaced by 50 paces

import turtle as t
import random

t.colormode(255)
spot = t.Turtle()
spot.speed(0)
spot.penup()
spot.hideturtle()

#start start position
spot.setheading(225)
spot.forward(300)
spot.setheading(0)

def draw_from_left():
    for _ in range(10):
        color = random.choice(color_list)
        spot.dot(20, color)
        spot.forward(50)

    spot.left(90)
    spot.forward(50)
    spot.right(90)
    spot.backward(500)

for row in range(10):
    draw_from_left()

screen = t.Screen()
screen.exitonclick()
