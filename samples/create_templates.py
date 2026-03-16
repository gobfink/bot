import cv2
import numpy as np
import os

IMAGE_PATH = "image.png"
OUT_DIR = "raw_digits"

LOWER_YELLOW = np.array([10, 60, 60], dtype=np.uint8)
UPPER_YELLOW = np.array([45, 255, 255], dtype=np.uint8)

os.makedirs(OUT_DIR, exist_ok=True)

img = cv2.imread(IMAGE_PATH)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)

# optional cleanup
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)

saved = 0
debug = img.copy()

for i in range(1, num_labels):
    x, y, w, h, area = stats[i]

    if area < 8:
        continue
    if w < 2 or h < 6:
        continue
    if w > 25 or h > 30:
        continue

    digit = mask[y:y+h, x:x+w]
    out_path = os.path.join(OUT_DIR, f"digit_{saved}.png")
    cv2.imwrite(out_path, digit)

    cv2.rectangle(debug, (x, y), (x + w, y + h), (0, 255, 0), 1)
    saved += 1

cv2.imwrite("debug_boxes.png", debug)
cv2.imwrite("debug_mask.png", mask)

print(f"saved {saved} digit crops to {OUT_DIR}/")