import cv2
import mediapipe as mp
import logging 

class FrameProcessor:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
    
    def process_frame(self, frame):
        try:
            with self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
                image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                landmarks = []
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        serialized_landmarks = []
                        for landmark in hand_landmarks.landmark:
                            print("landmarks:", landmark.x, landmark.y, landmark.z)
                            serialized_landmarks.append({
                                'x': landmark.x,
                                'y': landmark.y,
                                'z': landmark.z
                            })
                        landmarks.append(serialized_landmarks)
            return landmarks
        except Exception as e:
            logging.error(f"Error in process_frame: {e}")
            return []