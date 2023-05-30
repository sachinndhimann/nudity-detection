# camera.py

import cv2

class Camera:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)  # Initialize the video capture
    
    def capture_frame(self):
        ret, frame = self.video_capture.read()  # Read a frame from the camera
        
        if not ret:
            return None
        
        return frame
    
    def release(self):
        self.video_capture.release()  # Release the video capture resources
