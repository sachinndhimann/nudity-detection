# image_processing.py

import cv2

def load_image(image_path):
    return cv2.imread(image_path)

def show_image(image):
    cv2.imshow('Image', image)
