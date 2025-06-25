import random
from flask import Flask
app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route('/')
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<p>Type a number in the URL like this: /5</p>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


@app.route('/<int:number>')
def guess(number):
    if number == random_number:
        return f"<h1>🎉 That is correct! {number} is the right answer</h1>"
    elif number < random_number:
        return ("<h1>⬇️ Too low!</h1>"
                "<p>Guess again!</p>"
                "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")
    else:
        return ("<h1>⬆️ Too high!</h1>"
                "<p>Guess again!</p>"
                "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)






