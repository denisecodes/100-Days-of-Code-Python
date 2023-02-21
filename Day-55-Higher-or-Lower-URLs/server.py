from flask import Flask
import random
app = Flask(__name__)

def h1(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper


# When it goes to home route, with just a "/"
@app.route('/')
@h1
def home():
    return 'Guess a number between 0 and 9' \
           '<br><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = random.randint(0, 9)

@app.route("/<int:number>")
def guess_number(number):
    if number < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

# Checks app is in current file, not from an imported module
if __name__ == '__main__':
    # Activate debug mode, allows you to make changes and see it without you having to stop/start the file
    app.run(debug=True)