from flask_socketio import SocketIO
from frames_processor import FrameProcessor
import base64
import cv2
import numpy as np
import logging

class SocketHandler:
    def __init__(self, socketio: SocketIO, frame_processor: FrameProcessor):
        self.socketio = socketio
        self.frame_processor = frame_processor
    
    def register_events(self):
        @self.socketio.on('new_frame')
        def handle_frame(frame_data):
            try:
                frame_data = frame_data.split(',')[1]
                frame_data = base64.b64decode(frame_data)
                frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), -1)

                landmarks = self.frame_processor.process_frame(frame)
                print("emit landmarks:", landmarks)
                self.socketio.emit('landmarks', landmarks)
            except Exception as e:
                logging.error(f"Error in handle_frame: {e}")