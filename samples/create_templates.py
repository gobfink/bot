import cv2
import numpy as np

img = cv2.imread("brians.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([20,120,120])
upper = np.array([40,255,255])

mask = cv2.inRange(hsv, lower, upper)

contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

i = 0

for c in contours:
    x,y,w,h = cv2.boundingRect(c)

    if 8 < w < 40 and 10 < h < 40:

        roi = img[y:y+h, x:x+w]

        cv2.imwrite(f"digit_{i}.png", roi)

        i += 1