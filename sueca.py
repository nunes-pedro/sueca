
from flask import Flask, render_template

import sys
sys.path.append('/usr/SuecaPY/src')
from Deck import Deck
from Player import Player

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', role='yea')


@app.route("/sweet")
def sweet():
    d = Deck()
    p1 = Player('Dealer', 1)
    p1.getHand(d)
    return render_template('index.html', role=p1.role)


if __name__ == "__main__":
    app.run()
