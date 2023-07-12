"""Entry point for the application."""
from flask import Flask, render_template, request
from flask_socketio import SocketIO

from src.models.chat import Chat

from config import Config

def create_app(config_class=Config):
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/')
    def home_page():
        return render_template('index.html')


    @app.route('/chatbot', methods=['POST'])
    def chatbot_page():
        query = request.form['query']
        response = Chat.conversate(query)
        return render_template('index.html', response=response)

    return app
