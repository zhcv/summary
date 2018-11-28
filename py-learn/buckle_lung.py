import numpy as np
import cv2
from PIL import Image

filename = '0d9cbc9a-ec1f-4e3a-9b0b-7d3c753296ba_label.png'

arr = cv2.imread(filename)

gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
k = np.ones((4,4))
binary = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, k)


# find external contours of all shapes
im2 ,contours, hierarchy= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

try:
    hierarchy = hierarchy[0]
except:
    hierarchy = []


height, width = arr.shape[:2]
min_x, min_y = width, height
max_x = max_y = 0

# computes the bounding box for the contour, and draws it on the frame,
for contour, hier in zip(contours, hierarchy):
    (x,y,w,h) = cv2.boundingRect(contour)
    min_x, max_x = min(x, min_x), max(x+w, max_x)
    min_y, max_y = min(y, min_y), max(y+h, max_y)
    """
    if w > 80 and h > 80:
        cv2.rectangle(arr, (x,y), (x+w,y+h), (255, 0, 0), 2)
    """
if max_x - min_x > 0 and max_y - min_y > 0:
    cv2.rectangle(arr, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)


Image.fromarray(arr).show()
