import cv2
import pytesseract
import numpy as np

# load image
img = cv2.imread("image.png")

# convert to HSV (better for color detection)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask yellow color
lower_yellow = np.array([20, 150, 150])
upper_yellow = np.array([40, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# find contours (possible numbers)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

numbers = []

for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    # filter small noise
    if w > 10 and h > 10:
        roi = img[y:y+h, x:x+w]

        text = pytesseract.image_to_string(
            roi,
            config="--psm 7 -c tessedit_char_whitelist=0123456789"
        )

        text = text.strip()
        if text:
            numbers.append((x, text))

# sort left-to-right
numbers.sort()

print([n[1] for n in numbers])