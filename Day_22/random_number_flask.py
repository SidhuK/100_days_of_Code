# creating a random number guessing game using flask

from flask import Flask
import random

# create a random number

random_number = random.randint(0, 9)
print(random_number)

# creating a FLask app

app = Flask(__name__)


# making the home page with a decorator

@app.route("/")
def home():
    return "<h1>Guess a number between 1 and 9: </h1>" \
           "<img scr ='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    # if number is too high
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    # if number is low
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    # the correct number
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
