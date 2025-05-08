from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received: {msg}")
    socketio.emit('message', msg)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
