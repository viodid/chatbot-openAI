from flask import Flask, render_template, request
from models.chat import Chat

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/test')
    def test_page():
        return '<h1>Testing the Flask Application</h1>'

    @app.route('/chatbot', methods=['GET', 'POST'])
    def chatbot_page():
        if request.method == 'POST':
            query = request.form['query']
            response = Chat.conversate(query)
            return render_template('index.html', response=response)
        return render_template('index.html')

    return app