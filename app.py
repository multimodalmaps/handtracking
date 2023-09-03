from flask import Flask, render_template
from flask_cors import CORS
from frames_processor import FrameProcessor
from socket_handler import SocketHandler
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)  # Handle CORS
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    frame_processor = FrameProcessor()
    socket_handler = SocketHandler(socketio, frame_processor)
    socket_handler.register_events()
    socketio.run(app, debug=True)
