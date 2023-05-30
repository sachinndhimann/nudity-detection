# blur.py

import cv2

def blur_regions_with_nudity(image, regions):
    for (x, y, w, h) in regions:
        # Apply blur effect to the region of interest in the image
        image[y:y+h, x:x+w] = cv2.blur(image[y:y+h, x:x+w], (30, 30))
    
    return image
