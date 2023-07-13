"""Entry point for the application."""
from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit

from src.models.chat import Chat
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, logger=True, engineio_logger=True)

chat = Chat()

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/refresh')
def refresh_history():
    Chat.refresh_history(chat)
    return redirect(url_for('home_page'))


@socketio.on('messages')
def handle_message(data):
    print(repr(chat))
    emit('ai_answer', Chat.get_ai_answer(chat, data['data']), broadcast=False)
