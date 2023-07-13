from src import app, socketio


if __name__ == "__main__":
    socketio.run(app, debug=False, host='0.0.0.0', port=8888)
