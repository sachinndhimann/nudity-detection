# main.py

import cv2
from camera import Camera
from nudenet import NudeDetector
from utils.image_processing import load_image, show_image
from utils.blur import blur_regions_with_nudity

def main():
    camera = Camera()  # Initialize the camera object
    detector = NudeDetector()  # Initialize the NudeDetector object

    while True:
        frame = camera.capture_frame()  # Capture a frame from the camera
        if frame is None:
            break
        
        # Perform nudity detection on the frame
        nudity_detected, nudity_regions = detect_nudity(frame, detector)
        
        if nudity_detected:
            # Apply blur effect to the nudity regions
            frame = blur_regions_with_nudity(frame, nudity_regions)
        
        # Display the frame
        show_image(frame)
        
        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    camera.release()  # Release the camera resources
    cv2.destroyAllWindows()  # Close any open windows

def detect_nudity(frame, detector):
    # Use the NudeDetector to identify nudity in the frame
    detections = detector.detect(frame)
    nudity_regions = []

    for detection in detections:
        if detection["label"] == "NUDE":
            x, y, w, h = detection["box"]
            nudity_regions.append((x, y, w, h))

    nudity_detected = len(nudity_regions) > 0
    return nudity_detected, nudity_regions

if __name__ == '__main__':
    main()
