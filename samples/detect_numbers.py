import cv2
import pytesseract
import numpy as np

# If on Windows uncomment and set path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("brians.png")

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask yellow numbers
lower = np.array([20, 120, 120])
upper = np.array([40, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

# clean mask
kernel = np.ones((3,3),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# find digit blobs
contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

digits = []

for c in contours:
    x,y,w,h = cv2.boundingRect(c)

    # filter noise
    if 8 < w < 60 and 10 < h < 40:

        roi = mask[y:y+h, x:x+w]
        roi = cv2.resize(roi, None, fx=3, fy=3)

        text = pytesseract.image_to_string(
            roi,
            config="--psm 10 -c tessedit_char_whitelist=0123456789"
        ).strip()

        if text.isdigit():
            digits.append((x,text))

# sort left to right
digits.sort()

# merge digits into numbers
numbers = []
current = ""

prev_x = None

for x,d in digits:

    if prev_x is None or x - prev_x < 20:
        current += d
    else:
        numbers.append(current)
        current = d

    prev_x = x

if current:
    numbers.append(current)

print(numbers)
