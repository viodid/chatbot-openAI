# Chatbot using OpenAI API and Flask

<p>This project is a chatbot implementation using the OpenAI API for natural language processing and
the Flask framework in Python for the backend. The communication between the client and server is
facilitated through websockets using the Socket.IO library.</p>
<p>The chatbot's user interface (UI) is inspired by a CodePen design.</p>

## Project Structure

The project follows the following directory structure:

<img src="/src/static/img/tree.png">


## Getting Started

To run the chatbot locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/chatbot.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Start the server: `python run.py`
4. Open your web browser and go to `http://localhost:8888` to access the chatbot UI.


## Configuration

The `config.py` file contains configuration parameters for the chatbot. You may modify this file to customize the behavior of the chatbot, such as setting the API keys for the OpenAI API or adjusting other settings.

## Usage

Once the chatbot is running, users can interact with it through the web interface. Messages are sent to the server via websockets, and the Flask backend processes the user input using the OpenAI API to generate appropriate responses.

## Deploying with Docker

You can also deploy the chatbot using Docker. A Dockerfile is provided for easy deployment. Follow these steps to deploy the chatbot using Docker:

1. Build the Docker image: `docker build -t chatbot-app .`
2. Run the Docker container: `docker run -p 8888:8888 chatbot-app`

The chatbot will be accessible at `http://localhost:8888` just like when running locally.

<h2>Documentation</h2>

<p>Here are some helpful links for the documentation:</p>

<ul>
  <li>
    Flask-SocketIO Documentation:
    <a href="https://flask-socketio.readthedocs.io/en/latest/intro.html">https://flask-socketio.readthedocs.io/en/latest/intro.html</a>
  </li>
  <li>
    Socket.IO Documentation:
    <a href="https://socket.io/docs/v4/">https://socket.io/docs/v4/</a>
  </li>
</ul>

<p>The provided links will help you understand and utilize the technologies and tools used in this project, including Flask-SocketIO for server side WebSocket communication and Socket.IO for client side WebSocket communication.</p>

<h2>License</h2>

<p>This project is licensed under the Unlicense - a public domain dedication.</p>

<p>You are free to use, modify, and distribute the code in any way you see fit without any restrictions. The Unlicense allows you to do whatever you want with the code, including using it for commercial purposes, without requiring any attribution or permission from the original author.</p>

<p>The Unlicense is a permissive license that grants you the maximum freedom to use the software without imposing any legal obligations or limitations.</p>

<p>For more details, please refer to the <a href="https://unlicense.org">Unlicense</a> website.</p>

<p>Feel free to make this project your own and use it for any purpose you desire. Happy coding! 🚀</p>


## Acknowledgments

The chatbot UI design is based on a CodePen design created by Zenworm, which can be found at [source](https://codepen.io/zenworm/pen/KqLNPm). We express our gratitude for their contribution.

## Contributing

Contributions to this project are welcome. If you find any issues or have improvements to suggest, please feel free to submit a pull request.



<h2>Contact</h2>

<p>Hey there! I'm excited that you're exploring my chatbot project. If you have any questions, feedback, or just want to say hi, feel free to get in touch with me!</p>

<p>I'm always happy to chat about anything related to this project, and I'm open to suggestions for improvements or new features. Your input is valuable, and it helps make this chatbot even better.</p>

<p>You can reach out to me through any of the following channels:</p>

<ul>
  <li>Email: david.zwsse@simplelogin.co</li>
  <li>Twitter: <a href="https://twitter.com/Viodid1">@Viodid1</a></li>
  <li>LinkedIn: <a href="https://www.linkedin.com/in/davidyunta/">David Yunta</a></li>
</ul>

<p>Don't hesitate to contact me if you have any questions, run into issues, or just want to share your experience with the chatbot. I'm looking forward to hearing from you!</p>
