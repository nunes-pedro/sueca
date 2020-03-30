
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import jsonpickle
import time
import sys
sys.path.append('/usr/SuecaPY/src')
from Deck import Deck
from Player import Player

app = Flask(__name__)
socketio = SocketIO(app)

thread = None
iteration = 0


""" def background_thread():
    global iteration
    while True:
        socketio.emit('message', {'goodbye': "Goodbye " + str(iteration)})
        iteration = iteration + 1
        time.sleep(2)

 """


@socketio.on('connect')
def connect():
    serversend('Welcome to the server')
   # global thread
   # if thread is None:
   #     thread = socketio.start_background_task(target=background_thread)


@app.route("/")
def hello():
    return render_template('index.html', role='ya')


@socketio.on('sweetroom')
def test(data):
    if(len(users == 2)):
        emit("transfered", users)
    else:
        emit("transfered", {'message': "Not the correct amount of users"})


@socketio.on('c2server')
def c2server(message):
    print("Client says:" + str(message))


def serversend(message):
    socketio.emit("s2c_msg", {'str': str(message)})


@app.route("/sweet")
def sweet():
    d = Deck()
    p1 = Player("Tostas")
    p1.getHand(d)
    p2 = Player("Lima")
    p2.getHand(d)
    users = {p1, p2}

    print(str(p1.hand))
    serversend(str(p1.hand).extend())
    time.sleep(2)
    socketio.emit('message', {'p2': 'handp2'})
    return render_template('base.html')


if __name__ == "__main__":
    app.run()
