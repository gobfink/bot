import cv2
import numpy as np

img = cv2.imread("image.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

LOWER_YELLOW = np.array([24, 200, 200])
UPPER_YELLOW = np.array([30, 255, 255])

mask = cv2.inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)

cv2.imshow("mask", mask)
cv2.waitKey(0)