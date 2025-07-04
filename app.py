from flask import Flask, render_template, request
import random

app = Flask(__name__)

options = ("Rock", "Paper", "Scissors")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    player = ""
    computer = ""

    if request.method == "POST":
        player = request.form["choice"]
        computer = random.choice(options)

        if player == computer:
            result = "It's a tie!"
        elif player == "Rock" and computer == "Scissors":
            result = "You win!"
        elif player == "Paper" and computer == "Rock":
            result = "You win!"
        elif player == "Scissors" and computer == "Paper":
            result = "You win!"
        else:
            result = "You lose!"

    return render_template("index.html", result=result, player=player, computer=computer)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render ustawi PORT jako zmienną środowiskową
    app.run(host="0.0.0.0", port=port)