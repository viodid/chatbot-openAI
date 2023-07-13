"""Entry point for the application."""
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from src.models.chat import Chat
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot_page():
    query = request.form['query']
    response = Chat.conversate(query)
    return render_template('index.html', response=response)

@socketio.on('connect')
def handle_connect():
    print('connected')

@socketio.on('message')
def handle_message(data):
    print(data)

@socketio.emit('response')
def handle_response(data):
    print(data)
