import cv2
import numpy as np
import pyautogui
import time

# ---------- SETTINGS YOU MAY WANT TO TWEAK ----------
# HSV color bounds for your cyan border.
# If nothing is detected, adjust these.
LOWER_CYAN = np.array([78, 150, 150], dtype=np.uint8)
UPPER_CYAN = np.array([88, 255, 255], dtype=np.uint8)

# Minimum / maximum size (in pixels) of cyan tiles
MIN_W, MIN_H = 30, 30
MAX_W, MAX_H = 120, 120

# Delay between frames (seconds) – lower = smoother but more CPU
FRAME_DELAY = 0.1
# ----------------------------------------------------


def find_cyan_tiles(frame_bgr):
    """Return list of (x, y, w, h) for cyan-bordered tiles in a BGR image."""
    hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)

    # Mask out everything except the cyan border color
    mask = cv2.inRange(hsv, LOWER_CYAN, UPPER_CYAN)

    # Optional noise cleanup
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    tiles = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if MIN_W <= w <= MAX_W and MIN_H <= h <= MAX_H:
            tiles.append((x, y, w, h))
    return tiles


def main():
    print("Starting live highlight. Press 'q' in the window to quit.")

    while True:
        # Take screenshot and convert to OpenCV BGR format
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Find cyan tiles
        tiles = find_cyan_tiles(frame)

        # Draw rectangles around each tile
        for (x, y, w, h) in tiles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

        # Show the live annotated frame
        cv2.imshow("Cyan Tile Targets (press q to quit)", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(FRAME_DELAY)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
