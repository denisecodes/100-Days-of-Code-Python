import turtle
import pandas as pd

FONT = ("courier", 8, 'normal')

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()
write_state.color("black")

data = pd.read_csv("50_states.csv")
correct_guesses = []

while len(correct_guesses) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state name?")
    answer_capitalised = answer_state.title()
    # Stops while loop by break
    if answer_capitalised == "Exit":
        #run a loop to compare the correct guessed with the 50 states,
        #if not equal, then append to learning list
        learning_list = [state for state in data.state if state not in correct_guesses]
        data = pd.DataFrame(learning_list)
        data.to_csv("learning_list.csv")
        break
    for state in data.state:
        if answer_capitalised == state:
            state_data = data[data.state == state]
            state_x = int(state_data.x)
            state_y = int(state_data.y)
            write_state.goto(state_x, state_y)
            write_state.write(f"{answer_capitalised}", align='center', font=FONT)
            correct_guesses.append(answer_capitalised)


#TODO write location of state on x,y value if correct, no location written if guesed incorrectly



# Not needed as Angela has stored all the states x,y coordinates in CSV file
#def get_mouse_click_coor(x, y):
#    print(x, y)
#
## Event listener for mouse click
#turtle.onscreenclick(get_mouse_click_coor)
#
##Keep screen open
#turtle.mainloop()

